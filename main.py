from flask import Flask,jsonify
from extensions import db, jwt
from dotenv import load_dotenv
from auth import auth_bp
from users import user_bp
from models import User, TokenBlocklist

load_dotenv()

def create_app():
    app = Flask(__name__)
    
    app.config.from_prefixed_env()
    

    
    #initiaalize exts
    db.init_app(app)
    jwt.init_app(app)
    
    #register blueprint
    app.register_blueprint(auth_bp, url_prefix='/auth')
    app.register_blueprint(user_bp, url_prefix="/users")
    
    #load user
    @jwt.user_lookup_loader
    def user_look_callback(_jwt_headers,jwt_data):
        identity = jwt_data['sub']
        return User.query.filter_by(username=identity).one_or_none()
    
    
    #additional claims
    @jwt.additional_claims_loader
    def make_additional_claims(identity):
        if identity == "cara1":
            return {"is_staff":True}
        return {"is_staff":False}
    
    #JWT error handlers
    @jwt.expired_token_loader
    def expired_token_callback(jwt_header, jwt_data):
        return jsonify({"message":"Token has expired", "error":"token_expired"}), 401
    
    @jwt.invalid_token_loader
    def invalid_token_callback(erro):
        return jsonify({"message":"Signature verification failed", "error":"invalid_token"}), 401
    
    @jwt.unauthorized_loader
    def missing_token_callback(error):
        return jsonify({"message":"Request doesn't contain valid token", "error":"authorization_header"}), 401
    
    @jwt.token_in_blocklist_loader
    def token_in_blocklist_callback(jwt_header,jwt_data):
        jti = jwt_data['jti']
        
        token = db.session.query(TokenBlocklist).filter(TokenBlocklist.jti==jti).scalar()
        
        
        return token is not None
    
    
    return app


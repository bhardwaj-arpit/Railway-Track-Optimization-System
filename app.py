from flask import Flask
from flask_cors import CORS
from routes.auth import auth_bp
from routes.user_routes import user_bp

app = Flask(__name__)
CORS(app)  # Enable CORS for frontend-backend communication

# Register Blueprints
app.register_blueprint(auth_bp, url_prefix="/auth")
app.register_blueprint(user_bp, url_prefix="/users")

if __name__ == '__main__':
    app.run(debug=True)

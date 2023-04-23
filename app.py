from flask import Flask
from views import views

# Initialize application
app = Flask(__name__)

# Routes
app.register_blueprint(views, url_prefix="/views")

if __name__ == '__main__':
    app.run(debug=True, port=8000)
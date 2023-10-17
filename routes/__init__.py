from flask import Flask
from .projects import projects_bp
from .tasks import tasks_bp


def create_app():
    app = Flask(__name__)

    # Register blueprints
    app.register_blueprint(projects_bp)
    app.register_blueprint(tasks_bp)

    return app

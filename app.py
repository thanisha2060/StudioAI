from flask import Flask
from config import Config
from extensions import db, migrate


def create_app():
    app = Flask(__name__)
    app.config.from_object(Config)

    # Init extensions
    db.init_app(app)
    migrate.init_app(app, db)

    # Register blueprints
    from routes.project import project_bp
    from routes.ai import ai_bp
    app.register_blueprint(project_bp)
    app.register_blueprint(ai_bp)

    # Import models so Flask-Migrate can detect them
    with app.app_context():
        from models.project import Project  # noqa
        from models.contact import Contact  # noqa
        db.create_all()

    return app


app = create_app()

if __name__ == '__main__':
    app.run(debug=True, use_reloader=False)
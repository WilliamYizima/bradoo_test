import os

from flask import Flask
from flask_bootstrap import Bootstrap
from db.models import configure as config_db
from db.serialize import configure as config_ma
from flask_migrate import Migrate


def create_app():
    app = Flask(__name__)
    Bootstrap(app)
    app.config.from_object(os.environ['APP_SETTINGS'])
    app.config['JSON_AS_ASCII'] = False
    url_database_dev = "postgresql://will:123456@localhost:5432/bradoo_test"
    app.config['SQLALCHEMY_DATABASE_URI'] = url_database_dev

    config_db(app)
    config_ma(app)

    Migrate(app, app.db)

    from routes import vendor, page
    app.register_blueprint(page.page)
    app.register_blueprint(vendor.vendor, url_prefix='/vendor')

    return app

if __name__ == "__main__":
    create_app()

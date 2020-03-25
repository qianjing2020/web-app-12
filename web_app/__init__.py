
# web_app/__init__.py

from flask import Flask

from web_app.models import db, migrate
from web_app.routes.home_routes import home_routes
from web_app.routes.book_routes import book_routes

def create_app():
    # flask factories
    app = Flask(__name__)

    #app.config["SQLALCHEMY_DATABASE_URI"] = "sqlite:///web_app.db"
    app.config["SQLALCHEMY_DATABASE_URI"] = "sqlite:////Users/jing/Documents/LambdaSchool/LS_DS_unit3/DS-Unit-3-Sprint-3-Production-and-Cloud/web-app-12/web_app.db"

    db.init_app(app)
    # db is an a flask SQLAlchemy object created in models.py
    migrate.init_app(app, db)
    # migrate is a flask Migrate object created in models.py
    
    app.register_blueprint(home_routes)
    app.register_blueprint(book_routes)
    #register the routes (blueprint object) so app will recognize them
     
    return app

if __name__ == "__main__":
    # when this module is run as the main module
    # __name__ is a variable defined for each script that defines whether the script is being run as the main module or it is being run as an imported module
    my_app = create_app()
    my_app.run(debug=True)
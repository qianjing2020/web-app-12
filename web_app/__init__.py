# web_app/__init__.py

from flask import Flask

from web_app.routes.home_routes import home_routes

from web_app.routes.book_routes import book_routes

def create_app():
    # flask factories
    app = Flask(__name__)
    app.register_blueprint(home_routes)
    app.register_blueprint(book_routes)
    #regiter the routes blueprints so app will recognize them
    return app

if __name__ == "__main__":
    # when this module is run as the main module
    # __name__ is a variable defined for each script that defines whether the script is being run as the main module or it is being run as an imported module
    my_app = create_app()
    my_app.run(debug=True)
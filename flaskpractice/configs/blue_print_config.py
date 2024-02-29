from api.user.user import user_blueprint
from api.file.file import file_blueprint

class BluePrintConfig():
    def registerBlueprint(app):
        app.register_blueprint(user_blueprint)
        app.register_blueprint(file_blueprint)
        
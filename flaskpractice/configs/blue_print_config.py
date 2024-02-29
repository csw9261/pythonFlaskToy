from user.controller.userController import user_blueprint

class BluePrintConfig():
    def register_Blueprint(app):
        app.register_blueprint(user_blueprint)
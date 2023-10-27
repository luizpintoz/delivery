import view
from flask import Flask

def create_app():
    #Factory: uma função que recebe um objeto cru e muda esse objeto, o devolvendo alterado, elas servem para ser executadas no futuro.

    """Factory principal"""
    app = Flask(_name_)
    app.config['DEBUG'] = True

    view.init_app(app)
    return app
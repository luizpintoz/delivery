from flask import Flask
from delivery import view

def create_app():
    #Factory: uma função que recebe um objeto cru e muda esse objeto, o devolvendo alterado, elas servem para ser executadas no futuro.

    """Factory principal"""
    app = Flask(__name__)
    app.config['DEBUG'] = True

    view.init_app(app)
    return app
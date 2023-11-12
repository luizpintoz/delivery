"""Extensão flask"""


def init_app(app):
    """Inicialização de extensões"""

    @app.route('/')
    def index():
        return "Hello World!"

    @app.route('/contato')
    def contato():
        return "<form><input type='texto'></input></form>"
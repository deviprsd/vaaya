class Context:
    nlp = None
    db = None
    app = None

    @staticmethod
    def get_nlp():
        return Context.nlp

    @staticmethod
    def set_nlp(value):
        Context.nlp = value

    @staticmethod
    def get_db():
        return Context.db

    @staticmethod
    def set_db(value):
        Context.db = value

    @staticmethod
    def get_app():
        return Context.app

    @staticmethod
    def set_app(value):
        Context.app = value

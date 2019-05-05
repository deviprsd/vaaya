class ContextWrapper(type):
    __nlp = None
    __db = None
    __app = None
    __csw = None
    __tsw = None

    def __setattr__(self, key, value):
        if f'_ContextWrapper__{key}' in ContextWrapper.__dict__:
            setattr(ContextWrapper, key, value)

    def __getattr__(self, key):
        getattr(ContextWrapper, key, None)


class Context(metaclass=ContextWrapper):
    pass

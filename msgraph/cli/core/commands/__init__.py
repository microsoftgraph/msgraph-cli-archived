class CliCommandType(object):

    def __init__(self, overrides=None, **kwargs):
        if isinstance(overrides, str):
            raise ValueError("Overrides has to be a {} (cannot be a string)".format(CliCommandType.__name__))
        self.settings = {}
        self.update(overrides, **kwargs)

    def __repr__(self):
        return str(vars(self))

    def update(self, other=None, **kwargs):
        if other:
            self.settings.update(**other.settings)
        self.settings.update(**kwargs)

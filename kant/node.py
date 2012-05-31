from string import punctuation
from random import choice

class K(object):

    _classes = dict()

    def __init__(self, name, *args, **kwargs):
        self._classes[name] = self
        self.name = name
        self.children = args
        self.options = kwargs

    def __str__(self):
        child = choice(self.children)
        return str(child.format(**self._classes))


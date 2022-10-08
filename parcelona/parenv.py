""" parcelona.parenv: parcelona environment """

from particula.environment import Environment

class ParEnv(Environment):
    """ ParEnv """
    def __init__(self):
        super().__init__()
        self.add('parcelona', 'parcelona')

    def __str__(self):
        return 'ParEnv'

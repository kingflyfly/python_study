class Cell(object):
    @property
    def state(self):
        return self._state

    @state.setter
    def state(self, value):
        if 'alive' in value.lower():
            self._state = 'alive'
        else:
            self._state = 'dead'

    @property
    def is_dead(self):
        return not self._state.lower() == 'alive'


c = Cell()
c.state = 'Alive1'

print(c.state)

"""Hashable lists"""

class Yololist(list):
    def __hash__(self):
        return hash(tuple(self))

    def __eq__(self, other):
        return tuple(self) == tuple(other)

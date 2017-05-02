"""Hero class"""

class Hero:
    "Hero class for matchmaking"
    def __init__(self, name, role, unique=False):
        self.name = name
        self.role = role
        self.unique = unique

    def get_name(self):
        """returns hero's name"""
        return self.name

    def get_role(self):
        """"returns heroes role"""
        return self.role

    def is_unique(self):
        """checks if hero is unique"""
        return self.unique

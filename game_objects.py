from containers import Interfaces


class Player(object):
    def __init__(self, name) -> None:
        self.name = name
        self.original_role = None
        self.current_role_name = None
        self.vote = None

    def __str__(self) -> str:
        return self.name

    def assign(self, role):
        self.original_role = role
        self.current_role_name = role.name
        role.player = self

    def take_vote(self, players):
        m = self.name + " please vote.".format(len(players))
        self.vote = Interfaces.console_ui().pick_from_list(players, m)


class Role(object):
    def __init__(self, name, index) -> None:
        self.name = name
        self.index = index
        self.player = None

    def play(self, players):
        print("{}, you're a {}.".format(self.player.name, self.name))

    def __str__(self) -> str:
        return self.name

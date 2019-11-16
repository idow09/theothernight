class Player(object):
    def __init__(self, name) -> None:
        self.name = name
        self.original_role = None
        self.current_role_name = None
        self.vote = None

    def __str__(self) -> str:
        return "{}, playing a {}".format(self.name, self.original_role)

    def take_vote(self, players):
        i = input(self.name + " please vote against a player ([1-{}]): ".format(len(players)))
        self.vote = players[int(i) - 1]


class Role(object):
    def __init__(self, name, index) -> None:
        self.name = name
        self.index = index
        self.player = None

    def play(self, players):
        print("{}, you're a {}.".format(self.player.name, self.name))

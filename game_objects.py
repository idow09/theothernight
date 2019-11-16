class Player(object):
    id_seed = 0

    def __init__(self, name) -> None:
        self.id = self.generate_id()
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
        id_voted = input(self.name + " please vote against a player ([1-{}]): ".format(len(players)))
        player_voted_l = list(filter(lambda p: p.id is int(id_voted), players))
        if len(player_voted_l) is not 1:
            raise Exception("Unacceptable vote")
        self.vote = player_voted_l[0]

    @staticmethod
    def generate_id():
        Player.id_seed += 1
        return Player.id_seed


class Role(object):
    def __init__(self, name, index) -> None:
        self.name = name
        self.index = index
        self.player = None

    def play(self, players):
        print("{}, you're a {}.".format(self.player.name, self.name))

    def __str__(self) -> str:
        return self.name

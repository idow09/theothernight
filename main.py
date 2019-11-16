from game_objects import Player
from game_server import OneNight
from roles import WerewolfRole, SeerRole, VillagerRole, MasonRole

if __name__ == "__main__":
    _players = [Player("player1"), Player("player2"), Player("player3"), Player("player4"), Player("player5")]
    _roles = [WerewolfRole(), SeerRole(), VillagerRole(), MasonRole(), MasonRole()]
    game = OneNight(_players, _roles)
    game.run()

# Roles should all inherit Role, in a flat hierarchy. With only one abstract method: play
# Players should have ids, which will be used in voting and other referencing instead of name
# The game end should be somehow dependent upon the current participating roles.
# Input and output should be decoupled from the core BL.
# Async streams should be used as message buses in both communication directions.

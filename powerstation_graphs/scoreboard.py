from mcrcon import MCRcon


class Scoreboard(object):

    def __init__(self, host, password, port=25575):
        self.rcon = MCRcon(host, password, port=port)
    
    def __enter__(self):
        self.rcon.connect()

        return self
    
    def __exit__(self, type, value, tb):
        self.rcon.disconnect()
    
    def get_value_for_player(self, nickname: str, score: str) -> int:
        cmd_result = self.rcon.command('scoreboard players get {} {}'.format(nickname, score))
        value = cmd_result[cmd_result.find('has') + 4:cmd_result.find('[') - 1]
        return int(value)

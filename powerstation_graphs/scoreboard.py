from mcrcon import MCRcon


class Scoreboard(object):

    def __init__(self, host, password, port=25575):
        self.rcon = MCRcon(host, password, port=port)
    
    def __enter__(self):
        self.rcon.connect()

        return self
    
    def __exit__(self, type, value, tb):
        self.rcon.disconnect()
    
    def get_list_for_player(self, player: str) -> dict:
        cmd_result = self.rcon.command('scoreboard players list {}'.format(player))

        if cmd_result.startswith('Showing'):
            return Scoreboard.__parse_scoreboard_players_list(cmd_result)
        else:
            return None
    
    @staticmethod
    def __parse_scoreboard_players_list(src: str) -> dict:
        scores = dict()

        prefix = src[:src.find(':-') + 1]
        src = src[len(prefix) + 2:]

        for line in src.split(')-'):
            if line[-1] != ')':
                line += ')'
            
            line = line.strip()

            score_name = str(line[line.rfind('(') + 1:line.rfind(')')])
            score_value = int(line[line.find(': ') + 2: line.find(' (')])

            scores[score_name] = score_value

        return scores
    

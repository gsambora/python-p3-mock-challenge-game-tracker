class Game:
    def __init__(self, title):
        self.title = title

    @property
    def title(self):
        return self._title
    
    @title.setter
    def title(self, title):
        if not hasattr(self, "title") and isinstance(title, str) and len(title)>0:
            self._title = title
        else:
            raise ValueError("Title must be nonempty string")

    def results(self):
        return [result for result in Result.all if result.game == self]

    def players(self):
        return list(set([result.player for result in Result.all if result.game == self]))

    def average_score(self, player):
        scores = [result.score for result in Result.all if result.game == self and result.player == player]
        total = sum(scores)
        return total/player.num_times_played(self)

class Player:
    def __init__(self, username):
        self.username = username

    @property
    def username(self):
        return self._username
    
    @username.setter
    def username(self, username):
        if isinstance(username, str) and len(username) >= 2 and len(username) <= 16 :
            self._username = username
        else:
            raise ValueError("Username must be a string between 2 and 16 characters.")

    def results(self):
        return [result for result in Result.all if result.player == self]

    def games_played(self):
        return list(set([result.game for result in Result.all if result.player == self]))

    def played_game(self, game):
        if game in self.games_played():
            return True
        else:
            return False

    def num_times_played(self, game):
        return [result.game for result in Result.all if result.player == self].count(game)

class Result:
    all = []

    def __init__(self, player, game, score):
        self.player = player
        self.game = game
        self.score = score
        Result.all.append(self)
    
    @property
    def score(self):
        return self._score
    
    @score.setter
    def score(self, score):
        if  not hasattr(self, "score") and isinstance(score, int) and score >= 1 and score <= 5000:
            self._score = score
        else:
            raise ValueError("Score must be integer between 1 and 5000 and is immutable.")
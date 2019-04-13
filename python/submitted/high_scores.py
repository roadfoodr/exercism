class HighScores(object):
    """
    A class to maintain a list of high scores in numeric order, with access 
    also to latest chronological score.  Internal sort for numeric order is 
    performed only on 'read' (when a numerically-ordered score is requested).
    """
    def __init__(self, scores=None):
        if scores is None:
            scores = []
        self._latest = 0
        self._scores = []
        self.sorted_flag = False
        self.scores = scores
        return

    @property
    def scores(self):
        return self._scores
    
    @scores.setter
    def scores(self, scores):
        self._latest = scores[-1] if scores else 0
        self._scores = scores.copy()
        self.reset_sort()
        return

    def add(self, score):
        self.scores.append(score)
        self._latest = score
        self.reset_sort()
        return

    def latest(self):
        return self._latest

    def personal_best(self):
        self.update_sort()
        return self._scores[0] if self._scores else 0

    def personal_top_three(self):
        return self.personal_top_scores(3)
        
    def personal_top_scores(self, n=3):
        self.update_sort()
        return self._scores[0:min(n, len(self._scores))] \
                                  if self._scores else 0

    def reset_sort(self):
        self.sorted_flag = False
        return
    
    def update_sort(self):
        if not self.sorted_flag:
            self._scores.sort(reverse=True)
            self.sorted_flag = True
        return

    # https://www.highscoresaves.com/media/catalog/product/cache/1/thumbnail/600x600/9df78eab33525d08d6e5fb8d27136e95/f/r/freeplay-4_1.png
    def __str__(self):
        topfive = self.personal_top_scores(5)
        suffixes = ('ST', 'ND', 'RD', 'TH', 'TH')
        score_str = '  |  '.join([f'{i+1}{suffixes[i]} {s:0>5} PTS'
                                  for i, s in enumerate(topfive)])
        return f'SCORE RANKING:  {score_str if score_str else "None"}'
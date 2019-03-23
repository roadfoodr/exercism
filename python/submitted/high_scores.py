class HighScores(object):
    """
    A class to maintain a list of high scores, in both chronological and
    numeric order.  Internal sort for numeric order is performed only when
    a numerically-ordered score is requested.
    """
    def __init__(self, scores=[]):
        self._scores = scores
        self.reset_sort()
        return

    @property
    def scores(self):
        return self._scores
    
    @scores.setter
    def scores(self, scores):
        self._scores = scores
        self.reset_sort()
        return

    def add(self, score):
        self.scores.append(score)
        self.reset_sort()
        return

    def latest(self):
        return self.scores[-1] if self.scores else 0

    def personal_best(self):
        self.update_sort()
        return self.sorted_scores[0] if self.sorted_scores else 0

    def personal_top_three(self):
        return self.personal_top_scores(3)
        
    def personal_top_scores(self, n=3):
        self.update_sort()
        return self.sorted_scores[0:min(n, len(self.sorted_scores))] \
                                  if self.sorted_scores else 0

    def reset_sort(self):
        self.sorted_flag = False
        return
    
    def update_sort(self):
        if not self.sorted_flag:
            self.sorted_scores = sorted(self.scores, reverse=True)
            self.sorted_flag = True
        return

    # https://www.highscoresaves.com/media/catalog/product/cache/1/thumbnail/600x600/9df78eab33525d08d6e5fb8d27136e95/f/r/freeplay-4_1.png
    def __str__(self):
        topfive = self.personal_top_scores(5)
        suffixes = ['ST', 'ND', 'RD', 'TH', 'TH']
        score_str = '  |  '.join([f'{i+1}{suffixes[i]} {s:0>5} PTS'
                                  for i, s in enumerate(topfive)])
        return f'SCORE RANKING:  {score_str if score_str else "None"}'
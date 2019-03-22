class HighScores(object):
    """
    A class to maintain a list of high scores, in both chronological and
    numeric order.
    """
    def __init__(self, scores=[]):
        self.scores = scores
        self.sorted_scores = self.scores
        self.sorted_flag = False
        return

    def add(self, score):
        self.scores.append(score)
        self.sorted_scores = self.scores
        self.sorted_flag = False
        return

    def latest(self):
        return self.scores[-1] if self.scores else 0

    def personal_best(self):
        if self.sorted_flag == False:
            self.sorted_scores.sort(reverse=True)
            self.sorted_flag == True
        return self.sorted_scores[0] if self.sorted_scores else 0

    def personal_top_three(self):
        if self.sorted_flag == False:
            self.sorted_scores.sort(reverse=True)
            self.sorted_flag == True
        return self.sorted_scores[0:min(3, len(self.sorted_scores))] \
                                  if self.sorted_scores else 0

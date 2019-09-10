# setup begin

score_text = '''
Letter                           Value
A, E, I, O, U, L, N, R, S, T       1
D, G                               2
B, C, M, P                         3
F, H, V, W, Y                      4
K                                  5
J, X                               8
Q, Z                               10
'''

score_dict = {}
score_text = score_text.replace(","," ")
score_lines = score_text.splitlines()
for line in score_lines[2:]:
    letters = line.split()
    linescore = int(letters.pop())
    for letter in letters:
        score_dict[letter] = linescore

# setup end

def score(word):
    return sum((score_dict.get(letter, 0) for letter in word.upper()))

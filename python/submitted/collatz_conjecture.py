#setup begin
try: collatz_steps_memo
except NameError:
    collatz_steps_memo = {1: 0}
#setup end


def steps(number):
    '''
    Given a number, return the number of steps required to reach 1 when
    following the Collatz Conjecture algorithm.  All intermediate results
    are memoized in order to short-cut future computations.
    '''
    if number < 1:
        raise ValueError('Number must be larger than 0.')

    numbers_seen = [number]
    known_steps = 0

    while number > 1:
        known_steps = collatz_steps_memo.get(number, 0)
        if known_steps:
            break
        number = 3 * number + 1 if number % 2 else number // 2
        numbers_seen.append(number)

    # Update the global memo for every number traversed during this run
    for i, n in enumerate(reversed(numbers_seen)):
        collatz_steps_memo[n] = i + known_steps

    return collatz_steps_memo[numbers_seen[0]]

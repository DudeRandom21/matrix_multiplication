#(m, n)
import copy, random

def matrix_bad_but_accurate(lst):
    if len(lst) < 2:
        return 0
    best = -1
    for i in range(1, len(lst)):
        curr = lst[i]
        prev = lst[i-1]
        cost = prev[0] * curr[0] * curr[1]
        cpy = copy.deepcopy(lst)
        cpy[i] = (prev[0], curr[1])
        del cpy[i-1]
        cost = cost + matrix_bad_but_accurate(cpy)
        if best == -1 or cost < best:
            best = cost
    return best


def test_matrix(lst):
    lst = copy.deepcopy(lst)
    if len(lst) < 2:
        return 0

    costs = []
    best_metric = []
    for i in range(len(lst)-1):
        costs.append( (lst[i][0] * lst[i][1] * lst[i+1][1], i) )
        best_metric.append( ( lst[i][0] * lst[i+1][1], i ) )

    (best, index) = min(best_metric)
    new_matrix = (lst[index][0], lst[index+1][1])
    lst.pop(index)
    lst.pop(index)
    lst.insert(index, new_matrix)
    return costs[index][0] + test_matrix(lst)


def gen_test_cases(size, min_int, max_int):
    previous = random.randint(min_int, max_int)
    matrices = []
    for i in range(size):
        next = random.randint(min_int, max_int)
        matrices.append((previous, next))
        previous = next
    return matrices

def test():
    test_cases = []
    for i in range(50000):
        test = gen_test_cases(5, 1, 500)
        test_cases.append(test)
    for case in test_cases:
        correct = matrix_bad_but_accurate(case)
        test_ans = test_matrix(case)
        if correct != test_ans:
            print(case)
            print("Correct Answer: {correct} \n False Answer: {incorrect}".format(correct=correct, incorrect=test_ans))
            return False

test()
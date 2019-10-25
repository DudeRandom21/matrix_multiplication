#(m, n)
import random


def test_matrix(lst):
    if len(lst) == 1:
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


lst = [(1,2), (2,3), (3,4), (4,5)]

print(test_matrix(lst))

def gen_test_cases(size, min_int, max_int):
    previous = random.randint(min_int, max_int)
    matrices = []
    for i in range(size):
        next = random.randint(min_int, max_int)
        matrices.append((previous, next))
        previous = next
    return matrices

print(gen_test_cases(10, 1, 10))

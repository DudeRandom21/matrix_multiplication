#(m, n)
import copy, random

def matrix_bad_but_accurate(lst):
    if len(lst) < 2:
        return (0, [])
    best = -1
    best_idx = 0
    best_path = []
    for i in range(1, len(lst)):
        curr = lst[i]
        prev = lst[i-1]
        cost = prev[0] * curr[0] * curr[1]
        cpy = copy.deepcopy(lst)
        cpy[i] = (prev[0], curr[1])
        del cpy[i-1]
        (rec_cost, rec_path) = matrix_bad_but_accurate(cpy)
        cost = cost + rec_cost
        if best == -1 or cost < best:
            best = cost
            best_idx = i
            best_path = rec_path
    best_path.append(best_idx)
    return (best, best_path)

def test_matrix(lst):
    lst = copy.deepcopy(lst)
    if len(lst) < 2:
        return (0, [])

    costs = []
    best_metric = []

    if len(lst) == 2:
        best_metric.append( (1,0) )
        costs.append( (lst[0][0] * lst[0][1] * lst[1][1], 0) )
    else:
        m = min(min(item) for item in lst)
        for i in range(len(lst)-1):
            costs.append( (lst[i][0] * lst[i][1] * lst[i+1][1], i) )
        for i in range(len(lst)):
            if lst[i][0] == m:
                best_metric.append( (1, i) )
            elif lst[i][1] == m and i > 0:
                best_metric.append( (1, i-1) )

    (best, index) = min(best_metric)
    new_matrix = (lst[index][0], lst[index+1][1])
    lst.pop(index)
    lst.pop(index)
    lst.insert(index, new_matrix)
    (c, p) = test_matrix(lst)
    c += costs[index][0]
    p.append(index)
    return (c, p)


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
        test = gen_test_cases(8, 1, 200)
        test_cases.append(test)
    for case in test_cases:
        correct, path = matrix_bad_but_accurate(case)
        test_ans, test_path = test_matrix(case)
        if correct != test_ans:
            print("Correct Answer: {correct} \n False Answer: {incorrect}".format(correct=correct, incorrect=test_ans))
            print("Path: ", path)
            trace(case, path)
            print("Test_Path: ", test_path)
            trace(case, test_path)
            return False

def trace(lst, indecies):

    def helper(lst, indecies):
        if len(lst) < 2:
            print(lst)
            return
        lst = copy.deepcopy(lst)
        print(lst)
        indecies = copy.deepcopy(indecies)
        i = indecies.pop()
        (n1, left, _) = lst.pop(i-1)
        (n2, _, right) = lst.pop(i-1)
        lst.insert(i-1, (n1 + n2, left, right) )
        helper(lst, indecies)
    
    lst = copy.deepcopy(lst)
    for i in range(len(lst)):
        lst[i] = (chr(i+65), lst[i][0], lst[i][1])
    
    helper(lst, indecies)


test()

#use = [(428, 288), (288, 473), (473, 2), (2, 147), (147, 276), (276, 214)]
#(cost, path) = matrix_bad_but_accurate(use)
#print( (cost, path) )
#trace(use, path)


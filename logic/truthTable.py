from logic.logicElements import LogicSignal

def exps_to_table(exps, n:int = 0):
    """
        Return the truth table from expression
    :param exps: expressions with lambda
    :param n: number of input sources, not necessary
    :return: table in str

    >>> print_table(exps_to_table(lambda a,b: a * b))
    a b f
    0 0 0
    0 1 0
    1 0 0
    1 1 1
    """

    n = exps.__code__.co_argcount
    if n == 0:
        raise Exception("Expression Error!")

    total_rows = 2 ** n
    input = [[0 for _ in range(total_rows)] for _ in range(n)]
    for i in range(total_rows):
        t = i
        for j in range(n):
            input[n-j-1][i] = LogicSignal(t % 2)
            t //= 2

    output = list(map(exps, *input))
    table = input + [output]
    return table

def print_table(table : list):
    n = len(table) - 1
    print(*[chr(x) for x in range(ord('a'), ord('a') + n)], 'f', sep=" ", end="\n")
    for i in range(len(table[0])):
        print(*[str(table[x][i]) for x in range(n)], table[n][i], sep=" ")

if __name__ == '__main__':
    #Test Case: a mux
    # print_table(exps_to_table(lambda a,b,s: a * ~s + b * s))

    print_table(exps_to_table(lambda a0, a1, a2, a3: (a0%a1)&(a2%a3)|a0&a1&~a2&~a3|~a0&~a1&a2&a3))
    pass
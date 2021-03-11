import ast

if __name__ == '__main__':
    file = open('names_scores_input.txt', mode='r')
    names = sorted(ast.literal_eval(file.readlines()[0]))
    file.close()
    _sum = 0

    for idx, name in enumerate(names):
        _sum += sum([ord(char) - 64 for char in name]) * (idx + 1)

    print(_sum)




def merge(line):
    """

    :param line:
    :return: List
    """
    line, start_merging = move_zeros(line)
    for index in range(len(line) - 1, 0, -1):
        if line[index] == line[index - 1] and line[index] != 0:
            line[index] += line[index - 1]
            line[index - 1] = 0

    return move_zeros(line[0])


def move_zeros(line):
    """

    :param line:
    :return:List
    """
    updated_line = [x for x in line if x != 0]
    start_merging = len(line) - len(updated_line)
    for i in range(start_merging):
        updated_line.append(0)
    return updated_line, start_merging


print merge([4, 2, 2, 0])
print merge([0, 0, 2, 2])
print merge([2, 2, 0, 0])
print merge([2, 2, 2, 2])
print merge([8, 16, 16, 8])




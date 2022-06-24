def rec(data_mass, s):
    if len(s) <= 1 or s == "A":
        return 1
    for elem in data_mass[::-1]:
        f = True
        while s.find(elem.split('/')[0]) != -1 and f:
            if len(s) > 1:
                if rec(data_dict, s[:s.find(elem.split('/')[0])] + elem.split('/')[1] + s[s.find(
                        elem.split('/')[0]) + len(elem.split('/')[0]):]):
                    return 1
                f = False
    return 0


def read_data():
    data = []
    res = ""
    with open("input.txt") as f:
        r_data = f.read()
    r_data = r_data.split('\n')

    if r_data[len(r_data) - 1] == "":
        r_data.pop(len(r_data) - 1)
    for elem in r_data:
        if elem.split(' ')[0] != "Combination:":
            data.append(elem.split(' ')[1] + '/' + elem.split(' ')[0])
        else:
            res = elem.split(' ')[1]
    return data, res


if __name__ == "__main__":
    data_dict, s = read_data()
    if rec(data_dict, s):
        print("Допустимая комбинация")
    else:
        print("Недопустимая комбинация")
    pass
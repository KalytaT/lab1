Keys = []
shuffle_arr = [[]]
reduct_arr = [[]]

def map(filename,filepath):
    A = []
    f = open(filename,"r")
    lines = f.read().split('\n')
    for line in lines:
        A.append((line, 1))
    return A

def shuffle(lines):
    for w in lines:
        key, val = w
        if not Keys.__contains__(key):
            Keys.append(key)
            shuffle_arr.append([])
        i = Keys.index(key)
        shuffle_arr[i].append((key, val))
    b = 3


def reduce():
    i = 0
    shuffle_arr.remove(shuffle_arr[len(shuffle_arr) - 1])
    for entry in shuffle_arr:
        amount = 0
        key, num = entry[0]
        for e in entry:
            amount += 1
            reduct_arr.append([])
        reduct_arr[i].append((key, amount))
        i += 1


if __name__ == "__main__":
    fruit = map("fruit.txt", '')
    basket = map("basket.txt", '')
    shuffle(fruit)
    shuffle(fruit)
    reduce()
    print('------- SHUFFLE -------')
    for ent in shuffle_arr:
        for entr in ent:
            key, value = entr
            print(str(key) + ' ' + str(value))
        print(' ')
    print('------- REDUCTION -------')
    for ent in reduct_arr:
        for entr in ent:
            key, value = entr
            print(str(key) + ' ' + str(value))
        print()
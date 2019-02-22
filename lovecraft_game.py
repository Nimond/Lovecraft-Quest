import random


points = [[-1, -1, -1, -1],
          [-1, +1, -1, +1],
          [+1, -1, -1, -1],
          [+1, -1, -1, -1]]


def check(array):
    for a in array:
        for i in a:
            if i < 0:
                return False

    return True

def prettyfy(array):
    for a in array:
        for i in a:
            if i > 0:
                print('+' + str(i), end=' ')
            else:
                print(i, end=' ')
        print('\n', end='')

if __name__ == '__main__':
    count = 0
    while True:
        print('\n\nTry {}:'.format(count))

        steps = 0
        count += 1
        temp = [x[:] for x in points]
        while True:
            steps += 1

            i = random.randint(0, 3)
            j = random.randint(0, 3)
            print('click {}:{}'.format(j+1, i+1))

            for n in range(0, 4):
                temp[j][n] *= -1
                temp[n][i] *= -1
            temp[j][i] *= -1

            if steps > 20:
                break

            if check(temp):
                print('The way has been found!')
                prettyfy(temp)
                break

        if steps <= 20:
            break

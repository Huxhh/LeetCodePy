# coding=utf-8

def distributeCandies(candies, num_people):
    res = [0] * num_people

    j = 0
    while candies:
        res[j % num_people] += min(j + 1, candies)
        candies -= min(j + 1, candies)
        j += 1

    return res


if __name__ == '__main__':
    candies = 1
    num_people = 3
    print(distributeCandies(candies, num_people))

#!python3
from random import randint as randint


def rand_int(min=0, max=100):
    return randint(min, max)



def main():
    print(rand_int())



if __name__ == '__main__':
    main()

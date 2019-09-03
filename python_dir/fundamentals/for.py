#!python3

# Variables
lowNum=2
highNum=9
multi=3


def main():
    #basic
    for x in range(0,150):
        print(x)

    #multiples of 5
    for x in range(5,1000,5):
        print(x)

    # Counting, the Dojo Way
    for x in range(1,100):
        if x%10==0:
            print("coding")
        elif x%5==0:
            print("dojo")
        else:
            print(x)

    # Whoa. That Sucker's Huge
    sum = 0
    for x in range(1,5000,2):
        sum += x
    print(x)

    # Countdown by Fours
    for x in range(2018,-1,-4):
        print(x)

    # Flexible Counter
    for x in range(lowNum,highNum,multi):
        print(x)






if __name__ == '__main__':
    main()

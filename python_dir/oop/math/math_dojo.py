#!python3

class MathDojo:

    def __init__(self):
    	self.result = 0

    def add(self, num, *nums):
        sum = num
        for x in nums:
            sum += x
        self.result+= sum
        return self

    def subtract(self, num, *nums):
        dif = num
        for x in nums:
            dif -= x
        self.result -=dif
        return self
    	# your code here



# def main():
# create an instance:
md = MathDojo()
# to test:
x = md.add(2).add(2,5,1).subtract(3,2).result
print(x)	# should print 5

# run each of the methods a few more times and check the result!


#
#
# if __name__ == '__main__':
#     main()

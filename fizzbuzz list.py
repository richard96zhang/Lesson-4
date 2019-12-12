class FizzBuzz():

    def Calu(self,num):
        if num % 5 == 0 and num % 3 == 0:
            list.append(fizzbuzz)
        elif num % 5 == 0:
            list.append(buzz)
        elif num % 3 == 0:
            list.append(fizz)
        else:
            list.append(num)
fizzbuzz = 'fizzbuzz'
buzz = 'buzz'
fizz = 'fizz'
example = FizzBuzz()
list = []
lower = int(input("Please type in a lower bound :"))
upper= int(input("Please type in an upper bound :"))
for a in range(lower, upper+1):
    example.Calu(a)

print(list)

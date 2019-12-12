
class FizzBuzz():
    def Calu(self,num):
        if num % 5 == 0 and num % 3 == 0:
            print ("Your number is a FizzBuzz")
        elif num % 5 == 0:
            print ("Your number is a Buzz")
        elif num % 3 == 0:
            print ("Your number is a Fizz")
        else:
            print ('Your number is ' ,num ,"it's not a fizz or buzz of FizzBuzz")

Example = FizzBuzz()
again = True
while again == True:
    Number = int(input("Please type in a number : "))
    Example.Calu(Number)
    answer = str(input("Would you like to try another number: [Y/N] "))
    if answer.lower() == 'y':
        again = True
    elif answer.lower() == 'n':
        again = False






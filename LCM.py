#Owner: Overrideveloper
#Description: LCM Program 

from memory_profiler import memory_usage
from datetime import datetime
startTime = datetime.now()

#Creating a function that uses two parameters 
def GCD(x, y):

   while(y):
       x, y = y, x % y

   return x
   
#Creating another function that uses two parameters 
def LCM(x, y):

    LCM = x*y//GCD(x, y)
    
    return LCM

#Taking user input 
FirstNumber = int(input("Enter the first number: /n"))

SecondNumber = int(input("Enter the second number: /n"))
ThirdNumber = int(input("Enter the third number: /n"))

FourthNumber = int(input("Enter the fourth number: /n"))

FifthNumber = int(input("Enter the fifth number: /n"))

output = LCM(FirstNumber, LCM(SecondNumber, LCM(ThirdNumber, LCM(FourthNumber,FifthNumber))))

print ("The Lowest Common Multiple of the five numbers is: ")

print (output)
        
print ("The execution time is ",(datetime.now()- startTime))

mem_usage = memory_usage(LCM)

print('Memory usage (in chunks of .1 seconds): %s'% mem_usage)

print('Maximum memory usage: %s'% max(mem_usage))

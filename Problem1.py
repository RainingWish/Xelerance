# given a max value n
# find a Fibonacci sequence that last index < n
# sum all odd value inside and return

def Fibonacci(max):

    #check input valid or not
    if max <= 0:
        print("Not Valid")
        return -1
    #check max = 1 or not
    if max == 1:
        print ([0])
        return 0

    #define two parameter, Fibonacci sequence, sum
    num1 = 0
    num2 = 1
    fibonacci_sequence = [0,1]
    sum = 1

    #check next value greater than max or not
    while num1 + num2 < max:
        #current value
        nth = num1 + num2
        #check odd or not
        if nth % 2 == 1:
            #if odd add to sum
            sum += nth
        #sign num1 and num2 to current
        num1 = num2
        num2 = nth
        #append current value nth to list
        fibonacci_sequence.append(nth)
    
    #print the fibonacci_sequence and return sum
    print(fibonacci_sequence)
    return sum
    
#let user input a vlaue
max = int(input("Input the max Fibonacci value:"))
#call the Fibonacci function print fibonacci_sequence and return sum value
odd_sum = Fibonacci(max)
#print the sum
print("Sum of the odd value is: ",odd_sum)

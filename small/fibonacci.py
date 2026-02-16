def fibonacci(p):
    #assuming p is prime and we don't need to check
    fibonacci = [0, 1]
    prev = 1
    i = prev
    #check remainder exists and not equal to 0
    while prev % p != 0:
        fibonacci.append(i)
        temp = i 
        i += prev 
        prev = temp
    return prev
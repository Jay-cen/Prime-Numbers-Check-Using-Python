import math

prime_array = []
p = 1000

def isPrime(number):
    x = 2 #initialize x to 2
    while( x <= math.sqrt(number) ):
        if (number%x == 0):
            return False
        x += 1 #i.e x=x+1
        
    if ( x > math.sqrt(number) ):
        return True

print('List before: ')
print(prime_array)

for i in range(2,p,1):
    if ( isPrime(i) ):
        prime_array.append(i)

print('List after:')
print(prime_array)
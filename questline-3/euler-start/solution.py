# Find the sum of all the multiples of 3 or 5 below 1000
sum = 0
for i in range(1000):
     if i % 3 == 0 or i % 5 == 0:
         sum += i
print("The sum of all multiples of 3 or 5 below 1000 is:", sum)


#What is the smallest positive number that is evenly divisible by all of the numbers from 1 to 20 ?

import math
def lcm(a, b):
     return abs(a * b) // math.gcd(a, b)
result = 1
for i in range(1, 21):
     result = lcm(result, i)
print("The smallest positive number evenly divisible by all the numbers from 1 to 20 is:", result)
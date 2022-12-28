
"""
Complete the prime_numbers function that gives all the prime numbers 
from 2 (included) to the given number (bigger than 1).
If you don't know what is a prime number, please look it up.

example input:  53
example output: [2, 3, 5, 7, 11, 13, 17, 19, 23, 29, 31, 37, 41, 43, 47, 53]

example input:  -5
example output: []


"""
def prime_numbers(prime):
    new_list=[]
    for i in range(2,prime+1):
        factor=0
        for j in range(1,i):
            if(i%j==0):
                factor+=1
        if factor<2:
            new_list.append(i)
    return new_list
    
  
    

print(prime_numbers(100))

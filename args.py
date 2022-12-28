"""
Write a function that accepts an infinite amount of positional arguments
Your function should take all the arguments and place them into a list.
Return the list

example input:  infinite_args(1,2,3,4,5)
example output: [1,2,3,4,5]

"""
# try 
def infinite_args(*args):
    new_list=[]
    for i in args:
        new_list.append(i)
    return new_list    
       

print(infinite_args(1,2,3,4,5))
    
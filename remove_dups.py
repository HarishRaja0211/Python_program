"""
Write a function `remove_dups` to remove duplicate elements of a list

example input: [1,1,1,2,2,3,4,'hello','a','a']
output: [1,2,3,4,'hello','a']

you may not use the set() function
You must write a for-loop --> if you do not write a for-loop you will get zero marks for this problem.
Even if autolab gives you full credit, I will be manually verifying that you solved it with a for-loop and adjust your marks accordingly.
"""

def remove_dups(inicial):
    new_list=[]
    for i in inicial:
        if i not in new_list:
            new_list.append(i)

    return new_list

print(remove_dups([1,1,1,2,2,3,4,'hello','a','a']))
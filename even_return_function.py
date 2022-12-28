"""
Finish the even_return function.
It should return the sum of values having even key, if no even key 
return 0

Input: Dictionary
Output: Integer Result

EXAMPLES:

input_A : {1:"45",7:"12",34:"765"}
output_A : 765

input_B : {4:"5",43:"342",72:"7"}
output_B:  12

input_C : 
output_C: 0
  
       

"""

def even_return(num_dict):
    sum_of_values=0

    for key,value in num_dict.items():
        if key%2==0: 
            x=int(value)
            sum_of_values += x
            
      
         

    return sum_of_values
  
    
    
      
        


print(even_return(({4:"5",43:"342",72:"7"})))
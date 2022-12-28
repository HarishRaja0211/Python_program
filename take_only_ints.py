"""
Finish the take_only_ints function.
Make a function that takes a number, transform it in a float() and return the product by 5, 
if the function is not given a number it should not break 
but should catch the specific error and display the corresponding message.
You Must USED a TRY/EXCEPTION block and not "if". Even if you get all the marks by Autolab 
for using if I will personally check and removed the marks from this exercise

Input: String
Outout: String

EXAMPLES:
input_A : 5
output_A : 25.0

input_B : 2.5
output_B : 12.5

input_C : "2.5"
output_C: 12.5

input_D : "hola"
output_D: "could not convert string to float: 'hola'"

input_E : [1,2,3,'a great day']
output_E: "float() argument must be a string or a number, not 'list'"

"""

def take_only_nums(insert):
    try:
        x=float(insert)
        return x*5
    except (ValueError):
        return f"could not convert string to float: '{insert}'"
    except (TypeError):
        return "float() argument must be a string or a number, not 'list'"



  
 


print(take_only_nums("helo"))

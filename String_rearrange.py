"""
Finish the str_rearrange function.
String contains the first character as the key followed by r numbers 
where odd indexed number is going to multiply in the key and even indexed 
going to removed from the key.


Input: String
Outout: String

EXAMPLES:
input_A : "s 5 3"
output_A : "ss"

input_B : "t 3 8 1 4"
output_B:  "0"

input_C : "sde 5 7 4"
output_C: "sdesde"

input_D : "fe 4"
output_D: "fefefefe"

"""


def str_rearrange(in_str):
    new_list=in_str.split(" ")     
  
         
    even=new_list[0::2]
    a=even.pop(0)
    odd=new_list[1::2]
    
    int_even=[int(i) for i in even]
    int_odd=[int(i) for i in odd]
    
    x=sum(int_even)
    y=sum(int_odd)
    c=y-x
    zero = "0"

    if c>0:
        result=c*a
        result=str(result)
        return result
           
    else:
        return zero
   
   
            
       
    
    
    
   
           
 
       

print(str_rearrange("fe 4"))

"""
Finish the swap_string function.
It should swap the adjacent characters in a string and add space after each pair,
if no swapping partner is there, just add space 


Input: String
Output: String

EXAMPLES:
input_A : "arvcwevw"
output_A : "ra cv ew wv"

input_B : "bsvcdwe"
output_B:  "sb cv wd  e"

input_C : "bswv325wev"
output_C: "sb vw 23 w5 ve"

"""

def swap_string(strin):
    x=""
    for i in range(0,len(strin),2):
       
        if len(strin)-1==i:
            x+=strin[i]+" "
           
        else :
            x+=strin[i+1]+strin[i+0]+" "
            
    output=x[0:len(x)-1]   


    return output
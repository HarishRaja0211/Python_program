"""
Finish the type_assign function.
It should take a list elements of any type (int, float, string, list, tuple, set, dictionary)
and return a dictionary counting how many of each element is giving in the input list.
Where the key is the datatype NAME and the value in the number of appearances. 


Input: list
Output: dictionary

EXAMPLES:
input_A : [1,70,2,84,15,36,14]
output_A : {'int': 7, 'float': 0, 'string': 0, 'list': 0, 'tuple': 0, 'set': 0, 'dictionary': 0}

input_B : ['Hello you', 85.41, 7, 4.0, 'another string']
output_B : {'int': 1, 'float': 2, 'string': 2, 'list': 0, 'tuple': 0, 'set': 0, 'dictionary': 0}

input_C : ['one',{'sugar':5, 'flour':4, 'oils':17},7,(84,8880,4236),42.5,5,'two',68,{1,2,3},{78,45,48}]
output_C : {'int': 3, 'float': 1, 'string': 2, 'list': 0, 'tuple': 1, 'set': 2, 'dictionary': 1}

"""

def type_assign(lista):
    result_dict={'int': 0, 'float': 0, 'string': 0, 'list': 0, 'tuple': 0, 'set': 0, 'dictionary': 0}
    for i in lista:
        
        if type(i)==int:
            result_dict['int']=result_dict.get('int',0)+1
        elif type(i)==float:
            result_dict['float']=result_dict.get('float',0)+1
        elif type(i)==str:
            result_dict['string']=result_dict.get('string',0)+1
        elif type(i)==list:
            result_dict['list']=result_dict.get('list',0)+1
        elif type(i)==tuple:
            result_dict['tuple']=result_dict.get('tuple',0)+1
        elif type(i)==set:
            result_dict['set']=result_dict.get('set',0)+1
        elif type(i)==dict:
            result_dict['dictionary']=result_dict.get('dictionary',0)+1
        else:
                return
    
    return result_dict

print(type_assign(['Hello you', 85.41, 7, 4.0, 'another string']))
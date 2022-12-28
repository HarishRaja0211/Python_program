"""
Write a function `password_check` to check the validity of a password. 
Return True if valid, False otherwise
  
Validation : 
Only letters (uppers and lowers), digit, and #, $, @ are allowed

At least 1 letter between [a-z] and 1 letter between [A-Z]. 
At least 1 digit from [0-9]. 
At least 1 character from [$#@]. 
Special characters not in the list of [$#@] are not allowed.
Minimum length 6 characters. 
Maximum length 16 characters. 

Examples:
Input: "amaZZ1_", output: False  (not valid)
Input: "aazzZZ12$$", output : True 
Input: "azZ1$", output: False  (too short)
Input: "a$gh1$123Af", output: False  (too long)

hint:
you can use the string functions: .isupper(), islower(), isdigit()
to tell if a string charatcer is an upper case letter, lower case letter or digit.


"""
def password_check(password):
    character=['$','#','@']
    upper_case=0
    lower_case=0
    digit=0
    chara=0
              
    for i in password:
        
        if i.isupper():
            upper_case +=1
        if i.islower():
            lower_case +=1
        if i.isdigit():
            digit +=1
        if i in character:
            chara +=1 
    
    
    if len(password)==6 or len(password)==10 and upper_case>=1 and lower_case>=1 and digit>=1 and chara>=1:
        return True
    else :
        return False  
    


print(password_check("amaZZ1_"))
print(password_check("aazzZZ12$$"))
print(password_check("azZ1$"))
print(password_check("a$gh1$123Af"))

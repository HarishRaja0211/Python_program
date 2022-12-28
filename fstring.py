"""
Write a function that using f-strings, print out the name, last name,
and quote of each person in the given dictionary,
formatted like so:
"The inspiring quote" - Lastname, Firstname

example input:


example output: 
I do not fear computers. I fear lack of them. -Asimov Isaac
A computer once beat me at chess, but it was no match for me at kick boxing. -Philips Emo
Computer Science is no more about computers than astronomy is about telescopes. -W. Edsger
The computer was born to solve problems that did not exist before. -Gates Bill

Note 1: Notice the empty line after the last sentence
Note 2: Don't make a script that blindly prints the given output because it will be graded with
a compound of 7 sentences. So make a program that takes correctly the input and give the desired output

Hint: The full name have 2 parts: first name and last name, you can look into the split() function.
"""
def famous_quotes(quote):
   
    
    output=""
    for i in quote:
        name=i['full_name']
        new_name =name.split()[1]+" "+name.split()[0]
        quote2=i['quote']
        output += f"{quote2} -{new_name}\n"
        
    
    return output

  
           
    
    
        
  
  
  
  
            
print(famous_quotes(
 [
    {"full_name": "Isaac Asimov", "quote": "I do not fear computers. I fear lack of them."},
    {"full_name": "Emo Philips", "quote": "A computer once beat me at chess, but it was no match for me at "
                                          "kick boxing."},
    {"full_name": "Edsger W. Dijkstra", "quote": "Computer Science is no more about computers than astronomy "
                                                 "is about telescopes."},
    {"full_name": "Bill Gates", "quote": "The computer was born to solve problems that did not exist before."}
]))


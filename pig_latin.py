"""
Write a function that converts a list of words into pig latin

Pig Latin is a language game, where you move the first letter of the word to the end and add "ay."
So "Python" becomes "ythonpay." 
You need to store the pig-latin in a dictionary, with the key as the original word and the value as the pig latin version

Example input:  ['hello', 'i', 'am', 'a' ,'dragon', 'named', 'rasevenous']
output: {'hello':'ellohay', 'i':'iay', 'am':'maay', 'a':'aay', 'dragon':'ragonday', 'named':'amednay', 'rasevenous':'asevenousray'}
"""

def pig_latin(begin):
    new_dict={}
    for i in begin:
        new_dict[i]= i[1:]+i[0]+"ay"

    return new_dict


print(pig_latin(['hello', 'i', 'am', 'a' ,'dragon', 'named', 'rasevenous']))
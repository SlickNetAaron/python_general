import json
from difflib import get_close_matches 

def translate(w):
    caps_matches = (w, w.lower(), w.title(), w.upper() )
    for case in caps_matches:
        if case in data:
            return data[case] 
    
    close_matches = get_close_matches(w, data.keys())
    for match in close_matches:
        prompt = "Did you mean > " + match + "< ? [y/n] "
        try_match = input(prompt).lower()
        if try_match == "y":
            return data[match]
            
    return "The word doesn't exist. Please double-check."

data = json.load(open("data.json"))
word = input("Enter a word: ")

result = (translate(word))
if isinstance(result, list):
    for r in result:
        print(r)
else:
    print(result)

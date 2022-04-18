import json
from difflib import get_close_matches 

data = json.load(open("data.json"))

def translate(w):
    if w in data:
        return data[w]
    else:
        w = w.lower()
        if w in data:
            return data[w] 
        close_matches = get_close_matches(w, data.keys())
        for match in close_matches:
            prompt = "Did you mean > " + match + "< ? [y/n] "
            try_match = input(prompt).lower()
            if try_match == "y":
                return data[match]
                
    return "The word doesn't exist. Please double-check."

word = input("Enter a word: ")

result = (translate(word))
if isinstance(result, list):
    for r in result:
        print(r)
else:
    print(result)

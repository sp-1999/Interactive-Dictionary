import json
from difflib import get_close_matches

data = json.load(open(r"C:\Users\SANGAM PRASAD\Desktop\project python\Interactive Dictionary\data.json"))

def translate(w):
    w = w.lower()
    if w in data:
        return data[w]
    elif len(get_close_matches(w, data.keys(),cutoff=0.8)) > 0:
        yn = input("Did you mean {} instead? Enter Y if yes, or N if no: ".format(get_close_matches(w, data.keys())[0]))
        if yn == "Y":
            return data[get_close_matches(w, data.keys())[0]]
        elif yn == "N":
            return 0
        else:
            return "We didn't understand your entry."
    else:
        return 0

word = input("Enter word: ")
output = translate(word)
if(output==0):
    print("Warning! The word doesn't exist. Please double check it.")
else:
    print("Meaning:")
    if type(output) == list:
        for i in range(len(output)):
            print(f"{i+1} --> {output[i]}")
    else:
        print(output)

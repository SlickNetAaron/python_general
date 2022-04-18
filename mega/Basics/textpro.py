# while loop until secret code
# input, 
    # if not secret code, 
    #   append input to list
    #   continue
    # if secret code, break

# for sayings in said
#   if a question,
#       set punctuation to "?"
#   else
#       set punctuation to "."
#   print saying, capitalized and with punctuation, no line break

def sentence_maker(phrase):
    interrogatives = ("how", "what", "why")
    capitalized = phrase.capitalize()
    if phrase.startswith(interrogatives):
        return "{}?".format(capitalized)
    else:
        return "{}.".format(capitalized)

# inline test
# print(sentence_maker("how are you"))

results = []
while True:
    user_input = input("Say something: ")
    if user_input == "\end":
        break
    else:
        results.append(sentence_maker(user_input))

print(results)

print(" ".join(results))
# How the heck does this get all items in the list?
# Why isn't there a space at the beginning?
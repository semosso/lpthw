import random
from urllib.request import urlopen # FROM urllib, get the "something" (e.g., class) REQUEST, and from that something import "something else" (e.g., function) urlopen
import sys

WORD_URL = "http://learncodethehardway.org/words.txt" # why all caps?
WORDS = []

PHRASES = {
    "class %%%(%%%):":
     "Make a class named %%% that is-a %%%.",
    "class %%%(object):\n\tdef __init__(self, ***)" : # why space before colon?
     "class %%% has-a __init__ that takes self and *** params.",
    "class %%%(object):\n\tdef ***(self, @@@)":
     "class %%% has-a function *** that takes self and @@@ params.",
    "*** = %%%()":
     "Set *** to an instance of class %%%.",
    "***.***(@@@)":
     "From *** get the *** function, call it with params self, @@@.",
    "***.*** = '***'":
     "From *** get the *** attribute and set it to '***'." # does this mean to change whatever is inside the class? i.e., change the class attribute?
}                                                          # or does it mean to take the value that's within the class attribute and assign it to what's after =?

# do they want to drill phrases first
if len(sys.argv) == 2 and sys.argv[1] == "english": # i.e., if i run the script with "english" as an additional parameter from the terminal
    PHRASE_FIRST = True
else:
    PHRASE_FIRST = False

# load up the words from the website
for word in urlopen(WORD_URL).readlines():
    WORDS.append(str(word.strip(), encoding="utf-8"))
    # what does strip() method do? A: remove both leading and trailing char (leading being \n in the list)


def convert(snippet, phrase):
    class_names = [w.capitalize() for w in
                   random.sample(WORDS, snippet.count("%%%"))] # first parameter of sample is sequence, second is how many elements should be chosen
    other_names = random.sample(WORDS, snippet.count("***"))
    results = []
    param_names = []

    for i in range(0, snippet.count("@@@")):
        param_count = random.randint(1,3) # this is what makes some examples have more than one parameter 
        param_names.append(", ".join(
            random.sample(WORDS, param_count)))
    
    for sentence in snippet, phrase:
        result = sentence[:] # Zed: "this is Python's way to copy a list" // no idea what this is doing

        # fake class names
        for word in class_names: # with ln 36, each time you found a %%%, you added a WORD; now you're replacing those %%% with the words
            result = result.replace("%%%", word, 1)
        # wouldn't the "result" from ln 52 be replaced by the results the "result" assignment from the other for statements?
        # actually not really, results is not a string, it's a list; what its doing is replacing specific words (%%, **, @@) with the applicable words (class, params, etc.)

        # fake other names
        for word in other_names:
            result = result.replace("***", word, 1)
        
        # fake parameter lists
        for word in param_names:
            result = result.replace("@@@", word, 1)
        
        results.append(result)

    return results


# keep going until they hit CTRL-D
try:
    while True: # loop eterno, except if I stop it with cmd-D or cmd-C
        snippets = list(PHRASES.keys())
        random.shuffle(snippets) # does this change snippets itself? I thought you'd need a new variable

        for snippet in snippets:
            phrase = PHRASES[snippet]
            question, answer = convert(snippet, phrase)
            if PHRASE_FIRST:
                question, answer = answer, question
            
            print(question)

            input("> ")
            print(f"ANSWER:  {answer}\n\n")
except EOFError:
    print("\nBye")
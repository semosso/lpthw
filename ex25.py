# important lesson: start programs with letters, no other characters (will return exception if number or other char)
def break_words(stuff):
    """This funcion will break up words for us.""" # these are DOCUMENTATION COMMENTS, notice they are loose strings
    words = stuff.split(' ')
    return words

def sort_words(words):
    """Sorts the words."""
    return sorted(words)
    # Python has native sorting through .sort() method or sorted() function
    # you can feed a key='' parameter to specify how to sort; KEY specifies a function to be called on each element prior to comparison
    # one such argument can be LAMBDA, a "one line function" (or anonymous function) -- lambda ARGUMENT: manipulate(argument)
    ## lambda x, y (i.e., ARGUMENT): x + y (i.e., WHAT TO DO WITH ARGUMENT)

def print_first_word(words):
    """Prints the first word after popping it off."""
    word = words.pop(0) # pop similar to pop in bash? if so, can I use similar modifiers?
    print(word)
    # p. 93, 'how can the words.pop method change the variable itself?'
    # in this case, words is a list, and because of that you can give it commands, and it'll retain the results of those commands 

def print_last_word(words):
    """Prints the last word after popping it off."""
    word = words.pop(-1) # ln 12: seems so... 0 and -1 would be positional arguments; 0 is first (L-R), -1 last (R-L)
    print(word)

def sort_sentence(sentence):
    """Takes in a full sentence and returns the sorted words."""
    words = break_words(sentence) # this will call BREAK and use it on SENTENCE argument
    return sort_words(words) # this will take RETURN of BREAK and use it as an argument of SORT function I created

def print_first_and_last(sentence):
    """Prints the first and last words of the sentence."""
    words = break_words(sentence)
    print_first_word(words)
    print_last_word(words)

def print_first_and_last_sorted(sentence):
    """Sorts the words then prints the first and last one."""
    words = sort_sentence(sentence)
    print_first_word(words)
    print_last_word(words)
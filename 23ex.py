# 1, how modern computers store human languages for display and processing and how Python calls this strings; 2, how you must encode and
# decode Python strings into a type called bytesl; 3, how to handle errors in your string and byte handling; 4, how to read code and 
# find out what it means even if you've never seen it before
import sys # imports the whole SYS library, not only ARGV like we've done before
script, input_encoding, error = sys.argv # "from the whole SYS library you imported above, use ARGV"?
# if I had used 'from sys import *' or even ARGV, wouldn't need 'sys.' above

def main(language_file, encoding, errors):
# it doesn't matter that I use same name for parameters in main and print_line, they are specific to each single function
    line = language_file.readline() # READLINE reads line until \n or end of file (EOF)

    if line: # is this here just in case READLINE reaches EOF? i.e., in which case READLINE would read nothing (or result in exception?)
             # i.e., I'm assuming that this meant "if line has any actual value assigned to it"
             # p. 83, yep, exactly right
        print_line(line, encoding, errors)
        return main(language_file, encoding, errors)
        # what does this do? RETURN of MAIN is calling MAIN again? Or "use the return from print_line as parameters for main"?
        # the first one; it means that calling MAIN again (it doesn't run forever, since IF is a EOF check, as cmmts above)


def print_line(line, encoding, errors):
    next_lang = line.strip() # STRIP is a METHOD of the line OBJECT; what does it do? A: strips \n after each line
    # it actually removes both leading (i.e., leftmost) and trailing (i.e., rightmost) characters 
    raw_bytes = next_lang.encode(encoding, errors=errors)
    # 1: what does ERRORS = ERRORS mean? what does it do? does it mean "when you run method encode, based on a given CODEX (i.e., a 
    # encoding standard you specify), assign any errors you get from that encoding process to the variable ERRORS? it's also something
    # I have to feed when running the script; see last comments for clarification (it's actually WHAT TO DO)
    # 2: what does encode do? I'll have to feed what type of "encoding standard" I need when I run the program from terminal
    # 3: p. 83 and layman: DECODE turns bytes into UTF strings; ENCODE turns UTF strings into bytes (DEEBEES)
    cooked_string = raw_bytes.decode(encoding, errors=errors) # similar to rationale above

    print(raw_bytes, '<===>', cooked_string) # this means print the ENCODED version, the middle string, and then the DECODED version
    # this should happen for every line inside the "language.txt" file, since MAIN will feed print_line one line at a time


languages = open('languages.txt', encoding='utf-8') # what if different than the standard I choose when I run the program? 

main(languages, input_encoding, error) # from example on p. 79, "error" seems to be a standard of error (or what to do when finding 
# errors) that I also get to decide when running the program; pp. 84-85 confirm this perception; if "mode" STRICT, Python acusa o erro; if
# "mode" REPLACE, it replaces the errors with a ? 
import sys # imports the whole SYS library, not only ARGV like we've done before
script, input_encoding, error = sys.argv # sys.argv means "from the whole SYS library you imported above, use ARGV"?


def main(language_file, encoding, errors):
    line = language_file.readline() # READLINE reads line until \n or end of file (EOF)

    if line: # is this here just in case READLINE reaches EOF? i.e., in which case READLINE would read nothing (or result in exception?)
             # i.e., I'm assuming that this meant "if line has any actual value assigned to it"
             # p. 83, yep, exactly right
        print_line(line, encoding, errors)
        return main(language_file, encoding, errors)


def print_line(line, encoding, errors):
    next_lang = line.strip() # STRIP is a METHOD of the line OBJECT; what does it do? A: strips \n after each line
    raw_bytes = next_lang.decode(encoding, errors=errors) # if OPEN mode on 23 is 'br', this has be DECODE and not ENCODE
    cooked_string = raw_bytes.encode(encoding, errors=errors)

    print(raw_bytes, '<===>', cooked_string, ) # this means print the ENCODED version, the middle string, and then the DECODED version


languages = open('llanguages.txt', 'br') # it doesn't matter what the contents of the file are, only the MODE you assign to function OPEN

main(languages, input_encoding, error)
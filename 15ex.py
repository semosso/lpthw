from sys import argv
# sys is a module/library; this says "from library SYS, import ARGV - an argument variable"
# sys is a package, ln 1 says to call the ARGV feature from that package
    
script, filename = argv

txt = open(filename) # function OPEN opens whatever you assigned to FILENAME when you ran from terminal, and assigns it to TXT

print(f'Here\'s your file {filename}:') # f = FORMAT function, tells python to call the variable FILENAME 
print(txt.read()) # '.read()' calls the function READ to act on variable TXT (function, command, method are interchangeable names)

# ln 10-15 do the same as 1-8, but with INPUT and not ARGV 
print('Type the filename again:')
file_again = input('> ') # the change is that you don't need to give argument (i.e., file name) on terminal when you run program

txt_again = open(file_again)
# this makes a FILE OBJECT, which is not the same as the file CONTENTS
#file object is the DVD player, contents are the DVD

print(txt_again.read())
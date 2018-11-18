# STUDY DRILLS
# SD6: working from python in terminal, READ by itself doesn't do anything (OPEN, however, does, and it's even called a function)
## also, I can't go with simply open(ex15_sample.txt) because the _, period, etc, mess up
### you have to assign it to a variable, e.g., this is how you'd run something similar FROM PYTHON WITHIN THE TERMINAL
### txt = open(input()) 
### print(txt.read()) 
# Would the following work? YES IT DOES!
txt = open(input('Type the filename:\n> '))
print(txt.read())

# SD7: it's important to close files when you're done with them, so add close(VARIABLE)
## what if you close between OPEN and PRINT? would that work?
txt = open(input('Type the filename:\n> '))
txt.close() # por que eu não consigo usar close(txt), como uso open(txt)??
## Takai: close é metodo do objeto. open é função global; pra fechar, voce tem que falar pro objeto que voce abriu "fechae"
## Rufflez: você “precisa” do open global pra poder instanciar um objeto do tipo file, que por sua vez vai ter o metodo close
print(txt.read()) # nope, I get an error because print is attempting to access a file that's already been closed
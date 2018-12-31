# this
mystuff = {"apple": "I AM APPLES!"}
print(mystuff["apple"])

# is the same as this, because there I defined the apple function as being print("I AM APPLES!")
import mystuff
mystuff.apple() # note difference between 7 and 8; 7 is calling a FUNCTION from MODULE mystuff; 8 is calling a variable defined there
print(mystuff.tangerine)

# very common pattern in Python: 1, take a key=value style container; 2, get something out of it by the key's name
# e.g., in a dict, the key is a string and the syntax is [key]; in a module, key is an identifier, and the syntax is .key (dot)
# class is similar: take functions and data and place inside a class, and access them with . (dot)

class MyStuff(object):

    def __init__(self):
        self.tangerine = "And now a thousand years between" # SELF refers to the class itself

    def apple(self):
        print("I AM CLASSY APPLES!")

# if a class is a mini-module, there has to be a concept similar to IMPORT for classes; it's called INSTANTIATE (i.e., create); when you INSTANTIATE, you get an OBJECT
thing = MyStuff()
thing.apple() # remember the idea of "with open("doc.txt") as f", f would work just like THING here
print(thing.tangerine)

# Getting Things from Things
# dict style
print(mystuff["apple"]) # pylint shows "error" because ln 6 imports a module of the same name as the dict, and it gets confused, but it's fine

# module style
import mystuff
mystuff.apple()
print(mystuff.tangerine)

# class style
thing = MyStuff()
thing.apple()
print(thing.tangerine)

# actual exercise on p. 150
class Song(object):

    def __init__(self, lyrics): # what does __init__ do? why do I need __init__ or even this whole self.lyrics = lyrics structure? 
        self.lyrics = lyrics

    def sing_me_a_song(self):
        for line in self.lyrics: # line could as well be x, or i, or whatever; so it's not really going by LINE, but by item inside LIST
            print(line)
    
happy_bday = Song(["Happy birthday to you",
                   "I don't want to get sued",
                   "So I'll stop right there"])

bulls_on_parade = Song(["They rally around tha family",
                        "With pockets full of shells"])

happy_bday.sing_me_a_song() # happy_bday jas already been assigned SONG class (or object?) when I created the variable; same with bulls...

bulls_on_parade.sing_me_a_song()

# STUDY DRILLS
# SD 2: put lyrics in separate variable, then pass that variable to the class to use instead
rebirth = ["cooling breeze from a summer day", "hearing echoes from my heart", "learning how to recompose the world", "let time just fly"]
Song(rebirth).sing_me_a_song()
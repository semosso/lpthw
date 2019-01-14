class Scene(object):

    def enter(self):
        print("nothing, just template for specific scenes")
        exit(1) # why the exit(1)?
    

class Engine(object):

    def __init__(self, scene_map):
        self.scene_map = scene_map # when I call a class like this (within a class) is it still called instantiate?
    
    def play(self):
        current_scene = self.scene_map.opening_scene()
        last_scene = self.scene_map.next_scene("finished") # i.e., KEY that references VALUE "Finished" in scenes DICT from Map class

        while current_scene != last_scene:
            next_scene_name = current_scene.enter() # this is where the magic happens; this shows the current scene and gets inputs to move to next
            current_scene = self.scene_map.next_scene(next_scene_name)
        
        current_scene.enter() # this only happens in FINISHED scene

class Death(Scene):

    def enter(self):
        print("you died")
        exit(1) # why the exit(1)?

class CentralCorridor(Scene):

    def enter(self):
        print("narrativa, ask for input")
        action = input("> ")

        if action == "boa":
            print("narrativa de sucesso")
            return "armory" # this will be passed to functions defined within Map class, which will keep the game going
        
        elif action == "errada":
            print("narrativa de fracasso")
            return "death" # these are keys to a dict inside Map class; next_scene will look at the key, and return the value
        
        else:
            print("wrong input")
            return "corridor"

class LaserWeaponArmory(Scene):

    def enter(self):
        print("narrativa, ask for input") # no caso do jogo do Zed, prompt de passcode no keypad com um while-loop, estudar
        code = input("> ")

        if code == "code certo":
            print("narrativa de sucesso")
            return "bridge"
        
        else:
            print("narrativa de fracasso")
            return "death"
    
class TheBridge(Scene):

    def enter(self):
        print("narrativa, ask for input")
        action = input("> ")

        if action == "boa":
            print("narrativa de sucesso")
            return "pod" # this will be passed to functions defined within Map class, which will keep the game going
        
        elif action == "errada":
            print("narrativa de fracasso")
            return "death" # these are keys to a dict inside Map class; next_scene will look at the key, and return the value
        
        else:
            print("wrong input")
            return "bridge"

class EscapePod(Scene):

    def enter(self):
        print("narrativa, com prompt") # no caso do Zed, prompt era para escolher qual pod funcionava, importanto random
        choice = input("> ")

        if choice == "certa":
            print("narrativa de sucesso")
            return "finished" # without this, there's a problem when you run engine; you could add an if-loop above there to solve it, I think
                              # e.g., if current_scene == last_scene, print("sucesso"), else: while-loop?
                              # maybe this way is more efficient, clean, etc.?
        
        else:
            print("narrativa de fracasso")
            return "death"

class Finished(Scene):
    
    def enter(self):
        print("you won")
        return "finished" # isn't this duplicative of return from EscapePod's enter function? how will Engine deal with this?

class Map(object):

    scenes = {
        "corridor": CentralCorridor(),
        "armory": LaserWeaponArmory(),
        "bridge": TheBridge(),
        "pod": EscapePod(),
        "death": Death(),
        "finished": Finished()
    }

    def __init__(self, start_scene): # this means "when you instantiate the empty object, initialize it with a variable start_scene set to parameter you called Map with"
        self.start_scene = start_scene

    def next_scene(self, scene_name):
        val = Map.scenes.get(scene_name) # GET(param) is a dict method that says "get me the value that is assigned to key param in dict"
        return val                       # why not use "self" instead of map? because then you would look for a dict in each specific Map instance, and they don't have it?
                                         # I think this gets at the CORE of classes/objects - with self, every object can have its own without messing the others
    def opening_scene(self):
        return self.next_scene(self.start_scene)


a_map = Map("corridor")
a_game = Engine(a_map)
a_game.play()

# explaining ln 123-125:
# 123: INSTANTIATES a_map OBJECT that is-a MAP (class), with an attribute start_scene set to "corridor"
# 124: INSTANTIATES a_game OBJECT, with an attribute scene_map set to "a_map"
# 125:
# 1, calls play FUNCTION with no additional parameters
# 2, play FUNCTION calls opening_scene METHOD from a_map OBJECT, with no additional parameters
# 2.1, opening_scene FUNCTION calls next_scene FUNCTION, with "corridor" as parameter (start_scene was given "corridor" value by __init__ function in ln 123)
# 2.2, next_scene FUNCTION searches scenes DICT for VALUE associated with "corridor" KEY and assigns CentralCorridor() to current_scene attribute
## note how DICT is fixed in class Map, not specific to each instance (se ln 116, it's "Map.scenes", not "self.scenes")
# 3, last_scene VARIABLE is hard set to "finished"
# 3, while LOOP runs as long as current_scene IS NOT equal to value associated with finished key (first iteration is CentralCorridor != Finished(), so true and it runs)
# 4.1, next_scene_name calls METHOD enter() from the CentralCorridor OBJECT that is-a SCENE (class); this is where the magic happens, this is the first message the user sees
# 4.2, enter() METHOD returns either a next step ("armory"), failure ("death"), or repeats prompt ("corridor")
# 4.3, current_scene calls METHOD next_scene from a_map OBJECT with next_scene_name (i.e., armory, death or corridor) as parameter
# 5, next_scene FUNCTION searches scenes DICT for VALUE associated with KEY received from current_scene and assigns such VALUE to current_scene attribute
# 6, while LOOP keeps repeating until next_scene FUNCTION returns Finished(), in which case python jumps to ln 21 and calls ENTER method from Finished()
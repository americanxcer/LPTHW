class Scene(object):
    def __init__(self, title, urlname, category, description,): #added category
        self.title = title
        self.urlname = urlname
        self.category = category
        self.description = description
        self.paths = {}

    def go(self, direction):
        default_direction = None #userinput
        if '*' in self.paths.keys():
            default_direction = self.paths.get('*')
        return self.paths.get(direction, default_direction) # geting value by key from the "paths" dictionary

    def add_paths(self, paths):
        self.paths.update(paths)

# Create the scenes of the game
central_corridor = Scene("Central Corridor", "central_corridor", "begin",
"""
The Gothons of Planet Percal #25 have invaded your ship and destroyed
your entire crew. You are the last surviving member (oh noes!) and your
last mission is to get the neutron destruct bomb from the Weapons Armory,
put it in the bridge, and blow up the ship after getting into an escape pod.

You're now running down the central corridor to the Weapons Armory when a
Gothon hops out in an evil clown costume filled with hate. He's blocking the door
to the Armory and about to pull a weapon to blast you.
""")

shoot_death = Scene("Shoot Death", "shoot_death", "end",
"""
Quick on the draw you yank out your blaster and fire it at the Gothon.
His clown costume is flowing and moving around his body, which throws
off your aim.  Your laster hits his costume but misses him entirely.  This makes him fly into an insane rage and blast you repeatedly in the face until"
you are dead.  Then he eats you.

You died. You kinda suck at this.
""")

dodge_death = Scene("Dodge Death", "dodge_death", "end",
"""
Like a world class boxer you dodge, weave, slip and slide right
as the Gothon's blaster cranks a laser past your head.
In the middle of your artful dodge your foot slips and you
bang your head on the metal wall and pass out.
You wake up shortly after only to die as the GOthon stomps on
your head and eats you.

You died. You kina suck at this.
""")

laser_weapon_armory = Scene("Laser Weapon Armory", "laser_weapon_armory", "normal",
"""
Lucky for you they made you learn Gothon insults in the academy.
You tell the one Gothon joke you know:
Lbhe zbgure vg fb sng, jura fur vfvg nebhaq gut ubhfr, fur fvgf nebhaq gut ubhfr.
The Gothon bursts into laughter and rolls around on the ground. While its
laughing you run up and use your copy of Nietzsche's notebooks (translated into Gothon)
to lecture the Gothon on the shaky foundations of its ideologies. While it tries
to cope with its existential crisis, you leap through the Weapon Armory door.

You dive roll into the Weapon Armory, crouch and scan the room for more Gothons
that might be hiding. It's dead quiet, too quiet.
You stand up and run to the far side of the room and find the neutron bomb in its
container. There's a keypad lock on the box and you need the code to get the bomb
out. If you get the code wrong 10 times then the lock closes forever and you can't
get the bomb. The code is 3 digits.
""")

code_fail_death = Scene("Code Fail Death", "code_fail_death", "end",
"""
The lock buzzes one last time and then you hear a sickening
meling sound as the mechanism is fused together.
you decide to sit there, and finally he Gothons blow up the
ship from their ship and you die.

You died. You kinda suck at this.
""")

the_bridge = Scene("The Bridge", "the_bridge", "normal",
"""
The container clicks open and the seal breaks, letting gas out. You grab the
neutron bomb and run like heck to the bridge where you place it in the right spot.

You burst into the Bridge with the bomb under your arm and surprise 5 Gothons
who are trying to take control of the ship. Each of them has an uglier clown costume
that the last. They don't pull their weapons out of fear that they will set off
the bomb under your arm.
""")

throw_death = Scene("Throw Death", "throw_death", "end",
"""
In a panic you throw the bomb at the group of Gothons
and make a leap for the door.  Right as you drop it a
Gothon shoots you right in the back killing you.
As you die you see another Gothon frantically try to disarm
the bomb.  You die knowing they will probably blow up when
it goes off.

You died.  You kind suck at this.
""")

escape_pod = Scene("Escape Pod", "escape_pod", "normal",
"""
You gesture towards the bomb and threaten to set it off, the Gothons put up
their arms and ask for a truce. You inch backwards to the door, open it, and
carefully place the bomb on the floor, waving your finger over the detonate button.
Then you jump back through the door, hit the close button and zap the lock so they
can't get out. Now that the bomb is placed you run to the escape pod.

You rush through the ship desperately trying to make it to the escape pod. It seems
like there's no Gothons around, so you run as fast as possible. Eventually you reach
the room with the escape pods, and you now need to pick one to take. Some of them could
be damaged, but you don't have time to look. There's 5 pods, which one do you take?
""")

the_end_winner = Scene("You Made It!", "the_end_winner", "end",
"""
You jump into pod 2 and hit the eject button. The pod flies out into space heading
to the planet below. As you're heading down, you look back and see your ship implode
and then explode like a supernova, taking down the Gothon ship at the same time.
You made it!
""")

the_end_loser = Scene("...", "the_end_loser", "end",
"""
You jump into a random pod and hit the eject button. The pod escapes into space
but there's a crack in the hull. Uh oh. The pod implodes and you with it.
""")

generic_death = Scene("Death...", "death", "end",
"You died.  You kinda suck at this.")

# Define the action commands available in each Scene, filling the dictionary
escape_pod.add_paths({  #i think there needs to be an if '' in statement here, how? Do i change everything here into objects and classes?
    '2': the_end_winner,
    '*': the_end_loser
})

the_bridge.add_paths({
    'throw the bomb': throw_death,
    'slowly place the bomb': escape_pod
})

laser_weapon_armory.add_paths({
    '132': the_bridge,
    '*': code_fail_death
})

central_corridor.add_paths({
    'shoot!': shoot_death,
    'dodge!': dodge_death,
    'tell a joke': laser_weapon_armory
})

# Make some useful variables to be used in the web application
SCENES = {
    central_corridor.urlname : central_corridor,
    shoot_death.urlname : shoot_death,
    dodge_death.urlname : dodge_death,
    laser_weapon_armory.urlname : laser_weapon_armory,
    code_fail_death.urlname : code_fail_death,
    the_bridge.urlname : the_bridge,
    throw_death.urlname : throw_death,
    escape_pod.urlname : escape_pod,
    the_end_winner.urlname : the_end_winner,
    the_end_loser.urlname : the_end_loser,
    generic_death.urlname : generic_death
}
START = central_corridor

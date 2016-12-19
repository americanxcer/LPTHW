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

intro = Scene("Get Chyo DrAnK OwN - Version 2.0", "intro", "begin",
"""This is a simple game with the goal of getting you virtually drunk
and having a good night!  Simply type your answer in the text field and hit
"SUBMIT" to submit your answer. IF you need HELP making up your mind, simply
type "help" in the text field.  So go on and Get Chyo Drank OwN!
________________________________________________________________________________
It's Friday night and you want to get hammered!
You've had a long-ass week and need to consume alcoholic beverages
to calm your burnt-out self down.

Do you want to go out or stay home?
""")

outside = Scene("You're Going Out and About", "outside", "normal",
"""Oyoiyoi ... The train isn't running due to the HVV being complete crap.
Well, the Rewe down the street is still open
and there's a soccer bar around the corner.
You want to get your drank on, right now!

Where do you go?
""")

rewe = Scene("You've Made it Inside Rewe", "rewe", "normal",
"""Ohhaohaoha...Rewe ist packed!
..and you're still sober!
What is this, gradeschool?
Forget about the beer, just get in line at the register
and grab whatever hard liquor is at kids' reach
(way to go Germany..).
-----------------------------------
Alrgiht, now you're back outside
and your nipps are about to freeze off!
Where are you going to go now?
Time for the soccer bar,
or are you done with the world and want to just go home?
""")

way_bar = Scene("On the Way to the Bar", "way_bar", "normal",
"""You managed to grab a box of some good ol' German Schnapps!
These 12 little babies are gonna get you in the right kind of mood.
You have about a 5 to 10 minute walk ahead of you..
How many mini bottles of goodness will you gulp down on the way?
""")

way_inside = Scene("On the Way Home", "way_inside", "normal",
"""You managed to grab a box of some good ol' German Schnapps!
These 12 little babies are gonna get you in the right kind of mood.
You have about a 5 to 10 minute walk ahead of you..
How many mini bottles of goodness will you gulp down on the way?
""")

way_drunk = Scene("You Drank too Much on the Way", "way_drunk", "end",
"""Well, I mean you did want to get wierd tonight,
but this just escalated far too quickly!  You need
to get ahold of yourself!  Now you've thrown your cookies
all over the sidewalk..Though I am a bit proud of you, you better just
go home and sleep..if you can find your way.
""")

inside_buzzed = Scene("Back at Home", "inside_buzzed", "normal",
"""Now you're a little buzzed and all warm in your humble abode!
You could kick it here with ya bad self, or ask if some peeps want to
come over.
Do you want to invite people to come get wrecked with you?
""")

inside_buzzed_invite = Scene("You're Buzzed! Invite People Over!", "inside_buzzed_invite", "end",
"""Congrats..
Both of your two friends are busy.
Well, so much for trying to be social!
Guess you'll be hanging out alone after all.
---------------------------------------------
Time to watch episodes of 'Intervention'
and drink everytime someone makes a worse life choice
than you have!

Yay for not being at the very bottom!
""")

inside_buzzed_alone = Scene("You're Buzzed, Who Needs People?", "inside_buzzed_alone", "end",
"""Now you're a little buzzed and all warm in your humble abode!
Time to watch episodes of 'Intervention'
and drink everytime someone makes a worse life choice
than you have!

Yay for not being at the very bottom!
""")

inside_sober = Scene("Stayin' In", "inside_sober", "normal",
"""Alright alright alright.
You could kick it here with ya bad self, or ask if some peeps want to
come over.
Do you want to invite people to come get wrecked with you?
""")

inside_sober_invite = Scene("Let's Invite People Over", "inside_sober_invite", "end",
"""Wow you're feeling socially acceptable today!
Three people are now at your place and you don't have much alcohol.
Way to go, you anti-social worm.
You're not drunk enough to be entertaining!
You forgot you can't handle being responsible for social encounters.
Akwardness
Overwhelms
You!

You're an anxious mess.
""")

inside_sober_alone = Scene("People are Gross", "inside_sober_alone", "end",
"""Wohoo! Time to drink what you've got and play some sweet video games until your eyes bleed!
Who needs other people to enjoy themselves?
Being socially awkward rules!
And the best part is:
You don't have to wear pants!

This is the (anti-social) life!
""")

bar_buzzed = Scene("You're Buzzed at this Bitchin' Bar", "bar_buzzed", "end",
"""On the way to the bar, you see the disco lights flashing
and you can here the German Schlager music being accompanied
by the voices of old people.
Nice.

The few bottles of liquor you drank are kicking in just in time!
You've consumed the perfect amount for this kind of thing!
Once you get in the bar everyone cheers, even though you don't know them!
Some old lady is celebrating the death of her husband and buying rounds
for everyone.

You hit the party jackpot! """)

bar_sober = Scene("You're too Sober for this Bar", "bar_sober", "end",
"""So now you're inside, and people seem to be having a good time.
The problem is: they are drunk; you are not!
You then realize that you can't pay with card here
and you don't have enough cash for a drink..
Even if you brought booze with you, you wouldn't be able to
drink it in here.  Way to go..
Because you're too sober to be socially acceptable, you can't
find the courage to ask the people celebrating if you can join.

You're uncomfortable and go home as the anxious mess that alaways had been.
""")

help_out_in = Scene("Do you need some help?", "help_out_in", "normal",
"""Don't over think it!  Type in the text field either
- "go out"
or
- "stay home"

""")

help_rewe_bar = Scene("Do you need some help?", "help_rewe_bar", "normal",
"""Don't over think it!  Type in the text field either
- "to Rewe"
or
- "to the soccer bar"
""")

help_home_bar = Scene("Do you need some help?", "help_home_bar", "normal",
"""Don't over think it!  Type in the text field either
- "home"
or
- "the soccer bar"
""")

help_way_bar = Scene("Do you need some help?", "help_way", "normal",
"""Don't over think it!  Type in the text field a number between 0 and 12.
""")

help_way_inside = Scene("Do you need some help?", "help_way", "normal",
"""Don't over think it!  Type in the text field a number between 0 and 12.
""")

help_invite_sober = Scene("Do you need some help?", "help_invite", "normal",
"""Don't over think it!  Type in the text field either
- "yes"
or
- "no"
""")

help_invite_buzzed = Scene("Do you need some help?", "help_invite", "normal",
"""Don't over think it!  Type in the text field either
- "yes"
or
- "no"
""")


# Define the action commands available in each Scene, filling the dictionary
intro.add_paths({
    'go out' : outside,
    'out' : outside,
    'stay home' : inside_sober,
    'home' : inside_sober,
    'help' : help_out_in
})

help_out_in.add_paths({
    'go out' : outside,
    'out' : outside,
    'stay home' : inside_sober,
    'home' : inside_sober
})

outside.add_paths({
    'rewe': rewe,
    'Rewe': rewe,
    'to rewe': rewe,
    'to Rewe': rewe,
    'the bar': bar_sober,
    'the soccer bar': bar_sober,
    'bar': bar_sober,
    'soccer bar': bar_sober,
    'help': help_rewe_bar
})

help_rewe_bar.add_paths({
    'rewe': rewe,
    'Rewe': rewe,
    'to rewe': rewe,
    'to Rewe': rewe,
    'the bar': bar_sober,
    'the soccer bar': bar_sober,
    'bar': bar_sober,
    'soccer bar': bar_sober
})

rewe.add_paths({
    'the bar': way_bar,
    'the soccer bar': way_bar,
    'bar': way_bar,
    'soccer bar': way_bar,
    'go home': way_inside,
    'just go home': way_inside,
    'home': way_inside,
    'help': help_home_bar
})

help_home_bar.add_paths({
    'the bar': way_bar,
    'the soccer bar': way_bar,
    'bar': way_bar,
    'soccer bar': way_bar,
    'go home': way_inside,
    'just go home': way_inside,
    'home': way_inside
})

way_bar.add_paths({
    '0': bar_sober,
    '1': bar_sober,
    '2': bar_sober,
    '3': bar_buzzed,
    '4': bar_buzzed,
    '5': bar_buzzed,
    '6': bar_buzzed,
    '7': bar_buzzed,
    '8': way_drunk,
    '9': way_drunk,
    '10': way_drunk,
    '11': way_drunk,
    '12': way_drunk,
    'help': help_way_bar
})

help_way_bar.add_paths({
    '0': bar_sober,
    '1': bar_sober,
    '2': bar_sober,
    '3': bar_buzzed,
    '4': bar_buzzed,
    '5': bar_buzzed,
    '6': bar_buzzed,
    '7': bar_buzzed,
    '8': way_drunk,
    '9': way_drunk,
    '10': way_drunk,
    '11': way_drunk,
    '12': way_drunk,
})

way_inside.add_paths({
    '0': inside_sober,
    '1': inside_sober,
    '2': inside_sober,
    '3': inside_buzzed,
    '4': inside_buzzed,
    '5': inside_buzzed,
    '6': inside_buzzed,
    '7': inside_buzzed,
    '8': way_drunk,
    '9': way_drunk,
    '10': way_drunk,
    '11': way_drunk,
    '12': way_drunk,
    'help': help_way_inside
})

help_way_inside.add_paths({
    '0': inside_sober,
    '1': inside_sober,
    '2': inside_sober,
    '3': inside_buzzed,
    '4': inside_buzzed,
    '5': inside_buzzed,
    '6': inside_buzzed,
    '7': inside_buzzed,
    '8': way_drunk,
    '9': way_drunk,
    '10': way_drunk,
    '11': way_drunk,
    '12': way_drunk
})

inside_buzzed.add_paths({
    'yes': inside_buzzed_invite,
    'Yes': inside_buzzed_invite,
    'no': inside_buzzed_alone,
    'No': inside_buzzed_alone,
    'help': help_invite_buzzed
})

help_invite_buzzed.add_paths({
    'yes': inside_sober_invite,
    'Yes': inside_sober_invite,
    'no': inside_sober_alone,
    'No': inside_sober_alone
})

inside_sober.add_paths({
    'yes': inside_sober_invite,
    'Yes': inside_sober_invite,
    'no': inside_sober_alone,
    'No': inside_sober_alone,
    'help': help_invite_sober
})

help_invite_sober.add_paths({
    'yes': inside_sober_invite,
    'Yes': inside_sober_invite,
    'no': inside_sober_alone,
    'No': inside_sober_alone
})



# Make some useful variables to be used in the web application
SCENES = {
    intro.urlname : intro,
    outside.urlname : outside,
    rewe.urlname : rewe,
    way_bar.urlname : way_bar,
    way_inside.urlname : way_inside,
    way_drunk.urlname : way_drunk,
    inside_buzzed.urlname : inside_buzzed,
    inside_buzzed_invite.urlname : inside_buzzed_invite,
    inside_buzzed_alone.urlname : inside_buzzed_alone,
    inside_sober.urlname : inside_sober,
    inside_sober_invite.urlname : inside_sober_invite,
    inside_sober_alone.urlname : inside_sober_alone,
    bar_buzzed.urlname : bar_buzzed,
    bar_sober.urlname : bar_sober,
    help_out_in.urlname : help_out_in,
    help_rewe_bar.urlname : help_rewe_bar,
    help_home_bar.urlname : help_home_bar,
    help_way_bar.urlname : help_way_bar,
    help_way_inside.urlname : help_way_inside,
    help_invite_sober.urlname : help_invite_sober,
    help_invite_buzzed.urlname : help_invite_buzzed
}
START = intro # i think i need 2 map files for the first 2 decisions in the beginnig

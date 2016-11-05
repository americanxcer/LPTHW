from sys import exit

# Outside
def outside():
    print """
    Oyoiyoi ... The train isn't running due to the HVV being complete crap.
    Well, the Rewe around the corner is still open
    and there's a HSV bar around the corner.
    You want to get your drank on, right now!
    Where do you go?
    """
    choice = raw_input("> ")
    if choice == "Rewe":
        print "Off to Rewe!"
        Rewe()
    elif choice == "HSV bar":
        print "Off to the HSV bar!"
        bar_sober()
    else:
        die()

# Outsid - Rewe
def Rewe():
    print """
    Ohhaohaoha...Rewe ist packed!
    ..and you're still sober!
    What is this, gradeschool?
    Forget about the beer, just get in line at the register
    and grab whatever hard liquor is at kids' reach
    (way to go Germany..). \n
    \n
    Alrgiht, now you're back outside
    and your nipps are about to freeze off!
    Where are you going to go now?
    Time for the HSV bar,
    or are you done with the world and want to just go home?
    """
    choice = raw_input("> ")
    if choice == "HSV bar":
        print "To the HSV bar!"
        way_bar()
    elif choice == "go home":
        print "Homeward bound!"
        way_inside()
    else:
        die()

# Outside - Rewe - way to the bar
def way_bar():
    print """
    You managed to grab a box of some good ol' German Schnapps!
    These 12 little babies are gonna get you in the right kind of mood.
    You have about a 5 to 10 minute walk ahead of you..
    How many mini bottles of goodness will you gulp down on the way?
    """
    choice = raw_input("> ")
    how_much = int(choice)

    if how_much < 3:
        bar_sober()
    elif 6 > how_much >= 3:
        bar_buzzed()
    else:
        loose("""
        Well, I mean you did want to get wierd tonight,
        but this just escalated far too quickly!  You need
        to get ahold of yourself!  Now you've thrown your cookies
        all over the sidewalk..Though I am a bit proud of you, you better just
        go home and sleep..if you can find your way.
        """)

# Outside - Rewe - way back home
def way_inside():
    print """
    You managed to grab a box of some good ol' German Schnapps!
    These 12 little babies are gonna get you in the right kind of mood.
    You have about a 5 to 10 minute walk ahead of you..
    How many mini bottles of goodness will you gulp down on the way?
    """
    choice = raw_input("> ")
    how_much = int(choice)

    if how_much < 3:
        inside_sober()
    elif 6 > how_much >= 3:
        inside_buzzed()
    else:
        loose("""
        Well, I mean you did want to get wierd tonight,
        but this just escalated far too quickly!  You need
        to get ahold of yourself!  Now you've thrown your cookies
        all over the sidewalk..Though I am a bit proud of you, you better just
        go home and sleep..if you can find your way.
        """)

# Outside - Rewe - Inside(buzzed)
def inside_buzzed():
    print """
    Now you're a little buzzed and all warm in your humble abode!
    You could kick it here with ya bad self, or ask if some peeps want to
    come over.
    Do you want to invite people to come get wrecked with you?
    """
    choice = raw_input("> ")

    if choice == "yes":
        print "Okay, let's get this party goin'!"
        inside_buzzed_invite()
    elif choice == "no":
        print "There's only enough liquor for numero uno."
        inside_buzzed_alone()
    else:
        die()


# Outside - Rewe - Inside(buzzed) Invite
def inside_buzzed_invite():
    print """
    Congrats..
    Both of your two friends are busy.
    Well, so much for trying to be social!
    Guess you'll be hanging out alone after all.
    """
    inside_buzzed_alone()

# Outside - Rewe - Inside(buzzed) ALone
def inside_buzzed_alone():
    print """
    Now you're a little buzzed and all warm in your humble abode!
    Time to watch episodes of 'Intervention'
    and drink everytime someone makes a worse life choice
    than you have!
    """
    win("Yay for not being at the very bottom!")

# Inside (sober)
def inside_sober():
    print """
    Alright alright alright.
    You could kick it here with ya bad self, or ask if some peeps want to
    come over.
    Do you want to invite people to come get wrecked with you?
    """
    choice = raw_input("> ")

    if choice == "yes":
        print "It'll be nice to have some social interaction."
        inside_sober_invite()
    elif choice == "no":
        print "Ew gross, people are icky."
        inside_sober_alone()
    else:
        die()

# Inside (sober) invite
def inside_sober_invite():
    print """
    Wow you're feeling socially acceptable today!
    Three people are now at your place and you don't have much alcohol.
    Way to go, you anti-social worm.
    You're not drunk enough to be entertaining!
    You forgot you can't handle being responsible for social encounters.
    Akwardness.
    Overwhelms.
    You!
    """
    loose("You're an anxious mess.")

# Inside(sober) - Alone
def inside_sober_alone():
    print """
    Wohoo! Time to drink what you've got and play some sweet video games until your eyes bleed!
    Who needs other people to enjoy themselves?
    Being socially awkward rules!
    And the best part is:
    You don't have to wear pants!
    """
    win("This is the (anti-social) life!")


# Outside - Rewe - bar(buzzed)
def bar_buzzed():
    print """
    On the way to the bar, you see the disco lights flashing
    and you can here the German Schlager music being accompanied
    by the voices of old people.
    Nice.
    The few bottles of liquor you drank are kicking in just in time!
    You've consumed the perfect amount for this kind of thing!
    Once you get in the bar everyone cheers, even though you don't know them!
    Some old lady is celebrating the death of her husband and buying rounds
    for everyone.
    """
    win("You hit the party jackpot!")

# Outside - Bar(sober)
def bar_sober():
    print """
    So now you're inside, and people seem to be having a good time.
    The problem is: they are drunk; you are not!
    You then realize that you can't pay with card here
    and you don't have enough cash for a drink..
    Even if you brought booze with you, you wouldn't be able to
    drink it in here.  Way to go..
    Because you're too sober to be socially acceptable, you can't
    find the courage to ask the people celebrating if you can join.
    """
    loose("You're uncomfortable and go home as the anxious mess that alaways had been.")


# End of game, added to the variable of "why"
def win(why):
    print why, "  Bitchin'."
    exit(0)

def loose(why):
    print why, "  Laaame.."
    exit (0)

def die():
    print """
    How dare you think out of the box?! You die sober!!
    """


# Begining of game
def start():
    print """
    It's Friday night and you want to get hammered!
    Do you want to go out or stay home?
    """
    choice = raw_input("> ")

    if choice == "out":
        outside()
    elif choice == "stay home":
        inside_sober()
    else:
        die()

start()

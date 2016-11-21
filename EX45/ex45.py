from sys import exit
from random import randint


class Engine(object):

    def __init__(self, scene_map):
        self.scene_map = scene_map

    def play(self):
        current_scene = self.scene_map.opening_scene()
        last_scene = self.scene_map.next_scene('finished')

        while current_scene != last_scene:
            next_scene_name = current_scene.being()
            current_scene = self.scene_map.next_scene(next_scene_name)

        current_scene.being()

class Scene(object):

    def being(self): # I use "being" because it's less about entering
        print "Oops, this didn't get configured!" # and more about "being" in a scene
        exit(1)


class Fail(Scene):

    quips = [
    "You're going to get deported.",
    "Goodbye everything you've worked so hard for.",
    "Damn German bureaucracy, you win again.",
    "Deep breaths, I'm sure you'll figure something out."
    ]

    def being(self):
        print "You didn't get your Visa renewed!"
        print Fail.quips[randint(0, len(self.quips)-1)]
        exit(1)


class Finished(Scene):

    def being(self):
        print """TADA!!
            There it is!
            The imaginary crowd in your head cheers "AHHHH! YEAAHH! AHHH!"
            You got your student visa renewed!
            The registration office cann kiss your sweet, foreign ass goodbye!
            ...until next year. ;)
            """
        exit(1)


class Home(Scene):

    def being(self):
        print """
        It's that time of year again.
        Being a foreign student in Germany, you're
        used to having to get your Student Visa renewed
        every year.
        This process is a bummer, but it has to be done.

        Now, you weren't born yesterday; you know going to any government building
        is a hassle. Do you think you should make an appointment first?
        """
        action = raw_input("> ")
        if "yes" in action:
            print """ It's a great idea to make an appointment before standing
            forever in a line at the registration office!
            ...
            Too bad you can't make one online (because this is Germany) and they
            don't answer their phones at the office itself.
            I mean, you had your head in the right place, but you have to bite
            the bullet and go wait in line, with out an appointment, like everyone
            else.
            """
            print "-" * 100
            return 'line'
        elif "no" in action:
            print """
            There's no use in even trying to make an appointment.  You can't make
            them online or over the phone.  You can only make an appointment in person
            and to do that you need to wait in line...so just going there really
            the only answer.
            """
            print "-" * 100
            return 'line'
        else:
            print "I'm sorry, I don't see where you are going with this.."
            return 'home'


class Line(Scene):

    def being(self):
        print """
        You're at the foreigners' registration office
        and surprise surprise, there's a looong line.
        Is it worth the wait, or do you maybe want to
        come back and another day?
        """
        action = raw_input("> ")

        if "wait" in action:
            print """
            Good choice.  You're already here, and
            it's this packed no matter what day or time.
            """
            print "-" * 100
            return 'lobby'

        elif "back" in action:
            print """
            Alright, so you left and came back the next day.
            Great, today's line is even longer.
            Newsflash: The line is ALWAYS long.
            Patience is a virtue, my friend.
            """
            print "-" * 100
            return 'lobby'

        else:
            print """
            ???
            I don't think you understood the question.
            Do you want to wait in line, or come back
            tomorrow?
            """
            return 'line'


class Lobby(Scene):

    def being(self):
        print """
        You're finally at the information desk!
        Soon you'll get to talk to someone and
        get things done!
        Haha, just kidding.  Now you get to take a number!
        That's right, you just waited to wait. Nice, right?
        """
        print "-" * 100
        return 'number'


class Number(Scene):

    def being(self):
        place = "%d%d%d" % ((3), randint(1, 3), randint(1, 9))
        print "You pulled lucky number %s!" % place
        if place > 330:
            print """
            Oh crap..this is going to be forever.
            Hold in there bud. \n\n\n
            ....
            (said with a French accent:) "One and a half hours later..."
            Yay your number finally got called!
            Get a go on!
            """
            print "-" * 100
            return 'office'
        else:
            print """
            Neat-o! This won't be that long at all!
            *does a little happy dance* \n\n\n
            ....
            (said with a French accent:) "Thirty minutes later..."
            """
            print "-" * 100
            return 'office'


class Office(Scene):

    def being(self):
        print """
        So, you're finally having an appointment with someone.
        While glaring at their computer and resisting to make eye contact
        with you, they ask
            "Pick up or register?"
        """
        action = raw_input("> ")
        if "pick" in action:
            print """
            "One moment please..."
            The employee leaves the room and you wait.
            ...
            You swear it's been over 5 Minutes and you look at the time on your
            phone and then are starteled by the overweight employee plopping
            down on their desk chair.
            Finally.
            They check your documents and give you a paper to sign.
            """
            print "-" * 100
            return 'finished'
        elif "register" in action:
            print """
            The employee looks at your papers, then at the screen, then the papers,
            then the screen, but god forbid they look at you even for a second!
            They insist that your insurance is unvaild.
            That's funny considering you have had the same insurance contract
            for 2 years and never had problems with it before!
            The office worker then finally glares at you and wants an explination.
            What do you say?
            """
            action = raw_input("> ")
            if "sorry" in action:
                print """
                The office worker loves when customers accept that they are
                at fault for everything. Apparently you just need to have a
                document signed by your insurance company and you should be good.
                Good job!
                """
                print "-" * 100
                return 'appt'
            else:
                print """
                Because you didn't apologize (even though you didn't
                do anything wrong) the office worker finds you incredibly rude!
                How dare you have a shread of dignity in the German bureaucratic system!
                The worker is upset with your tone and refuses to help you any further.
                """
                print "-" * 100
                return 'fail'
        else:
            print "I'm sorry, try again!"
            return 'office'

class Appt(Scene):

    def being(self):
        print """
        So, after all of this, you're going to need to come back.
        Good news is, you can schedule an appointment here!
        Bad news is, the next avalible one is in 3 months.
        Do you want to schedule an appointment or try on your own terms next week?
        """
        action = raw_input("> ")
        if "appointment" in action:
            print """
            Alrighty, three months it is.
            You do know your Visa expires in four months, right?
            Meh, that should be enough time.
            """
            print "-" * 100
            return 'appt_line'
        elif "try" in action:
            print """
            You're not thrilled about wasting a whole new day at this place,
            but hey, at least you'll have all this behind you sooner!
            You'r visa is only good for four more months.  Three months
            wait would be too risky.
            """
            print "-" * 100
            return 'no_appt_line'
        else:
            "I guess you didn't read the question correctly.."
            return 'appt'


class NoApptLine(Scene):

    def being(self):
        print """
        So, a week has gone by! That went quick. Now you have all the
        documents you need.  Time to get in line and get your stuff done!

        After a while, you're finally at the info point and get to take a number.
        Hey! This time you pulled the lucky number 310 and don't have to wait that
        long at all! Decent!
        """
        print "-" * 100
        return 'second_office'


class ApptLine(Scene):

    def being(self):
        print """
        So three months have passed and you have all the documents you need.
        With your fancy appointment already scheduled, you should be able to
        sit down with someone right away.
        Haha, you're funny.
        In order to tell them you have an appointment, you have to wait in
        that first dreaded line again or, I guess you could always budge ahead..?
        """
        action = raw_input("> ")

        if "wait" in action:
            print """
            I know this sucks, but it's just crap you gotta deal with.
            Nobody likes a budger, and everyone here is just as stressed
            and high-strung as you. Trying to rip them off could be fatal..
            """
            print "-" * 100
            return 'second_office'

        elif "budge" in action:
            print """
            Hey buddy, nobody likes a budger, and everyone here is just as stressed
            and high-strung as you.  People start yelling at you and some old lady
            even hits you with her purse.  They get so rowdy, an employee comes out
            of the info desk and tells you to leave or she'll call the cops.
            Noone cares if you have an appointment or not.  Now waiting isn't
            even an option.  You gotta get out!
            """
            print "-" * 100
            return 'fail'
        else:
            print "Say whuuuuuuutt? Try again!"
            return 'appt_line'


class SecondOffice(Scene):

    def being(self):
        print """
        You're at in the office at your appointment.
        Everything works out.  Your visa will be processed.
        They say you'll get a letter in the mail telling you
        when you can pick up your new visa.  You go on your merry way home.
        """
        print "-" * 100
        return 'mailbox'


class Mailbox(Scene):

    def being(self):
        print """
        Over four weeks go by and you still haven't recieved the letter in the mail,
        asking you to pick up your new visa at the office.  You're worried the
        letter got misplaced, but also don't want to go to the office for nothing.
        Do you continue to wait or go to the office?
        """
        action = raw_input("> ")
        if "wait" in action:
            print """
            They said they'd mail you...so they're going to mail you!
            ...right?
            Wellp another month goes by and you still haven't recieved any notification.
            I guess you better go to the office..
            """
            print "-" * 100
            return 'pickup'
        if "go" in action:
            print """
            You really just want to get this over with!  The registration office
            can't be trusted to actually send you a letter like they said they
            would. If you don't go know you might end up waiting so long that
            your visa expires.
            You must preserviere! Get to the office today!  I believe in you!
            """
            print "-" * 100
            return 'pickup'
        else:
            print "Say What?  Do you go to the office or wait for your letter?!"
            return 'mailbox'

class Pickup(Scene):

    def being(self):
        print """
        Now you're back at the foreigners' registration office for the third
        damn time.  You're already expecting the big line, no surprise here,
        but you're hoping once you get to the info desk, you'll just have to
        say your name and get your new visa..

        Bahahaha..you're cute!
        You get to the info desk after waiting in line.  They confirm that your
        documents are indeed there (thanks for the letter...), but you still
        have to sign some things. So...Take a number, please!
        """
        print "-" * 100
        return 'number'


class Map(object):

    scenes = {
    'fail': Fail(),
    'finished': Finished(),
    'home': Home(),
    'line': Line(),
    'lobby': Lobby(),
    'number': Number(),
    'office': Office(),
    'appt': Appt(),
    'no_appt_line': NoApptLine(),
    'appt_line': ApptLine(),
    'second_office': SecondOffice(),
    'mailbox': Mailbox(),
    'pickup': Pickup(),
    }

    def __init__(self, start_scene) :
        self.start_scene = start_scene

    def next_scene(self, scene_name):
        val = Map.scenes.get(scene_name)
        return val

    def opening_scene(self):
        return self.next_scene(self.start_scene)


a_map = Map('home')
a_game = Engine(a_map)
a_game.play()

print "Es ist Freitag Abend und du willst richtig geil eine Abschiessen!! WOOOH JA PARTY!"
print "Gehst du raus ( 1 ) oder bleibst du zu Hause ( 2 )?"

wo = raw_input("> ")

# Raus
if wo == "1":
    print "Hurra! Las mal raus gehen!"
    print """
    Oyoiyoi..der Bahn hat Mega doofe Verpsaetung.
    Rewe hat allerdings noch auf und es gibt eine HSV Kneipe um die Ecke.
    Du willst sooofoooort mit m' saaufen anfangen!
    Wo gehst du hin?
    ( 1 ) Rewe, da ist billig, dat will ich!
    ( 2 ) Ne Kneipe ist ne Kneipe! Mal rein in der alte Stube!
    """
    gehen = raw_input ("> ")

# Raus - Rewe
    if gehen == "1":
        print """
        Ohhaohaoha..Rewe ist ja voll
        ...und du so gar nicht!
        Scheiss aufs Bier, hol dir mal alles was vor der Kasse haengt.
        Hauptsache Raus aus der Puff..
        Jetzt bis du nun raus in der Kalte.
        Gllug! Gluuuggg!
        Hmm..Schanpps sind nun alle.
        Also jetzt doch in der Kneipe ( 1 ) oder haddu kein Bock mehr ( 2 ) ?
        """
        kalt = raw_input ("> ")

# Raus - Rewe - Kneipe
        if kalt == "1":
            print """
            Auf dem Weg zu der Kneipe, siehst du schon die bunte Lichter und
            kannst die Schlager tief in deiner Schritt spueren!
            Die Krauterschnapps fangen puenktlich an zu wirken und auf einmal
            hast du TANZFIEBER!
            Du gehst rein und da stept der Baer, dass sag ich dir!
            Irgendeine Oma feiert den Tod ihres Mannes und es wird immer wieder
            Getraenke ausgegeben.
            Hier bist du genau richtig meinen Freund!
            Geil alter, moin.
            """
# Raus - Rewe - Hause
        elif kalt == "2":
            print """
            Achsoo.. du bist ja kaputt von der ganzen Spass, ne?
            Scheiss Menschen!
            Zu Hause ist es warm und da kannst du Zocken ohne ende!
            Ach du meine Nase..
            Da steht sogar noch Schanpps aufs Balkon..und ein paar Bier!
            Wieso gehst du ueberhaupt raus in der Welt?
            Zu Hause brauchst du nicht mehr eine Hose an!
            Geil alter, moin.
            """
# Raus - Rewe - Anderes
        else:
            print """
            Du Fuchs du! Du denkst du kannst einfach frei entscheiden!?
            Eine dritte Option einach ausdenken?
            Einfach so?!
            Also..dass ist wie eine Bombe in der Kita..
            GEHT JA GAAAR NICHT.
            Weil du denkst du bis besser als mich:
            Waehrend du draussen vor Rewe weg gehen willst
            (wohin auch immer..ist mir doch shit egal)
            stoelperst du ueber deine eigenen Fuesse (voll Idiot)
            brickst deine genick, und einen Penner Pinkelt dich an.
            Schade alter, moin.
            """
# Raus - Kneipe
    if gehen == "2":
        print """
        Auf dem Weg zu der Kneipe, siehst du schon die bunte Lichter und
        kannst die Schlager tief in deiner Schritt spueren!
        Die Krauterschnapps fangen puenktlich an zu wirken und auf einmal
        hast du TANZFIEBER!
        Du gehst rein und da stept der Baer, dass sag ich dir!
        Irgendeine Oma feiert den Tod ihres Mannes und es wird immer wieder
        Getraenke ausgegeben.
        Hier bist du genau richtig meinen Freund!
        Geil alter, moin.
        """
# Hause
if wo == "2":
    print """
    Achsoo.. du bist ja kaputt von der ganzen Spass, ne?
    Scheiss Menschen!
    Zu Hause ist es warm und da kannst du Zocken ohne ende!
    Ach du meine Nase..
    Da steht sogar noch Schanpps aufs Balkon..und ein paar Bier!
    Wieso gehst du ueberhaupt raus in der Welt?
    Zu Hause brauchst du nicht mehr eine Hose an!
    Geil alter, moin.
    """

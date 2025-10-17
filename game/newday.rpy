

label newday:
    $ day += 1
    $ Hour = 9
    $ mcorr += 2
    $ binjected = 0
    $ laundry = 0
    $ toiletcleaned = 0
    $ dwashed = 0
    $ joshvisitpool = 0
    $ bstudied = 0
    $ bexercise = 0
    $ joshuadaydone = 0
    scene broom_day with fade
    b "New day"
    if wsusp <0:
        $ wsusp = 0
        pass
    else:
        pass
    scene mgoodmorning with dissolve
    m "Good morning my hero"
    if wk >=4 and bandageremove ==0:
        scene mgoodmorning1 with dissolve
        m "Today we go to see the doctor"
        b "Oh is it time already?"
        m "Yes it's already 4 weeks, we should have gone last week, but I was busy"
        pass
    else:
        pass
    m "..."
    if day == 1:
        $ dayname = (_("Monday"))
    elif day == 2:
        $ dayname = (_("Tuesday"))
    elif day == 3:
        $ dayname = (_("Wednesday"))
    elif day == 4:
        $ dayname = (_("Thursday"))
    elif day == 5:
        $ dayname = (_("Friday"))
    elif day == 6:
        $ dayname = (_("Saturday"))
    elif day == 7:
        $ dayname = (_("Sunday"))
    elif day >= 8:
        $ day = 1
        $ wk += 1
        $ dayname = (_("Monday"))
    m "I've prepared breakfast for you"
    if wk >=4 and bandageremove ==0:
        m "We leave after breakfast"
        jump doctorvisit
    elif christmas_withwanda_done == 1:
        $ christmas_withwanda_done = 2
        scene mgoodmorning1a with dissolve
        b "Where is Joshua?"
        m "They left very early"
        scene mgoodmorning2 with dissolve
        m "What re you doing?"
        b "I can't hold anymore"
        b "Yesterday night you killed me"
        if mrel >=150:
            scene mgmafterxmas with hpunch
            m "Ah [bname]"
            scene mgmafterxmas1 with dissolve
            m "Wow [bname]!"
            scene mgmafterxmas2 with dissolve
            m "Oh"
            scene mgmafterxmas3 with dissolve
            m "It's painful"
            b "Come take it in your mouth"
            scene mgmafterxmas4 with dissolve
            b "Ahhh"
            scene mgoodmorning6 with fade
            m "Dress up and let's eat"
            call screen gnav
        else:
            m "No [bname]"
            m "I'm tired of this"
            m "Dress up and let's have breakfast"
            call screen gnav
        

    elif bandageremove ==1:
        scene mgoodmorning1a with dissolve
        m "Breakfast is ready"
        scene mgoodmorning2 with dissolve
        b "I'll have my breakfast here"
        m "My God [bname]"
        m "Is there a time you're not horny"
        scene mgoodmorning3 with dissolve
        m "[bname]"
        scene mgoodmorning4 with dissolve
        m "..."
        scene mgoodmorning5 with dissolve
        m "Uhh [bname]"
        m "Enough"
        scene mgoodmorning6 with fade
        m "Dress up please"
        if joshjaneyphotos ==1:
            scene black
            "MEANWHILE"
            $ joshjaneyphotos = 2
            $ persistent.unlock_53 = True
            scene jstalkjaney with fade
            j "{i}(That's it, what's the worst that can happen){/i}"
            scene jstalkjaney1 with dissolve
            j "..."
            scene jstalkjaney2 with dissolve
            j "{i}(My heartbeat){/i}"
            scene jstalkjaney3 with dissolve
            j "..."
            scene jstalkjaney4 with dissolve
            j "..."
            play sound "sounds/jstjasound.mp3"
            scene jstja with dissolve
            j "..."
            j "..."
            j "{i}(Oh my God, I can't anymore){/i}"
            stop sound
            scene jstalkjaney5 with dissolve
            j "..."
            scene black
            "..."
            scene jstalkjaney6 with fade
            j "Ugghh"
            scene jstalkjaney7 with dissolve
            j "Ahhh"
            scene black
            "..."
            pass
        else:
            if escortrequest == 3 and jendidgo == 0 and day ==6:
                $ jendidgo = 1
                m "[bname] there's something I want to ask you"
                b "What is it?"
                m "Someone invited me on a trip for the weekend"
                m "And I really can't decide"
                scene mgoodmorning7 with dissolve
                b "What? Where to?"
                m "A yacht trip"
                b "Ahh Okay"
                m "Do you think I should accept?"
                b "Definitely!"
                m "Do you really think so?"
                b "Of course, just go and enjoy your time"
                b "Be happy"
                scene mgoodmorning8 with dissolve
                m "Do you really think so?"
                m "Because I don't know if it's a good idea or not"
                b "I'm sure, and I want you to go"
                scene mgoodmorning7 with dissolve
                m "Thank you for always giving me confidence honey"
                m "I'll ask Wanda to visit you"
                b "Is she gonna accept?"
                m "Let's see"
                m "I'll go get ready"
                jump twodaysout
            else:
                call screen gnav

    else:
        pass
    scene mgoodmorning1 with dissolve
    m "Dress up and let's eat"
    call screen gnav
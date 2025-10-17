


label mnamejoshua:
    #
    b "Why don't you change"
    m "What do you mean?"
    m "I'm fully naked"
    b "Why don't you put something different"
    m "Like what?"
    menu:
        "Your choice":
            jump differentchoicejoshua

        "Some nice corset with stockings":
            pass
    m "I think I have something to wear"
    m "Good idea"
    m "I'll be back"
    scene mlh9n with dissolve
    "..."
    scene mlh10n with dissolve
    b "Sit tight"
    b "You're gonna get some action today"
    b "Just don't freak out when I give you sign to join"
    b "And no fucking word or moan"
    b "Or you're doomed"
    j "Ok"
    menu:
        "Let's solve your issue of last time" if persistent.unlock_63 == True:
            j "What do you mean?"
            scene mlh11n with dissolve
            b "Take this masturbate to it"
            b "It will make you last longer"
            b "I'll go buy us some more time"
            scene black
            "..."
            scene mlh10n with dissolve
            b "Are you done?"
            j "Yes"
            b "Here are some tissues, clean it up"
            j "Ok"
            $ jmasturbate = 1
            b "...."
            pass

        "Continue":
            pass
    b "Here she comes"
    scene mlh12n with dissolve
    b "Oh my god, wow"
    b "Can we take photos with a blindfold"
    if mcorr >=40:
        $ persistent.unlock_63 = True
        m "Ok"
        scene mlh13n with dissolve
        b "Oh my, I feel I want to eat you"
        m "Hehe"
        scene mlh14n with dissolve
        b "Can I play with this?"
        m "Men don't ask [bname]"
        b "Undress yourself"
        scene mlh15n with dissolve
        b "..."
        scene mlh16n with dissolve
        m "[bname] your hands are sweating"
        m "Are you stressed"
        b "Uhh no no"
        b "Just feeling hot"
        m "It's ok, I kind of like it"
        m "Steamy"
        b "{i}(Oh damn she's gonna notice his shirt){/i}"
        b "I'll take off my clothes"
        m "Ok"
        scene mlh17n with dissolve
        m "You love them so much"
        m "Are you undressed?"
        b "Yes"
        m "I'll go down on my knees"
        if jmasturbate == 1:
            scene mlh48ja with fade
            b "{i}(I'll capture this){/i}"
            scene mlh18n with dissolve
            j "..."
            scene mlh19n with dissolve
            show screen jcorr
            j "Ahh"
            $ jcorr += 1
            hide screen jcorr
            scene mlh20n with dissolve
            b "{i}(Shut the fuck up){/i}"
            m "Come on give it to me!"
            scene mlhjanim with dissolve
            j "Ahh"
            m "Mmm"
            j "Ohhh"
            j "Ahh"
            scene mlh21n with vpunch
            j "Oh"
            scene mlh22n with dissolve
            m "mmmm"
            scene mlh23n with dissolve
            m "Ahh"
            menu:
                "He's going to cum now":
                    scene mlh24n with dissolve
                    j "Ahhhhhh"
                    scene mlh25n with dissolve
                    j "..."
                    m "Nice baby"
                    b "{i}(Why the fuck does she call me that){/i}"
                    scene mlh20n with dissolve
                    b "{i}(Get out damn){/i}"
                    j "Uh huh!"
                    scene mlh26n with dissolve
                    m "Where did you go?"
                    b "Here wiping my dick"
                    b "I'll go"
                    scene jday4 with fade
                    b "Are you okay?"
                    j "Yes"
                    b "Did you clean?"
                    j "Yes"
                    b "That was dangerous"
                    j "I'll go now"
                    menu:
                        "Yes leave quick":
                            b "Yes quick"
                            call screen gnav

                        "One thing before you go" if josh_hidden_cam ==0:
                            b "I think it's time you give me something more"
                            j "Like what?"
                            b "I gave you [mname]"
                            b "You need to give me Wanda"
                            scene jday5 with dissolve
                            j "Huh"
                            j "I'll be disowned"
                            j "Or even get killed"
                            b "Relax, just get me some photos"
                            j "Not possible"
                            menu:
                                "Try your best":
                                    j "I'll do"
                                    b "Go now"
                                    call screen gnav

                                "I have an idea, come with me" if mny >= 200:
                                    j "Where to?"
                                    b "My room"
                                    scene jday6 with fade
                                    $ mny -= 200
                                    $ josh_hidden_cam = 1
                                    j "What are we doing?"
                                    b "Ordering for you a hidden camera"
                                    j "Err"
                                    j "What for?"
                                    b "This is your solution"
                                    j "But it can't be delivered to me"
                                    j "She checks everything"
                                    b "Relax, it will come here"
                                    j "I need to go"
                                    b "Wait, 20 minutes it will be delivered"
                                    j "Oh god"
                                    scene jday4 with fade
                                    b "All setup, , put it in the lamp holder or on a top shelf"
                                    b "Just charge the battery every other day"
                                    j "Wish me luck"
                                    b "Good luck go now"
                                    j "Bye"
                                    b "{i}(Hehehe I set the cam to stream to my computer){/i}"
                                    b "{i}(I'll go and check later){/i}"
                                    call screen gnav

                "Continue":
                    m "Are you close?"
                    b "Yes"
                    m "Give me in my mouth"
                    scene mlh27n with fade
                    m "Mmm"
                    scene mlh28n with dissolve
                    j "..."
                    scene mlh29n with dissolve
                    j "Uhhh"
                    scene mlh20n with dissolve
                    b "{i}(Get out damn){/i}"
                    j "Uh huh!"
                    scene mlh30n with dissolve
                    m "Where did you go?"
                    b "Here wiping my dick"
                    b "I'll go"
                    scene jday4 with fade
                    b "Are you okay?"
                    j "Yes"
                    b "Did you clean?"
                    j "Yes"
                    b "That was dangerous"
                    j "I'll go now"
                    menu:
                        "Yes leave quick":
                            b "Yes quick"
                            call screen gnav

                        "One thing before you go" if josh_hidden_cam ==0:
                            b "I think it's time you give me something more"
                            j "Like what?"
                            b "I gave you [mname]"
                            b "You need to give me Wanda"
                            scene jday5 with dissolve
                            j "Huh"
                            j "I'll be disowned"
                            j "Or even get killed"
                            b "Relax, just get me some photos"
                            j "Not possible"
                            menu:
                                "Try your best":
                                    j "I'll do"
                                    b "Go now"
                                    call screen gnav

                                "I have an idea, come with me" if mny >= 200:
                                    j "Where to?"
                                    b "My room"
                                    scene jday6 with fade
                                    $ mny -= 200
                                    $ josh_hidden_cam = 1
                                    j "What are we doing?"
                                    b "Ordering for you a hidden camera"
                                    j "Err"
                                    j "What for?"
                                    b "This is your solution"
                                    j "But it can't be delivered to me"
                                    j "She checks everything"
                                    b "Relax, it will come here"
                                    j "I need to go"
                                    b "Wait, 20 minutes it will be delivered"
                                    j "Oh god"
                                    scene jday4 with fade
                                    b "All setup, , put it in the lamp holder or on a top shelf"
                                    b "Just charge the battery every other day"
                                    j "Wish me luck"
                                    b "Good luck go now"
                                    j "Bye"
                                    b "{i}(Hehehe I set the cam to stream to my computer){/i}"
                                    b "{i}(I'll go and check later){/i}"
                                    call screen gnav

        else:
            scene mlh35j with dissolve
            b "{i}(Get out damn){/i}"
            scene mlh36j with dissolve
            m "Where did you go?"
            b "Here wiping my dick"
            b "I'll go"
            scene jday4 with fade
            b "Are you okay?"
            j "Yes"
            b "Did you clean?"
            j "Yes"
            b "That was dangerous"
            j "I'll go now"
            b "Yes quick"
            call screen gnav

    else:
        m "No"
        "YOU DON'T HAVE ENOUGH CORRUPTION POINTS"
        "40 NEEDED"
        scene mlh23j with dissolve
        m "Let's take something on the floor"
        scene mlh37j with dissolve
        b "Hmm"
        scene mlh38j with dissolve
        b "..."
        scene mlh39j with dissolve
        b "Maybe you should undress"
        m "No [bname]"
        b "Please"
        scene mlh40j with dissolve
        m "Scram! Go!"
        scene mlh41j with dissolve
        j "{i}(Oh no! He left){/i}"
        j "{i}(What to do!? What to do?!){/i}"
        j "{i}(It's better I'll keep quiet){/i}"
        scene hall_d with fade
        b "{i}(Damn I need to get Joshua out){/i}"
        scene jday3 with fade
        b "You're okay?"
        j "Can I use the toilet?"
        b "{i}(Hahaha he wet himself){/i}"
        b "Yes, make it quick and leave after"
        call screen gnav



label differentchoicejoshua:
    m "I think I have something to wear"
    m "Good idea"
    m "I'll be back"
    scene mlh9n with dissolve
    "..."
    scene mlh10n with dissolve
    b "Sit tight"
    b "You're gonna get some action today"
    b "Just don't freak out when I give you sign to join"
    b "And no fucking word or moan"
    b "Or you're doomed"
    j "Ok"
    menu:
        "Let's solve your issue of last time" if persistent.unlock_63 == True:
            j "What do you mean?"
            scene mlh11n with dissolve
            b "Take this masturbate to it"
            b "It will make you last longer"
            b "I'll go buy us some more time"
            scene black
            "..."
            scene mlh10n with dissolve
            b "Are you done?"
            j "Yes"
            b "Here are some tissues, clean it up"
            j "Ok"
            $ jmasturbate = 1
            b "...."
            pass

        "Continue":
            pass
    b "Here she comes"
    scene mlh56j with dissolve
    b "Oh my god, wow"
    b "Can we take photos with a blindfold"
    if mcorr >=40:
        m "Ok"
        scene mlh57j with dissolve
        b "Oh my, I feel I want to eat you"
        m "Hehe"
        scene mlh58j with dissolve
        m "How about like this?"
        scene mlh59j with dissolve
        b "Can I play with this?"
        m "Men don't ask [bname]"
        b "Undress yourself"
        scene mlh60j with dissolve
        b "..."
        scene mlh61j with dissolve
        m "[bname] your hands are sweating"
        m "Are you stressed?"
        b "Uhh no no"
        b "Just feeling hot"
        m "It's ok, I kind of like it"
        m "Steamy"
        b "{i}(Oh damn she's gonna notice his shirt){/i}"
        b "I'll take off my clothes"
        m "Ok"
        scene mlh62j with dissolve
        m "You love them so much"
        scene mlh63j with dissolve
        m "{i}(His hair feels different){/i}"
        m "Are you undressed?"
        b "Yes"
        if jmasturbate == 1:
            scene mlh65j with fade
            b "{i}(I'll capture this){/i}"
            scene mlh66j with dissolve
            j "..."
            scene mlh67j with dissolve
            show screen jcorr
            j "Ahh"
            $ jcorr += 1
            hide screen jcorr
            m "Come on give it to me!"
            scene mlh68j with dissolve
            "..."
            scene mlh69j with dissolve
            b "{i}(The idiot is gonna cry){/i}"
            scene mjanim00 with dissolve
            j "Ahh"
            scene mjanim07 with dissolve
            m "Mmm"
            scene mjanim15 with dissolve
            j "Ohhh"
            b "{i}(Shut it up){/i}"
            j "Ahh"
            scene mlh70j with vpunch
            j "Oh"
            m "Nice baby"
            b "{i}(Why the fuck does she call me that){/i}"
            scene mlh20n with dissolve
            b "{i}(Get out damn){/i}"
            j "Uh huh!"
            scene mlh75j with dissolve
            m "Where did you go?"
            b "Here wiping my dick"
            b "I'll go"
            scene jday4 with fade
            b "Are you okay?"
            j "Yes"
            b "Did you clean?"
            j "Yes"
            b "That was dangerous"
            j "I'll go now"
            menu:
                "Yes leave quick":
                    b "Yes quick"
                    call screen gnav

                "One thing before you go" if josh_hidden_cam ==0:
                    b "I think it's time you give me something more"
                    j "Like what?"
                    b "I gave you [mname]"
                    b "You need to give me Wanda"
                    scene jday5 with dissolve
                    j "Huh"
                    j "I'll be disowned"
                    j "Or even get killed"
                    b "Relax, just get me some photos"
                    j "Not possible"
                    menu:
                        "Try your best":
                            j "I'll do"
                            b "Go now"
                            call screen gnav

                        "I have an idea, come with me" if mny >= 200:
                            j "Where to?"
                            b "My room"
                            scene jday6 with fade
                            $ mny -= 200
                            $ josh_hidden_cam = 1
                            j "What are we doing?"
                            b "Ordering for you a hidden camera"
                            j "Err"
                            j "What for?"
                            b "This is your solution"
                            j "But it can't be delivered to me"
                            j "She checks everything"
                            b "Relax, it will come here"
                            j "I need to go"
                            b "Wait, 20 minutes it will be delivered"
                            j "Oh god"
                            scene jday4 with fade
                            b "All setup, , put it in the lamp holder or on a top shelf"
                            b "Just charge the battery every other day"
                            j "Wish me luck"
                            b "Good luck go now"
                            j "Bye"
                            b "{i}(Hehehe I set the cam to stream to my computer){/i}"
                            b "{i}(I'll go and check later){/i}"
                            call screen gnav


        else:
            scene mlh65j with fade
            b "{i}(I'll capture this){/i}"
            scene mlh66j with dissolve
            j "..."
            scene mlh67j with dissolve
            j "Ahh"
            scene mlh67ja with dissolve
            "..."
            scene mlh67jb with dissolve
            j "Ahh"
            scene mlh35j with dissolve
            b "{i}(Get out damn){/i}"
            scene mlh67jc with dissolve
            m "Where did you go?"
            b "Here wiping my dick"
            b "I'll go"
            scene jday4 with fade
            b "Are you okay?"
            j "Yes"
            b "Did you clean?"
            j "Yes"
            b "That was dangerous"
            j "I'll go now"
            b "Yes quick"
            call screen gnav

    else:
        m "No"
        "YOU DON'T HAVE ENOUGH CORRUPTION POINTS"
        "40 NEEDED"
        scene mlh71j with dissolve
        b "Hmm"
        scene mlh73j with dissolve
        b "Maybe you should undress"
        m "No [bname]"
        b "Please"
        m "Please go"
        scene mlh74j with dissolve
        j "{i}(Oh no! He left){/i}"
        j "{i}(What to do!? What to do?!){/i}"
        j "{i}(It's better I'll keep quiet){/i}"
        scene hall_d with fade
        b "{i}(Damn I need to get Joshua out){/i}"
        scene jday3 with fade
        b "You're okay?"
        j "Can I use the toilet?"
        b "{i}(Hahaha he wet himself){/i}"
        b "Yes, make it quick and leave after"
        call screen gnav
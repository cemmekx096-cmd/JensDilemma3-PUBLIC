

label msundaybeach:
    menu:
        "Can we take [sname]?":
            scene msbeach with dissolve
            m "Yes why not"
            jump msundaybeachwithsname

        "Say nothing":
            pass
    scene msbeach2b with fade
    b "Nice place"
    scene msbeach2c with dissolve
    m "Ahh yeah"
    b "You seem tired?"
    m "..."
    b "By the way, what happened with the guy who shot me"
    scene msbeach3b with dissolve
    m "He's going to rot in jail"
    b "Good to know"
    b "If you want to swim, go ahead"
    m "Yes come with me let's go to that side"
    scene msbeach5a with fade
    b "The boat is not here"
    scene msbeach6a with fade
    m "I'll take a dip"
    m "Won't be late"
    if bandageremove ==1:
        m "Don't you want to swim?"
        b "No"
        m "I thought you couldn't wait to remove that bandage"
        b "Yes but I don't feel like swimming now"
        pass
    else:
        pass
    scene msbeach6b with fade
    m "Done, have you got my towel?"
    b "Yes here"
    scene msbeach8b with dissolve
    b "You know, shorter hair suits you"
    m "..."
    scene msbeach8a with dissolve
    m "You think so?"
    b "Yeah"
    menu:
        "Come closer and grab her from behind" if bandageremove ==1:
            scene msbeach35 with dissolve
            m "[bname] what are you doing? Not here"
            scene msbeach36 with dissolve
            b "Why not, there's no one here"
            scene msbeach37 with dissolve
            m "..."
            scene msbeach38 with dissolve
            m "Mmm"
            scene msbeach39 with fade
            "..."
            scene msbeach40 with dissolve
            m "..."
            scene msbeacha with dissolve
            play sound "sounds/beachlove.mp3"
            m "Ahh"
            m "Mmm"
            "..."
            m "Ahhh"
            "..."
            scene msbeach41 with hpunch
            m "Mmm"
            scene msbeach42_1 with dissolve
            m "Mmmm nice"
            scene msbeach42_2 with dissolve
            m "You're getting better and better"
            scene msbeach42_3 with dissolve
            m "Ahh [bname]"
            scene msbeach42_end with dissolve
            m "Ahhhhhh"
            stop sound fadeout 1.0
            scene msbeach43 with fade
            b "Oh I love this"
            scene msbeach44 with dissolve
            b "Ahh"
            scene msbeach45 with dissolve
            b "Fuck!"
            scene msbeach46 with dissolve
            m "Mm"
            scene msbeach5a with fade
            "YOU GET BACK HOME"
            scene hall_d with fade
            "..."
            call screen gnav

        "Can we try?":
            scene msbeach9 with dissolve
            m "Here?"
            menu:
                "Yes why not" if bandageremove ==1:
                    b "Why not?"
                    scene msbeachs24
                    $ persistent.unlock_33 = True
                    b "I see no one around"
                    scene msbeachs26 with dissolve
                    m "..."
                    scene msbeachs26 with dissolve
                    m "Mmm"
                    scene msbeachs27 with dissolve
                    m "Come here"
                    menu:
                        "Give her love":
                            scene msbeachs30 with dissolve
                            m "Mmhm"
                            scene msbeachs31 with dissolve
                            m "I love how you're obsessed with me"
                            scene msbeachs32 with dissolve
                            b "Damn I am"
                            scene msbeachs33 with dissolve
                            m "Mmm"
                            scene msbeachs34 with dissolve
                            m "..."
                            scene msbeachs35 with dissolve
                            m "Ohh"
                            scene msbeachs36 with dissolve
                            m "Ahhh"
                            menu:
                                "Cum inside":
                                    scene msbeachs37 with dissolve
                                    b "Ahh fuck"
                                    scene msbeach5a with fade
                                    "YOU GET BACK HOME"
                                    scene hall_d with fade
                                    "..."
                                    call screen gnav
                                    
                                "Cum on her belly":
                                    scene msbeachs38 with dissolve
                                    b "Ahhh"
                                    scene msbeachs39 with dissolve
                                    m "Mmm"
                                    scene msbeach5a with fade
                                    "YOU GET BACK HOME"
                                    scene hall_d with fade
                                    "..."
                                    call screen gnav
                        "Fuck her ass":
                            scene msbeachs28 with dissolve
                            b "I want this"
                            m "Here?"
                            b "Let's move to the shade"
                            scene mbeachanim with fade
                            play sound "sounds/analbeach.mp3"
                            m "..."
                            m "Yeah"
                            m "Ahh"
                            "..."
                            m "Yes fuck me"
                            m "Faster"
                            stop sound fadeout 1.0
                            scene mbeachanims with dissolve
                            "..."
                            m "Ahh"
                            stop sound fadeout 1.0
                            scene msbeachs29 with fade
                            b "Shall we go?"
                            scene msbeach5a with fade
                            "YOU GET BACK HOME"
                            scene hall_d with fade
                            "..."
                            call screen gnav

                "Maybe behind the trees":
                    pass
            b "Mmm"
            if mrel >=150:
                b "Maybe behind the trees over there?"
                m "..."
                scene msbeach10 with dissolve
                m "Fine let's go"
                scene msbeach11 with dissolve
                m "..."
                menu:
                    "69":
                        b "Ahh yes"
                        scene msbeach12 with dissolve
                        b "{i}(She's fucking squeezin my balls){/i}"
                        if binjected ==0:
                            scene msbeach13 with dissolve
                            b "Ahh"
                            m "You see! You're ok"
                            m "Let's go"
                            "YOU FORGOT TO INJECT YOURSELF"
                            scene msbeach23 with fade
                            "YOU STAY FOR A WHILE AND GET BACK HOME"
                            scene hall_d with fade
                            "..."
                            call screen gnav
                        else:
                            b "This is not working"
                            b "Can we try something else?"
                            scene msbeach14 with dissolve
                            m "Like what?"
                            b "I need to feel something"
                            b "Maybe 69?"
                            if mrel >=180:
                                scene msbeach15 with dissolve
                                m "Ahh"
                                scene msbeach16 with dissolve
                                m "..."
                                scene msbeach17 with dissolve
                                m "..."
                                scene msbeach18 with dissolve
                                m "Mmm"
                                scene msbeach19 with dissolve
                                b "Ah"
                                scene msbeach20 with dissolve
                                b "Yess"
                                scene msbeach21 with dissolve
                                b "Ahhh"
                                m "Happy now?"
                                scene msbeach22 with dissolve
                                b "Yeah I'm safe"
                                b "For now"
                                scene msbeach23 with fade
                                "YOU STAY FOR A WHILE AND GET BACK HOME"
                                scene hall_d with fade
                                "..."
                                call screen gnav
                            else:
                                m "No [bname]"
                                m "Sorry"
                                m "Let's go"
                                "RAISE YOUR POINTS TO 180"
                                scene msbeach23 with fade
                                "YOU STAY FOR A WHILE AND GET BACK HOME"
                                scene hall_d with fade
                                "..."
                                call screen gnav
                    "Doggy":
                        m "Hmm"
                        scene msbeach24 with dissolve
                        m "..."
                        scene msbeach25 with dissolve
                        m "..."
                        scene msbeach26 with dissolve
                        m "Ah"
                        scene msbeach27 with dissolve
                        m "Mmm"
                        scene msbeach28 with dissolve
                        m "..."
                        if binjected ==0:
                            scene msbeach31 with dissolve
                            m "Ohhh"
                            scene msbeach33 with dissolve
                            b "Ahhh fuck"
                            m "Ahh"
                            m "Looks like you're ok"
                            m "Let's go"
                            scene msbeach23 with fade
                            "YOU STAY FOR A WHILE AND GET BACK HOME"
                            scene hall_d with fade
                            "..."
                            call screen gnav

                        else:
                            scene msbeach29 with dissolve
                            m "Yes"
                            scene msbeach30 with dissolve
                            m "Mmm"
                            scene msbeach31 with dissolve
                            m "Ohhh"
                            scene msbeach32 with dissolve
                            b "Ahh"
                            scene msbeach34 with dissolve
                            b "Fuck!"
                            scene msbeach33 with dissolve
                            m "Ahh"
                            m "Looks like you're ok"
                            m "Let's go"
                            scene msbeach23 with fade
                            "YOU STAY FOR A WHILE AND GET BACK HOME"
                            scene hall_d with fade
                            "..."
                            call screen gnav

            else:
                m "No [bname] not here"
                "RAISE YOUR POINTS TO 150"
                pass
        "Say nothing":
            pass
    scene msbeach23 with fade
    "YOU STAY FOR A WHILE AND GET BACK HOME"
    scene hall_d with fade
    "..."
    call screen gnav



label msundaybeachwithsname:
    scene msbeachsa with fade
    if persistent.patch_enabled:
        s "Nice bikini mom"
        pass
    else:
        s "Nice bikini"
        pass
    m "Yes this one was from [bname]"
    scene msbeachs1a with fade
    s "Do you guys want something to drink?"
    m "And where are you planning to get it from?"
    m "There are no shops here"
    s "Oh right, damn!"
    b "I have beer"
    s "[bname] is always ready"
    b "I thought we might want to drink something"
    s "I wasn't speaking about drinks"
    s "Hehehe"
    scene msbeachs2a with dissolve
    b "..."
    scene msbeachs3a with dissolve
    b "Where are you going?"
    m "Start drinking, I'll swim a bit"
    m "I will be quick"
    scene msbeachs8 with fade
    s "So..."
    scene msbeachs9 with dissolve
    s "Is it true that you can't get it up?"
    b "Who told you?"
    if persistent.patch_enabled:
        b "Mom?"
        pass
    else:
        b "[mname]?"
        pass
    scene msbeachs10 with dissolve
    s "Look we're worried about you"
    b "Yes that's why no one is helping me"
    s "What do you mean? Look at what she's doing for you, she's like your personal maid"
    s "Or even your personal slave"
    b "Duh! If I can't get it up, what kind of help do I need?"
    scene msbeachs11 with dissolve
    s "..."
    scene msbeachs12 with dissolve
    s "Duh!!"
    b "Why are you being silly?"
    s "Because it's obvious what you want"
    scene msbeachs13 with dissolve
    s "Because it's obvious where this discussion is heading"
    s "You want to fuck"
    menu:
        "I want love":
            b "No true!"
            b "I just want to be sensual with you, no fucking"
            b "Maybe some love will make it grow and get back to normal"
            if srel >= 140:
                b "Think of it as a romance movie practice"
                scene msbeachs10 with dissolve
                s "Here?"
                b "We can go behind the trees"
                scene msbeachs14 with dissolve
                s "And what about her?"
                b "She won't notice, just keep a bottle of drinks for her"
                s "Ok"
                b "Let's go!?"
                scene msbeachs9 with dissolve
                s "Anyway who am I kidding, I know what's been going on"
                scene msbeachs15 with fade
                s "..."
                scene msbeachs16 with dissolve
                s "Come"
                scene msbeachs18 with dissolve
                s "Mmm"
                scene msbeachs19 with dissolve
                s "Turn"
                scene msbeachs17 with dissolve
                b "Uhh"
                s "Can you do it without breaking something in your organs?"
                b "Yes turn"
                scene msbs with fade
                play sound "sounds/snameonbeach.mp3"
                s "Ahh"
                s "..."
                s "..."
                s "Mmm"
                s "..."
                s "Ahh"
                s "..."
                scene msbeachs20 with dissolve
                stop sound
                s "I finished [bname]"
                if binjected ==1:
                    b "Get on your knees"
                    scene msbj with dissolve
                    $ persistent.unlock_3 = True
                    s "Mmm"
                    s "Gulp"
                    s "..."
                    s "Mm"
                    scene msbj_end with dissolve
                    b "Ahhh"
                    scene msbeachs21 with dissolve
                    s "God, you were so rough"
                    s "Where are my glasses"
                    scene msbeachs22 with fade
                    m "Where have you been?"
                    b "We went for a walk"
                    m "Ok, it's time to go"
                    pass
                else:
                    b "Me too"
                    scene msbeachs21a with dissolve
                    s "God, you were so rough"
                    s "Where are my glasses"
                    scene msbeachs22 with fade
                    m "Where have you been?"
                    b "We went for a walk"
                    m "Ok, it's time to go"
                    pass

            else:
                s "Out of question"
                scene msbeachs23 with fade
                m "Ah very hot"
                m "Come on kids, it's time we go"
                pass

        "I want a threesome with you and her":
            scene msbeachs10 with dissolve
            s "What?"
            s "Are you serious?"
            s "I'm fun and all, but she won't"
            scene msbeachs14 with dissolve
            b "Trust me she will"
            s "You are so confident"
            scene msbeachs9 with dissolve
            b "I have something that can make her want it"
            s "What is it?"
            b "Something in her drink"
            b "I'll prepare the beer and come back"
            scene msbeachs40 with fade
            b "Right on time"
            b "Drinks are ready!"
            scene msbeachs41 with dissolve
            m "So good this beer"
            scene msbeachs42 with dissolve
            m "Is it turning hot or it's me!"
            b "I'm cool"
            m "I'll go behind the trees"
            m "Just to chill if you want to come with me"
            b "I'll follow you"
            scene msbeachs11 with dissolve
            b "You follow and catch us in the act"
            b "And you know how to handle it from there"
            scene msbeachs43 with fade
            b "Mmm"
            scene msbeachs44 with dissolve
            m "Ah yes"
            scene msbeachs45 with dissolve
            m "Mhmm"
            scene msbeachs46 with dissolve
            m "Oh"
            scene msbeachs47 with dissolve
            m "Ahh"
            scene msbeachs48 with dissolve
            s "What the hell!!"
            scene msbeachs49 with dissolve
            m "Ohhh"
            s "I bet you're going to say it's not what it looks like"
            m "..."
            s "Carry on, don't mind me"
            scene msbeachs50 with dissolve
            "..."
            scene msbeachs51 with dissolve
            "..."
            scene msbeachsms with fade
            s "Ahh"
            m "..."
            "..."
            m "Mmm"
            b "I'm about to cum"
            m "Give it to me [bname]"
            scene msbeachs52 with dissolve
            m "Mmmm"
            scene msbeachs53 with dissolve
            s "..."
            pass

    scene hall_d with fade
    "..."
    call screen gnav
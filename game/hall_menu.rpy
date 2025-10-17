

label hall_menu:
    if Hour == 9:
        $ Hour += 1
        scene mhall_morning with fade
        b "Good morning"
        scene mhall_morning1 with dissolve
        m "Good morning"
        menu:
            "I'll wash the dishes":
                scene srg39 with dissolve
                b "{i}(...){/i}"
                scene srg40 with dissolve
                "..."
                scene srg41 with dissolve
                b "Done"
                $ mrel += 5
                show screen mrelup
                m "[bname], you really don't have to"
                b "Easy, I can still do basic stuff"
                hide screen mrelup
                pass

            "What's for breakfast?":
                scene mhall_morning2 with dissolve
                m "Eat, you have to get healthy, no questions asked"
                scene srg39 with dissolve
                b "{i}(...){/i}"
                scene srg40 with dissolve
                "..."
                scene srg41 with dissolve
                m "[bname], you really don't have to"
                b "Easy, I can still do basic stuff"
                pass


        scene mhall_morning3 with dissolve
        m "This is especially for you dear"
        b "Thanks"
        b "Good morning [sname]"
        s "How are you today?"
        b "Good"
        scene mhall_morning4 with dissolve
        m "Enjoy your breakfast"
        scene mhall_morning5 with dissolve
        b "I'll clear the table"
        m "it's fine dear, I'll do it"
        b "Ok"
        if day ==2:
            m "What's your plan for today?"
            b "I don't know, I can't go out, so probably I'll sleep"
            m "Yes, it's better you don't do any activities these days"
            m "Just relax until you recover"
            pass
        elif smorehelpwithjoshua ==1 and masqueradeaccepted ==0:
            b "Now that [sname] left"
            b "There's something I wanted to ask you"
            m "What is it?"
            b "Did [sname] tell you about the tanqueray?"
            m "What's tanqueray?"
            b "I don't remember but it's a tanqueray ball something something..."
            m "Are you trying to be funny?"
            b "No"
            b "Why asking?"
            m "It's called masquerade"
            m "And my answer is no, I don't want her to go to such parties"
            b "But why!?"
            b "Do you want her sneaking out rather than asking you"
            scene mhall_morning6 with dissolve
            m "Tell her she can try sneaking"
            b "Come on! Please"
            m "No, I said No!"
            scene hall_d with fade
            b "Damn it"
            b "{i}(I wonder what's with this masquerade){/i}"
            call screen gnav
        else:
            pass
        scene hall_d with fade
        "..."
        call screen gnav


    elif Hour >=10 and Hour <=12:
        scene hall_d with fade
        b "{i}(Maybe I can...){/i}"
        menu:
            "Watch TV" :
                if mellastrequest == 2:
                    $ Hour += 1
                    play sound "sounds/mobilering.wav"
                    $ mellastrequest = 3
                    stop sound
                    b "Melinda!"
                    scene mlc with dissolve
                    ml "{i}(Hi [bname]){/i}"
                    b "Hi"
                    ml "{i}(Amy progress with [mname]?){/i}"
                    b "No"
                    ml "{i}(Don't worry I'll take care of it){/i}"
                    ml "{i}(I just want you to take her for dinner to this restaurant){/i}"
                    ml "{i}(Any day in the evening after her work){/i}"
                    ml "{i}(Just give me a call before){/i}"
                    b "Uh... Ok"
                    ml "{i}(I'll do the reservation for you){/i}"
                    ml "{i}(Your task is to do like last time){/i}"
                    ml "{i}(The gentleman will do the rest){/i}"
                    b "Got it"
                    ml "{i}(Good luck [bname]){/i}"
                    pass
                elif jenlastmovie ==1 and mellastrequest ==0:
                    $ persistent.unlock_75 = True
                    $ Hour += 1
                    play sound "sounds/mobilering.wav"
                    $ mellastrequest = 1
                    b "Melinda!"
                    stop sound
                    scene mlc with dissolve
                    ml "{i}(Hi [bname]){/i}"
                    b "Hi"
                    ml "{i}(Are you free?){/i}"
                    b "Yes why?"
                    ml "{i}(There's a new request){/i}"
                    b "Hmm it's harder this time"
                    ml "{i}(Can you visit me?){/i}"
                    scene mlc1 with fade
                    ml "He's going to be here any minute"
                    ml "We need this, it's a lot of money"
                    c "He's here already"
                    scene mlc2 with dissolve
                    c "Here's my handsome man"
                    scene mlc3 with dissolve
                    c "I'll get you a drink"
                    scene mlc4 with dissolve
                    ml "So, can you help this time?"
                    b "Ah... I don't know really"
                    ml "It's really important this time"
                    ml "Big guns"
                    scene mlc5 with dissolve
                    ml "Speaking of guns"
                    b "..."
                    scene mlc6 with dissolve
                    ml "Stand up"
                    ml "Let Cheryl give you pleasure"
                    scene mlc7 with dissolve
                    ml "Good boy"
                    scene mlc8 with dissolve
                    ml "..."
                    scene mlc9 with dissolve
                    ml "Ahh"
                    scene mlc10 with dissolve
                    "..."
                    scene mlc11 with fade
                    ml "Look at that beautiful cock"
                    scene mlc12 with dissolve
                    "..."
                    scene mlc13 with dissolve
                    "..."
                    scene mlc14 with dissolve
                    b "Ahhh"
                    scene mlc13 with dissolve
                    b "Come here Melinda"
                    ml "Enjoy her first"
                    ml "I'll join"
                    scene mlc15 with dissolve
                    c "Ahh"
                    scene mlc16 with dissolve
                    c "God!"
                    scene mlc17 with fade
                    "..."
                    scene mlc18 with fade
                    ml "So do you think you can convince her now?"
                    b "I'll try, but you know [mname]"
                    b "On top of that, she made up her mind"
                    ml "I trust you can"
                    c "See you soon baby"
                    jump broom_menu
                else:
                    pass
                "..."
                $ Hour += 1
                if day !=7:
                    scene b_tv_d with fade
                    "..."
                    scene b_tv_d1 with dissolve
                    m "..."
                    b "Oh hi"
                    scene b_tv_d2 with dissolve
                    m "Carry on dear, don't worry"
                    m "I'm looking for the the drain liquid"
                    scene b_tv_d3 with dissolve
                    if bandageremove ==1:
                        b "I'll help you with it"
                        b "Why do you always need it"
                        scene b_tv_d3a with dissolve
                        m "Hmm it's... It's the toilet"
                        m "Got blocked"
                        b sur "Always?!"
                        m "..."
                        b "Let's do it anyway"
                        scene black
                        scene b_tv_d3b with fade
                        b "Wow that was a big one"
                        m "Sorry for that dear"
                        b "Don't be, that's normal"
                        menu:
                            "Get closer and hug her":
                                scene b_tv_d3c with dissolve
                                m "[bname] I need to take a bath"
                                b "I only wanted to hug you"
                                scene b_tv_d3d with dissolve
                                m "Ah here you go"
                                scene b_tv_d3e with dissolve
                                b "{i}(I'll never get enough of this ass){/i}"
                                menu:
                                    "Rip her clothes off":
                                        scene b_tv_d3f with dissolve
                                        m "Huh! [bname]!"
                                        m ang "No"
                                        if mrel >=190:
                                            scene b_tv_d3g with hpunch
                                            b "Don't let me use force"
                                            $ persistent.unlock_38 = True
                                            scene btvboanim with dissolve
                                            play sound "sounds/btvboan.ogg"
                                            m "Mmm"
                                            b "Oh"
                                            m "Ahh"
                                            m "Mm"
                                            m "I'd kill you if you did anal"
                                            scene b_tv_d3h with dissolve
                                            stop sound fadeout 1.0
                                            m "Ahhhhhhh"
                                            b "Get on the floor"
                                            scene b_tv_d3i with fade
                                            $ mcorr += 5
                                            show screen mcorr
                                            m "..."
                                            hide screen mcorr
                                            scene b_tv_d with fade
                                            b "{i}(Wow that was something){/i}"
                                            call screen gnav
                                        else:
                                            m ang "Stop it!"
                                            m "I'm dirty, I need to shower"
                                            b "It's more hot this way"
                                            m ang "[bname] get out or else"
                                            b "Ok Ok ! I'll go"
                                            scene b_tv_d with fade
                                            "YOU NEED 190 RELATIONSHIP POINTS"
                                            b "{i}(Damn){/i}"
                                            call screen gnav
                                    "No, risky":
                                        pass
                            "Continue":
                                pass
                        b "I'll go"
                        m "Thank you dear"
                        scene b_tv_d with fade
                        b "{i}(I'll continue watching){/i}"
                        call screen gnav

                    else:
                        pass
                    b "You know, I can still help you with something"
                    m "No, need, just get better"
                    m "There is time later"
                    scene b_tv_d with fade
                    b "{i}(I'll continue watching){/i}"
                    call screen gnav
                else:
                    scene b_tv_d with fade
                    "..."
                    scene b_tv_d4 with dissolve
                    m "..."
                    b "Oh hi"
                    scene b_tv_d5 with dissolve
                    b "What's up?"
                    m "Ah nothing, I just need a drink"
                    b "Isn't it early?"
                    if mrel >=120:
                        scene b_tv_d7 with dissolve
                        m "How's your little poor thing?"
                        m "Still paralyzed?"
                        if persistent.patch_enabled:
                            b "Mom, it's not funny!"
                            pass
                        else:
                            b "It's not funny"
                            pass
                        scene b_tv_d6 with dissolve
                        m "Then don't meddle with my drinking"
                        menu:
                            "Follow her, see why she's drinking so early":
                                scene b_tv_d with fade
                                b "{i}(We'll see){/i}"
                                #V9?
                                jump mdrinking

                            "Continue watching tv":
                                scene b_tv_d with fade
                                b "{i}(I'll continue watching){/i}"
                                call screen gnav
                    else:
                        scene b_tv_d6 with dissolve
                        m "..."
                        scene b_tv_d with fade
                        b "{i}(I'll continue watching){/i}"
                        "GET YOUR POINTS TO 120"
                        call screen gnav


            "Clean" :
                if mellastrequest == 2:
                    $ Hour += 1
                    play sound "sounds/mobilering.wav"
                    $ mellastrequest = 3
                    b "Melinda!"
                    stop sound
                    scene mlc with dissolve
                    ml "{i}(Hi [bname]){/i}"
                    b "Hi"
                    ml "{i}(Amy progress with [mname]?){/i}"
                    b "No"
                    ml "{i}(Don't worry I'll take care of it){/i}"
                    ml "{i}(I just want you to take her for dinner to this restaurant){/i}"
                    ml "{i}(Any day in the evening after her work){/i}"
                    ml "{i}(Just give me a call before){/i}"
                    b "Uh... Ok"
                    ml "{i}(I'll do the reservation for you){/i}"
                    ml "{i}(Your task is to do like last time){/i}"
                    ml "{i}(The gentleman will do the rest){/i}"
                    b "Got it"
                    ml "{i}(Good luck [bname]){/i}"
                    pass
                elif jenlastmovie ==1 and mellastrequest ==0:
                    $ persistent.unlock_75 = True
                    $ Hour += 1
                    play sound "sounds/mobilering.wav"
                    $ mellastrequest = 1
                    b "Melinda!"
                    stop sound
                    scene mlc with dissolve
                    ml "{i}(Hi [bname]){/i}"
                    b "Hi"
                    ml "{i}(Are you free?){/i}"
                    b "Yes why?"
                    ml "{i}(There's a new request){/i}"
                    b "Hmm it's harder this time"
                    ml "{i}(Can you visit me?){/i}"
                    scene mlc1 with fade
                    ml "He's going to be here any minute"
                    ml "We need this, it's a lot of money"
                    c "He's here already"
                    scene mlc2 with dissolve
                    c "Here's my handsome man"
                    scene mlc3 with dissolve
                    c "I'll get you a drink"
                    scene mlc4 with dissolve
                    ml "So, can you help this time?"
                    b "Ah... I don't know really"
                    ml "It's really important this time"
                    ml "Big guns"
                    scene mlc5 with dissolve
                    ml "Speaking of guns"
                    b "..."
                    scene mlc6 with dissolve
                    ml "Stand up"
                    ml "Let Cheryl give you pleasure"
                    scene mlc7 with dissolve
                    ml "Good boy"
                    scene mlc8 with dissolve
                    ml "..."
                    scene mlc9 with dissolve
                    ml "Ahh"
                    scene mlc10 with dissolve
                    "..."
                    scene mlc11 with fade
                    ml "Look at that beautiful cock"
                    scene mlc12 with dissolve
                    "..."
                    scene mlc13 with dissolve
                    "..."
                    scene mlc14 with dissolve
                    b "Ahhh"
                    scene mlc13 with dissolve
                    b "Come here Melinda"
                    ml "Enjoy her first"
                    ml "I'll join"
                    scene mlc15 with dissolve
                    c "Ahh"
                    scene mlc16 with dissolve
                    c "God!"
                    scene mlc17 with fade
                    "..."
                    scene mlc18 with fade
                    ml "So do you think you can convince her now?"
                    b "I'll try, but you know [mname]"
                    b "On top of that, she made up her mind"
                    ml "I trust you can"
                    c "See you soon baby"
                    jump broom_menu
                else:
                    pass
                "..."
                $ Hour += 1
                if day !=7:
                    scene bclean with fade
                    play sound "sounds/vacuum_cleaner.mp3"
                    "..."
                    scene bclean1 with dissolve
                    m "What are you doing?"
                    b "{i}(Is she sober? Looks like it){/i}"
                    scene bclean2 with dissolve
                    m "..."
                    b "Cleaning"
                    $ mrel += 5
                    scene bclean3 with dissolve
                    m "[bname] please stop it"
                    m "You don't need to"
                    b "Alright"
                    scene bclean4 with dissolve
                    stop sound
                    m "Thank you sweetheart"
                    show screen mrelup
                    hide screen mrelup
                    m "I can take care of it"
                    menu:
                        "Kiss her":
                            scene bclean21 with dissolve
                            stop sound
                            m "Mmm"
                            if mrel >= 120:
                                m "..."
                                scene bclean22 with dissolve
                                m "Where... Are you taking me"
                                b "You will see"
                                menu:
                                    "Put her on the table":
                                        scene bclean23 with fade
                                        m "What are you doing?"
                                        b "I'm fucking you"
                                        scene bclean24 with dissolve
                                        m "[bname]! Not my ass"
                                        if mrel >=180:
                                            scene bclean26 with dissolve
                                            b "You don't say!"
                                            m "Please"
                                            b "I'll plow it slowly"
                                            scene bcanal
                                            m "Ahh"
                                            m "..."
                                            b "If only you can see your face right now"
                                            m "Oh [bname]"
                                            b "I'm close"
                                            scene bcanalf with dissolve
                                            m "Ahh"
                                            b "Your ass is opening up"
                                            m "Ahh"
                                            b "Fuck yes"
                                            menu:
                                                "Cum in her":
                                                    scene bclean27 with dissolve
                                                    m "Ahhh"
                                                    scene hall_d with fade
                                                    b "Damn, that was nice"
                                                    call screen gnav

                                                "Cum on her face":
                                                    scene bclean28 with dissolve
                                                    m "Mmm"
                                                    scene hall_d with fade
                                                    b "Damn, that was nice"
                                                    call screen gnav
                                        else:
                                            scene bclean25 with dissolve
                                            b "Why?"
                                            m "I said no!"
                                            scene hall_d with fade
                                            b "Damn"
                                            call screen gnav

                                    "Take her to the bed" if bandageremove ==1 and mrel >=160:
                                        scene bclean29 with fade
                                        $ persistent.unlock_47 = True
                                        m "Huh [bname] wait"
                                        play sound "sounds/morgasm1.mp3"
                                        b "Can't wait anymore"
                                        scene bmbedanim with dissolve
                                        m "Ahh"
                                        "..."
                                        b "Yes baby"
                                        m "More [bname]"
                                        scene bmbedanim with dissolve
                                        m "Mmm"
                                        m "Ahh"
                                        "..."
                                        stop sound fadeout 1.0
                                        b "Oh fuck"
                                        menu:
                                            "Cum on her back":
                                                scene bclean30 with dissolve
                                                b "Ahhh"
                                                scene bclean31 with dissolve
                                                m "..."
                                                scene hall_d with fade
                                                b "Damn, that was nice"
                                                call screen gnav

                                            "Cum on her face":
                                                b "Get on the floor quick"
                                                scene bclean28 with fade
                                                m "Mmm"
                                                scene hall_d with fade
                                                b "Damn, that was nice"
                                                call screen gnav
                                        
                            else:
                                m "No [bname]"
                                scene bclean4 with dissolve
                                b "But why?"
                                m "Let's leave it here please"
                                b "..."
                                "INCREASE YOUR RELATIONSHIP POINTS TO 120"
                                pass
                        "Don't":
                            pass
                    scene hall_d with fade
                    stop sound
                    b "Ok"
                    call screen gnav


                else:
                    scene bclean with fade
                    play sound "sounds/vacuum_cleaner.mp3"
                    "..."
                    scene bclean5 with dissolve
                    m "What are you doing?"
                    b "{i}(Is she sober? Looks like it){/i}"
                    scene bclean6 with dissolve
                    m "..."
                    b "Cleaning"
                    $ mrel += 5
                    scene bclean7 with dissolve
                    m "[bname] please stop it"
                    m "You don't need to"
                    b "Alright"
                    scene bclean8 with dissolve
                    stop sound
                    m "Thank you sweetheart"
                    show screen mrelup
                    hide screen mrelup
                    m "I can take care of it"
                    scene hall_d with fade
                    stop sound
                    b "Ok cool"
                    call screen gnav


    elif Hour >12 and Hour <=15:
        if day !=7:
            scene mhall_noona2 with fade
            b "Hmm"
            menu:
                "Wash the dishes" if dwashed==0:
                    $ Hour += 1
                    $ dwashed = 1
                    scene srg39 with dissolve
                    b "Pff"
                    scene srg40 with dissolve
                    b "..."
                    scene srg41 with dissolve
                    b "And done!"
                    m "[bname] what are you doing?"
                    $ mrel += 5
                    b "Cleaning the dishes"
                    scene mhall_noona3 with dissolve
                    show screen mrelup
                    m "Oh honey, leave everything"
                    hide screen mrelup
                    m "You don't have to"
                    b "But I wanted to help"
                    m "Get some rest please"
                    b "Ok"
                    if snameacceptjoshua == 1 and snamecherylparty ==0:
                        b "There's something I want to ask you"
                        m "What is it?"
                        b "Did [sname] tell you about the party she's invited to?"
                        scene mhall_noona5 with dissolve
                        m "Yes and it's a no!"
                        b "I think you're making a mistake"
                        b "It's better if she keeps asking you rather than sneaking without telling you"
                        m "Tell her she can try"
                        b "That's not my point, and I don't think she will do that"
                        b "But think about it, you're out most of the time"
                        b "And you won't be able to do this forever"
                        b "Plus you don't want her to rebel"
                        b "Just be on her side, and contain her"
                        scene mhall_noona6 with dissolve
                        m "..."
                        scene mhall_noona7 with dissolve
                        m "You know, you're right"
                        m "I'll go tell her I changed my mind"
                        b "Great"
                        scene mhall_noona2 with fade
                        b "One promise fulfilled"
                        $ snamecherylparty = 1
                        call screen gnav
                    else:
                        call screen gnav

                "Sit and relax":
                    scene b_tv_d with fade
                    b "{i}(Boring){/i}"
                    if Hour ==15:
                        $ Hour += 1
                        scene mhall_noona4 with dissolve
                        m "[sname] come for lunch"
                        m "[bname] come, let's eat"
                        scene mhall_morning3 with fade
                        m "Sit"
                        scene mhall_morning4 with dissolve
                        s "Emm I will go out later this evening"
                        m "And you're going to leave [bname] alone?"
                        s "Sorry it's an important modeling shoot"
                        m "For how long?"
                        s "For 2 weeks"
                        m ang "Oh perfect"
                        s "It's really important"
                        b "Don't worry about me, I'll be fine"
                        "YOU EAT YOUR MEAL IN SILENCE AND EVERYONE GOES BACK TO THEIR ROOMS"
                        call screen gnav
                    else:
                        $ Hour += 1
                        if sbmbname == 1:
                            scene mhall_noons with dissolve
                            $ persistent.unlock_16 = True
                            b "Hey [sname]"
                            s "There's something you should see"
                            b "What is it?"
                            scene mhall_noons1 with dissolve
                            s "See for yourself"
                            $ sbmbname = 2
                            scene mhall_noonsshot with dissolve
                            b "Uh huh!"
                            s "..."
                            scene mhall_noons2 with dissolve
                            b "Yeah big deal, so what!?"
                            s "You know what to do [bname]"
                            b "Oh for fucks sake, again with this?"
                            b "Alright, I'll clean your room"
                            b "Fine"
                            scene mhall_noons3 with dissolve
                            s "You know, you're such a cutie sometimes"
                            s "You want to clean my room in return for not posting this on my social media pages"
                            b "Are you serious?"
                            scene mhall_noons4 with dissolve
                            s "Yes I am"
                            b "So what do you want for not posting it?"
                            scene mhall_noons5 with dissolve
                            s "I have an odd request from one of my fans on my fansonly page"
                            s "And you are the only one to help me fulfill it"
                            b "Well..."
                            b "If it's sex related, yeah, count me in"
                            s "Great"
                            b "When do we do this?"
                            s "Meet me in my room at 16:00"
                            b "Ok"
                            scene mhall_noons6 with dissolve
                            s "You can also clean my room"
                            call screen gnav

                        else:
                            call screen gnav


        elif Hour ==13 and day ==7:
            $ Hour += 1
            scene mhall_noona with fade
            b "Hello"
            b "Are you ok?"
            m "Yes, just feeling sleepy"
            m "I'm going to get a quick nap"
            b "Ok"
            if jendidgo == 1 and bmporn2done == 1:
                m "Just thinking about life"
                scene mhall_noona8 with dissolve
                $ persistent.unlock_71 = True
                b "Why? What's wrong with our life?"
                scene mhall_noona9 with dissolve
                m "I'm thinking to stop this acting thing"
                b "What! No!!"
                m "I've made up my mind"
                $ jenlastmovie = 1
                scene mhall_noona1 with dissolve
                b "{i}(Damn that's bad news){/i}"
                call screen gnav
            else:
                m "Yes, just feeling sleepy"
                m "I'm going to get a quick nap"
                b "Ok"
                scene mhall_noona1 with dissolve
                "..."
                call screen gnav

        elif Hour ==14 and day ==7:
            $ Hour += 1
            scene mhall_noona with fade
            b "Hello"
            b "Are you ok?"
            if jendidgo == 1 and bmporn2done == 1:
                m "Just thinking about life"
                scene mhall_noona8 with dissolve
                $ persistent.unlock_71 = True
                b "Why? What's wrong with our life?"
                scene mhall_noona9 with dissolve
                m "I'm thinking to stop this acting thing"
                b "What! No!!"
                m "I've made up my mind"
                $ jenlastmovie = 1
                scene mhall_noona1 with dissolve
                b "{i}(Damn that's bad news){/i}"
                call screen gnav
            else:
                m "Yes, just feeling sleepy"
                m "I'm going to get a quick nap"
                b "Ok"
                scene mhall_noona1 with dissolve
                "..."
                call screen gnav

        elif Hour ==15 and day ==7:
            $ Hour += 1
            scene mhall_noona4 with fade
            m "[sname] come for lunch"
            m "[bname] come, let's eat"
            scene mhall_morning3 with fade
            m "Sit"
            scene mhall_morning4 with dissolve
            s "Emm I will go out later this evening"
            s "just to see my friends"
            m "For how long?"
            s "For a couple of hours"
            m "Ok"
            "YOU EAT YOUR MEAL IN SILENCE AND EVERYONE GOES BACK TO THEIR ROOMS"
            call screen gnav

    elif Hour ==16:
        $ Hour += 1
        if day ==7:
            play sound "sounds/ehhh.mp3"
            scene mhall_sunday1 with fade
            b "{i}(Wow){/i}"
            stop sound
            m "Hi [bname]!"
            b "Hi"
            scene mhall_sunday5 with dissolve
            m "Let's go to the beach"
            m "Some vitamin D for both of us"
            if cherylpoolparty ==1:
                b "Mmm"
                menu:
                    "Tell her that you're going out with [sname]":
                        m "Ok as you wish"
                        m "I'll meet up with Wanda instead"
                        jump cherylpoolparty

                    "Okay let's go":
                        pass
            "..."
            if joshuacorrupted >= 1:
                m "Or do you want to visit your friend?"
                b "Who?"
                m "Joshua"
                menu:
                    "Wanda":
                        b "Joshua of course"
                        m "Ok, but you have to behave there, ok?"
                        m "Wanda is very strict, even though she doesn't show it"
                        b "Sure"
                        jump wandapool
                    "Beach":
                        b "Beach"
                        jump msundaybeach
            else:
                jump msundaybeach

        else:
            scene mhall_wg with fade
            b "Hi"
            m "Hi"
            b "Going to work?"
            m "Yes"
            m "Take care honey, call me if you need anything"
            menu:
                "Can I invite someone over?":
                    b "So you can have peace of mind"
                    m "That's a good idea, they'll look after you?"
                    m "Elaine maybe?"
                    menu:
                        "Yes Elaine":
                            b "Great, I'll call her"
                            jump elainebs

                        "Is it possible Cheryl?":
                            scene mhall_wg3 with dissolve
                            m "Does it have to be her?" 
                            b "I mean, why not"
                            m "Alright, but make sure she leaves before I come"
                            m "And don't make a habit of it"
                            jump cherylbs

                        "The neighbors?":
                            m "Ok sounds good"
                            jump neighbs

                        "Joshua":
                            m "See if his mom allows him"
                            b "Ok I'll call him now"
                            jump joshuavisit
                        "No one, visit her at work" if wk >=2:
                            b "I'll wait for you"
                            if bandageremove ==1:
                                menu:
                                    "Visit her as Jedi":
                                        jump jvisitm
                                    "Visit as [bname]":
                                        jump bvisitm
                            else:
                                jump bvisitm

                "Ok I'll wait for you":
                    scene mroom_ent_out3 with dissolve
                    b "Ok I'll wait for you"
                    jump waitform

    elif Hour ==17 and day==7:
        $ Hour += 1
        scene hallpms with fade
        c "Oh here's my baby"
        c "How are you feeling"
        m "Aunt cheryl came to check on you"
        menu:
            "I'm good":
                b "Not bad"
                c "Good to know"
                pass
            "Now I feel better":
                c "Oh thank you, you're so adorable saying this"
                $ mrel -= 5
                show screen mreldw
                scene hallpms2 with dissolve
                m "Isn't he?"
                hide screen mreldw
                pass
        
        scene hallpms1 with dissolve
        if cwatch ==0:
            c "I have something for you"
            b "What is it?"
            $ cwatch = 1
            c "A watch, so you remember me during every second of your day"
            b "Oh thank you"
            c "Well, I'm glad that you are better"
            c "I just came to check on you"
            c "See you another time"
            scene hallpms3 with fade
            m "Show me that watch"
            pass
        else:
            c "Well, I'm glad that you are better"
            c "I just came to check on you"
            c "See you another time"
            pass

        scene hallpms4 with fade
        b "Can I ask why do you hate her?"
        m "Because she's a bitch"
        b "Oh come on"
        m "A bitch is not only in being a slut"
        m "A bitch can also be a bitch in character"
        m "But she's a bitch of a all sorts"
        b "{i}(I can't change her mind){/i}"
        b "{i}(So I'll keep quiet){/i}"
        if movieplusone >= 1:
            b "Do you still have filming?"
            $ movieplusone = 2
            scene hallpms6 with dissolve
            m "Yes, but I'm thinking to call sick"
            b "It's probably the last time, why would you want to call sick"
            b "Jut get on with it, and that's it"
            scene hallpms5 with dissolve
            m "Do you think so?"
            b "Yes probably"
            jump lastmovie1

        elif jendidgo == 1 and bmporn2done == 1:
            $ jenlastmovie = 1
            b "Do you have filming today?"
            scene hallpms6 with dissolve
            $ persistent.unlock_71 = True
            m "I don't know"
            m "I'm thinking to stop this acting thing"
            scene hallpms5 with dissolve
            b "What! No!!"
            m "No [bname]"
            m "I've made up my mind"
            b "Damn!"
            b "So what happens now?"
            scene hallpms4 with dissolve
            m "I'll go inform them, I guess there should be a notice"
            m "Do you want to come with me?"
            b "Crap"
            b "Yes"
            jump lastmovie

        elif jenlastmovie ==1:
            b "So did you really made up your mind about acting?"
            scene hallpms6 with dissolve
            $ persistent.unlock_71 = True
            m "Yes"
            b "Damn!"
            b "So what happens now?"
            scene hallpms4 with dissolve
            m "I'll go inform them, I guess there should be a notice"
            m "Do you want to come with me?"
            b "Crap"
            b "Yes"
            jump lastmovie

        else:
            pass
        b "Ok, I'll go to my room"
        if melcallivan ==0 and persistent.unlock_28 == True:
            $ melcallivan = 1
            b "By the way?"
            b "Aren't we going to the shooting today?"
            m "Not I don't have today"
            m "I have a meeting with them"
            b "Ok I'll go with you"
            m "They're sending me a car"
            m "No need to come"
            b "No, I'd like to come"
            play sound "sounds/mobilering.wav"
            b "Oh my phone"
            b "Yes hello"
            scene melcall2 with fade
            ml "Hi [bname]"
            ml "Are you busy?"
            b "{i}(Well yes I was going out){/i}"
            m "{i}(No need dear, just go with your friends){/i}"
            menu:
                "Go visit Melinda":
                    b "{i}(Just a moment){/i}"
                    "IF YOU CHOOSE TO VISIT MELINDA YOU'LL HAVE AN OPTION TO SEE THE MOVIE AGAIN"
                    scene hallpms5 with dissolve
                    b "Are you sure?"
                    m "Yes, I have a driver don't worry"
                    scene melcall2 with dissolve
                    b "{i}(Ok I'll be there){/i}"
                    ml "Here's the address"
                    scene melcall3 with dissolve
                    ml "He's coming"
                    c "Cool"
                    ml "Why are you always so keen on meeting him"
                    ml "What's with him?"
                    c "Nothing specific, I don't want to be out of the picture"
                    c "Here he comes"
                    jump melcherpool

                "Watch [mname] from player's perspective":
                    "DON'T WORRY YOU'LL BE ABLE TO SEE THIS AGAIN"
                    "IF YOU WANT YOU CAN ROLLBACK AND GO VISIT MELINDA"
                    jump mpornmovie1
        elif wk >=2:
            m "Go get ready"
            b "Why?"
            m "I have shooting today"
            m "If you want to come with me"
            menu:
                "Can I film with you?" if bmmovie ==0:
                    m "What do you mean?"
                    $ bmmovie = 1
                    b "I want to star with you in a movie"
                    m ang "No way"
                    m "Now get ready, we need to be there in half an hour"
                    jump mpornmovie

                "Sure":
                    if bmmovie ==3:
                        if bmporn2done == 1:
                            jump mpornmovie2
                        if persistent.unlock_28 == True:
                            jump bmporn2
                        
                        elif persistent.unlock_19 == True:
                            jump bmporn1
                        else:
                            jump bmporn
                    else:
                        jump mpornmovie
        else:
            jump broom_menu

    elif Hour ==18 and day==7:
        jump snamehallsunday

    elif Hour >=19 and day==7:
            scene halln_m_in with fade
            b "Hi"
            m "Hi are you ok?"
            b "Yes,I just want to watch some TV?"
            m "Yes"
            b "Where is [sname]"
            menu:
                "She's not here":
                    m "She's not here"
                    pass
                "She's in her room":
                    m "She's in her room"
                    $ nadiajoin = 1
                    pass

            
            b "Ah Ok"
            scene halln_m_in1 with dissolve
            m "What are we watching?"
            scene halln_m_in2 with dissolve
            b "A romantic movie"
            m ang "No it's not"
            m "That's porn"
            b "Well, can I see a little bit, at least, I want to know if I can still get it up"
            if mrel>=110:
                m "Ok, just for few minutes"
                scene halln_m0 with dissolve
                b "Damn it, I didn't feel anything"
                m "Relax honey, it's just normal after an operation"
                b "I'm really worried"
                m "Stop being paranoid please"
                m "She's good isn't she?"
                menu:
                    "She looks like Wanda":
                        b "Kind of reminds me of Wanda"
                        m "Really!?"
                        b "Sort of"
                        scene halln_m1 with dissolve
                        b "Hmm"
                        scene halln_m2 with dissolve
                        m "Undress yourself"
                        scene halln_m3 with dissolve
                        m "Wanda ey!"
                        scene halln_m4 with dissolve
                        m "Who is hotter, wanda or me?"
                        b "I like this game"
                        b "Wanda!"
                        scene halln_m5 with dissolve
                        m "..."
                        scene halln_m6 with dissolve
                        m "Seems your little penis says otherwise"
                        scene halln_m7 with dissolve
                        m "..."
                        scene halln_m8 with dissolve
                        m "Right?"
                        scene halln_m9 with dissolve
                        m "Oops sorry"
                        if binjected ==0:
                            m "What happened"
                            m "Did you?"
                            scene halln_m10 with dissolve
                            m "I'm so sorry"
                            m "Good night sweetie"
                            b "{i}(I forgot to inject, it's better I go sleep){/i}"
                            jump newday
                        else:
                            b "Ahh"
                            m "Ok I'll do this for you on one condition"
                            m "You don't move a tiny bit"
                            m "No hands nothing"
                            b "Like nothing?"
                            m "Nothing, no hands, no abdomen nothing"
                            m "I'm worried about your wound"
                            m "If you move I'll stop and you go to sleep"
                            b "Ok"
                            scene rcm
                            b "..."
                            b "Ah"
                            b "Ahh"
                            "..."
                            menu:
                                "Continue":
                                    pass
                                "Take a break and move her to the floor":
                                    scene halln_m29 with fade
                                    $ persistent.unlock_26 = True
                                    m "Ah Just be careful honey"
                                    scene halln_m30 with dissolve
                                    m "Ugh"
                                    scene halln_m31 with dissolve
                                    m "Yeah"
                                    scene halln_m32 with dissolve
                                    m "Ahh"
                                    m "I want your dirty asshole"
                                    b "Yes"
                                    scene halln_m33 with dissolve
                                    m "Mmm"
                                    scene halln_m34 with dissolve
                                    m "..."
                                    scene halln_m35 with dissolve
                                    m "..."
                                    scene halln_m36 with dissolve
                                    m "Oh"
                                    b "Fuck!"
                                    scene halln_m37 with fade
                                    m "Good night"
                                    b "Good night"
                                    jump newday

                            b "Ahhhhh"
                            scene halln_m11 with dissolve
                            m "Mhhm good"
                            b "Yeah"
                            b "That was torture, but totally worth it"
                            m "At least now you know it's working"
                            b "True, thank you"
                            m "Good night honey"
                            b "Good night"
                            jump newday


                    "But not as beautiful as you":
                        scene halln_m12 with dissolve
                        m "Oh honey, that's so sweet"
                        if bandageremove ==1:
                            scene halln_m38 with dissolve
                            m "Mmm"
                            scene halln_m39 with dissolve
                            m "What about [sname]? She may come any minute"
                            b "Don't worry she's sleeping"
                            scene halln_m40 with dissolve
                            m "..."
                            scene halln_m41 with dissolve
                            m "Let me..."
                            scene halln_m42 with dissolve
                            m "Mmmhhm"
                            scene halln_m43 with dissolve
                            m "I know you want this"
                            m "Happy?"
                            scene halln_m44 with dissolve
                            m "What, cat got your tongue?"
                            scene halln_m45 with dissolve
                            b "No"
                            m "Ahh"
                            scene halln_m46 with dissolve
                            m "Yes"
                            scene halln_m47 with dissolve
                            m "..."
                            scene halln_m48 with dissolve
                            m "Ohhh"
                            b "Mmm"
                            scene halln_m49 with dissolve
                            b "..."
                            scene halln_m50 with dissolve
                            m "Ughhh"
                            scene halln_m51 with fade
                            b "Good night"
                            m "Good night"
                            scene halln_m52 with fade
                            m "{i}(Why is it only him who can make me cum so hard){/i}"
                            scene halln_m53 with dissolve
                            m "{i}(Is it the taboo?){/i}"
                            scene halln_m54 with dissolve
                            m "Ahhh"
                            scene black
                            "..."
                            jump newday


                        else:
                            pass
                        b "Can you help me with my problem?"
                        m "Ah naughty boy"
                        scene halln_m8 with dissolve
                        m "But you know! you deserve it"
                        m "Aha, you're so quick to undress"
                        scene halln_m13 with dissolve
                        b "Mmm"
                        scene halln_m14 with dissolve
                        "..."
                        if nadiajoin == 1:
                            b "Ride on me"
                            scene halln_mn with fade
                            m "Don't move"
                            m "Let me do it"
                            scene halln_mn1 with dissolve
                            b "Yeah"
                            scene halln_mn2 with dissolve
                            m "Ahh"
                            scene halln_mn3 with dissolve
                            s "Huh"
                            scene halln_mn4 with dissolve
                            m "Oh honey, it isn't..."
                            s "It's exactly what it is"
                            $ persistent.unlock_12 = True
                            scene halln_mn5 with dissolve
                            m "Listen"
                            m "I'm not happy doing this"
                            m "But his condition is worrying"
                            s "Wow, as if you don't know [bname]"
                            b "Come on, I'm suffering here"
                            if srel >= 140:
                                s "You little shit"
                                scene halln_mn6 with dissolve
                                b "Me?"
                                s "Yes, no body likes you"
                                scene halln_mn7 with dissolve
                                m "I'll teach you how to do it for him"
                                s "Don't be so excited"
                                m "It's for his sake, ride on him"
                                scene halln_mn8 with dissolve
                                b "[mname] your lips are great"
                                scene halln_mn9 with dissolve
                                m "Mmmm"
                                scene halln_mn10 with dissolve
                                s "Wow"
                                scene halln_mn11 with dissolve
                                m "Oh"
                                scene halln_mn12 with dissolve
                                s "Mmm"
                                b "Your turn [sname]"
                                scene halln_mn13 with dissolve
                                s "Ohhh"
                                b "It's close"
                                scene halln_mn14 with fade
                                s "..."
                                scene halln_mn15 with dissolve
                                m "Mmm"
                                scene halln_mn16 with dissolve
                                s "I hate you"
                                b lau "Good night"
                                jump newday
                            else:
                                s "No, I don't want to have a share in ruining this family"
                                s "Sorry"
                                m "Hmm"
                                m "Ok"
                                "YOU NEED 140 [sname] RELATIONSHIP POINTS"
                                if mrel >=140:
                                    m "I'll go to sleep now, good night honey"
                                    scene halln_m16 with fade
                                    b "Wait"
                                    scene halln_m17 with dissolve
                                    m "I know you love them honey, but you've got to sleep"
                                    scene halln_m18 with dissolve
                                    m "Ok you can play a little"
                                    m "But no fucking"
                                    b "Oh yeah!"
                                    scene halln_m19 with dissolve
                                    m "Mmm"
                                    m "Be careful"
                                    scene halln_m20 with dissolve
                                    play sound "sounds/mldm.mp3"
                                    m "Oh"
                                    stop sound
                                    scene halln_m20a with dissolve
                                    b "Yeah!"
                                    scene halln_m21 with dissolve
                                    m "Ahhh"
                                    m "Show me your wound, you're such a clumsy boy!!"
                                    scene halln_m22 with dissolve
                                    m "Seems ok"
                                    m "Oh you didn't finish?"
                                    b "I can't, I told you there's a problem"
                                    menu:
                                        "Maybe you can suck it?" if mrel >=160:
                                            scene halln_m23 with dissolve
                                            m "Oh really?!"
                                            scene halln_m24 with fade
                                            m "..."
                                            scene halln_m25 with dissolve
                                            b "Good girl"
                                            scene halln_m26 with dissolve
                                            b "Ughh"
                                            scene halln_m27 with fade
                                            $ persistent.unlock_7 = True
                                            m "..."
                                            menu:
                                                "Piss":
                                                    "THIS EVENT IS AVAILABLE FOR HIGHEST TIER ONLY"
                                                    scene halln_m27p with dissolve
                                                    m "Huh!"
                                                    scene halln_m28p with dissolve
                                                    m "Ughh"
                                                    scene halln_m29p with fade
                                                    show screen mcorr
                                                    m "{i}(...){/i}"
                                                    hide screen mcorr
                                                    $ mcorr += 5
                                                    "ALTHOUGH SHE FELT HUMILIATED, BUT SHE LIKED IT"
                                                    jump newday

                                                "Continue":
                                                    m "Good night"
                                                    b "Good night"
                                                    jump newday
                                        "Continue":
                                            m "You're just paranoid"
                                            m "I'll go to sleep now, good night honey"
                                            b "Good night"
                                            "140 POINTS NEEDED"
                                            jump newday
                                else:
                                    scene halln_m16 with fade
                                    m "I'll go to sleep now, good night honey"
                                    b "Good night"
                                    "140 POINTS NEEDED"
                                    jump newday
                        else:
                            m "..."
                            pass
                        "..."
                        if binjected ==0:
                            m "Ahh see, you're hard"
                            scene halln_m15 with dissolve
                            m "Did you finish?"
                            m "I'm so sorry"
                            m "Good night sweetie"
                            b "{i}(I forgot to inject, it's better I go sleep){/i}"
                            jump newday

                        else:
                            m "You're hard at least that's a good sign"
                            b "Yes, but not like before"
                            m "Thanks god no more donkey dick"
                            b "Hey it's not nice"
                            if mrel >=140:
                                m "Anyway [bname] that's a good sign"
                                m "I'll go to sleep now, good night honey"
                                scene halln_m16 with dissolve
                                b "Wait"
                                scene halln_m17 with dissolve
                                m "I know you love them honey, but you've got to sleep"
                                scene halln_m18 with dissolve
                                m "Ok you can play a little"
                                m "But no fucking"
                                b "Oh yeah!"
                                scene halln_m19 with dissolve
                                m "Mmm"
                                m "Be careful"
                                scene halln_m20 with dissolve
                                play sound "sounds/mldm.mp3"
                                m "Oh"
                                stop sound
                                scene halln_m20a with dissolve
                                b "Yeah!"
                                scene halln_m21 with dissolve
                                m "Ahhh"
                                m "Show me your wound, you're such a clumsy boy!!"
                                scene halln_m22 with dissolve
                                m "Seems ok"
                                m "Oh you didn't finish?"
                                b "I can't, I told you there's a problem"
                                menu:
                                    "Maybe you can suck it?" if mrel >=160:
                                        scene halln_m23 with dissolve
                                        m "Oh really?!"
                                        scene halln_m24 with fade
                                        m "..."
                                        scene halln_m25 with dissolve
                                        b "Good girl"
                                        scene halln_m26 with dissolve
                                        b "Ughh"
                                        scene halln_m27 with fade
                                        $ persistent.unlock_7 = True
                                        m "..."
                                        menu:
                                            "Piss":
                                                "THIS EVENT IS AVAILABLE FOR HIGHEST TIER ONLY"
                                                scene halln_m27p with dissolve
                                                m "Huh!"
                                                scene halln_m28p with dissolve
                                                m "Ughh"
                                                scene halln_m29p with fade
                                                show screen mcorr
                                                m "{i}(...){/i}"
                                                hide screen mcorr
                                                $ mcorr += 5
                                                "ALTHOUGH SHE FELT HUMILIATED, BUT SHE LIKED IT"
                                                jump newday

                                            "Continue":
                                                m "Good night"
                                                b "Good night"
                                                jump newday
                                    "Continue":
                                        m "You're just paranoid"
                                        m "I'll go to sleep now, good night honey"
                                        b "Good night"
                                        "140 POINTS NEEDED"
                                        jump newday
                            else:
                                m "Anyway [bname] that's a good sign"
                                m "I'll go to sleep now, good night honey"
                                b "Good night"
                                "140 POINTS NEEDED"
                                jump newday
            else:
                m "All right"
                m "I'm really tired I need to sleep"
                m "Good night"
                scene halln_m_in3 with dissolve
                b "{i}(Damn){/i}"
                scene hall_night with fade
                b "{i}(It's better I go sleep){/i}"
                "RAISE YOUR POINTS TO 110 AT LEAST"
                jump newday


############################################################################33

    elif Hour >=17 and day!=7:
        scene hall_night with fade
        b "{i}(There's nothing to do){/i}"
        menu:
            "Who to call?":
                b "{i}(Hmm){/i}"
                menu:
                    "Elaine":
                        jump elainebs

                    "Cheryl?":
                        jump cherylbs

                    "The neighbors?":
                        jump neighbs

                    "Joshua":
                        jump joshuavisit

            "Wait for [mname]":
                jump waitform

            "Go to another room":
                call screen gnav
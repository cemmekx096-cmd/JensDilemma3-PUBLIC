

label mlaptophelp:
    scene mlh with fade
    b "So what exactly are you looking for?"
    scene mlh1 with dissolve
    m "There's this website Elaine told me about"
    m "Where you can sell your photos and videos"
    b "Ah you mean this one?"
    scene mlh2 with dissolve
    m "Yes that's it"
    scene mlh1 with dissolve
    if buyjewelry ==3:
        b "But I don't get it, why do you want to post here"
        b "When you can work with an elite ageency?"
        m "What do you mean?"
        b "There are Elite VIP escort agencies"
        b "Where you can meet wealthy people"
        m "No [bname] I'm not doing that"
        b "I don't understand what have you got against such work"
        b "It's much better than being a freelancer"
        b "And in such agencies you can meet people of the same caliber as Trump"
        m "Is it? Really?"
        b "Yeah"
        scene mlh3 with dissolve
        m "Hmmm"
        m "{i}(If this is true){/i}"
        scene mlh4 with dissolve
        m "{i}(It would open great opportunities){/i}"
        m "{i}(I need to verify this){/i}"
        m "{i}(But how come Elaine never told me about it){/i}"
        b "Ermm the page is set up"
        b "Mm shall we take some photos then?"
        scene mlh5 with dissolve
        m "Yeah! Great! Thank you"
        b "Here take a look"
        scene mlh1 with dissolve
        m "Looks perfect"
        b "Let's go then"
        if joshuadaydone == 1:
            m "By the way"
            m "Where's Joshua?"
            m "I heard him coming"
            b "He left, long time ago"
            b "Can't stay more than one hour"
            m "Ok let's go"
            pass
        else:
            pass
        if persistent.unlock_64 == True:
            scene mlh6n with fade
            b "Nice dress"
            menu:
                "Keep it":
                    b "Yep, that's great, keep the serious look"
                    b "Another shot"
                    scene mlh7n with dissolve
                    b "Perfect"
                    b "Close up"
                    scene mlh8n with dissolve
                    b "Cool"
                    if joshuadaydone == 1:
                        $ persistent.unlock_54 = True
                        scene mlh9j with dissolve
                        j "..."
                        pass
                    else:
                        pass
                    b "Do you have a different thing to wear?"
                    if mrel >=150 and joshuadaydone == 1:
                        jump mnamejoshua
                    else:
                        m "That's enough for today"
                        b "Oh come on!"
                        m "I said enough"
                        scene hall_d with fade
                        b "{i}(Damn this){/i}"
                        call screen gnav

                "Wear Lingerie better":
                    scene mlh6bn with dissolve
                    b "Yeah that's better"
                    b "Another shot"
                    scene mlh7bn with dissolve
                    b "Perfect"
                    b "Close up"
                    scene mlh8bn with dissolve
                    b "Cool"
                    if joshuadaydone == 1:
                        $ persistent.unlock_54 = True
                        scene mlh9j with dissolve
                        j "..."
                        pass
                    else:
                        pass
                    b "Do you have a different thing to wear?"
                    if mrel >=150 and joshuadaydone == 1:
                        jump mnamejoshua
                    else:
                        m "That's enough for today"
                        b "Oh come on!"
                        m "I said enough"
                        scene hall_d with fade
                        b "{i}(Damn this){/i}"
                        call screen gnav
            
        else:
            pass
        scene mlh6 with fade
        b "Yep, that's great, keep the serious look"
        b "And..."
        b "Done"
        b "Another shot"
        scene mlh7 with dissolve
        b "Perfect"
        b "Close up"
        scene mlh8 with dissolve
        b "A bit more explicit"
        scene mlh9 with dissolve
        b "Cool"
        if joshuadaydone == 1:
            $ persistent.unlock_54 = True
            scene mlh9j with dissolve
            j "..."
            pass
        else:
            pass
        b "Do you have a different thing to wear?"
        if mrel >=150:
            $ persistent.unlock_45 = True
            scene mlh10 with dissolve
            m "Yes I'll change"
            scene mlh11 with fade
            b "Oh wow great"
            b "Can you turn?"
            b "Let's take a shot of the back"
            scene mlh12 with dissolve
            b "{i}(Oh my fucking god){/i}"
            menu:
                "Put the camera and go to her":
                    scene mlh14 with dissolve
                    m "[bname] not now please"
                    b "Ok"
                    b "Let's take one more"
                    pass
                "Continue":
                    pass
            scene mlh15 with dissolve
            b "Wow"
            m "Happy now?"
            b "Indeed"
            b "Let's take more"
            m "Let me change, I have an outfit to try for my next shoot"
            b "Ok cool"
            scene mlh16 with fade
            b "Not bad!"
            scene mlh17 with dissolve
            b "Something more hot maybe?"
            scene mlh18 with dissolve
            b "Oh wow"
            b "More?"
            scene mlh19 with dissolve
            m "Last one"
            b "Oh come on!"
            m "No [bname] just leave"
            if joshuadaydone == 1:
                b "Why don't you change"
                m "What do you mean?"
                b "Why don't you put something on"
                m "I think I have something to wear"
                scene mlh20a with dissolve
                m "Good idea"
                m "I'll be back"
                scene mlh21j with dissolve
                b "Sit tight"
                b "You're gonna get some action today"
                b "Just don't freak out when I give you sign to join"
                b "And no fucking word or moan"
                b "Or you're doomed"
                j "Ok"
                menu:
                    "Let's solve your issue of last time" if persistent.unlock_63 == True:
                        j "What do you mean?"
                        scene mlh10j with dissolve
                        b "Take this masturbate to it"
                        b "It will make you last longer"
                        scene mlh11j with dissolve
                        b "I'll go buy us some more time"
                        scene black
                        "..."
                        scene mlh21j with dissolve
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
                scene mlh22j with dissolve
                b "Oh my god, wow"
                b "Can we take photos with a blindfold"
                if mcorr >=40:
                    $ persistent.unlock_63 = True
                    m "Ok"
                    scene mlh24j with dissolve
                    b "Oh my, I feel I want to eat you"
                    m "Hehe"
                    scene mlh25j with dissolve
                    b "Can I play with this?"
                    m "Men don't ask [bname]"
                    b "Undress yourself"
                    scene mlh26j with dissolve
                    b "..."
                    scene mlh27j with dissolve
                    m "[bname] your hands are sweating"
                    m "Are you stressed"
                    b "Uhh no no"
                    b "Just feeling hot"
                    m "It's ok, I kind of like it"
                    m "Steamy"
                    b "{i}(Oh damn she's gonna notice his shirt){/i}"
                    b "I'll take my shirt off"
                    m "Ok"
                    scene mlh28j with dissolve
                    m "That's better"
                    scene mlh29j with dissolve
                    m "You're so passionate and warm today [bname]"
                    scene mlh30j with dissolve
                    m "You love them so much"
                    m "You know I like this blindfold thing"
                    m "Why don't you kiss more"
                    b "He's not gonna last long"
                    scene mlh31j with dissolve
                    m "What?"
                    b sur "Errr."
                    b "I mean my penis will blow soon"
                    b "Let's try anyway"
                    m "No, I want to suck you"
                    if jmasturbate == 1:
                        b "Ok"
                        pass
                    else:
                        b sur "I won't last long, come on!"
                        pass
                    m "I said I want"
                    m "No choice"
                    b "{i}(Damn){/i}"
                    b "Ok let me undress"
                    scene mlh32j with dissolve
                    j "...."
                    b "Do it!"
                    m "What?"
                    b "Nothing, my zipper"
                    scene mlh33j with dissolve
                    j "Ahh"
                    b "{i}(I must be really sick in order to do this){/i}"
                    m "Lots of precum today [bname]"
                    j "Ahhhh"
                    scene mlh34j with dissolve
                    m "Mmm"
                    if jmasturbate == 1:
                        scene mlh42j with dissolve
                        j "..."
                        scene mlh43j with dissolve
                        show screen jcorr
                        j "Ahh"
                        $ jcorr += 1
                        hide screen jcorr
                        scene mlh35j with dissolve
                        b "{i}(Shut the fuck up){/i}"
                        scene mlh44j with dissolve
                        b "{i}(How I wish I can join in){/i}"
                        scene mlh45j with dissolve
                        m "Come on give it to me!"
                        scene mlh46j with dissolve
                        b "{i}(Do it idiot!){/i}"
                        scene mlh47j with dissolve
                        $ persistent.unlock_64 = True
                        b "{i}(Go ahead){/i}"
                        "[bname] NODS FOR HIM"
                        scene mlh48j with dissolve
                        j "..."
                        scene mlh48ja with dissolve
                        b "{i}(I'll capture this){/i}"
                        $ bmljosh = 1
                        scene mlh48j with dissolve
                        j "..."
                        scene mlh49j with dissolve
                        m "Ahh"
                        b "On the floor"
                        scene mlh50j with dissolve
                        b "Let's do it harder"
                        m "Just shut it and fuck me"
                        scene mlh51j with dissolve
                        m  "Yes like that"
                        scene mlh52j with dissolve
                        m "Ahh yess!"
                        scene mlh54j with dissolve
                        m "That was hot baby boy"
                        b "{i}(What the fuck, why did she call me that){/i}"
                        scene mlh35j with dissolve
                        b "{i}(Get out damn){/i}"
                        j "Uh huh!"
                        scene mlh55j with dissolve
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

                            "One thing before you go"if josh_hidden_cam ==0:
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
                        pass
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
            else:
                b "Okay"
                pass
            scene hall_d with fade
            b "{i}(Nice){/i}"
            call screen gnav

        else:
            m "That's enough for today"
            b "Uh ok"
            scene hall_d with fade
            b "{i}(Dang!){/i}"
            "RAISE YOUR RELATIONSHIP POINTS WITH [mname] TO 150"
            call screen gnav
    elif escortrequest == 2:
        b "But I don't get it, why do you want to post here"
        b "When you can work with an elite ageency?"
        m "What do you mean?"
        b "There are Elite VIP escort agencies"
        b "Where you can meet wealthy people"
        m "No [bname] I'm not doing that"
        b "I don't understand what have you got against such work"
        b "It's much better than being a freelancer"
        b "And in such agencies you can meet people of the same caliber as Trump"
        m "Is it? Really?"
        b "Yeah"
        scene mlh3 with dissolve
        m "Hmmm"
        m "{i}(If this is true){/i}"
        scene mlh4 with dissolve
        m "{i}(It would open great opportunities){/i}"
        m "{i}(I need to verify this){/i}"
        m "{i}(But how come Elaine never told me about it){/i}"
        b "Ermm the page is set up"
        b "Mm shall we take some photos then?"
        scene mlh5 with dissolve
        m "Yeah! Great! Thank you"
        b "Here take a look"
        scene mlh1 with dissolve
        m "Looks perfect"
        b "Let's go then"
        if joshuadaydone == 1:
            m "By the way"
            m "Where's Joshua?"
            m "I heard him coming"
            b "He left, long time ago"
            b "Can't stay more than one hour"
            m "Ok let's go"
            pass
        else:
            pass
        scene mlh6 with fade
        b "Yep, that's great, keep the serious look"
        b "And..."
        b "Done"
        b "Another shot"
        scene mlh7 with dissolve
        b "Perfect"
        b "Close up"
        scene mlh8 with dissolve
        b "A bit more explicit"
        scene mlh9 with dissolve
        b "Cool"
        if joshuadaydone == 1:
            $ persistent.unlock_54 = True
            scene mlh9j with dissolve
            j "..."
            pass
        else:
            pass
        b "Do you have a different thing to wear?"
        if mrel >=150:
            $ persistent.unlock_45 = True
            scene mlh10 with dissolve
            m "Yes I'll change"
            scene mlh11 with fade
            b "Oh wow great"
            b "Can you turn?"
            b "Let's take a shot of the back"
            scene mlh12 with dissolve
            b "{i}(Oh my fucking god){/i}"
            menu:
                "Put the camera and go to her":
                    scene mlh14 with dissolve
                    m "[bname] not now please"
                    b "Ok"
                    b "Let's take one more"
                    pass
                "Continue":
                    pass
            scene mlh15 with dissolve
            b "Wow"
            m "Happy now?"
            b "Indeed"
            b "Let's take more"
            m "Let me change, I have an outfit to try for my next shoot"
            b "Ok cool"
            scene mlh16 with fade
            b "Not bad!"
            scene mlh17 with dissolve
            b "Something more hot maybe?"
            scene mlh18 with dissolve
            b "Oh wow"
            b "More?"
            scene mlh19 with dissolve
            m "Last one"
            b "Oh come on!"
            m "No [bname] just leave"
            if joshuadaydone == 1:
                b "Why don't you put the jewelry on"
                scene mlh20a with dissolve
                m "Good idea"
                m "I'll be back"
                scene mlh21j with dissolve
                b "Sit tight"
                b "You're gonna get some action today"
                b "Just don't freak out when I give you sign to join"
                b "And no fucking word or moan"
                b "Or you're doomed"
                j "Ok"
                menu:
                    "Let's solve your issue of last time" if persistent.unlock_63 == True:
                        j "What do you mean?"
                        scene mlh10j with dissolve
                        b "Take this masturbate to it"
                        b "It will make you last longer"
                        scene mlh11j with dissolve
                        b "I'll go buy us some more time"
                        scene black
                        "..."
                        scene mlh21j with dissolve
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
                scene mlh22j with dissolve
                b "Oh my god, wow"
                b "Can we take photos with a blindfold"
                if mcorr >=40:
                    $ persistent.unlock_63 = True
                    m "Ok"
                    scene mlh24j with dissolve
                    b "Oh my, I feel I want to eat you"
                    m "Hehe"
                    scene mlh25j with dissolve
                    b "Can I play with this?"
                    m "Men don't ask [bname]"
                    b "Undress yourself"
                    scene mlh26j with dissolve
                    b "..."
                    scene mlh27j with dissolve
                    m "[bname] your hands are sweating"
                    m "Are you stressed"
                    b "Uhh no no"
                    b "Just feeling hot"
                    m "It's ok, I kind of like it"
                    m "Steamy"
                    b "{i}(Oh damn she's gonna notice his shirt){/i}"
                    b "I'll take my shirt off"
                    m "Ok"
                    scene mlh28j with dissolve
                    m "That's better"
                    scene mlh29j with dissolve
                    m "You're so passionate and warm today [bname]"
                    scene mlh30j with dissolve
                    m "You love them so much"
                    m "You know I like this blindfold thing"
                    m "Why don't you kiss more"
                    b "He's not gonna last long"
                    scene mlh31j with dissolve
                    m "What?"
                    b sur "Errr."
                    b "I mean my penis will blow soon"
                    b "Let's try anyway"
                    m "No, I want to suck you"
                    if jmasturbate == 1:
                        b "Ok"
                        pass
                    else:
                        b sur "I won't last long, come on!"
                        pass
                    m "I said I want"
                    m "No choice"
                    b "{i}(Damn){/i}"
                    b "Ok let me undress"
                    scene mlh32j with dissolve
                    j "...."
                    b "Do it!"
                    m "What?"
                    b "Nothing, my zipper"
                    scene mlh33j with dissolve
                    j "Ahh"
                    b "{i}(I must be really sick in order to do this){/i}"
                    m "Lots of precum today [bname]"
                    j "Ahhhh"
                    scene mlh34j with dissolve
                    m "Mmm"
                    if jmasturbate == 1:
                        scene mlh42j with dissolve
                        j "..."
                        scene mlh43j with dissolve
                        show screen jcorr
                        j "Ahh"
                        $ jcorr += 1
                        hide screen jcorr
                        scene mlh35j with dissolve
                        b "{i}(Shut the fuck up){/i}"
                        scene mlh44j with dissolve
                        b "{i}(How I wish I can join in){/i}"
                        scene mlh45j with dissolve
                        $ persistent.unlock_64 = True
                        m "Come on give it to me!"
                        scene mlh46j with dissolve
                        b "{i}(Do it idiot!){/i}"
                        scene mlh47j with dissolve
                        b "{i}(Go ahead){/i}"
                        "[bname] NODS FOR HIM"
                        scene mlh48j with dissolve
                        j "..."
                        scene mlh48ja with dissolve
                        b "{i}(I'll capture this){/i}"
                        $ bmljosh = 1
                        scene mlh48j with dissolve
                        j "..."
                        scene mlh49j with dissolve
                        m "Ahh"
                        b "On the floor"
                        scene mlh50j with dissolve
                        b "Let's do it harder"
                        m "Just shut it and fuck me"
                        scene mlh51j with dissolve
                        m  "Yes like that"
                        scene mlh52j with dissolve
                        m "Ahh yess!"
                        scene mlh54j with dissolve
                        m "That was hot baby boy"
                        b "{i}(What the fuck, why did she call me that){/i}"
                        scene mlh35j with dissolve
                        b "{i}(Get out damn){/i}"
                        j "Uh huh!"
                        scene mlh55j with dissolve
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

                            "One thing before you go":
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
                        pass
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
            else:
                b "Okay"
                pass
            scene hall_d with fade
            b "{i}(Nice){/i}"
            call screen gnav

        else:
            m "That's enough for today"
            b "Uh ok"
            scene hall_d with fade
            b "{i}(Dang!){/i}"
            "RAISE YOUR RELATIONSHIP POINTS WITH [mname] TO 150"
            call screen gnav

    else:
        b "I'll help you setup the page"
        m "Great"
        b "And then we can take some photos"
        scene mlh4 with dissolve
        b "Ermm the page is set up"
        b "Mm shall we take some photos then?"
        scene mlh5 with dissolve
        m "Yeah! Great! Thank you"
        b "Here take a look"
        scene mlh1 with dissolve
        m "Looks perfect"
        b "Let's go then"
        if joshuadaydone == 1:
            m "By the way"
            m "Where's Joshua?"
            m "I heard him coming"
            b "He left, long time ago"
            b "Can't stay more than one hour"
            m "Ok let's go"
            pass
        else:
            pass
        scene mlh6 with fade
        b "Yep, that's great, keep the serious look"
        b "And..."
        b "Done"
        b "Another shot"
        scene mlh7 with dissolve
        b "Perfect"
        b "Close up"
        scene mlh8 with dissolve
        b "A bit more explicit"
        scene mlh9 with dissolve
        b "Cool"
        if joshuadaydone == 1:
            $ persistent.unlock_54 = True
            scene mlh9j with dissolve
            j "..."
            pass
        else:
            pass
        b "Do you have a different thing to wear?"
        if mrel >=150:
            $ persistent.unlock_45 = True
            scene mlh10 with dissolve
            m "Yes I'll change"
            scene mlh11 with fade
            b "Oh wow great"
            b "Can you turn?"
            b "Let's take a shot of the back"
            scene mlh12 with dissolve
            b "{i}(Oh my fucking god){/i}"
            menu:
                "Put the camera and go to her":
                    scene mlh14 with dissolve
                    m "[bname] not now please"
                    b "Ok"
                    b "Let's take one more"
                    pass
                "Continue":
                    pass
            scene mlh15 with dissolve
            b "Wow"
            m "Happy now?"
            b "Indeed"
            b "Let's take more"
            m "Let me change, I have an outfit to try for my next shoot"
            b "Ok cool"
            scene mlh16 with fade
            b "Not bad!"
            scene mlh17 with dissolve
            b "Something more hot maybe?"
            scene mlh18 with dissolve
            b "Oh wow"
            b "More?"
            scene mlh19 with dissolve
            m "Last one"
            b "Oh come on!"
            m "No [bname] just leave"
            if joshuadaydone == 1:
                b "Why don't you put the jewelry on"
                scene mlh20a with dissolve
                m "Good idea"
                m "I'll be back"
                scene mlh21j with dissolve
                b "Sit tight"
                b "You're gonna get some action today"
                b "Just don't freak out when I give you sign to join"
                b "And no fucking word or moan"
                b "Or you're doomed"
                j "Ok"
                menu:
                    "Let's solve your issue of last time" if persistent.unlock_63 == True:
                        j "What do you mean?"
                        scene mlh10j with dissolve
                        b "Take this masturbate to it"
                        b "It will make you last longer"
                        scene mlh11j with dissolve
                        b "I'll go buy us some more time"
                        scene black
                        "..."
                        scene mlh21j with dissolve
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
                scene mlh22j with dissolve
                b "Oh my god, wow"
                b "Can we take photos with a blindfold"
                if mcorr >=40:
                    $ persistent.unlock_63 = True
                    m "Ok"
                    scene mlh24j with dissolve
                    b "Oh my, I feel I want to eat you"
                    m "Hehe"
                    scene mlh25j with dissolve
                    b "Can I play with this?"
                    m "Men don't ask [bname]"
                    b "Undress yourself"
                    scene mlh26j with dissolve
                    b "..."
                    scene mlh27j with dissolve
                    m "[bname] your hands are sweating"
                    m "Are you stressed"
                    b "Uhh no no"
                    b "Just feeling hot"
                    m "It's ok, I kind of like it"
                    m "Steamy"
                    b "{i}(Oh damn she's gonna notice his shirt){/i}"
                    b "I'll take my shirt off"
                    m "Ok"
                    scene mlh28j with dissolve
                    m "That's better"
                    scene mlh29j with dissolve
                    m "You're so passionate and warm today [bname]"
                    scene mlh30j with dissolve
                    m "You love them so much"
                    m "You know I like this blindfold thing"
                    m "Why don't you kiss more"
                    b "He's not gonna last long"
                    scene mlh31j with dissolve
                    m "What?"
                    b sur "Errr."
                    b "I mean my penis will blow soon"
                    b "Let's try anyway"
                    m "No, I want to suck you"
                    if jmasturbate == 1:
                        b "Ok"
                        pass
                    else:
                        b sur "I won't last long, come on!"
                        pass
                    m "I said I want"
                    m "No choice"
                    b "{i}(Damn){/i}"
                    b "Ok let me undress"
                    scene mlh32j with dissolve
                    j "...."
                    b "Do it!"
                    m "What?"
                    b "Nothing, my zipper"
                    scene mlh33j with dissolve
                    j "Ahh"
                    b "{i}(I must be really sick in order to do this){/i}"
                    m "Lots of precum today [bname]"
                    j "Ahhhh"
                    scene mlh34j with dissolve
                    m "Mmm"
                    if jmasturbate == 1:
                        scene mlh42j with dissolve
                        j "..."
                        scene mlh43j with dissolve
                        show screen jcorr
                        j "Ahh"
                        $ jcorr += 1
                        hide screen jcorr
                        scene mlh35j with dissolve
                        b "{i}(Shut the fuck up){/i}"
                        scene mlh44j with dissolve
                        b "{i}(How I wish I can join in){/i}"
                        scene mlh45j with dissolve
                        m "Come on give it to me!"
                        scene mlh46j with dissolve
                        b "{i}(Do it idiot!){/i}"
                        scene mlh47j with dissolve
                        $ persistent.unlock_64 = True
                        b "{i}(Go ahead){/i}"
                        "[bname] NODS FOR HIM"
                        scene mlh48j with dissolve
                        j "..."
                        scene mlh48ja with dissolve
                        b "{i}(I'll capture this){/i}"
                        $ bmljosh = 1
                        scene mlh48j with dissolve
                        j "..."
                        scene mlh49j with dissolve
                        m "Ahh"
                        b "On the floor"
                        scene mlh50j with dissolve
                        b "Let's do it harder"
                        m "Just shut it and fuck me"
                        scene mlh51j with dissolve
                        m  "Yes like that"
                        scene mlh52j with dissolve
                        m "Ahh yess!"
                        scene mlh54j with dissolve
                        m "That was hot baby boy"
                        b "{i}(What the fuck, why did she call me that){/i}"
                        scene mlh35j with dissolve
                        b "{i}(Get out damn){/i}"
                        j "Uh huh!"
                        scene mlh55j with dissolve
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

                            "One thing before you go":
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
                        pass
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
            else:
                b "Okay"
                pass
            scene hall_d with fade
            b "{i}(Nice){/i}"
            call screen gnav

        else:
            m "That's enough for today"
            b "Uh ok"
            scene hall_d with fade
            b "{i}(Dang!){/i}"
            "RAISE YOUR RELATIONSHIP POINTS WITH [mname] TO 150"
            call screen gnav
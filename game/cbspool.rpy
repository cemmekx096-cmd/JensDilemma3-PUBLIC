

label cbspool:
    if bandageremove ==1:
        scene sroom_c1 with fade
        b "Let's go?"
        s "Rowena is back in town, I'm thinking to call her if she wants to come with us"
        s "What do you say?"
        menu:
            "Yes why not":
                s "Ok I'll call her"
                jump cbsrpool
                
            "Not this time please":
                s "Hmm ok"
                pass

    scene cbspa with fade
    c "Oh hey guys"
    c "I'm here"
    scene cbsp1 with dissolve
    c "Come in"
    scene cbsp2a with dissolve
    c "Glad that you guys like this place"
    scene cbsp3 with dissolve
    b "Yeah"
    c "Oh [bname]"
    scene cbsp3a with dissolve
    c "I'm so sorry for you"
    c "I wish I can visit you every day"
    c "To... Take care of you"
    c "But you know your mom"
    scene cbsp2a with dissolve
    c "Who wants a cocktail?"
    s "Oh yeah"
    scene cbsp4a with fade
    c "I've got your drinks"
    c "Where is [bname]?"
    b "Here, coming"
    b "{i}(God! Look at her, beautiful, elegant){/i}"
    scene cbsp5 with dissolve
    b "{i}(Fortunately, she's a skank){/i}"
    b "{i}(But too bad she doesn't act in porno, unlucky me){/i}"
    if bandageremove ==1:
        pass
    else:
        b "I am not allowed to swim"
        pass
    s "This looks smackin"
    c "You bet"
    if bandageremove ==1:
        scene cbsp6a with dissolve
        pass
    else:
        scene cbsp6a with dissolve
        pass
    s "Mmm, nice"
    scene cbsp7 with dissolve
    c "Can [bname] drink?"
    c "Yeah why not? I mean he did his operation long enough"
    s "Ok"
    c "So how's life?"
    c "Are you working"
    s "Yes, and no"
    c "What do you mean?"
    s "Part time job"
    c "Ah nice, in what?"
    s "Modeling"
    b "{i}(Modeling my ass){/i}"
    c "That's great"
    c "You have what it takes"
    c "And a great figure"
    s "Maybe I only need a little breast augmentation"
    c "Wow!"
    scene cbsp8 with dissolve
    c "..."
    scene cbsp7 with dissolve
    c "No don't"
    c "Small boobs are beautiful"
    b "No they aren't"
    b "Do you girls like small cocks"
    b "It's the same"
    scene cbsp9 with dissolve
    s "Shut your face!"
    scene cbsp7 with dissolve
    c "Probably [bname] hasn't seen big boobs"
    c "And how they droop once released"
    s "He hasn't seen anything since he was nursing"
    b "What!?"
    scene cbsp10a with dissolve
    c "Come [sname] let's show him the difference"
    s "I don't do free shows"
    if srel< 120:
        s "Especially for losers"
        c "Oh [sname] be nice, he's recovering"
        s "No, nothing for free"
        scene cbsp17a with fade
        "YOU SPEND SOME TIME"
        $ Hour += 1
        c "I'll miss you till next time"
        s "We will come again"
        "RAISE [sname] points to 120"
        jump broom_menu
    else:
        c "Oh [sname] be nice, he's recovering"
        s "And numb"
        b sur "What the hell"
        b sur "Who told you?"
        b "[sname] how did you know?"
        pass
    scene cbsp11 with dissolve
    c "So what's better?"
    c "Big or small?"
    menu:
        "Cheryl":
            scene cbsp12 with dissolve
            c "Not a very smart answer"
            scene cbsp14a with dissolve
            c "But I like it"
            "She whispers"
            s "..."
            s "[bname] remember you promised [mname] only one hour"
            b "Oh yes, I forgot"
            pass

        "[sname]":
            b "Although I can't see much"
            scene cbsp15 with dissolve
            c "Smart boy"
            s "Ahh"
            c "She's gorgeous"
            scene cbsp16 with dissolve
            s "You're more gorgeous"
            c "Let's get some more drinks"
            scene cbsp14a with dissolve
            c "I know what you want"
            c "That's why I put something in her drinks"
            c "She's going to beg for your cock"
            b "Wow, no one understands me better than you"
            b "We need to try this on [mname]"
            c "All you need is to invite me home, and I'll deal with the rest"
            b "[mname] is a tough nut"
            c "I'll crack her"
            b "Cool"
            c "Let's see the effect on [sname]"
            scene cbsp15 with fade
            c "Let me take care of you [sname]"
            scene cbsp19 with dissolve
            s "Ahhh"
            scene cbsp16 with dissolve
            c "Let's take care of [bname]"
            s "No, we have to go, he promised [mname] to stay only one hour"
            menu:
                "Hey [sname] try your drink, it's awesome":
                    c "You haven't tried your drink"
                    s "Oh yes"
                    scene cbsp22 with fade
                    s "Mmm"
                    scene cbsp23 with dissolve
                    c "Get ready"
                    scene cbsp21 with fade
                    s "Ah careful my drink"
                    scene cbsp24 with dissolve
                    b "..."
                    menu:
                        "Wait and watch them" if bandageremove ==1:
                            scene cbsp32 with fade
                            s "Mmm"
                            scene cbsp33 with dissolve
                            s "What are you doing?"
                            c "I'm going to lick your cute little thing"
                            b "Ohh how romantic"
                            scene lesacbsp with dissolve
                            s "Ahh"
                            scene lesacbsp1 with dissolve
                            s "..."
                            scene lesacbsp2 with dissolve
                            c "Mmm"
                            b "I think that's enough"
                            b "Time for a ride"
                            scene cbsp34 with fade
                            c "Take it easy stallion"
                            scene cbsp35 with dissolve
                            c "Ahhh"
                            scene cbsp36 with dissolve
                            s "Mmm"
                            c "[bname] yes!"
                            scene cbsp37 with dissolve
                            c "Fuck that ass"
                            scene cbsp38 with dissolve
                            b "Ahh yes, take that load"
                            pass
                        "Continue":
                            scene cbsp25 with dissolve
                            s "Ah"
                            c "Get down [sname]"
                            c "Time for pure enjoyement"
                            scene cbsp26 with dissolve
                            s "Mmm"
                            scene cbsp27 with dissolve
                            s "Ahh"
                            scene cbsp28 with dissolve
                            s "Urghh"
                            c "Come here [bname] give me your cock"
                            scene cbsp29 with dissolve
                            c "Mmm"
                            scene cbsp30 with fade
                            c "..."
                            pass
                "Continue":
                    s "Maybe next time"
                    c "{i}(Ah, she didn't touch her drink){/i}"
                    pass
    scene cbsp17a with fade
    $ Hour += 1
    c "I'll miss you till next time"
    if joshuacorrupted >=1:
        c "I tell you what"
        c "I'm having a pool party soon"
        c "It's for a full weekend"
        c "Why don't you join me"
        c "You can sleep here for two days"
        s "Ah you know [mname], she's never going to accept"
        c "Try if she does then it would be cool to have you with us"
        jump broom_menu
    else:
        s "We will come again"
        jump broom_menu





    label cbsrpool:
        scene cbspar with fade
        a "Nice place"
        scene cbsp1 with dissolve
        c "Hey guys, make yourself at home"
        c "I'll be with you in a minute"
        scene cbsp2ar with fade
        s "Aunt Cheryl"
        c "Hey!"
        scene cbsp2ar1 with dissolve
        c "Hi Rowena, nice to meet you"
        s "Can we get your yummy drinks again?"
        scene cbspar1 with dissolve
        c "Right on!"
        s "You're the best"
        c "Try the pool while I get the drinks, the water is amazing"
        scene cbspar2 with fade
        b "Err..."
        c "What is it [bname]?"
        b "I have a request"
        b "Can you put something in their drinks?"
        b "If you have of course"
        scene cbspar3 with dissolve
        $ persistent.unlock_55 = True
        if mcherylrecording ==0:
            c "And what makes you think I will do that for free?!"
            b "Oh god, you're all the same"
            $ mcherylrecording = 1
            c "Hmm"
            b "So what do you want?"
            c "I want you to record me and [mname] doing something naughty"
            scene cbspar4 with dissolve
            b "Seriously?"
            c "Yes"
            scene cbspar3 with dissolve
            c "When I have the video, you'll get what you want"
            b "Ok I'll see if I can do it"
            pass

        elif mcherylrecording ==2:
            c "Do you have the recording?"
            b "Yes, you know I did it"
            c "But you didn't send to me"
            b "Hmm Ok, I'll send you now"
            scene cbspar5 with dissolve
            c "Great, waiting for it"
            scene cbspar6 with fade
            c "I've got your drinks"
            s "Yay!"
            c "[bname] you have to go and get yours"
            scene cbspar7 with fade
            a "Hmm"
            a "Nice"
            scene cbspar8 with fade
            "YOU CHAT WITH CHERYL UNTIL THE LIQUID TAKES EFFECT"
            "AND THEN"
            scene cbspar9 with dissolve
            s "Come on Rowena let's dance"
            scene cbspar10 with dissolve
            c "It's taking effect"
            b "Yes, I see"
            scene cbsrdance with dissolve
            s "..."
            a "come on [sname] we need some music"
            scene cbspar11 with dissolve
            s "Yeah"
            scene cbspar12 with dissolve
            c "Let's join them"
            scene cpdance with dissolve
            c "..."
            c "..."
            c "Come here baby"
            "..."
            c "[bname]"
            scene cbspar13 with dissolve
            a "Oh"
            c "Come girls"
            scene cbspar14 with dissolve
            c "..."
            scene cbspar15 with dissolve
            c "What do you say Rowena?"
            a "Mmm I don't know"
            menu:
                "I will go":
                    a "Yes that's better"  
                    scene cbspar16 with dissolve
                    s "Ah"
                    scene cbspar17 with fade
                    a "..."
                    scene cbspar18 with dissolve
                    c "Mmm"
                    scene cbspar19 with fade
                    c "Ahhh"
                    scene cbspar20 with dissolve
                    a "Ahhh"
                    scene cbspar21 with dissolve
                    a "Mmm"
                    scene cbspar22 with dissolve
                    a "Mmm"
                    scene cbspar19 with dissolve
                    c "Mmm"
                    scene cbspar23 with dissolve
                    c "Ahh"
                    scene cbspar22 with dissolve 
                    b "I'm about to cum"
                    scene cbspar24 with dissolve
                    s "Ahhh"
                    b "Fuck"
                    scene cbspar25 with fade
                    c "Mmm"
                    scene cbspar34 with fade
                    $ cherylpoolparty = 1
                    a "See you next time miss cheryl"
                    s "By the way auntie"
                    s "When are you going to invite me foor your pool parties"
                    c "Ahh Yes, this weekend I'm a bit busy"
                    c "I'm invited to a pool with my friends"
                    s "Ahh too bad"
                    c "But I think a new party most likely in the next version I promise"
                    scene cbspar35 with dissolve
                    c "Oh don't be sad"
                    c "You can join me"
                    c "Remember, come Sunday at 16:00"
                    scene cbspar36 with dissolve
                    c "All of you"
                    scene black
                    "..."
                    scene cbsparend with fade
                    "YOU RETURN HOME"
                    jump broom_menu


                "You go Rowena":
                    a "Do you think so?"
                    s "Yes, just enjoy yourself"
                    s "No judging baby"
                    scene cbspar26 with dissolve
                    c "Come here Rowena"
                    scene cbspar27 with fade
                    "..."
                    a "Ah"
                    scene cbspar29 with dissolve
                    s "Mmm"
                    scene cbspar30 with dissolve
                    a "Ahh"
                    scene cbspar31 with dissolve
                    a "[sname]"
                    a "I'm cumming"
                    scene cbspar32 with dissolve
                    b "I will cum"
                    scene cbspar33 with dissolve
                    b "Ahhh"
                    scene cbspar34 with fade
                    $ cherylpoolparty = 1
                    a "See you next time miss cheryl"
                    s "By the way auntie"
                    s "When are you going to invite me foor your pool parties"
                    c "Ahh Yes, this weekend I'm a bit busy"
                    c "I'm invited to a pool with my friends"
                    s "Ahh too bad"
                    c "But I think a new party most likely in the next version I promise"
                    scene cbspar35 with dissolve
                    c "Oh don't be sad"
                    c "You can join me"
                    c "Remember, come Sunday at 16:00"
                    scene cbspar36 with dissolve
                    c "All of you"
                    scene black
                    "..."
                    scene cbsparend with fade
                    "YOU RETURN HOME"
                    jump broom_menu

                "Let's go both":
                    scene cbspar37 with fade
                    c "Come [bname]"
                    s "We don't need him"
                    scene cbspar38 with dissolve
                    c "Yes we don't"
                    scene cbspar39 with dissolve
                    a "Haha look at him"
                    b "{i}(Hmmm){/i}"
                    scene cbspar40 with dissolve
                    s "Ahh"
                    scene cbspar41 with dissolve
                    b "Hmmm"
                    scene cbspar42 with dissolve
                    a "Ahhhhhhh"
                    scene cbspar43 with dissolve
                    b "..."
                    scene cbspar44 with dissolve
                    a "Ahhh"
                    scene cbspar45 with dissolve
                    s "That little bitch is so happy"
                    scene cbspar46 with dissolve
                    b "Ahh shit!"
                    b "Get up! Quick!"
                    scene cbspar47 with dissolve
                    b "Mmmm"
                    scene cbspar34 with fade
                    $ cherylpoolparty = 1
                    a "See you next time miss cheryl"
                    s "By the way auntie"
                    s "When are you going to invite me foor your pool parties"
                    c "Ahh Yes, this weekend I'm a bit busy"
                    c "I'm invited to a pool with my friends"
                    s "Ahh too bad"
                    c "But I think a new party most likely in the next version I promise"
                    scene cbspar35 with dissolve
                    c "Oh don't be sad"
                    c "You can join me"
                    c "Remember, come Sunday at 16:00"
                    scene cbspar36 with dissolve
                    c "All of you"
                    scene black
                    "..."
                    scene cbsparend with fade
                    "YOU RETURN HOME"
                    jump broom_menu
        else:
            c "Do you have the recording?"
            b "No"
            c "Then, nothing in the drinks"
            pass

        scene cbspar6 with fade
        c "I've got your drinks"
        s "Yay!"
        c "[bname] you have to go and get yours"
        scene cbspar7 with fade
        a "Hmm"
        a "Nice"
        scene cbspar8 with fade
        "YOU CHAT FOR A WHILE"
        scene cbsparend with fade
        "AND YOU RETURN HOME"
        jump broom_menu

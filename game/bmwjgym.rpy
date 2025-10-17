

label bmwjgym:
    scene gwj with fade
    $ gymwithwanda = 1
    m "That's it"
    b "{i}(I wonder how did Wanda wear such an outfit){/i}"
    b "{i}(Maybe [mname] convinced her){/i}"
    w "Yes, you were right, it's empty"
    m "It is, at this time of the day"
    m "Shall we?"
    scene gwj1 with fade
    j "This is boring"
    b "I know how to make it exciting for you"
    j "You do?"
    b "Watch and learn"
    scene gwj2 with dissolve
    if persistent.patch_enabled:
        b "Mom! Are you done?"
        pass
    else:
        b "Are you done?"
        pass
    m "Almost, why?"
    b "Let me help you with that"
    m "Go help Joshua"
    b "He's bored, he doesn't want"
    m "Ok"
    b "Come on the mat"
    scene gwj3 with fade
    b "Yes that's it, one more"
    scene gwj4 with fade
    b "Hold it like that"
    b "Lift your glutes"
    scene gwj5 with dissolve
    j "..."
    scene gwj6 with dissolve
    w "I'm done"
    w "What's going on?"
    scene gwj7 with dissolve
    b "I'm controlling her moves for best effect"
    b "I can do it for you as well"
    if wsusp <5:
        $ persistent.unlock_36 = True
        w "Yes that would be nice"
        scene gwj11 with dissolve
        b "..."
        scene gwj12 with dissolve
        j "..."
        scene gwj13 with dissolve
        b "{i}(Oh sweet!){/i}"
        w "I think we're done [bname]"
        m "Time for a shower"
        scene gwj10 with dissolve
        w "Let's go"
        scene gwj14 with fade
        b "Hey! Do you want to have some fun?"
        j "What kind of fun?"
        b "We go sneak in their shower"
        j "Oh God, we will get caught"
        j "And it's going to be bad"
        b "Don't worry I have my way, they won't even know"
        j "Pff I don't know"
        scene gwj15 with fade
        w "I'm glad there is no one around"
        m "It's completely empty during the day"
        j "I'm scared man"
        b "Shh"
        scene gwj16 with dissolve
        w "And thank you for helping with Joshua"
        scene gwj17 with dissolve
        w "At least he spent half an hour in the gym"
        scene gwj18 with dissolve
        m "We should do this often"
        scene gwj19 with dissolve
        m "Let's get into the showers"
        w "Yes"
        b "Wow"
        "[bname] whispers"
        b "Come here watch"
        j "I can't, it's too scary"
        b "I'll click a photo for you"
        scene gwj20 with dissolve
        b "Cool"
        scene gwj21 with dissolve
        j "Let's go please"
        b "No, wait"
        b "Just get behind the door"
        scene gwj24 with dissolve
        b "..."
        scene gwjanim with dissolve
        "..."
        b "See I told you"
        "..."
        scene gwjcup000 with dissolve
        b "Huh"
        scene gwjcup015 with dissolve
        b "Oh my"
        scene gwjcup030 with dissolve
        j "Gulp"
        scene gwjcup045 with dissolve
        b "We were going to miss this"
        scene gwjkiss000 with dissolve
        b "Oh my god"
        scene gwjkiss006 with dissolve
        w "..."
        scene gwjkiss018 with dissolve
        w "..."
        scene gwjkiss030 with dissolve
        m "Mmm"
        scene gwjkiss042 with dissolve
        j "Ahhh I..."
        scene gwjkiss054 with dissolve
        j "I can't anymore"
        if mcorr >= 30:
            scene gwjkiss055a with dissolve
            w "[mname] it's risky"
            b "Let's go"
            pass
        else:
            b "[mname] stopped"
            b "Let's go"
            pass
        scene gwj22 with fade
        j "Oh"
        b "Who's ass is better?"
        $ jcorr += 1
        show screen jcorr
        j "Hehehe"
        hide screen jcorr
        pass


        pass
    else:
        w "I'll help Joshua thanks"
        "YOU HAVE HIGH SUSPICIONS"
        scene gwj8 with dissolve
        b "{i}(I need to take a quick look){/i}"
        scene gwj9 with dissolve
        b "{i}(Sweet ass){/i}"
        m "I think we're done [bname]"
        m "That's enough"
        m "Time for shower"
        scene gwj10 with dissolve
        w "Let's go"
        w "[bname] help Josh a little more please"
        b "Sure"
        scene gwj14 with fade
        b "Hey! Do you want to have some fun?"
        j "What kind of fun?"
        b "We go sneak in their shower"
        j "Oh God, we will get caught"
        j "And it's going to be bad"
        b "Don't worry I have my way, they won't even know"
        j "No no, I don't want to risk it"
        pass


    scene gwj23 with dissolve
    m "Ready to go guys?"
    b "Yes"
    w "Did you shower? Joshua?"
    j "Err"
    b "Yes we did"
    w "Let's go then"
    jump broom_menu 
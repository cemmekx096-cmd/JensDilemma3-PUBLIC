

label melcherpool:
    $ Hour += 1
    b "Hello"
    scene melcall4 with fade
    b "Oh you're here"
    c "Just a handshake?"
    c "Get your ass over here and hug me"
    scene melcall5 with dissolve
    c "Mmm"
    c "Don't be shy, we went through a lot together"
    scene melcall6 with dissolve
    ml "Hi [bname]"
    b "Hi Ms Melinda"
    c "How have you been?"
    b "Better than before"
    scene melcall7 with dissolve
    c "And what about your wound?"
    b "Almost healed"
    c "That's good to know"
    c "You know [bname]"
    c "There's something I've been wanting to tell you"
    b "What is it?"
    scene melcall8 with dissolve
    c "I honestly think you shouldn't stay in such environment"
    b "What do you mean?"
    c "I don't think it's healthy for you and [sname] to stay with [mname]"
    scene melcall9 with dissolve
    b sur "Huh!"
    c "I mean... Well just saying"
    c "If you feel... You are both welcome to stay with me"
    c "It's your decision"
    c "Your call, I'm just saying, you have a place if one day things get difficult"
    scene melcall10 with dissolve
    b "I'll keep that in mind"
    b "{i}(Damn bitch, stop talking and let me focus on Melinda's ass){/i}"
    c "Do you want to swim?"
    b "Nah"
    c "I'll join Melinda then"
    b "Ok"
    scene melcall11 with fade
    b "{i}(Oh god, fucking hot){/i}"
    scene melcall12 with fade
    b "{i}(Oh wow){/i}"
    scene melcall13 with fade
    c "Melinda? Do you have Prosecco?"
    ml "Of course"
    scene melcall14 with dissolve
    c "[bname] get it with flute glasses"
    b "Where is it?"
    ml "In the pantry, ask Anna she's there"
    b "Anna!?"
    ml "The maid"
    scene melcall15 with fade
    b "I've got it"
    c "Coming"
    scene melcall16 with dissolve
    ml "Cheers"
    if escortrequest >= 1:
        ml "So [bname]"
        $ persistent.unlock_31 = True
        ml "Any success with [mname]?"
        b "About the request?"
        ml "Yes, the travel companion"
        if escortrequest == 2:
            b "I tried, but she snapped"
            pass
        else:
            b "No, nothing yet"
            pass
        b "I'll have to try more"
        ml "Hmm"
        ml "Maybe you need some incentive"
        scene melcall17 with dissolve
        ml "Right Cheryl?"
        scene melcall18 with fade
        c "Indeed"
        scene melcall19 with dissolve
        b "Yeah I need this"
        scene melcall20 with dissolve
        b "Ahh"
        scene melcall21 with dissolve
        b "{i}(That bitch is sucking it deep){/i}"
        scene melcall22 with dissolve
        b "..."
        scene melcall23 with dissolve
        b "..."
        scene melcall24 with dissolve
        c "Mmmm"
        scene melcall25 with fade
        b "..."
        menu:
            "Fuck Cheryl":
                scene melcall26 with dissolve
                c "Ahhh"
                scene melcall27 with dissolve
                b "Mmmm"
                scene melcall28 with dissolve
                c "Oahhh"
                scene melcall29 with dissolve
                b "{i}(Fuck I'm suffocating){/i}"
                pass

            "Tit-fuck Melinda":
                scene melcall31 with fade
                b "..."
                scene melcall30 with dissolve
                b "Ahhh"
                scene melcall32 with hpunch
                c "Mmm"
                pass
        scene melcall33 with fade
        b "Bye!"
        ml "Stay in touch"
        c "Bye sweetheart, I'll miss you"
        if siteunlocked ==0:
            b "Ermm, by the way"
            b "I wanted to ask you..."
            b "How can I apply for a credit card?"
            c "What do you need it for honey?"
            b "I want to buy some online stuff"
            scene melcall34 with dissolve
            c "Really? I thought you are already buying online products"
            ml "Yeah true"
            scene melcall35 with dissolve
            if escortrequest == 2:
                ml "You even bought that bikini for her"
                pass
            else:
                pass
            b "Well to be honest, I want it for some..."
            b "Some naughty site"
            ml "I know which one"
            ml "don't worry, I'll let Jonas send you a user and pass"
            b sur "Wow, you really understand me"
            ml "You go now"
            c "Bye sweetie"
            $ siteunlocked = 1
            call screen gnav
        else:
            call screen gnav
    else:
        "YOU SPEND SOME TIME AND GO BACK HOME"
        "IF MELINDA DISCUSSED THE ESCORT REQUEST FOR [mname] YOU'LL GET DIFFERENT OPTION HERE"
        call screen gnav


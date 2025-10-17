
define mar = Character("Martin")

label bmdnr:
    scene bmdinner with fade
    m "..."
    scene bmdinner1 with dissolve
    b "We have a reservation in the name of [bname]"
    "Yes please follow me"
    scene bmdinner2 with dissolve
    m "{i}(How sweet and innocent he is){/i}"
    m "{i}(Trying to act like a grown up){/i}"
    scene bmdinner3 with dissolve
    m "You know about the wine this time, right?"
    b "Of course"
    scene bmdinner4 with dissolve
    b "You look so beautiful"
    scene bmdinner5 with dissolve
    m "Thank you"
    m "Let's order food"
    b "Mhm I'll go use the toilet first"
    scene bmdinner6 with dissolve
    b "Hmmm"
    b "{i}(That must be the suitor){/i}"
    b "Good evening"
    scene bmdinner7 with dissolve
    "Good evening"
    m "{i}(What does this one wants now){/i}"
    "My name is Martin"
    m "Good evening Martin"
    scene bmdinner8 with dissolve
    mar "May I sit?"
    m "You already did"
    mar "Sorry for intruding"
    mar "I couldn't help but come and talk to you"
    mar "Seeing how elegant and beautiful you are"
    m "Thank you"
    mar "May I ..."
    mar "May I invite you for a dinner sometime this week?"
    m "Why is it always when I'm having dinner with my ..."
    m "With my date, that someone comes and asks me out"
    mar "Because you are extremely gorgeous"
    mar "Trust me my motives are purely good"
    m "Uhuh"
    scene bmdinner9 with dissolve
    mar "May I have your phone number?"
    mar "No pressure though"
    mar "You don't have to answer my call if you don't like"
    m "Ok"
    m "Here it is, and please leave now before my date returns"
    scene bmdinner10 with fade
    b "{i}(I hope it's done){/i}"
    scene bmdinner11 with dissolve
    b "I see you ordered food"
    m "Yes I didn't want to waste time"
    scene bmdinner12 with dissolve
    m "And I know what's best for you"
    m "In case you don't remember I'm still ..."
    b "Ok Ok we know that"
    scene bmdinner13 with fade
    m "[bname] you didn't settle the bill!"
    b "{i}(Fuck what do I tell her){/i}"
    b "I did, earlier, you didn't see me"
    scene bmdinner14 with fade
    m "Ahh my feet"
    b "Do you need a massage"
    m "No honey, I'll go wash my hair and sleep"
    b "No, keep your hair later"
    scene bmdinner15 with dissolve
    b "Here I'll make you feel better"
    scene bmdinner16 with dissolve
    m "That's good honey"
    m "Come here, let me thank you for the bag"
    scene bmdinner17 with dissolve
    m "..."
    scene bmdinner18 with dissolve
    m "..."
    scene bmdan with fade
    "..."
    m "Mmm"
    "..."
    m "Mhhm"
    $ persistent.unlock_82 = True
    scene bmang with fade
    m "..."
    "..."
    m "..."
    "..."
    menu:
        "Get on your knees":
            scene bmdinner19 with dissolve
            "..."
            scene bmdinner20 with dissolve
            b "Ahh"
            scene bmdinner21 with dissolve
            b "I love those lashes"
            scene bmdinner22 with dissolve
            b "Ohh"
            scene bmdinner23 with dissolve
            m "Mmm"
            pass
        
        "Continue":
            scene bmdinner24 with dissolve
            b "Uh"
            scene bmdinner25 with dissolve
            b "..."
            pass

    scene bmdinner_last with fade
    m "Good night baby"
    m "Go to sleep please"
    m "Also put my dress in the laundry room please"
    jump newday


    
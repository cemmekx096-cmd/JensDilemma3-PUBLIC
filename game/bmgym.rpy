


label bmgym:
    scene mgym with fade
    m "..."
    scene mgym1 with dissolve
    m "Take it easy there [bname]"
    m "Don't lift hard"
    b "Ok"
    scene mgym2 with fade
    b "I guess I'll just coach you"
    m "Yeah right"
    scene mgym3 with dissolve
    m "Fff"
    scene mgym2 with dissolve
    m "..."
    scene mgym3 with dissolve
    b "That should be enough"
    b "Let's get to the leg press"
    scene mgym4 with fade
    m "..."
    scene mgym5 with dissolve
    m "Mhmm"
    b "One more"
    scene mgym6 with dissolve
    b "Great"
    scene mgym7 with fade
    m "Let's get to the shower"
    menu:
        "Ask if Joshua can join you in the gym" if wandagym == 1 and persistent.unlock_24 == True:
            b "Can we get Joshua to train with us"
            $ wandagym = 2
            m "Why?"
            b "No specific reason, probably I want to feel better about myself"
            b "And to add some more incentive"
            scene mgym7a with dissolve
            m "It's good to be honest [bname]"
            m "I appreciate it"
            b "You will need to talk to Wanda right?"
            m "Yes, I will see what I can do"
            $ renpy.notify (_("[mname] will talk to Wanda"))
            b "Cool"
            pass
        "Show her your progress":
            pass
    b "Let me show you my progress"
    scene mgym8a with dissolve
    b "What do you think?"
    scene mgym9 with dissolve
    m "..."
    scene mgym10 with dissolve
    m "Nice"
    m "I'm going to shower"
    scene mgym12a with fade
    m "..."
    m "[bname] what are you doing here?"
    m "You can't be in the ladies shower"
    scene mgym13a with dissolve
    b "Why not?"
    m "[bname] not here"
    scene mgym14a with dissolve
    b "Why not?"
    scene mgym15a with dissolve
    b "That's the thrill of doing it in public"
    m "I said no [bname]"
    b "Alright"
    scene black
    "YOU SHOWER AND GET BACK HOME"
    "AND THAT'S ALL HERE FOR THIS VERSION"
    jump broom_menu 



label snamehallsunday:
    $ Hour += 1
    scene shall_night with fade
    b "Hmm"
    b "Wha are you doing?"
    s "Nothing!"
    b "You sure?"
    s "Yes"
    b "Come let's watch tv"
    scene shall_night3 with fade
    s "Are you sure you are allowed to drink?"
    b "Mhm"
    s "She's gonna come and yell at you"
    scene shall_night4 with dissolve
    b "Always scrolling, what the hell are you looking for?"
    scene shall_night4a with dissolve
    s "Why are you bothered?!"
    s "Carry on looking and oggling my breasts"
    s "By the way, I can't help but ask you"
    s "Can you still get a boner after the operation?"
    b  ang "..."
    scene shall_night5a with dissolve
    m "[bname] what are you doing?"
    s "Oops"
    m "I told you not to drink"
    b "Sorry"
    scene shall_night6a with dissolve
    m "Mhhm"
    b "You bet I can get a boner"
    "HE WHISPERS"
    scene shall_night4a with dissolve
    if persistent.patch_enabled:
        s "Let's see if you can, I'll give you a blowjob while mom is here"
        pass
    else:
        s "Let's see if you can, I'll give you a blowjob while she's here"
        pass
    scene shall_night7a with dissolve
    m "[sname] can you help me?"
    m "[sname]!!"
    scene shall_night8a with dissolve
    b "Ahh"
    b "She's busy!"
    m "Busy with what?"
    scene shall_night10a with dissolve
    b "Her phone, as..."
    m "As what?"
    scene shall_night11a with dissolve
    b "Ugh as usual"
    b "She has her headphones on"
    scene shall_night12a with dissolve
    m "Nevermind, you can both come, dinner is ready"
    scene shall_night9a with fade
    m "Eat"
    m "The meatballs are good for you"
    s "Yeah!"
    if janeyseduction == 3:
        "WHEN YOU'RE ABOUT TO FINISH YOUR MEAL"
        play sound "sounds/doorbell.wav"
        m "[bname] see who's at the door"
        m "[sname] clear the table"
        scene shall_night13a with dissolve
        $ persistent.unlock_57 = True
        b "Hey Joshua"
        w "Good evening"
        scene shall_night14a with dissolve
        m "Oh Hi Wanda"
        m "Please sit, I'll be right back"
        scene shall_night15 with dissolve
        m "Will change real quick"
        w "Take your time"
        w "How are you [bname]"
        b "All good"
        scene shall_night16 with dissolve
        "..."
        scene shall_night17 with dissolve
        "..."
        scene shall_night18 with fade
        b "Let's go Joshua"
        j "Mom can we go?"
        scene shall_night19 with dissolve
        w "Of course dear"
        scene shall_night20 with fade
        w "Better like that"
        scene shall_night21 with fade
        "AFTER PLAYING FOR A WHILE"
        if repeatjphotos ==0:
            $ repeatjphotos = 1
            b "Alright that's all, let's get back"
            b "{i}(NEXT time I'll kill him if he doesn't get me something){/i}"
            scene shall_night22 with fade
            m "Hey guys"
            w "Right on time, we should leave"
            scene shall_night23 with fade
            m "You saw how many different jewelry she got"
            b "Yeah"
            m "Good night"
            b "Good night"
            jump newday
        else:
            scene shall_night24 with dissolve
            j "Oh my God"
            b "Did you get me something?"
            j "What do you mean?"
            scene shall_night25 with dissolve
            if joshjaneyphotos ==0:
                b "I mean I always show you photos"
                b "And you never get me something in return"
                b "Looks like you're taking advantage of me"
                j "But it's not easy for me"
                b "What's not easy? Getting some photos in the toilet?"
                b "Or from the bedroom window?"
                j "Ok Ok don't be angry"
                j "I will try"
                $ joshjaneyphotos = 1
                b "Alright, let's get back"
                scene shall_night22 with fade
                m "Hey guys"
                w "Right on time, we should leave"
                scene shall_night23 with fade
                m "You saw how many different jewelry she got"
                b "Yeah"
                m "Good night"
                b "Good night"
                jump newday

            elif joshjaneyphotos ==1:
                b "I mean I always show you photos"
                b "And you never get me something in return"
                b "Looks like you're taking advantage of me"
                j "It's not easy for me"
                b "What's not easy? Getting some photos in the toilet?"
                b "Or from the bedroom window?"
                j "Ok Ok don't be angry"
                j "I am trying"
                $ joshjaneyphotos = 1
                b "Alright, let's get back"
                scene shall_night22 with fade
                m "Hey guys"
                w "Right on time, we should leave"
                scene shall_night23 with fade
                m "You saw how many different jewelry she got"
                b "Yeah"
                m "Good night"
                b "Good night"
                jump newday
                

            elif joshjaneyphotos ==2:
                b "I mean I always show you photos"
                b "And you never get me something in return"
                b "Looks like you're taking advantage of me"
                scene shall_night26 with dissolve
                j "I've got something"
                j "On my phone"
                j "Make it silent"
                b "Ok"
                scene jstja with dissolve
                b "Huh"
                b "Oh my god"
                scene jstjb000 with dissolve
                b "..."
                scene jstjb010 with dissolve
                b "Nice"
                scene jstjb020 with dissolve
                b "Mmm"
                b "Wow, that was something"
                b "Have you tried something with her?"
                j "No"
                b "Come on!"
                scene shall_night27 with dissolve
                j "No"
                j "I can't, she's..."
                b "She's what?"
                j "She has a condition"
                b "What condition?"
                j "I don't know if I can tell you"
                b "She's a retard? Mental?"
                j "No, she's..."
                b "Come on tell me"
                j "She's something like autistic"
                j "Bipolar or something like that"
                j "I'm not sure what, mom doesn't say exactly"
                b "Ah I see"
                b "That makes sense"
                b "I guess I owe you something more now"
                j "Like what?"
                b "Maybe you can visit me during the days?"
                j "No, mom won't accept"
                b "I'll see what I can do about that"
                b "Let's get back to them"
                scene shall_night22 with fade
                m "Hey guys"
                w "Right on time, we should leave"
                scene shall_night23 with fade
                m "You saw how many different jewelry she got"
                b "Yeah"
                b "Why don't you buy, you have money now"
                m "You don't get it [bname] a women never buys jewelry for herself"
                m "It has to be gifted"
                b "Ah like that?"
                m "Good night"
                b "Good night"
                jump newday

            elif joshjaneyphotos ==3 and buyjewelry ==0:   
                b "So do you have anything?"
                j "The same on my phone"
                b "Let me see"
                scene shall_night26 with dissolve
                j "Make it silent"
                b "Ok"
                scene jstja with dissolve
                b "Nice"
                scene jstjb020 with dissolve
                b "..."
                scene jstjb030 with dissolve
                b "Nice"
                scene jstjb040 with dissolve
                b "Mmm"
                b "I can never be bored with this"
                b "..."
                b "Let's get back to them"
                scene shall_night22 with fade
                m "Hey guys"
                w "Right on time, we should leave"
                scene shall_night23 with fade
                m "You saw how many different jewelry she got"
                b "Yeah"
                b "Why don't you buy, you have money now"
                m "You don't get it [bname] a women never buys jewelry for herself"
                m "It has to be gifted"
                $ buyjewelry = 1
                b "Ah like that?"
                m "Good night"
                b "Good night"
                jump newday

            elif buyjewelry ==3: 
                b "So do you have anything?"
                j "Yes I have something new"
                b "Let me see"
                scene shall_night26 with dissolve
                j "Put it on silent"
                b "Ok"
                scene jstj with fade
                b "Oh my fucking god"
                scene jstj1 with dissolve
                b "Woah!"
                scene jstj2 with dissolve
                b "..."
                scene jstj3 with dissolve
                b "..."
                b "Mmm"
                scene jstj4 with dissolve
                b "I can never be bored with this"
                b "..."
                scene shall_night26 with dissolve
                b "I have something to show you"
                scene mlh21 with dissolve
                j "Oh"
                scene mlh22 with dissolve
                j "..."
                scene mlh23 with dissolve
                b "Maybe you should try to take the same with Wanda"
                scene shall_night27 with dissolve
                j "Oh wow, no that's very dangerous"
                b "I don't know, I'm just saying try"
                b "Let's get back to them"
                scene shall_night22a with fade
                m "Hey guys"
                m "Right on time, we were coming to you"
                m "We decided to go out for a couple hours"
                w "Joshua behave, we won't be late"
                w "Just one drink in the local"
                scene shall_night24b with dissolve
                b "I'll be back"
                j "Where are you going?"
                b "I'll be back, relax we will have some fun time"
                b "I'm going to let you explore your sexuality"
                scene shall_night25b with dissolve
                j "Huh!"
                b "Just chill man"
                scene shall_night26a with dissolve
                b "Hey there"
                s "Yes [bname]"
                b "Care to give us a show?"
                s "Who?"
                b "Me and Joshua"
                b "We will come and watch you, just pretend you don't know"
                s "I'll put my mask on and remove it as soon as you hide"
                b "You're the best"
                s "Nothing is free"
                b "Hehe ok"
                scene shall_night24b with fade
                b "Come with me quick, she's in the toilet"
                j "Who!"
                b "Just come"
                scene jbst22a with fade
                b "Shh..."
                scene shall_night27a with dissolve
                b "Let's shut the door"
                scene jbst23a with dissolve
                s "Anyone here?"
                b "..."
                scene shall_night28 with dissolve
                s "Hmmm"
                s "I wish Joshua is here"
                scene shall_night29 with dissolve
                j "Huh"
                b "See man, she desires you"
                b "{i}(Time to push him out){/i}"
                scene shall_night30 with hpunch
                j "Ahh"
                s "Oh Joshua"
                scene shall_night31 with dissolve
                s "What are you doing here?"
                s "What are you hiding over there?"
                s "Oh I know"
                scene shall_night32 with dissolve
                j "Uhhh"
                s "Chillax"
                $ persistent.unlock_62 = True
                scene shall_night33 with dissolve
                s "OMG so big"
                j "Errm I need to go"
                scene shall_night34 with dissolve
                s "No you're not"
                s "I want you so bad"
                scene sjanim with dissolve
                s "Mmm"
                "..."
                j "Ah"
                j "Oh my god"
                s "..."
                scene shall_night35 with dissolve
                "..."
                scene shall_night36 with fade
                s "I'll let you wash up"
                scene shall_night37 with fade
                m "Here they are"
                w "Let's go Josh, right on time"
                scene shall_night23a with fade
                m "Why is he all flushed"
                b "No idea"
                m "Good night"
                b "Good night"
                "THAT WAS ALL HERE"
                jump newday

    else:
        "THEY EAT IN SILENCE"
        call screen gnav

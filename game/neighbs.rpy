

label neighbs:
    scene bna_call with fade
    b "What's up?"
    n "Good"
    b "Would you like to join me for dinner?"
    b "I'm alone, and there's no one to eat with"
    if day ==4:
        nd "Oh [bname] sorry, I'm a little busy tonight"
        scene cnd with dissolve
        nd "My cousin is staying over"
        nd "And we're planning to watch a movie"
        b "Oh crap"
        nd "Hey you know what?"
        nd "Mom can send you some food"
        b "Yes sounds a good idea"
        nd "Cool, I'll tell her"
        nd "Kiss you!"
        b "Kisses to you too"
        jump katybs

    elif day==5:
        nd "Oh [bname] sorry, I'm a little busy tonight"
        scene cnd with dissolve
        nd "My cousin is staying over"
        nd "And we're planning to watch a movie"
        b "Oh crap"
        nd "Hey you know what?"
        nd "Mom can send you some food"
        b "Yes sounds a good idea"
        nd "Cool, I'll tell her"
        nd "Kiss you!"
        b "Kisses to you too"
        jump katybs

    else:
        nd "Why don't you come then, the dinner is ready"
        b "Well I can't leave the house"
        nd "Ok we will bring our food and come"
        b ang "{i}(We! What does she mean!?){/i}" 
        b "Ok"
        pass

    scene bna9 with fade
    b "Please come on"
    n "Let's eat before it's cold"
    scene bna10 with fade
    b "Thank you for the dinner"
    n "Glad you enjoyed it"
    n "So what's new? How's your injury"
    b "Well still, there are few things I can't do"
    b "I can't shower, I can't umm..."
    scene bna10b with dissolve
    n "Yeah I understand"
    n "Well we'd better go"
    n "Let me know if you need anything"
    b "You can keep me company"
    n "When is [mname] returning?"
    b "Around midnight"
    n "What does she work exactly?"
    b "Ermm restaurant"
    if day ==1:
        scene bna10 with dissolve
        n "We can't stay tonight, my husband is home"
        n "And we need to return"
        b "Ah damn"
        b "Alright, see you another time"
        nd "Bye [bname] see you tomorrow"
        jump waitform

    elif day ==2:
        n "Well, I really need to go, but Masha can stay"
        n "See you another day"
        n "I'll leave you two to watch some tv"
        n "Masha has to return by 11"
        b "Sure"
        scene cnd3 with fade
        b "I missed you"
        nd "Shush she's still at the door"
        scene cnd25 with dissolve
        b "No, she left"
        nd "[bname] what are we?"
        b "You're my girlfriend Masha"
        nd "Are you sure?"
        scene cnd25b with dissolve
        nd "..."
        scene cnd26a with hpunch
        nd "..."
        scene cnd27a with dissolve
        nd "Mmmm"
        scene cnd28a with dissolve
        b "Yeah"
        b "Come up baby"
        menu:
            "Doggy":
                scene cnd29a with dissolve
                nd "Fuck me baby"
                scene cnd30a with dissolve
                nd "Oh"
                scene cnd30aa with dissolve
                nd "Ahhh"
                scene mascnd with dissolve
                nd "Mmmm"
                scene mascnd1 with dissolve
                nd "Ahhhhh"
                b "I'm done"
                scene cnd31a with dissolve
                nd "I love you [bname]"
                scene cnd26 with fade
                nd "..."
                scene bna11a with fade
                "TRY OTHER DAYS"
                b "{i}(Time to sleep){/i}"
                jump newday
                
            "Cowgirl":
                scene cndcg with fade
                nd "Slowly baby"
                scene cndcg1 with dissolve
                nd "Mmhmm"
                scene cndcg2 with dissolve
                nd "Ahh"
                scene cndcg1 with dissolve
                nd "Ah"
                scene cndcg2 with dissolve
                nd "Yes baby"
                b "You're so tight"
                scene cndcg3 with dissolve
                b "Ahhh"
                scene cndcg4 with dissolve
                nd "So hot baby"
                b "Yes"
                b "It was"
                nd "I mean your cum"
                scene cndcg5 with fade
                nd "I'll wash and leave"
                b "Love you babe"
                scene bna11a with fade
                "TRY OTHER DAYS"
                b "{i}(Boring night, it's time to sleep){/i}"
                jump newday


    elif day ==3:
        n "Well, I really need to go, but Masha can stay"
        n "See you another day"
        n "I'll leave you two to watch some tv"
        n "Masha has to return by 11"
        b "Sure"
        scene cnd3 with fade
        b "I missed you"
        nd "Shush she's still at the door"
        scene cnd25 with dissolve
        b "No, she left"
        nd "[bname] what are we?"
        b "You're my girlfriend Masha"
        nd "Are you sure?"
        scene cnd25b with dissolve
        nd "..."
        scene cnd26a with hpunch
        nd "Mmm"
        scene cnd26c with dissolve
        "..."
        scene cnd26b with dissolve
        m "{i}(Finally he has a girlfriend){/i}"
        m "{i}(I should leave them alone){/i}"
        m "{i}(I'll just lock the door){/i}"
        scene cnd27a with dissolve
        nd "Mmmm"
        scene halln_m_in11 with fade
        if bandageremove ==1:
            jump jmasha
        else:
            pass
        m "{i}(I hope he doesn't do something stupid and open his wound){/i}"
        m "{i}(I should check on them){/i}"
        m "{i}(Come on [mname] just a quick peek I promise){/i}"
        scene cnd27a with dissolve
        "..."
        scene cnd29b with dissolve
        m "{i}(Oh good, seems something light){/i}"
        m "{i}(Nothing dangerous for his wounds){/i}"
        m "{i}(Time to return to my room){/i}"
        if mcorr >=35:
            scene mascnd2m with dissolve
            m "{i}(Wow she's good at sucking){/i}"
            m "{i}(If she can take my baby's big cock){/i}"
            m "{i}(God what am I doing?){/i}"
            m "{i}(Oh they're coming close){/i}"
            scene mascnd3m with dissolve
            nd "Baby it's painful"
            scene mascnd4m with dissolve
            m "Ahh"
            scene mascnd5m with dissolve
            b "Ok baby let's get back there"
            m "Hmm"
            m "{i}(Boring teenager sex){/i}"
            scene cnd27c with dissolve
            m "{i}(Time to interrupt this bore){/i}"
            pass
        else:
            "RAISE HER CORRUPTION POINTS TO 35"
            scene cnd27c with dissolve
            m "{i}(Or maybe I'll get a glass of water){/i}"
            pass
        scene cnd27b with dissolve
        nd "Oh God miss [mname], I'm..."
        scene cnd27d with dissolve
        nd "I'm so sorry"
        m "Oh why are you leaving, the night is still early?"
        b "Masha, your shirt"
        if mrel >=120:
            scene cnd30b with fade
            m "I'm sorry dear, I just wanted to drink water"
            b "Say sorry to him"
            scene cnd31b with dissolve
            b "..."
            scene cnd32b with dissolve
            b "What do you want now?"
            m "I'll make up for my mistake"
            m "Come here"
            scene cnd33b with dissolve
            b "Huh"
            m "Try to finish while kissing me"
            scene mmp1 with dissolve
            play sound "sounds/mpleasure.mp3"
            b "Mmm"
            scene mmp2 with dissolve
            b "Mmm"
            stop sound
            scene cnd35b with dissolve
            b "Mmm"
            menu:
                "Cum":
                    scene cnd34b with dissolve
                    "THERE IS ANOTHER OPTION HERE IF YOU HAVE 140 POINTS"
                    b "Ahhh"
                    scene cnd36b with dissolve
                    m "Good night dear"
                    scene bna11a with fade
                    b "{i}(That was good){/i}"
                    b "{i}(Time to sleep){/i}"
                    jump newday

                "Make her pay for cockblocking you" if mrel >=140:
                    $ mcorr += 5
                    b "This is not working"
                    show screen mcorr
                    scene cnd37b with dissolve
                    m "Huh, [bname] what?"
                    b "You're going to make up for cock blocking me"
                    hide screen mcorr
                    scene cnd38b with dissolve
                    b "I said come"
                    m "Ok honey easy on your wound"
                    scene cnd39b with dissolve
                    m "What?"
                    m "What do you want me to do?"
                    menu:
                        "I want you to beg me":
                            scene cnd40b with dissolve
                            m "Do whatever you want but don't kill me"
                            b "Shut up and"
                            scene cnd41b with dissolve
                            b "Suck it"
                            b "Fuck, I'm about to"
                            scene cnd42b with dissolve
                            m "Gulp"
                            scene cnd42bb with hpunch
                            play sound "sounds/mgag.mp3"
                            m "Hurghh!"
                            stop sound
                            scene cnd43b with fade
                            b "Thank you, and I'm sorry"
                            m "Don't worry dear"
                            m "Go to sleep, you need some rest"
                            jump newday

                        "Manhandle her":
                            scene bmhm with dissolve
                            m "Mmm [bname]"
                            m "Don't be angry"
                            scene bmhm1 with dissolve
                            m "Ahh"
                            scene bmhm2 with dissolve
                            m "..."
                            scene bmhm3 with dissolve
                            m "Ahhh"
                            b "Get down!"
                            scene bmhm4 with dissolve
                            m "MmmM"
                            scene bmhm5 with dissolve
                            b "Ahhh"
                            b "Show me that you're going to swallow"
                            scene bmhm6 with dissolve
                            b "Good girl"
                            b "Good night"
                            jump newday

        else:
            scene bna11a with fade
            b "{i}(Fucking brilliant){/i}"
            b "{i}(Time to sleep){/i}"
            "YOU NEED 120 POINTS WITH [mname]"
            jump newday


    else:
        scene bna10 with dissolve
        n "We can't stay tonight, my husband is home"
        n "And we need to return"
        b "Ah damn"
        b "Alright, see you another time"
        nd "Bye [bname] see you tomorrow"
        scene bna11 with dissolve
        nd "Good night"
        jump waitform

label katybs:
    scene cnd28b with fade
    n "Good evening [bname]"
    n "I got you some food"
    b "Please come in"
    n "I can't stay late"
    n "But tell me if you need anything"
    n "First let me reheat this for you"
    scene cnd28c with fade
    b "This is so tasty"
    b "Thank you"
    if bandageremove ==1:
        n "How's your wound?"
        b "I removed it long time ago"
        b "Let's sit"
        scene cnd29c with dissolve
        b "You know Katy"
        b "No one cared about me like you do"
        scene cnd31d with dissolve
        n "What are you doing"
        b "Thanking you"
        n "I am glad you appreciate [bname]"
        n "I got to go"
        scene cnd32d with hpunch
        b "Wait"
        scene cnd33d with dissolve
        n "You can't do that"
        b "But why? I'm really attracted to you"
        scene cnd36d with dissolve
        n "[bname]"
        n "What did you just do?"
        n "Listen!"
        n "I could be your grandmother"
        n "Do you really love Masha?"
        b "Of course I do"
        b "But she's my sweetheart, not my sextoy"
        b "There are things, I can't do to with her"
        n "So you fuck her mom instead?"
        b "True, especially that her mom is steaming hot"
        n "Hmm you know how to sweet talk into a woman pants"
        scene cnd38c with dissolve
        n "So what are the things that you don't want to do to my daughter?"
        b "I'll show you"
        scene cnd39d with dissolve
        n "Ahh"
        scene cnd41d with dissolve
        n "Mmm [bname]"
        n "I'm old for this"
        b "You're not old"
        scene cnd42d with dissolve
        b "You're the hottest woman ever"
        scene cnd43d with dissolve
        b "Ohh"
        scene cnd42d with dissolve
        b "Yes baby"
        scene cnd43d with dissolve
        n "Ahh [bname]"
        scene cnd41e with fade
        m "{i}(Aha! Wth his girlfriend again){/i}"
        pass

    else:
        n "Is there anything I can do for you while I'm here?"
        b "Well, can you take a look at my wound, see if it needs cleaning?"
        n "Let's see it"
        scene cnd29c with dissolve
        b "I'll remove my shirt"
        scene cnd30c with dissolve
        n "Mmm this is not your shirt"
        b lau "Yes I thought it's better to ease everything"
        scene cnd31c with dissolve
        n "You really have the guts to do this with the mother of your girlfriend"
        b "You clearly misunderstood this"
        n "It's obvious [bname] don't deny it"
        b "No no, why would I undress in the living room if I had different thing on my mind"
        n "Ok let me see it"
        scene cnd32c with dissolve
        n "Looks good to me"
        n "Put the wrapper back on"
        b "Can you help me?"
        scene cnd33c with dissolve
        n "Done"
        scene cnd34c with dissolve
        n "Uhh"
        b "Let me remove your dress"
        scene cnd35c with dissolve
        n "[bname]"
        n "What did you just do?"
        b "Sorry I thought you..."
        n "You thought I ... What?"
        n "Listen!"
        n "Do you really love Masha?"
        scene cnd36c with dissolve
        b "Of course I do"
        b "But she's my sweetheart, not my sextoy"
        b "There are things, I can't do to with her"
        n "So you fuck her mom instead?"
        b "True, especially that her mom is steaming hot"
        n "Hmm you know how to sweet talk into a woman pants"
        scene cnd37c with dissolve
        n "Ahh"
        scene cnd38c with dissolve
        n "So what are the things that you don't want to do with my daughter?"
        b "I'll show you"
        scene cnd39c with vpunch
        n "Ahh"
        scene cnd40c with dissolve
        $ persistent.unlock_6 = True
        n "Mmm"
        scene cnd41c with dissolve
        m "{i}(Aha! Wth his girlfriend again){/i}"
        pass

    m "{i}(I should leave them alone){/i}"
    m "{i}(I'll just lock the door){/i}"
    scene halln_m_in11 with fade
    m "{i}(What's wrong with you [mname]){/i}"
    m "{i}(I should check on them){/i}"
    m "{i}(God! Am I jealous){/i}"
    m "{i}(Come on [mname] just a quick peek I promise){/i}"
    scene cnd42c with fade
    m "{i}(Oh he slept){/i}"
    m "{i}(I will leave him alone){/i}"
    scene halln_m_in11 with fade
    m "Hmm"
    m "{i}(I wonder where is Jedi all this time? He stopped coming to the club){/i}"
    scene sleep1 with fade
    b "Huh!! She's calling me on Jedi number"
    b "I can't see her like this"
    scene halln_m_in10 with fade
    m "Hey! you forgot about me?"
    "{i}(Not at all){/i}"
    m "Then why you're not coming to see me?"
    "{i}(Sorry I've been busy recently){/i}"
    m "No call even nothing?"
    m "Come to my place and all forgiven"
    "{i}(Ermm I'm sorry I'm out of town){/i}"
    m "Fine"
    scene halln_m_in11 with dissolve
    m "{i}(Asshole){/i}"
    menu:
        "She's going to call Rob":
            scene cnd103 with fade
            m "Cheers"
            r "Long time"
            r "I miss you [mname]"
            scene cnd106 with dissolve
            m "Mmm"
            scene cnd104 with dissolve
            r "Let's go to your room"
            scene cnd105 with dissolve
            "..."
            menu:
                "Continue scene":
                    scene dtra28 with fade
                    m "Come here big boy"
                    m "..."
                    scene dtra29 with dissolve
                    m "Mmmm"
                    scene dtra30 with dissolve
                    r "You're simply gorgeous"
                    scene dtra31a with dissolve
                    m "Let me take care of you"
                    r "Yes baby"
                    scene dtra35 with dissolve
                    r "Ahh yes"
                    scene dtra35a with dissolve
                    m "That's what I needed"
                    scene dtra35b with dissolve
                    m "Ready?"
                    scene dtra35 with dissolve
                    m "Gulp!"
                    r "Get up"
                    scene dtra36 with fade
                    m "Ahh"
                    scene dtra37 with dissolve
                    m "Ohh"
                    scene dtra38 with dissolve
                    r "You taste good [mname]"
                    scene dtra39 with dissolve
                    r "I'm going to fuck you good my love"
                    scene dtra40 with dissolve
                    m "Oh lord"
                    r "Turn"
                    play sound "sounds/mrdmsound1.mp3"
                    scene mrdm with fade
                    m "Oh"
                    "..."
                    m "God"
                    m "Don't stop"
                    m "..."
                    r "I'm fucking going to cum"
                    m "Ahhh"
                    m "Fuck me Rob"
                    stop sound fadeout 1.0
                    r "Come here"
                    scene dtra50b with fade
                    m "Ughh"
                    scene dtra50a with dissolve
                    r "Good night bitch"
                    jump newday

                "Skip this":
                    b "{i}(It's time to sleep){/i}"
                    jump newday

        "She's going for [bname]":
            scene cnd87 with fade
            b "{i}(I think now she's going to come and check on me){/i}"
            b "{i}(Anytime now){/i}"
            m "[bname]?"
            scene cnd88a with dissolve
            m "Are you awake?"
            m "{i}(God I want a cock so bad){/i}"
            m "{i}(His ready while asleep){/i}"
            m "[bname] why are you sleeping naked?"
            scene cnd43c with dissolve
            m "{i}(I'll cover him){/i}"
            scene cnd44c with dissolve
            b "{i}(What is she doing?!){/i}"
            scene cnd45c with dissolve
            b "{i}(Hmm cool){/i}"
            scene cnd47c with dissolve
            "SHE JUMPS ON HIM"
            b "Haa!"
            m "Don't move dear"
            m "Just relax"
            scene cnd46c with dissolve
            b "Ahh"
            scene cnd48c with dissolve
            b "..."
            scene cnd49c with dissolve
            m "Mmm"
            scene cnd50c with dissolve
            m "..."
            scene cnd51c with dissolve
            m "Ahhhh"
            scene cnd52c with fade
            m "Good night dear"
            scene cnd53c with dissolve
            m "I'm the star of this show!"
            play sound "sounds/mobilering.wav"
            m "Huh!"
            scene bnah7a with dissolve
            stop sound
            m "Hi Wanda!"
            if today < datetime.date(2024, 12, 24):
                pass

            else:
                m "No no, I have everything"
                m "The turkey is almost ready"
                m "Uhuh yes you get the yule"
                jump wandavisit
                
            m "Yes sure"
            m "Waiting for you"
            scene cnd52c with fade
            m "Wanda and Joshua are coming to visit us"
            m "If you want her to let him visit you, you behave! All right?"
            b "Ok"
            m "Put something on and go wait for them in the living room"
            m "I'll change first"
            scene black
            "..."
            jump wandavisit



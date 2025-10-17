


label cherylbs:
    scene bna_call with dissolve
    c "{i}(I'll drop everything and come to my favorite baby){/i}"
    b "Oh thank you"
    scene b_alone18 with fade
    c "So how did it happen exactly"
    b "I was coming back with [mname] from her work"
    b "And this guy came out of nowhere and shot me"
    c "Her work? At the club?"
    b "{i}(Oh god why is everyone acting smart){/i}"
    scene b_alone19 with dissolve
    c "So, I'm baby sitting you right?"
    c "What can I do for you?"
    b "Hmm"
    menu:
        "Do you know something about these masquerade parties" if askcherylforhelp ==1:
            $ askcherylforhelp = 2
            scene b_alone18 with dissolve
            c "What about it?"
            b "I wanted to go, but [sname] said it's for invitation only"
            b "Can you help me get one?"
            c "I thought you'd ask me earlier"
            b "Hmm"
            b "So you can do?"
            scene b_askcher with dissolve
            c "I can do, one on condition"
            b "What is it?"
            c "You attach a small pov cam on your body"
            b "Easy"
            b "Of course I can"
            scene b_askcher1 with dissolve
            c "Then we have a deal"
            c "Now fuck me as you always do"
            scene bfcangled with fade
            c "Ah"
            c "Yes"
            c "Yes"
            "..."
            scene b_alone20a with dissolve
            m "Good evening [bname]"
            m "Good evening Masha"
            m "{i}(Thanks God they didn't see me this way){/i}"
            b "She thought you're Masha"
            c "Ah yes"
            b "Maybe we can lure her into something?"
            c "Not this time [bname]"
            c "I'll just leave"
            menu:
                "Try your luck":
                    scene b_alone20b with dissolve
                    if persistent.patch_enabled:
                        b "Mom! Wait"
                        pass
                    else:
                        b "Wait"
                        pass
                    m "What honey?"
                    b "Can you join us?"
                    m "What?"
                    m "With you and Masha?"
                    m "No honey, it's not right"
                    b "She doesn't know what to do, and honestly, no one is like you"
                    if mrel >=180:
                        m "Are you sure you want me to do that?"
                        b "Yes, you're the hottest of them all"
                        scene b_alone21b with dissolve
                        b "Pst, get her a drink"
                        menu:
                            "Cheryl will put something in her drink":
                                scene chejen with fade
                                c "Drink this"
                                b "Oh wow! Did you?"
                                c "Yes"
                                scene chejen1 with fade
                                b "Yesss"
                                c "Why do you hate me [mname]?"
                                scene chejen2 with hpunch
                                m "Mmhhm I don't"
                                c "Uh"
                                scene chejen3 with dissolve
                                m "Mmm"
                                c "You do not?"
                                m "No, I love you"
                                scene chejen4 with dissolve
                                m "Ahh"
                                c "Prove it"
                                scene chejen5 with dissolve
                                c "Ah yes"
                                scene chejen6 with dissolve
                                m "Sit"
                                if mcherylrecording ==1:
                                    menu:
                                        "Record this for Cheryl":
                                            $ persistent.unlock_56 = True
                                            scene chejen16 with dissolve
                                            b "Go on ladies, do something"
                                            $ mcherylrecording = 2
                                            b "Come close"
                                            scene chejen20 with dissolve
                                            b "Wow [mname] is very horny"
                                            scene chejen17 with dissolve
                                            b "I should take several angles"
                                            scene chejen18 with dissolve
                                            b "Hmm"
                                            scene chejen19 with dissolve
                                            b "Cool"
                                            scene chejen21 with dissolve
                                            b "Yes! Look at me"
                                            b "Straight to the phone"
                                            scene chejen22 with vpunch
                                            b "Huh"
                                            m "You're filming?"
                                            scene chejen23 with dissolve
                                            m "Then film this"
                                            play sound "sounds/cjbjbsound1.mp3"
                                            scene cjbjb with fade
                                            b "Oh"
                                            stop sound
                                            play sound "sounds/cjbjbsound2.mp3"
                                            b "..."
                                            stop sound
                                            play sound "sounds/cjbjbsound1.mp3"
                                            b "Yes"
                                            "..."
                                            stop sound
                                            b "Suck it bitch"
                                            b "Arghh"
                                            scene chejen24 with fade
                                            b "Mmm yes!!"
                                            b "Give it to her"
                                            scene chejen25 with vpunch
                                            "SPIT"
                                            scene b_alone37b with fade
                                            b "You were awesome"
                                            m "Good night baby"
                                            jump newday


                                        "No":
                                            pass
                                else:
                                    pass
                                scene chejen7 with dissolve
                                b "Whoa!"
                                scene chejen8 with dissolve
                                c "Ahhh"
                                b "Enough, I want to join in"
                                scene chejen9 with dissolve
                                c "Oh yeah"
                                scene chejen10 with dissolve
                                b "Mmm"
                                scene chejen11 with dissolve
                                m "Ahh"
                                scene chejen12 with dissolve
                                b "Cheryl come ride me"
                                scene chejen13 with dissolve
                                m "..."
                                scene chejen14 with dissolve
                                c "Ahhh"
                                scene chejen13 with dissolve
                                b "Yes"
                                scene chejen14 with dissolve
                                m "Mmm"
                                scene chejen15 with dissolve
                                $ persistent.unlock_48 = True
                                b "Ahh shit!"
                                scene b_alone37b with fade
                                b "You were awesome"
                                m "Good night baby"
                                jump newday



                                

                            "Continue":
                                pass
                        scene b_alone22b with fade
                        c "Let's lose this"
                        m "Mmm"
                        scene b_alone23b with dissolve
                        m "Let me teach you how to kiss properly"
                        scene b_alone24c with dissolve
                        m "Cheryl!?"
                        c "I know you don't like me"
                        c "I don't like you either but..."
                        c "We need to do this for [bname]"
                        if mrel >=200 and mcorr >=25:
                            scene b_alone26b with dissolve
                            $ persistent.unlock_5 = True
                            c "Right [bname]?"
                            b "Yes, come on do something together maybe I can get it up"
                            c "What do you want us to do?"
                            menu:
                                "Play and make out between yourselves":
                                    scene b_alone27b with dissolve
                                    c "You're going to enjoy this"
                                    scene b_alone28c with dissolve
                                    m "..."
                                    scene b_alone29b with dissolve
                                    "[mname] WAS EXHALING FASTER THAN USUAL"
                                    "THIS WASN'T EASY FOR HER AS..."
                                    "DIFFERENT THOUGHTS RUNNING THROUGH HER MIND"
                                    "SHE CAN'T STAND THIS WOMAN"
                                    "BUT HERE SHE IS DOING THIS FOR THE SAKE OF [bname]"
                                    scene b_alone30c with dissolve
                                    m "Ahh"
                                    scene b_alone31b with dissolve
                                    m "..."
                                    scene b_alone32m with dissolve
                                    m "Ahh"
                                    b "Enough, you got me going"
                                    b "Cheryl turn"
                                    scene b_alone34b with dissolve
                                    c "Ahh"
                                    b "[mname] come near"
                                    scene b_alone33c with dissolve
                                    c "Ahh yes, that's hard"
                                    b "I'm close, come here bitch"
                                    scene b_alone35b with dissolve
                                    m "Gulp"
                                    scene b_alone36b with fade
                                    b "Oh yeah!"
                                    b "I think she deserves some pleasure"
                                    scene b_alone36bb with dissolve
                                    m "Ahhh"
                                    scene b_alone37b with fade
                                    b "You were awesome"
                                    b "I cum twice"
                                    m "Glad that you're getting back to normal"
                                    m "But next time, don't bring Cheryl"
                                    b "But why?"
                                    m "I hate this woman"
                                    m "Good night"
                                    jump newday

                                "Dominate [mname]":
                                    c "Get me my bag"
                                    scene b_alone38b with dissolve
                                    c "You're going to love this, bitch"
                                    m "Huh"
                                    scene b_alone39b with dissolve
                                    m "Ahh!"
                                    scene b_alone40b with dissolve
                                    "[mname] WAS EXHALING FASTER THAN USUAL"
                                    "SHE CAN'T STAND THIS WOMAN"
                                    "BUT SHE IS DOING THIS FOR THE SAKE OF [bname]"
                                    c "Let's try what you like"
                                    scene b_alone41b with dissolve
                                    m "Ahh"
                                    scene b_alone42b with dissolve
                                    m "Ohhh"
                                    scene b_alone43b with dissolve
                                    b "Enough, you got me going"
                                    b "My turn now"
                                    if mcorr >=35:
                                        scene mdche with dissolve
                                        m "Not yet"
                                        c "Ahh"
                                        b "What?"
                                        m "Stay out of this [bname]"
                                        scene mdche1 with dissolve
                                        c "Uhhh"
                                        m "Payback time bitch!"
                                        scene mdche2 with dissolve
                                        b "Oh my..."
                                        scene mdche3 with dissolve
                                        b "...Fucking god"
                                        scene mdche4 with dissolve
                                        c "Ahhh [mname]!"
                                        scene mdche5 with dissolve
                                        "[bname] was already wetting himself"
                                        scene mdche6 with dissolve
                                        m "You think you're a tough bitch!?"
                                        scene mdche6a with dissolve
                                        c "Oaaahh!"
                                        scene mdche7 with dissolve
                                        c "[mname]! Please"
                                        scene mdche8 with dissolve
                                        m "Shut up"
                                        b "My turn"
                                        scene mdche9 with dissolve
                                        b "Get up"
                                        scene mdche10 with dissolve
                                        m "Ahh"
                                        scene mdche11 with dissolve
                                        c "Yes baby"
                                        scene mdche10 with dissolve
                                        m "..."
                                        scene mdche12 with dissolve
                                        m "Ohh"
                                        scene mdche10 with dissolve
                                        m "Mm yes"
                                        m "Give it to her"
                                        scene mdche13 with dissolve
                                        m "Yeah cum dump her"
                                        scene mdche14 with dissolve
                                        c "Pfft!"
                                        scene b_alone37b with fade
                                        b "You were awesome"
                                        m "Next time, don't bring Cheryl"
                                        b "But why?"
                                        m "I hate this woman"
                                        m "Good night"
                                        jump newday

                                    else:
                                        pass
                                    "..."
                                    menu:
                                        "Deepthroat [mname]":
                                            scene b_alone44b with dissolve
                                            c "Oh nice"
                                            scene b_alone45b with dissolve
                                            m "Gulp"
                                            scene b_alone46b with dissolve
                                            b "Ahh yess! Fuck"
                                            scene b_alone47b with fade
                                            c "I'm amazed [bname]"
                                            b "Oh yeah?!"
                                            scene b_alone37b with fade
                                            b "You were awesome"
                                            b "I cum twice"
                                            m "Glad that you're getting back to normal"
                                            m "But next time, don't bring Cheryl"
                                            b "But why?"
                                            m "I hate this woman"
                                            m "Good night"
                                            jump newday

                                        "More":
                                            scene b_alonecm with dissolve
                                            c "Ahh"
                                            c "I need that cock now"
                                            scene b_alonecm1 with dissolve
                                            c "Ahhh"
                                            b "Take it out and suck it [mname]"
                                            scene b_alonecm2 with dissolve
                                            b "Ah yes"
                                            scene b_alonecm3 with dissolve
                                            m "Mmm"
                                            scene b_alone37b with fade
                                            b "You were awesome"
                                            b "I cum twice"
                                            m "Glad that you're getting back to normal"
                                            m "But next time, don't bring Cheryl"
                                            b "But why?"
                                            m "I hate this woman"
                                            m "Good night"
                                            jump newday

                        else:
                            m "No!"
                            scene b_alone25b with dissolve
                            $ mrel -= 5
                            show screen mreldw
                            m "No way!"
                            hide screen mreldw
                            c "I'll go [bname]"
                            "YOU NEED 200 POINTS AND 25 CORRUPTION"
                            pass
                    else:
                        m "No [bname], I can't do that"
                        "YOU DON'T HAVE ENOUGH POINTS, 180 NEEDED AT LEAST"
                        pass
                "Continue":
                    pass
            scene b_alone21 with fade
            m "Oh God, I need to change and clean my face"
            scene b_alone24a with fade
            m "What's up?"
            b "Watching TV"
            m "Alone?"
            b "Yes"
            m "I thought I saw Masha with you"
            b "Euh! Yes she just left"
            m "Ah good, so all came back to normal?"
            b "What do you mean?"
            m "Your worries are they gone?"
            b "No, still the same"
            menu:
                "Maybe you can do something about it?":
                    m "Do I have a choice?"
                    b "Cool"
                    m "But not here, in the bed room"
                    b "Ok meanwhile, why don't you put some makeup"
                    scene mdom with fade
                    b "Ah, you came here?"
                    m "Yes"
                    m "So?"
                    menu:
                        "Get on your knees":
                            "YOU'LL GET TO BE DOMINATING SLOWLY IN EVERY VERSION"
                            scene mdom1 with dissolve
                            m "Ok"
                            scene mdom2 with dissolve
                            b "Crawl on all four"
                            m "Let me remove my lingerie first, I don't want to damaged it"
                            scene mdom3 with dissolve
                            "..."
                            scene mdom4 with dissolve
                            b "Yes! That's how I want you"
                            if binjected ==1:
                                b "I love it this way"
                                scene mdom5 with dissolve
                                b "Yess"
                                scene mdom6 with dissolve
                                b "Enough, roll"
                                scene mdom7a with dissolve
                                b "Mmm"
                                scene mdom7b with dissolve
                                m "Uhh"
                                scene mdom8a with dissolve
                                m "It's clearly not going to work [bname]"
                                m "You won't cum"
                                if mrel >=120:
                                    $ persistent.unlock_35 = True
                                    b "Let's try something else"
                                    scene mdom9 with fade
                                    m "I see you like this position"
                                    scene mdom10 with dissolve
                                    b "Just be quiet"
                                    scene mdom11 with dissolve
                                    m "Woah!"
                                    scene mdom12 with dissolve
                                    m "[bname] this position is painful"
                                    scene mdom13 with dissolve
                                    b "How about this"
                                    m "Ahh"
                                    b "Shut up"
                                    scene mdom14 with dissolve
                                    m "Where's your penis?"
                                    m "Is that all?"
                                    b "Get down"
                                    scene mdom15 with dissolve
                                    m "Oh really?"
                                    scene mdom16 with hpunch
                                    m "AOOH!"
                                    scene mdom17 with dissolve
                                    m "..."
                                    scene mdom18 with dissolve
                                    m "..."
                                    scene mdom19 with dissolve
                                    m "..."
                                    scene mdom20 with dissolve
                                    m "..."
                                    scene mdom21 with dissolve
                                    m "..."
                                    scene mdom20 with dissolve
                                    m "..."
                                    scene mdom22 with hpunch
                                    m "Ahh"
                                    scene mdom23 with fade
                                    b "Good girl"
                                    m "..."
                                    b "{i}(I'll go  sleep){/i}"
                                    jump newday

                                else:
                                    "RAISE YOUR RELATIONSHIP POINTS TO 120"
                                    pass
                                m "I really need to sleep"
                                scene mdom with fade
                                m "Good night"
                                b "{i}(Damn){/i}"
                                b "{i}(I'll go to sleep){/i}"
                                jump newday
                            else:
                                scene mdom4a with dissolve
                                b "Ahh fuck!"
                                scene mdoma with fade
                                m "Good night"
                                b "{i}(Damn I forgot to inject){/i}"
                                b "{i}(I'll go to sleep){/i}"
                                jump newday

                "Say nothing":
                    m "Ah I'm so tired"
                    m "I had one too many drinks probably"
                    m "Good night"
                    b "{i}(Damn){/i}"
                    b "{i}(I'll go to sleep){/i}"
                    jump newday

        "Well I'm having this erection problem and...":
            c "And you need my help?"
            scene bfc
            c "Ah"
            c "Yes"
            c "Yes"
            "..."
            scene b_alone20a with dissolve
            m "Good evening [bname]"
            m "Good evening Masha"
            m "{i}(Thanks God they didn't see me this way){/i}"
            b "She thought you're Masha"
            c "Ah yes"
            b "Maybe we can lure her into something?"
            c "Not this time [bname]"
            c "I'll just leave"
            menu:
                "Try your luck":
                    scene b_alone20b with dissolve
                    if persistent.patch_enabled:
                        b "Mom! Wait"
                        pass
                    else:
                        b "Wait"
                        pass
                    m "What honey?"
                    b "Can you join us?"
                    m "What?"
                    m "With you and Masha?"
                    m "No honey, it's not right"
                    b "She doesn't know what to do, and honestly, no one is like you"
                    if mrel >=180:
                        m "Are you sure you want me to do that?"
                        b "Yes, you're the hottest of them all"
                        scene b_alone21b with dissolve
                        b "Pst, get her a drink"
                        menu:
                            "Cheryl will put something in her drink":
                                scene chejen with fade
                                c "Drink this"
                                b "Oh wow! Did you?"
                                c "Yes"
                                scene chejen1 with fade
                                b "Yesss"
                                c "Why do you hate me [mname]?"
                                scene chejen2 with hpunch
                                m "Mmhhm I don't"
                                c "Uh"
                                scene chejen3 with dissolve
                                m "Mmm"
                                c "You do not?"
                                m "No, I love you"
                                scene chejen4 with dissolve
                                m "Ahh"
                                c "Prove it"
                                scene chejen5 with dissolve
                                c "Ah yes"
                                scene chejen6 with dissolve
                                m "Sit"
                                if mcherylrecording ==1:
                                    menu:
                                        "Record this for Cheryl":
                                            $ persistent.unlock_56 = True
                                            scene chejen16 with dissolve
                                            b "Go on ladies, do something"
                                            $ mcherylrecording = 2
                                            b "Come close"
                                            scene chejen20 with dissolve
                                            b "Wow [mname] is very horny"
                                            scene chejen17 with dissolve
                                            b "I should take several angles"
                                            scene chejen18 with dissolve
                                            b "Hmm"
                                            scene chejen19 with dissolve
                                            b "Cool"
                                            scene chejen21 with dissolve
                                            b "Yes! Look at me"
                                            b "Straight to the phone"
                                            scene chejen22 with vpunch
                                            b "Huh"
                                            m "You're filming?"
                                            scene chejen23 with dissolve
                                            m "Then film this"
                                            play sound "sounds/cjbjbsound1.mp3"
                                            scene cjbjb with fade
                                            b "Oh"
                                            stop sound
                                            play sound "sounds/cjbjbsound2.mp3"
                                            b "..."
                                            stop sound
                                            play sound "sounds/cjbjbsound1.mp3"
                                            b "Yes"
                                            "..."
                                            stop sound
                                            b "Suck it bitch"
                                            b "Arghh"
                                            scene chejen24 with fade
                                            b "Mmm yes!!"
                                            b "Give it to her"
                                            scene chejen25 with vpunch
                                            "SPIT"
                                            scene b_alone37b with fade
                                            b "You were awesome"
                                            m "Good night baby"
                                            jump newday


                                        "No":
                                            pass
                                else:
                                    pass
                                scene chejen7 with dissolve
                                b "Whoa!"
                                scene chejen8 with dissolve
                                c "Ahhh"
                                b "Enough, I want to join in"
                                scene chejen9 with dissolve
                                c "Oh yeah"
                                scene chejen10 with dissolve
                                b "Mmm"
                                scene chejen11 with dissolve
                                m "Ahh"
                                scene chejen12 with dissolve
                                b "Cheryl come ride me"
                                scene chejen13 with dissolve
                                m "..."
                                scene chejen14 with dissolve
                                c "Ahhh"
                                scene chejen13 with dissolve
                                b "Yes"
                                scene chejen14 with dissolve
                                m "Mmm"
                                scene chejen15 with dissolve
                                $ persistent.unlock_48 = True
                                b "Ahh shit!"
                                scene b_alone37b with fade
                                b "You were awesome"
                                m "Good night baby"
                                jump newday



                                

                            "Continue":
                                pass
                        scene b_alone22b with fade
                        c "Let's lose this"
                        m "Mmm"
                        scene b_alone23b with dissolve
                        m "Let me teach you how to kiss properly"
                        scene b_alone24c with dissolve
                        m "Cheryl!?"
                        c "I know you don't like me"
                        c "I don't like you either but..."
                        c "We need to do this for [bname]"
                        if mrel >=200 and mcorr >=25:
                            scene b_alone26b with dissolve
                            $ persistent.unlock_5 = True
                            c "Right [bname]?"
                            b "Yes, come on do something together maybe I can get it up"
                            c "What do you want us to do?"
                            menu:
                                "Play and make out between yourselves":
                                    scene b_alone27b with dissolve
                                    c "You're going to enjoy this"
                                    scene b_alone28c with dissolve
                                    m "..."
                                    scene b_alone29b with dissolve
                                    "[mname] WAS EXHALING FASTER THAN USUAL"
                                    "THIS WASN'T EASY FOR HER AS..."
                                    "DIFFERENT THOUGHTS RUNNING THROUGH HER MIND"
                                    "SHE CAN'T STAND THIS WOMAN"
                                    "BUT HERE SHE IS DOING THIS FOR THE SAKE OF [bname]"
                                    scene b_alone30c with dissolve
                                    m "Ahh"
                                    scene b_alone31b with dissolve
                                    m "..."
                                    scene b_alone32m with dissolve
                                    m "Ahh"
                                    b "Enough, you got me going"
                                    b "Cheryl turn"
                                    scene b_alone34b with dissolve
                                    c "Ahh"
                                    b "[mname] come near"
                                    scene b_alone33c with dissolve
                                    c "Ahh yes, that's hard"
                                    b "I'm close, come here bitch"
                                    scene b_alone35b with dissolve
                                    m "Gulp"
                                    scene b_alone36b with fade
                                    b "Oh yeah!"
                                    b "I think she deserves some pleasure"
                                    scene b_alone36bb with dissolve
                                    m "Ahhh"
                                    scene b_alone37b with fade
                                    b "You were awesome"
                                    b "I cum twice"
                                    m "Glad that you're getting back to normal"
                                    m "But next time, don't bring Cheryl"
                                    b "But why?"
                                    m "I hate this woman"
                                    m "Good night"
                                    jump newday

                                "Dominate [mname]":
                                    c "Get me my bag"
                                    scene b_alone38b with dissolve
                                    c "You're going to love this, bitch"
                                    m "Huh"
                                    scene b_alone39b with dissolve
                                    m "Ahh!"
                                    scene b_alone40b with dissolve
                                    "[mname] WAS EXHALING FASTER THAN USUAL"
                                    "SHE CAN'T STAND THIS WOMAN"
                                    "BUT SHE IS DOING THIS FOR THE SAKE OF [bname]"
                                    c "Let's try what you like"
                                    scene b_alone41b with dissolve
                                    m "Ahh"
                                    scene b_alone42b with dissolve
                                    m "Ohhh"
                                    scene b_alone43b with dissolve
                                    b "Enough, you got me going"
                                    b "My turn now"
                                    if mcorr >=35:
                                        scene mdche with dissolve
                                        m "Not yet"
                                        c "Ahh"
                                        b "What?"
                                        m "Stay out of this [bname]"
                                        scene mdche1 with dissolve
                                        c "Uhhh"
                                        m "Payback time bitch!"
                                        scene mdche2 with dissolve
                                        b "Oh my..."
                                        scene mdche3 with dissolve
                                        b "...Fucking god"
                                        scene mdche4 with dissolve
                                        c "Ahhh [mname]!"
                                        scene mdche5 with dissolve
                                        "[bname] was already wetting himself"
                                        scene mdche6 with dissolve
                                        m "You think you're a tough bitch!?"
                                        scene mdche6a with dissolve
                                        c "Oaaahh!"
                                        scene mdche7 with dissolve
                                        c "[mname]! Please"
                                        scene mdche8 with dissolve
                                        m "Shut up"
                                        b "My turn"
                                        scene mdche9 with dissolve
                                        b "Get up"
                                        scene mdche10 with dissolve
                                        m "Ahh"
                                        scene mdche11 with dissolve
                                        c "Yes baby"
                                        scene mdche10 with dissolve
                                        m "..."
                                        scene mdche12 with dissolve
                                        m "Ohh"
                                        scene mdche10 with dissolve
                                        m "Mm yes"
                                        m "Give it to her"
                                        scene mdche13 with dissolve
                                        m "Yeah cum dump her"
                                        scene mdche14 with dissolve
                                        c "Pfft!"
                                        scene b_alone37b with fade
                                        b "You were awesome"
                                        m "Next time, don't bring Cheryl"
                                        b "But why?"
                                        m "I hate this woman"
                                        m "Good night"
                                        jump newday

                                    else:
                                        pass
                                    "..."
                                    menu:
                                        "Deepthroat [mname]":
                                            scene b_alone44b with dissolve
                                            c "Oh nice"
                                            scene b_alone45b with dissolve
                                            m "Gulp"
                                            scene b_alone46b with dissolve
                                            b "Ahh yess! Fuck"
                                            scene b_alone47b with fade
                                            c "I'm amazed [bname]"
                                            b "Oh yeah?!"
                                            scene b_alone37b with fade
                                            b "You were awesome"
                                            b "I cum twice"
                                            m "Glad that you're getting back to normal"
                                            m "But next time, don't bring Cheryl"
                                            b "But why?"
                                            m "I hate this woman"
                                            m "Good night"
                                            jump newday

                                        "More":
                                            scene b_alonecm with dissolve
                                            c "Ahh"
                                            c "I need that cock now"
                                            scene b_alonecm1 with dissolve
                                            c "Ahhh"
                                            b "Take it out and suck it [mname]"
                                            scene b_alonecm2 with dissolve
                                            b "Ah yes"
                                            scene b_alonecm3 with dissolve
                                            m "Mmm"
                                            scene b_alone37b with fade
                                            b "You were awesome"
                                            b "I cum twice"
                                            m "Glad that you're getting back to normal"
                                            m "But next time, don't bring Cheryl"
                                            b "But why?"
                                            m "I hate this woman"
                                            m "Good night"
                                            jump newday

                        else:
                            m "No!"
                            scene b_alone25b with dissolve
                            $ mrel -= 5
                            show screen mreldw
                            m "No way!"
                            hide screen mreldw
                            c "I'll go [bname]"
                            "YOU NEED 200 POINTS AND 25 CORRUPTION"
                            pass
                    else:
                        m "No [bname], I can't do that"
                        "YOU DON'T HAVE ENOUGH POINTS, 180 NEEDED AT LEAST"
                        pass
                "Continue":
                    pass
            scene b_alone21 with fade
            m "Oh God, I need to change and clean my face"
            scene b_alone24a with fade
            m "What's up?"
            b "Watching TV"
            m "Alone?"
            b "Yes"
            m "I thought I saw Masha with you"
            b "Euh! Yes she just left"
            m "Ah good, so all came back to normal?"
            b "What do you mean?"
            m "Your worries are they gone?"
            b "No, still the same"
            menu:
                "Maybe you can do something about it?":
                    m "Do I have a choice?"
                    b "Cool"
                    m "But not here, in the bed room"
                    b "Ok meanwhile, why don't you put some makeup"
                    scene mdom with fade
                    b "Ah, you came here?"
                    m "Yes"
                    m "So?"
                    menu:
                        "Get on your knees":
                            "YOU'LL GET TO BE DOMINATING SLOWLY IN EVERY VERSION"
                            scene mdom1 with dissolve
                            m "Ok"
                            scene mdom2 with dissolve
                            b "Crawl on all four"
                            m "Let me remove my lingerie first, I don't want to damaged it"
                            scene mdom3 with dissolve
                            "..."
                            scene mdom4 with dissolve
                            b "Yes! That's how I want you"
                            if binjected ==1:
                                b "I love it this way"
                                scene mdom5 with dissolve
                                b "Yess"
                                scene mdom6 with dissolve
                                b "Enough, roll"
                                scene mdom7a with dissolve
                                b "Mmm"
                                scene mdom7b with dissolve
                                m "Uhh"
                                scene mdom8a with dissolve
                                m "It's clearly not going to work [bname]"
                                m "You won't cum"
                                if mrel >=120:
                                    $ persistent.unlock_35 = True
                                    b "Let's try something else"
                                    scene mdom9 with fade
                                    m "I see you like this position"
                                    scene mdom10 with dissolve
                                    b "Just be quiet"
                                    scene mdom11 with dissolve
                                    m "Woah!"
                                    scene mdom12 with dissolve
                                    m "[bname] this position is painful"
                                    scene mdom13 with dissolve
                                    b "How about this"
                                    m "Ahh"
                                    b "Shut up"
                                    scene mdom14 with dissolve
                                    m "Where's your penis?"
                                    m "Is that all?"
                                    b "Get down"
                                    scene mdom15 with dissolve
                                    m "Oh really?"
                                    scene mdom16 with hpunch
                                    m "AOOH!"
                                    scene mdom17 with dissolve
                                    m "..."
                                    scene mdom18 with dissolve
                                    m "..."
                                    scene mdom19 with dissolve
                                    m "..."
                                    scene mdom20 with dissolve
                                    m "..."
                                    scene mdom21 with dissolve
                                    m "..."
                                    scene mdom20 with dissolve
                                    m "..."
                                    scene mdom22 with hpunch
                                    m "Ahh"
                                    scene mdom23 with fade
                                    b "Good girl"
                                    m "..."
                                    b "{i}(I'll go  sleep){/i}"
                                    jump newday

                                else:
                                    "RAISE YOUR RELATIONSHIP POINTS TO 120"
                                    pass
                                m "I really need to sleep"
                                scene mdom with fade
                                m "Good night"
                                b "{i}(Damn){/i}"
                                b "{i}(I'll go to sleep){/i}"
                                jump newday
                            else:
                                scene mdom4a with dissolve
                                b "Ahh fuck!"
                                scene mdoma with fade
                                m "Good night"
                                b "{i}(Damn I forgot to inject){/i}"
                                b "{i}(I'll go to sleep){/i}"
                                jump newday

                "Say nothing":
                    m "Ah I'm so tired"
                    m "I had one too many drinks probably"
                    m "Good night"
                    b "{i}(Damn){/i}"
                    b "{i}(I'll go to sleep){/i}"
                    jump newday


        "Let's go to my room?":
            scene b_alone26a with fade
            c "Wow you're too..."
            scene b_alone27a with dissolve
            c "Fast"
            scene b_alone28b with dissolve
            b "Mmm"
            scene b_alone29a with dissolve
            c "Yes [bname]"
            scene b_alone30b with dissolve
            c "Fuck my big ass"
            scene b_alone31a with dissolve
            c "Oh yes!"
            scene b_alone32a with fade
            c "Yes!!!"
            scene b_alone32b with dissolve
            c "Ahh!"
            if persistent.patch_enabled:
                c "You know your aunty loves it rough"
                pass
            else:
                c "You know I love it rough"
                pass
            m "Honey I'm home"
            scene b_alone33a with dissolve
            m "Did Cheryl come?"
            scene b_alone33b with fade
            c "Hi [mname]"
            m "Where is [bname]"
            c "I don't know, I was using the toilet, I left him here"
            c "I'll be going, good night"
            m "Here's [bname]"
            scene b_alone34a with dissolve
            c "Oh my baby, it's time I go"
            scene b_alone21 with fade
            m "Oh God, I need to change and clean my face"
            scene b_alone24b with fade
            m "How's my baby Ernesto?"
            b "Who's Ernesto?"
            menu:
                "Can we do the thing?":
                    scene b_alone24a with dissolve
                    m "Which thing?"
                    b "You know, trying myself if all is good"
                    m "'Sigh' Ok"
                    m "But not here, in the bed room"
                    b "Ok meanwhile, why don't you put some makeup"
                    scene mdom with fade
                    b "Ah, you came here?"
                    m "Yes"
                    m "So?"
                    menu:
                        "Get on your knees":
                            "YOU'LL GET TO BE DOMINATING SLOWLY IN EVERY VERSION"
                            scene mdom1 with dissolve
                            m "Ok"
                            scene mdom2 with dissolve
                            b "Crawl on all four"
                            m "Let me remove my lingerie first, I don't want to damaged it"
                            scene mdom3 with dissolve
                            "..."
                            scene mdom4 with dissolve
                            b "Yes! That's how I want you"
                            if binjected ==1:
                                b "I love it this way"
                                scene mdom5 with dissolve
                                b "Yess"
                                scene mdom6 with dissolve
                                b "Enough, 69"
                                scene mdom7 with dissolve
                                b "Mmm"
                                scene mdom8 with dissolve
                                m "It's not going to work [bname]"
                                if mrel >=120:
                                    b "Let's try something else"
                                    scene mdom24 with fade
                                    m "..."
                                    scene mdom25 with dissolve
                                    m "Ohh"
                                    m "[bname] why so rough!?"
                                    scene mdom26 with dissolve
                                    b "Shut up"
                                    scene mdom27 with dissolve
                                    m "Ahhh"
                                    menu:
                                        "Let her give you a rim job":
                                            scene mdom30 with dissolve
                                            m "..."
                                            scene mdom31 with dissolve
                                            b "Ah shit!"
                                            pass
                                        "Give her rim job":
                                            scene mdom28 with dissolve
                                            b "Mmm"
                                            scene mdom29 with dissolve
                                            m "Ooh [bname]"
                                            pass
                                    scene mdom32 with fade
                                    m "..."
                                    b "I'll go sleep"
                                    jump newday

                                else:
                                    "RAISE YOUR RELATIONSHIP POINTS TO 120"
                                    pass
                                m "I really need to sleep"
                                scene mdom with fade
                                m "Good night"
                                b "{i}(Damn){/i}"
                                b "{i}(I'll go to sleep){/i}"
                                jump newday
                            else:
                                scene mdom4a with dissolve
                                b "Ahh fuck!"
                                scene mdoma with fade
                                m "Good night"
                                b "{i}(Damn I forgot to inject){/i}"
                                b "{i}(I'll go to sleep){/i}"
                                jump newday

                        


                "Continue":
                    m "Ah I'm so tired"
                    m "I had one too many drinks probably"
                    m "Good night"
                    b "{i}(Damn){/i}"
                    b "{i}(I'll go to sleep){/i}"
                    jump newday

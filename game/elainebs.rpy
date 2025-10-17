

label elainebs:
    scene bna_call with dissolve
    b "Yeah, I'm alone"
    e "{i}(Sure dear, I'll be there shortly){/i}"
    b "Would you like to come to spend time with me?"
    e "{i}(Cool, tell [mname] to prepare soup for me){/i}"
    b "Err she's not here"
    b "She's at work, that's why"
    b "She said I can call you to come"
    e "{i}(Ah yeah, I forgot){/i}"
    e "{i}(Then prepare, or order soup please){/i}" 
    b "Sure thing"
    scene bna with fade
    e "Thank you for the food"
    b "At least better than your shuka"
    scene bna_laugh with dissolve
    e "Hahaha shuba, chuka is seaweed"
    b "Yeah, as if I care"
    b "It's sickening"
    e "Do you have wine?"
    b "Of course"
    b "Me always ready"
    scene bna1 with fade
    e "Are you sure you can drink?"
    b "Yeah I don't care, I didn't know you smoke"
    e "[mname] told me about your problem down there"
    e "I hope it's not permanent"
    e "If you know what I mean"
    e "It's going to be an unfortunate loss for the sisterhood"
    menu:
        "I'm ok now" if bandageremove ==1:
            b "I'm ok now"
            b "But you can still give me a shower if you want"
            scene bna1a with dissolve
            e "You mean a golden shower?"
            e "Or a real shower?"
            scene bna1b with dissolve
            b "No! Not that one"
            e "Hahaha"
            e "Let's go"
            menu:
                "Shower right?*NEW*":
                    b "Real shower?"
                    e "Yes let's go"
                    scene bna44 with fade
                    e "You always cut to the chase [bname]"
                    e "Never wasting a minute"
                    e "And that's what I like about you"
                    e "You never try to hide your pussy worshipping"
                    scene bna45 with dissolve
                    b "Whaaat!"
                    e "Come on!"
                    e "We both know we're not here for shower"
                    e "Sit!"
                    scene bna46 with dissolve
                    b "You're the best sucker Elaine"
                    scene bna47 with dissolve
                    b "Ahh! Yes!"
                    b "Come, enough"
                    scene etoianim00 with dissolve
                    e "Ahh"
                    scene etoianim02 with dissolve
                    e "..."
                    scene etoianim07 with dissolve
                    e "[bname]"
                    scene etoianim18 with dissolve
                    e "..."
                    scene etoianim24 with dissolve
                    e "Mmhmm"
                    scene etoianim040 with dissolve
                    e "Ahh!"
                    scene bna48 with dissolve
                    b "Ohh!"
                    pass
                "Continue":
                    scene bna3 with fade
                    e "Undress yourself"
                    e "And lay on the floor"
                    b "Come here"
                    scene bna4b with dissolve
                    b "..."
                    scene bna8b with dissolve
                    "..."
                    b "Let's do it on the floor"
                    scene bnaanim with dissolve
                    e "Uh [bname]"
                    e "You're getting good"
                    e "Ahh"
                    "..."
                    b "Oh"
                    scene bna8c with dissolve
                    e "Ahhhh"
                    b "Fuck"
                    scene bna8b with fade
                    e "Why did you finish in me?"
                    b "Couldn't pull"
                    e "Luckily I'm on the pill"
                    e "Always"
            scene bme with fade
            m "Hi Elaine, thanks for coming"
            e "My pleasure"
            b "{i}(Hehehe true, my pleasure as well){/i}"
            m "And please, don't smoke inside"
            e "Yeah..."
            m "I'll clean up and come, don't go"
            e "Be quick"
            m "[bname] do we have food?"
            b "Yes, I'll get something for you"
            scene bme1 with fade
            m "Finally!"
            scene bme2 with dissolve
            m "I'm sorry I got you into this"
            e "It's fine"
            m "So how's life, long time we didn't chat"
            e "Say! Let's go have fun the two of us"
            m "Only if I can get a cig"
            scene bme3 with dissolve
            e "We can also call guys here if you want?"
            menu:
                "No*":
                    m "But I think it's better if we stick to [bname]"
                    m "Maybe next time"
                    pass
                "I don't know!":
                    e "You'll like it"
                    scene bme3b with dissolve
                    m "I can't have guys here in front of [bname]"
                    e "Leave [bname] to me, that's easy"
                    m "God Elaine! I am saying No"
                    e "Nevermind, just wait here, I'll go get [bname]"
                    m "Ok but no guys"
                    m "I'll get some drinks"
                    scene bme26 with fade
                    e "Hey"
                    b "What's up?"
                    e "I'm thinking to have some guys around"
                    e "What do you say?"
                    menu:
                        "Cool, the more the merrier":
                            $ persistent.unlock_67 = True
                            $ mcorr += 5
                            show screen mcorr
                            b "Cool I'm in"
                            hide screen mcorr
                            e "Ok great, I thought you won't accept"
                            b "[mname] sent you to ask me?"
                            e "She doesn't want, or maybe hesitating to do it while you're here"
                            b "Mm I see"
                            b "Who's coming?"
                            e "Some guys you don't know"
                            b "Can I join?"
                            e "You and your luck"
                            e "I got to get back to [mname]"
                            b "Take this put it in her drink"
                            e "What is it?"
                            b "It's safe, just do it"
                            scene bme27 with fade
                            m "Let's go see [bname]"
                            e "Just 5 minutes, let's finish this drink first"
                            scene bme28 with dissolve
                            play sound "sounds/doorbell.wav"
                            m "Who is it at this time?"
                            stop sound
                            m "Come in, it's open"
                            scene bme29 with dissolve
                            ca "Good evening"
                            m "Huh"
                            m "Carlos?"
                            m "How did you know my address?"
                            scene bme30 with dissolve
                            m "Elaine!!"
                            e "Hehe yes, I invited them"
                            m "So that's where you get all these guys"
                            m "From work!"
                            e "Let's not keep them waiting, come in guys"
                            scene bme29 with dissolve
                            e "I'll get you drinks"
                            scene bme31 with fade
                            e "{i}(First we get rid of the dress){/i}"
                            m "Yeah... Hahaha"
                            scene bme32 with dissolve
                            e "Here's your drink Karl"
                            scene bme33 with dissolve
                            e "Oh my god [mname]"
                            e "Don't be a prude"
                            scene bme34 with dissolve
                            e "There's no harm in a show for the guys"
                            scene bme35 with dissolve
                            ca "Come on [mname] help her put a nice show"
                            scene bme36 with dissolve
                            "..."
                            scene bme37 with dissolve
                            m "Carlos is mine"
                            e "Let's ask them"
                            scene bme38 with dissolve
                            ca "What do you say Karl?"
                            menu:
                                "Both [mname]":
                                    ka "Let's do [mname]"
                                    ka "We can have Elaine almost any day"
                                    ca "You said it bro"
                                    scene bme39 with dissolve
                                    b "{i}(Cool){/i}"
                                    scene bme40 with dissolve
                                    m "Elaine where do you find such huge dongs?"
                                    e "Hahaha, of course, they work as strippers!"
                                    scene bme41 with dissolve
                                    m "Mmmm"
                                    scene bme42 with dissolve
                                    m "..."
                                    ca "Turn"
                                    scene bme43 with dissolve
                                    m "Ahh Karl!!"
                                    scene bme44 with dissolve
                                    m "AhhH"
                                    scene bme39 with dissolve
                                    b "Nice"
                                    b "{i}(I'll go to Elaine){/i}"
                                    scene bme45 with dissolve
                                    e "..."
                                    scene bme46 with fade
                                    b "Yes baby"
                                    e "Ahh"
                                    scene bme47 with dissolve
                                    "AS YOU FUCK ELAINE"
                                    "YOU DECIDE TO LOOK AT [mname]"
                                    scene bme48 with dissolve
                                    b "{i}(Cool){/i}"
                                    menu:
                                        "Say something to trigger her":
                                            b "Oh Elaine I love your bouncing boobs"
                                            m "..."
                                            scene bme49 with dissolve
                                            e "Yes baby"
                                            m "Enough of me guys, go get Elaine"
                                            scene bme50 with dissolve
                                            m "Enough"
                                            m "My turn, go to your guys"
                                            scene bmea with dissolve
                                            m "You want boobies huh!"
                                            m "..."
                                            m "Mmm"
                                            scene bmeb with dissolve
                                            m "..."
                                            m "Mmm"
                                            m "Oooh"
                                            m "..."
                                            b "Fuck"
                                            b "Give me"
                                            scene bmea with dissolve
                                            m "Ahh"
                                            m "Yes"
                                            m "Let me breastfeed you"
                                            b "Oh god yes"
                                            scene bme51 with dissolve
                                            m "Ahhh"
                                            scene bme52 with fade
                                            b "..."
                                            scene bme53 with dissolve
                                            b "Ahh"
                                            scene bme54 with fade
                                            m "It was a good idea indeed"
                                            scene bme4 with fade
                                            b "What a night"
                                            jump newday

                                        "Continue fucking Elaine":
                                            scene bme49 with dissolve
                                            e "Yes baby"
                                            scene bme55 with fade
                                            b "..."
                                            scene bme56 with dissolve
                                            e "..."
                                            scene bme57 with dissolve
                                            b "Ahh"
                                            scene bme58 with fade
                                            m "...."
                                            scene bme59 with dissolve
                                            e "Ahhh I'm cumming"
                                            scene bme60 with fade
                                            m "It was a good idea indeed"
                                            scene bme4 with fade
                                            b "What a night"
                                            jump newday



                                "I'll have [mname]":
                                    m "Haha I win"
                                    scene bme39 with dissolve
                                    b "{i}(Cool){/i}"
                                    scene bme61 with dissolve
                                    ka "You're going to experience something you've never done"
                                    m "Oh is it?"
                                    ka "Get down on your knees"
                                    scene bme62 with dissolve
                                    m "Mmm"
                                    scene bme63 with dissolve
                                    m "Gag"
                                    ka "get on all four"
                                    scene bme64 with dissolve
                                    m "Ahh slowly please"
                                    scene bme65 with dissolve
                                    m "Ahh"
                                    scene bme66 with dissolve
                                    m "..."
                                    scene bme67 with fade
                                    ka "..."
                                    scene bme69 with dissolve
                                    ka "..."
                                    scene bme68 with dissolve
                                    ka "Ahhh"
                                    scene bme70 with vpunch
                                    m "Mmmm"
                                    scene bme54 with fade
                                    m "It was a good idea indeed"
                                    scene bme71 with dissolve
                                    b "..."
                                    scene bme4 with fade
                                    b "What a night"
                                    jump newday

                            

                        "No":
                            b "No, I don't like it"
                            b "Just bring her here let's have some fun together"
                            e "Ok"
                            e "I'll be back"
                            pass

                
            scene bme4 with fade
            b "..."
            scene bme5 with dissolve
            m "You were expecting us or what!?"
            b "No, not at all"
            m "Why are you naked then?"
            scene bme6 with dissolve
            m "Liar!"
            e "{i}(The cigarette has taken effect quicker than I expected){/i}"
            m "Come Elaine"
            scene bme7a with dissolve
            b "Mmm"
            scene bme8a with dissolve
            m "What do we do with him Elaine?"
            e "Let's fuck him good"
            m "Hmm"
            m "Good idea"
            e "Isn't it!?"
            m "Me first"
            scene bme12a with dissolve
            e "Wait [bname]"
            m "Yes let her align it"
            scene bme13a with dissolve
            e "Mmm"
            scene bme14a with dissolve
            m "Ahhh"
            scene bme15a with dissolve
            e "Oh my god"
            scene bme16a with dissolve
            m "Ohhhh"
            m "Cum inside [bname]"
            if persistent.patch_enabled:
                m "I'll let you do whatever you want! Give it to mommy"
                pass
            else:
                m "I'll let you do whatever you want! Give it to me!"
                pass
            e "Yes [bname] fill her filthy pussy"
            scene bme17 with fade
            b "Come on girls, I want to sleep"
            scene bme17a with fade
            m "So, what do you want honey?"
            b "What do you mean?"
            m "Your reward because you filled me"
            b "Nah I'm spent, next version maybe"
            scene bme4 with fade
            b "What a night"
            jump newday



        "Continue":
            pass
    b "I don't know"
    b "What did [mname] exactly told you"
    e "Ah she keeps on overthinking"
    e "And she's feeling guilty about the whole situation"
    e "She thinks everything happened because of her"
    b "Funny, to me she seems coping very well here"
    e "She's a tough person on the outside"
    e "So what can I do for you while I'm here?"
    b "No, I have everything"
    b "But maybe you can give me a shower?"
    e "Hmm"
    scene bna1a with dissolve
    e "You mean a golden shower?"
    e "Or a real shower?"
    b "The first, whatever that means"
    e "Ah you don't know?"
    b "How the hell would I know?"
    e "You are kidding me"
    b "No I swear"
    e "Ok let me finish my wine and I'll give you one"
    b "We go to my room"
    scene bna3 with fade
    e "Undress yourself"
    e "And lay on the floor"
    b "Just a moment"
    scene bna4a with dissolve
    "..."
    scene bna5a with dissolve
    b "So what now?"
    e "Just wait"
    scene bna6a with dissolve
    b "What the fuck!"
    e "Don't you like?"
    menu:
        "I like but I want something else":
            scene bna7a with dissolve
            e "Take more"
            b "Uhhh"
            pass
        "I don't like, I want something else":
            pass

    scene bna8a with dissolve
    e "We're not going to fuck [bname]"
    e "I don't want to tear your ribs"
    b "But you can still take care of me by other means"
    e "Ok, lay down"
    scene bna9a with dissolve
    e "..."
    scene bna12a with dissolve
    e "..."
    b "Ahh yes, great"
    scene bna13a with dissolve
    b "Ahhh"
    menu:
        "Turn":
            scene bna14b with dissolve
            e "Ah nice"
            scene bna15b with dissolve
            b "Yes"
            e "Slow!"
            b "Stop pretending, you're taking a black cock everyday"
            scene bna16b with dissolve
            e "Ahhh!"
            scene bna15a with fade
            m "Hi honey"
            b "Ah when did you return"
            m "Just now"
            m "Where is Elaine?"
            b "I think in the toilet"
            b "Here she is"
            scene bna16a with dissolve
            m "Elaine, thanks for coming"
            e "Don't kiss me, I was smoking"
            m "It's fine"
            e "I really have to go"
            m "I don't know what happened to her"
            m "I'll be back honey"
            pass

        "Continue":
            scene bna14a with dissolve
            b "Ahh"
            scene bna8a with fade
            b "That was nice, thank you"
            b "Do you want to..."
            e "To what?"
            b "Have a duo with [mname]?"
            e "I don't think she's going to accept now"
            b "Leave it to me"
            e "Ok but make it quick, I need to go early"
            b "I promise"
            scene bme with fade
            m "Hi Elaine, thanks for coming"
            e "My pleasure"
            b "{i}(Hehehe true, my pleasure as well){/i}"
            m "And please, don't smoke inside"
            e "Yeah..."
            m "I'll clean up and come, don't go"
            e "Be quick"
            m "[bname] do we have food?"
            b "Yes, I'll get something for you"
            scene bme1 with fade
            m "Finally!"
            if persistent.patch_enabled:
                b "Mom are you there?"
                pass
            else:
                b "Are you there?"
                pass
            m "Yes honey what do you want?"
            scene toi_m_n3a with dissolve
            b "Err I wanted to ask you..."
            m "Say it [bname]"
            m "You're not shy at all, why do you like to pretend that you are"
            b "Ok you're right, but it's kind of an awkward request"
            b "Can I try with you and Elaine?"
            if mrel >=160:
                m "Go now we will see later"
                scene bme4 with fade
                b "{i}(Dammit! Nothing to do){/i}"
                scene bme2 with dissolve
                m "I'm sorry I got you into this"
                e "It's fine, we just treat him like a customer"
                e "{i}(And there was me thinking I am good at manipulation){/i}"
                e "{i}(This guy can give me lessons){/i}"
                m "When are you going to quit this thing?"
                e "Sorry"
                m "Can I get one?"
                e "Sure"
                m "I'll smoke it and we go see [bname]"
                scene bme3 with dissolve
                m "I won't finish it, too strong"
                e "Hmm"
                m "Let's go"
                scene bme4 with fade
                b "..."
                scene bme5 with dissolve
                m "You were expecting us or what!?"
                b "No, not at all"
                m "Why are you naked then?"
                scene bme6 with dissolve
                $ persistent.unlock_4 =True
                m "Liar!"
                e "{i}(The cigarette has taken effect quicker than I expected){/i}"
                e "{i}(Good that she didn't smoke the whole thing){/i}"
                m "Come Elaine"
                scene bme7 with dissolve
                b "Mmm"
                scene bme8 with dissolve
                m "What do we do with him Elaine?"
                menu:
                    "Let's dominate":
                        scene bme9 with dissolve
                        m "Hmm"
                        scene bme10 with dissolve
                        m "Good idea"
                        e "Isn't it!?"
                        e "Where do we start"
                        menu:
                            "Lick [mname]":
                                scene bmets with fade
                                m "Mmm yes [bname]"
                                e "Oh yes"
                                scene bmets1 with dissolve
                                m "Ahh"
                                m "Slowly on the tongue"
                                m "Sniff my hole first"
                                scene bmets2 with dissolve
                                e "Mmm"
                                m "Yes like a dog!"
                                m "Now you can lick"
                                scene bmets3 with dissolve
                                e "Ahhh"
                                if mrel >=180 and mcorr >= 40:
                                    b "Like a dog you said?"
                                    m "Yes"
                                    scene bmets6 with dissolve
                                    $ persistent.unlock_39 = True
                                    m "Hi yes doggy"
                                    e "Guys come here, you're boring me"
                                    m "Give me a cigarette!"
                                    e "Here come"
                                    b "I'll give you a thick cigarette"
                                    scene bmets7 with dissolve
                                    m "Don't overdo it [bname]"
                                    m "We're just boosting your confidence"
                                    scene bmets8 with dissolve
                                    b "Boost more, I need it"
                                    scene bmets9 with dissolve
                                    e "How does that cigarette feel?"
                                    scene bmets10 with dissolve
                                    m "Mmm"
                                    scene bmets11 with dissolve
                                    m "Ah Elaine"
                                    m "What are you doing?"
                                    scene bmets12 with dissolve
                                    e "Enjoying your ass"
                                    m "It's not the first time my ass gets banged"
                                    m "Come here, give me something to suck on"
                                    b "Wow"
                                    b "{i}(She lost all her inhibitions, if any){/i}"
                                    scene bmets13 with dissolve
                                    b "Oh Dammit"
                                    b "Get on your knees"
                                    pass
                                else:
                                    b "Get on your knees"
                                    "YOU NEED 40 CORRUPTION AND 180 RELATIONSHIP"
                                    pass
                                
                                scene bme24 with fade
                                m "..."
                                scene bmets4 with dissolve
                                m "Gulp"
                                scene bmets5 with dissolve
                                m "Mmmm"
                                scene bme4a with fade
                                b "What a night"
                                b "I'll go to sleep"
                                jump newday

                            "Elaine to fuck [mname] with a strapon":
                                e "What about if I use my strap-on"
                                m "Not now, maybe after his surgery"
                                e "Ok, I'll use it on you then"
                                scene bme19 with dissolve
                                b "Mmm nice"
                                scene bme20 with dissolve
                                b "You girls are fucking hot"
                                scene bme21 with dissolve
                                m "Ahh"
                                scene bme22 with dissolve
                                b "Uhhgh"
                                scene bme23 with dissolve
                                b "..."
                                scene bme24a with fade
                                if persistent.patch_enabled:
                                    m "Give it"
                                    b "What?"
                                    m "[bname] Give it to mommy"
                                    pass
                                else:
                                    m "[bname] Give it to me!"
                                    pass
                                scene bmets4 with dissolve
                                m "Gulp"
                                scene bmets5 with dissolve
                                m "Mmmm"
                                scene bme4a with fade
                                b "What a night"
                                b "I'll go to sleep"
                                jump newday

                    "Let's blow his stick":
                        scene bme9 with dissolve
                        m "Hmm"
                        scene bme10 with dissolve
                        m "Good idea"
                        e "Isn't it!?"
                        scene bme11 with dissolve
                        if binjected ==1:
                            b "Mmm"
                            scene bme12 with dissolve
                            e "Wait [bname]"
                            m "Yes let her align it"
                            scene bme13 with dissolve
                            m "I'm heavy right [bname]"
                            b "{i}(What's wrong with her? She's so talkative){/i}"
                            b "Take this"
                            scene bme14 with dissolve
                            m "Ahh"
                            scene bme15 with dissolve
                            m "Yeaah"
                            scene bme16 with dissolve
                            m "Cum inside [bname]"
                            if persistent.patch_enabled:
                                m "I'll let you do whatever you want! Give it to mommy"
                                pass
                            else:
                                m "I'll let you do whatever you want! Give it to me!"
                                pass
                            e "Yes [bname] fill her filthy pussy"
                            scene bme17 with fade
                            b "Come on girls, I want to sleep"
                            scene bme17a with fade
                            m "So, what do you want honey?"
                            b "What do you mean?"
                            m "Your reward because you filled me"
                            b "Nah I'm spent, next version maybe"
                            scene bme4 with fade
                            b "What a night"
                            jump newday

                        else:
                            b "Ahh"
                            scene bme18 with fade
                            m "Let's go Elaine, he's done"
                            scene bme4 with fade
                            b "{i}(I forgot to inject){/i}"
                            b "{i}(Time to sleep){/i}"
                            jump newday        


            else:
                m sad "No dear, I can't drag Elaine into this"
                "GET 160 RELATIONSHIP POINTS AT LEAST"
                scene bna17b with fade
                b "..."
                pass

    scene bna17a with fade
    b "Can I get you something to drink?"
    m "Yes, wine please"
    scene bna18a with dissolve
    m "So how was your afternoon?"
    b "Normal"
    b "Here's your wine"
    scene bna19a with dissolve
    m "I hope you didn't drink in my absence"
    menu:
        "I had only one drink":
            scene bna20b with dissolve
            m "You did what?"
            m "[bname] you can't drink!"
            b "Sorry I thought it might help with..."
            b "You know, circulation and stuff"
            m "What about your wound?"
            m "Did your little brain down there consider that it may be dangerous for the scar"
            pass
        "No, I'm not feeling well":
            m "Oh good"
            b "I'm still not getting it up"
            m "That again"
            b "Yeah"
            m "All right, I'll finish my glass of wine, and will take a look at it"
            scene bnah0 with dissolve
            m "Undress yourself"
            scene bnah with fade
            b "..."
            m "Kiss me"
            scene bnah1 with dissolve
            m "Mmm"
            scene bnah2 with dissolve
            b "Ah"
            scene bnah3 with dissolve
            m "Mm"
            scene bnah4 with dissolve
            m "Hmm"
            scene bnah5 with dissolve
            b "Oh yes"
            scene bnah6 with dissolve
            b "Ahhh"
            if day ==2:
                play sound "sounds/mobilering.wav"
                m "Huh!"
                scene bnah7 with dissolve
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
                scene bna21d with dissolve
                m "Wanda and Joshua are coming to visit us"
                m "Now if you want her to let him come visit you, then you behave, clear?!"
                scene black
                "..."
                jump wandavisit

            elif day ==4:
                play sound "sounds/mobilering.wav"
                m "Huh!"
                scene bnah7 with dissolve
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
                scene bna21d with dissolve
                m "Wanda and Joshua are coming to visit us"
                m "Now if you want her to let him come visit you, then you behave, clear?!"
                scene black
                "..."
                jump wandavisit

            else:
                scene bnah6a with dissolve
                b "Ahh yeah!"
                m "Mmm"
                scene bnah8 with fade
                pass

    m "I'm so tired, I will go to bed"
    b "Good night"
    jump newday
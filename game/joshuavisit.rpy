


label joshuavisit:
    scene joshuacall with fade
    j "Hi [bname]"
    j "Err I don't... I don't know"
    j "Hold on"
    w "Who is it?"
    j "It's [bname]"
    scene joshuacall1 with dissolve
    w "Hi [bname] it's Wanda"
    w "Joshua is busy at home"
    if wandaride ==1:
        w "If you like, you can come and visit him"
        b "Oh that's great, I'll change and come"
        w "No, I'll go and get you"
        w "Remember I promised you a ride"
        b "Cool"
        scene black
        "..."
        scene jpool0 with fade
        w "Hey [bname]"
        w "Get in"
        scene jpool00 with dissolve
        "..."
        scene jpool00_ with dissolve
        "..."
        scene jpool000_ with dissolve
        b "{i}(Holy crap){/i}"
        scene jpool0000 with dissolve
        b "{i}(Mmm when, just when I get to fuck this beauty){/i}"
        b "{i}(Don't complain [bname]){/i}"
        b "{i}(Things are better than ever with her){/i}"
        jump joshuapool
    elif wsusp <5:
        w "But if you like, you can come and visit him"
        b "Oh that's great, I'll change and come"
        jump joshuapool
    else:
        w "Sorry for that"
        "YOU NEED TO MAKE HER SUSPICIONS DROP BELOW 5 TO MAKE HER ACCEPT"
        pass
    b "Ok thanks"
    b "{i}(What a woman!){/i}"
    b "{i}(Who to call instead?){/i}"
    menu:
        "Call Elaine":
            jump elainebs

        "Cheryl":
            jump cherylbs

        "The neighbors?":
            jump neighbs


label joshuapool:
    scene jpool with fade
    b "..."
    if wandaride ==1:
        scene jpool01 with dissolve
        pass
    else:
        scene jpool1 with dissolve
        w "Hi [bname]"
        pass
    w "Joshua take him to your room"
    w "Or you can use the pool if you want"
    w "Joshua can give you swimming shorts if you want"
    w "But [bname] you can't swim correct?"
    if bandageremove ==1:
        b "I can, I already removed the bandage"
    else:
        b "Yes, I can just sit in the sun"
        pass
    w "Ok good"
    scene jpool2 with dissolve
    b "So what's next?"
    j "We swim"
    if bandageremove ==1:
        b "You can do it alone if you want"
        b "I'm not in the mood"
    else:
        b "Duhh! I can't swim"
        pass
    
    "..."
    menu:
        "Ask if he has taken some action" if joshjaneyphotos ==0:
            b "So!"
            b "Did you get me something?"
            j "What do you mean?"
            b "I mean I always show you photos"
            b "And you never get me something in return"
            b "Looks like you're taking advantage of me"
            j "But it's not easy for me"
            b "What's not easy? Getting some photos in the toilet?"
            b "Or from the bedroom window?"
            j "Ok Ok don't be angry"
            j "I will try"
            $ joshjaneyphotos = 1
            b "Alright, I'll wait"
            b "You will show me next time"
            pass

        "Go to the toilet*" if bmljosh == 1:
            scene jpool3 with fade
            w "I've brought you soda and lemonade"
            j "Thanks mom"
            w "Josh, I'll be in the gym room if you need me"
            scene jpool4 with dissolve
            b "This soda is real pain in the ass"
            j "Is it?"
            b "I need to use the toilet"
            j "You're lucky, I am not allowed to drink"
            j "Except on some occasions"
            b "Ah and I've always wondered why you take the lemonade"
            b "Anyway, I need to pee"
            j "I'll come with you"
            b "There's no need I know where it is"
            b "Oh come on"
            j "I'm sorry I can't"
            if sleepingpills == 0:
                b "{i}(I can threaten him by showing the photos I took when he was doing [mname]){/i}"
                b "{i}(But I'd rather keep them for something more important){/i}"
                if bandageremove ==1:
                    scene jpool10a with fade
                    j "It's up here"
                    scene jpool11a with dissolve
                    b "Hmm"
                    pass
                else:
                    scene jpool10 with fade
                    j "It's up here"
                    scene jpool11 with dissolve
                    b "{i}(She changed back to this?){/i}"
                    pass

                b "Hey listen, let's go  by the balcony"
                j "No no!"
                j "That's really trouble"
                b "Follow me"
                scene jpool49 with fade
                j "[bname] please!!!"
                b "Shhh"
                scene jpool32 with dissolve
                b "Come here"
                scene jpool33 with dissolve
                j "We got to leave [bname] this is risky"
                b "Come here take a look at this hot ass"
                scene jpool34 with dissolve
                j "..."
                j "Please we need to get back to the pool"
                scene jpool16 with fade
                b "What a chicken!"
                b "{i}(Next time I will use some arm twisting){/i}"
                b "Alright it's time to go"
                scene jpool48 with fade
                b "{i}(I'll use some intimidation and threating to show the photos I've got){/i}"
                b "{i}(But first I need to buy something){/i}"
                scene black
                "LATER ON"
                scene broom_camera1 with fade
                menu:
                    "Buy sleeping pills to use on Wanda":
                        b "I'm sorry but this woman needs to be put to sleep in order to loosen her prig brain"
                        if mny >= 50:
                            b "Done!"
                            $ sleepingpills = 1
                            b "Oh boy, these are too strong"
                            b "It's name is scary, stillknocks"
                            b "Knocks the hell out of you"
                            b "Let's go see who's around"
                            jump waitform
                        else:
                            b "Damn, I don't have $50"
                            b "Another time maybe"
                            b "Let's go see who's around"
                            b "Tomorrow I can ask [sname] to lend me some"
                            jump waitform
                    "Don't buy":
                        jump waitform

            else:
                b ang "You wanna come with me! Fine!"
                b "But there's something you need to see before we go"
                j "Cool"
                scene jpool22e with dissolve
                j "Oh"
                b "You got it right!"
                b "That's your photo fucking [mname]"
                scene jpool16 with dissolve
                b "So! Are you gonna do what I tell you?"
                b "Or I show these photos to Wanda!"
                j "..."
                b "I'll put some pills in your lemonade"
                b "You take it and tell Wanda it tastes bitter"
                b "Knowing her, I assume she's going to taste it"
                b "And you come back here"
                b "We wait for some time, and then we go inside"
                scene jpool22f with fade
                b "Fucking huge house"
                b "Here he comes"
                scene jpool18 with dissolve
                b "So?"
                j "She said probably from the lemons some of them are bitter by nature"
                j "And said, she's going to prepare another fresh one for me"
                b "What the hell I don't care about all this"
                b "Did she taste it?"
                j "Yes she did"
                j "Is it enough?"
                b "I put 3 pills in that"
                b "One or two sips are more than enough"
                j "Oh here she comes"
                scene jpool3c with dissolve
                w "Honey, here's your lemonade"
                w "That should be good"
                scene jpool3d with dissolve
                w "God, I'm so sleepy,I'll go to sleep, I started to hallucinate"
                w "Take it Josh, I'll go have a short nap"
                scene jpool22b with fade
                b "Now is the time"
                menu:
                    "Take him with you":
                        jump wandasleeping
                    "Go alone":
                        scene jpool6b with dissolve
                        b "I'll be back"
                        jump wandasleepingalone


        "Chill and talk":
            pass
    scene jpool3 with fade
    w "Joshua I'll be in the study room"
    w "I've brought you soda and lemonade"
    j "Thanks mom"
    if colaspike >=2:
        scene jpool3a with dissolve
        pass
    else:
        pass
    w "[bname], next time you can bring [sname] with you"
    b "Ah, I'm not sure, she's always busy"
    b "But I'll tell her"
    b "{i}(I wish she accepts){/i}"
    if colaspike >=2:
        scene jpool4a with dissolve
        b "Thanks for the drinks"
        w "You're welcome dear"
        b "{i}(What a hot ass){/i}"
        pass
    else:
        pass
    scene jpool4 with dissolve
    j "So, what did you want to tell me?"
    b "About what?"
    j "Last time you were saying something about girls"
    b "Well..."
    if joshjaneyphotos >=3 and day==2:
        scene jpool5 with dissolve
        b "{i}(Here's the retard){/i}"
        b "Here's Janey"
        b "Anything new for her?"
        scene jpool6 with dissolve
        j "What do you mean?"
        b "{i}(What's gotten into him?){/i}"
        b "I mean photos"
        j "Nothing so far"
        b "Ahh ok"
        b "Where did she go?"
        scene jpool4 with dissolve
        j "She's always like that"
        scene jpool3b with dissolve
        w "Joshua, can you come please"
        scene jpool4b with dissolve
        w "I have a night out"
        w "Make sure [bname] leaves soon"
        j "Okay"
        w "Ursula is watching Janey"
        j "Okay"
        w "And behave"
        j "Understood"
        scene jpool20 with dissolve
        b "What was it about?"
        j "She said she has to go out"
        j "Probably one of her  community nights"
        b "What's that?"
        j "She says she do public service"
        j "She takes a full bag of clothes with her"
        b "I hear you"
        j "She says she distributes it to the needy"
        b "Go on..."
        j "That's all"
        b "Okay, what can we do now?"
        j "I don't know, but you can't stay late"
        b "Did she say that?"
        j "Yes"
        b "Mm, maybe you can call Janey then?"
        j "No, not possible, I'm sorry"
        b "Ok I'm going to swim"
        scene jpool43 with dissolve
        j "I'll swim too"
        ja "Hey"
        scene jpool44 with dissolve
        ja "Can I swim with you?"
        scene jpool45 with dissolve
        j "No Janey!"
        j "Where is Ursula?"
        ja "She's on the phone"
        j "Please go, you can't swim with us"
        ja "Why not?"
        scene jpool46 with dissolve
        ja "We can do what we did the other day?"
        j "..."
        scene jpool47 with dissolve
        j "Huh!"
        j "No!! Go now!"
        b "{i}(Interesting){/i}"
        scene jpool4 with fade
        "YOU SPEND THE REST OF THE TIME"
        "WITH JOSHUA BARELY SPEAKING"
        b "It's time I go"
        scene jpool48 with fade
        b "{i}(I should check the camera thoroughly){/i}"
        b "{i}(There's clearly something fishy){/i}"
        jump waitform

    elif joshjaneyphotos >=3 and day==4:
        scene jpool5 with dissolve
        b "{i}(Here's the retard){/i}"
        b "Here's Janey"
        b "Anything new for her?"
        scene jpool6 with dissolve
        j "What do you mean?"
        b "{i}(What's gotten into him?){/i}"
        b "I mean photos"
        j "Nothing so far"
        b "Ahh ok"
        b "Where did she go?"
        scene jpool4 with dissolve
        j "She's always like that"
        scene jpool3b with dissolve
        w "Joshua, can you come please"
        scene jpool4b with dissolve
        w "I have a night out"
        w "Make sure [bname] leaves soon"
        j "Okay"
        w "Ursula is watching Janey"
        j "Okay"
        w "And behave"
        j "Understood"
        scene jpool20 with dissolve
        b "What was it about?"
        j "She said she has to go out"
        j "Probably one of her  community nights"
        b "What's that?"
        j "She says she do public service"
        j "She takes a full bag of clothes with her"
        b "I hear you"
        j "She says she distributes it to the needy"
        b "Go on..."
        j "That's all"
        b "Okay, what can we do now?"
        j "I don't know, but you can't stay late"
        b "Did she say that?"
        j "Yes"
        b "Mm, maybe you can call Janey then?"
        j "No, not possible, I'm sorry"
        b "Ok I'm going to swim"
        scene jpool43 with dissolve
        j "I'll swim too"
        ja "Hey"
        scene jpool44 with dissolve
        ja "Can I swim with you?"
        scene jpool45 with dissolve
        j "No Janey!"
        j "Where is Ursula?"
        ja "She's on the phone"
        j "Please go, you can't swim with us"
        ja "Why not?"
        scene jpool46 with dissolve
        ja "We can do what we did the other day?"
        j "..."
        scene jpool47 with dissolve
        j "Huh!"
        j "No!! Go now!"
        b "{i}(Interesting){/i}"
        scene jpool4 with fade
        "YOU SPEND THE REST OF THE TIME"
        "WITH JOSHUA BARELY SPEAKING"
        b "It's time I go"
        scene jpool48 with fade
        b "{i}(I should check the camera thoroughly){/i}"
        b "{i}(There's clearly something fishy){/i}"
        jump waitform

    else:
        scene jpool5 with dissolve
        b "{i}(What is she doing there?){/i}"
        b "{i}(She looks like a retard){/i}"
        j "Oh that's Janey"
        b "{i}(Oh so that's her name){/i}"
        menu:
            "Say hi":
                b "Hi Janey"
                scene jpool5a with dissolve
                ja "..."
                scene jpool6a with dissolve
                b "Hello I'm [bname]"
                ja "Hmm"
                scene jpool4 with dissolve
                b "What's wrong with her?"
                j "Let her be"
                j "What were you saying?"

            "No need":
                scene jpool4 with dissolve
                pass
                
    
    b "My point was is if you keep living like that you will never get a girlfriend"
    j "Yes I guess I'm doomed"
    j "What would you do, if you were in my place?"
    b "I would start learning with janey"
    j "Learn what?"
    b "Stuff... What do girls like..."
    b "Ask her questions"
    b "Practice kissing, learn about their physical needs..."
    j "Nah, out of question, Janey is..."
    b "Is what?"
    j "Nevermind, it's not going to work with Janey"
    b "Then you're left with one choice"
    b "Ms. Wanda"
    scene jpool6 with dissolve
    j "Eww!!"
    b "What Eww?"
    j "Besides ewww, if I ask her about this stuff!"
    j "She's going to kill me point blank"
    b "Then let her allow you to go out on your own"
    j "She's too strict, I need to figure out other ways"
    b "I'll think about new ideas for next time"
    if sjosh>=2:
        b "By the way"
        scene jpool4 with dissolve
        b "How was [sname] panty"
        j "It is ok, I'm keeping it in my room"
        b "But... Let me ask you"
        b "What did you do with it?"
        j "Nothing, I just hid under my bed"
        scene jpool9 with dissolve
        b "What!!?"
        b "You mean you didn't masturbate using it?"
        b "Or even sniff it?"
        j "No, why would I do that?"
        b "Oh God"
        b "Guys use the scent of girls to be turned on"
        scene jpool4 with dissolve
        $ persistent.unlock_11 = True
        b "I need to use the restroom"
        if joshuatoilet ==0:
            b "Is it on this level?"
            $ joshuatoilet += 1
            j "I'll come with you"
            scene jpool10 with fade
            j "It's up here"
            scene jpool11 with dissolve
            b "{i}(She changed back to this?){/i}"
            pass

        elif joshuatoilet >=3:
            j "I'll come with you"
            b "There's no need, I know where it is"
            if colaspike ==2:
                b "I mean... when you're at my place"
                b "I let you go alone, so what's the big deal"
                $ colaspike = 3
                j "No, I have to"
                b "{i}(I'll teach him a lesson){/i}"
                pass
            elif colaspike ==4:
                b "Oh I almost forgot"
                scene jpool20 with dissolve
                b "There's something I want to show you"
                scene jpool21 with dissolve
                j "Show me"
                b "{i}(Great he took the bait){/i}"
                b "Get hold of yourself"
                b "{i}(I need to give him more hints){/i}"
                b "Let me find them, there are photos that I can't show"
                scene jpool22 with dissolve
                b "Here"
                j "Oh"
                b "Damn, I really need to use the toilet"
                b "Here take the phone"
                scene jpool23 with dissolve
                b "Don't go to the favorites folder please"
                scene jpool24 with fade
                b "{i}(Where to now?){/i}"
                menu:
                    "Check the gym":
                        $ persistent.unlock_24 = True
                        scene jpool13 with dissolve
                        b "..."
                        scene jpool25 with dissolve
                        b "Wow"
                        scene jpool26 with dissolve
                        b "..."
                        scene jpool27 with dissolve
                        w "[bname]!!"
                        w "What are you doing here?"
                        b "Sorry I lost my way"
                        w "Where is Joshua?!"
                        b "I lost him on the stairs"
                        scene jpool28 with dissolve
                        w "It's fine, get back to the pool please"
                        scene jpool29 with fade
                        j "Cool!"
                        b "So how is it?"
                        scene jpool30 with dissolve
                        j "Awesome"
                        menu:
                            "Ask him if he'd like to join you in the gym" if wandagym <1:
                                b "You look so skinny man"
                                $ wandagym = 1
                                b "Why don't we workout together?"
                                b "I need to lose some weight, and you'll get the motivation"
                                scene jpool18 with dissolve
                                j "I don't like the gym, I just do it sometimes because my mom pushes me to"
                                b "Ah... Alright"
                                b "It's time to go"
                                scene jpool8 with fade
                                j "Bye, see you"
                                scene jpool19 with dissolve
                                w "Get inside! You have some explanation to do"
                                $ joshvisitpool = 1
                                jump waitform

                            "Time to go":
                                scene jpool18 with dissolve
                                b "Ah... Alright"
                                b "It's time to go"
                                scene jpool8 with fade
                                j "Bye, see you"
                                scene jpool19 with dissolve
                                w "Get inside! You have some explanation to do"
                                $ joshvisitpool = 1
                                jump waitform


                    "Check the rooms":
                        b "{i}(Let's see where the rooms are){/i}"
                        scene jpool31 with fade
                        b "Hmmm"
                        scene jpool32 with dissolve
                        b "Wow"
                        scene jpool33 with dissolve
                        b "{i}(Fucking great, she's changing){/i}"
                        menu:
                            "Continue 'Risky'":
                                scene jpool34 with dissolve
                                $ persistent.unlock_32 = True
                                b "{i}(Oh boy){/i}"
                                scene jpool35 with dissolve
                                b "{i}(What a hot woman){/i}"
                                menu:
                                    "Continue":
                                        scene jpool36 with dissolve
                                        b "Mmm"
                                        scene jpool37 with dissolve
                                        b "{i}(Oh wow!){/i}"
                                        b "What the fuck!"
                                        scene jpool38 with dissolve
                                        ja "Blerrr"
                                        menu:
                                            "Run":
                                                $ wsusp += 10
                                                show screen wsuspup
                                                scene jpool39 with dissolve
                                                w "{i}(What was that?){/i}"
                                                hide screen wsuspup
                                                w "Janey?!"
                                                pass
                                            "Talk to her" if janeyseduction == 0:
                                                $ persistent.unlock_50 = True
                                                scene jpool40 with dissolve
                                                b "Hey what?"
                                                b "I lost my way"
                                                $ janeyseduction = 1
                                                ja "Boo"
                                                b "You know! You're cute"
                                                ja "Thank you"
                                                scene jpool41 with dissolve
                                                b "Hehehe"
                                                pass
                                    "Leave":
                                        pass
                                
                            "Go back to Joshua":
                                pass
                        scene jpool29 with fade
                        j "Cool!"
                        b "So how is it?"
                        scene jpool30 with dissolve
                        j "Awesome"
                        menu:
                            "Ask him if he'd like to join you in the gym" if wandagym <1:
                                b "You look so skinny man"
                                $ wandagym = 1
                                b "Why don't we workout together?"
                                b "I need to lose some weight, and you'll get the motivation"
                                scene jpool18 with dissolve
                                j "I don't like the gym, I just do it sometimes because my mom pushes me to"
                                b "Ah... Alright"
                                b "It's time to go"
                                scene jpool8 with fade
                                j "Bye, see you"
                                scene jpool19 with dissolve
                                w "Get inside! You have some explanation to do"
                                $ joshvisitpool = 1
                                jump waitform

                            "Talk about Janey" if janeyseduction >=1 and janeyseduction <=2:
                                b "Emm"
                                b "I just met Janey on my way back here"
                                b "You know, she's cute"
                                b "Have you ever thought..."
                                b "Of spying on her?"
                                scene jpool42 with dissolve
                                $ janeyseduction = 2
                                j "Huh!"
                                j "What?"
                                b "Nevermind"
                                b "Time to go"
                                scene jpool8 with fade
                                j "Bye, see you"
                                b "{i}(I have to find a way to make him take pictures of his mom or sister){/i}"
                                scene jpool19 with dissolve
                                w "Get inside! You have some explanation to do"
                                $ joshvisitpool = 1
                                jump waitform

                            "Time to go":
                                scene jpool18 with dissolve
                                b "Ah... Alright"
                                b "It's time to go"
                                scene jpool8 with fade
                                j "Bye, see you"
                                scene jpool19 with dissolve
                                w "Get inside! You have some explanation to do"
                                $ joshvisitpool = 1
                                jump waitform

                    "Go back to Joshua and show some photos" if josh_r_photos >=1:
                        scene jpool29 with fade
                        $ persistent.unlock_44 = True
                        j "Cool!"
                        b "So how is it?"
                        scene jpool30 with dissolve
                        j "Awesome"
                        b "Do you want to see more photos?"
                        j "Do you have?"
                        b "yes"
                        scene jpool22a with dissolve
                        j "Who's that?"
                        b "[mname]"
                        j "How can you take such photos?"
                        scene jpool22b with dissolve
                        b "Err I found it in her mobile"
                        b "Here's one more"
                        scene jpool22c with dissolve
                        j "Wow"
                        b "Yeah"
                        b "And here is [sname]"
                        scene jpool22d
                        menu:
                            "Continue":
                                scene jpool18 with dissolve
                                b "Alright, time to go"
                                scene jpool8 with fade
                                j "Bye, see you"
                                scene jpool19 with dissolve
                                w "Get inside! You have some explanation to do"
                                $ joshvisitpool = 1
                                jump waitform

                        

            else:
                j "No, I have to"
                pass
            
            b "Alright fine"
            $ joshuatoilet += 1
            scene jpool10 with fade
            b "..."
            scene jpool11 with dissolve
            b "{i}(Maybe she told him to stay with me all times?){/i}"
            b "{i}(Could be...){/i}"
            b "{i}(I need to find a way to come alone){/i}"
            scene black
            "..."
            scene jpool12 with fade
            b "You know even though your house is big"
            b "But I started to know my way around"
            j "Yes, it's big"
            menu:
                "Pretend to have lost your way":
                    scene jpool13 with dissolve
                    $ persistent.unlock_18 = True
                    b "{i}(Hmm let's see where this door goes){/i}"
                    scene jpool14 with dissolve
                    b "Wow"
                    scene jpool14a with dissolve
                    b "{i}(Hot!!!){/i}"
                    scene jpool15 with dissolve
                    w "[bname]!! What are you doing here?"
                    w "Where is Joshua?!"
                    b "Sorry I lost my way"
                    b "He brought me to the toilet and I lost him"
                    b "I'm sorry, I'll get out of here"
                    w "Ground floor"
                    b "Ok, sorry"
                    scene jpool17 with dissolve
                    b "{i}(To hell with this place, it's so big){/i}"
                    b "{i}(Wait a minute, if she's into working out){/i}"
                    b "{i}(Maybe we can workout together){/i}"
                    scene jpool16 with fade
                    b "Sorry I lost you"
                    b "It took me sometime to find my way out"
                    j "Where did you go?"
                    b "No where, just lost my way on the stairs"
                    menu:
                        "Ask him if he'd like to join you in the gym" if wandagym <1:
                            b "You look so skinny man"
                            $ wandagym = 1
                            b "Why don't we workout together?"
                            b "I need to lose some weight, and you'll get the motivation"
                            scene jpool18 with dissolve
                            j "I don't like the gym, I just do it sometimes because my mom pushes me to"
                            b "Ah... Alright"
                            b "It's time to go"
                            scene jpool8 with fade
                            j "Bye, see you"
                            scene jpool19 with dissolve
                            w "Get inside! You have some serious explanation to do"
                            $ joshvisitpool = 1
                            jump waitform

                        "Continue":
                            pass

                "Continue following him":
                    pass

        else:
            j "I'll come with you"
            b "There's no need, I know where it is"
            j "No, I have to"
            $ joshuatoilet += 1
            scene jpool10 with fade
            b "..."
            scene jpool11 with dissolve
            b "{i}(Maybe she told him to stay with me all times?){/i}"
            b "{i}(Could be...){/i}"
            b "{i}(I need to find a way to come alone){/i}"
            pass



    else:
        pass
    
    
    scene black
    "..."
    scene jpool7 with fade
    m "I don't know, let me think about it"
    m "I'll decide and get the papers ready"
    scene black
    "..."
    scene jpool8 with fade
    j "..."
    $ joshvisitpool = 1
    jump waitform

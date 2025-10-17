

label waitform:
    scene black
    "LATER AT NIGHT"
    if mellastrequest ==3:
        scene bmdinner0 with dissolve
        menu:
            "Call Melinda to arrange dinner reservation":
                scene melcall with fade
                $ mellastrequest = 4
                ml "Hi [bname]"
                ml "Yes I can now"
                ml "I'll send you the restaurant address but don't leave soon"
                ml "I'll send a gift in your name"
                "..."
                ml "Bye"
                scene black
                "..."
                scene bna15a with fade
                m "Hi honey"
                b "Hi, how was your evening"
                m "I'll be right back"
                scene bna17a with fade
                b "Why did you change, I did a reservation to a restaurant"
                m "Oh really?"
                m "I'm not in the mood"
                b "We'll see for that"
                b "Can I get you something to drink?"
                m "Yes, wine please"
                scene bna18a with dissolve
                m "So how was your afternoon?"
                play sound "sounds/doorbell.wav"
                b "Huh"
                m "Who's that?"
                b "Open"
                stop sound
                m "I'll open that"
                $ escortrequest = 2
                scene bmanipulate with dissolve
                m "Oh!"
                scene bmdinner00 with dissolve
                m "[bname] how can you afford a D'or handbag!?"
                b "Happy!?"
                m "Of course I am happy"
                m "But even me with all the money I'm making"
                m "I can't throw $5000 on a bag"
                b "I saved from the repair work I'm doing during the day"
                b "Maybe you don't like it?"
                m "Of course I do"
                m "Now I'm in the mood to go for a dinner"
                m "I'll go get ready"
                m "Meanwhile you go dress up"
                m "I need some time to fix and change my hair"
                b "We can't be so late for the reservation"
                m "Stop complaining, do you want to see me in a new hair or not?"
                b "Yes I do"
                m "Then go start, and wait for me"
                jump bmdnr

                
            "No need, just wait for [mname] and do something else":
                pass
    else:
        pass
    if jenvisitmasquerade >= 2 :
        $ jenvisitmasquerade = 3
        scene myt6 with fade
        b "Whoa! Nice uniform"
        b "Let's have some fun"
        s "Sorry mister, this is not for you"
        s "I'm going out"
        b "I can come with you"
        scene myt7 with dissolve
        s "No civilian person, not allowed"
        b "What the fuck, I'll just follow you"
        s "They won't let you in, you need a pass"
        b "A pass you said!? Hmm Ok"
        s "Bye"
        b "{i}(Hmmm){/i}"
        scene smas73 with fade
        w "Here she is"
        scene smas74 with dissolve
        w "Look to your left!"
        scene smas75 with fade
        m "Huh!"
        scene smas76 with fade
        w "You don't want to confront her?"
        m "No, I want to know what brought her here"
        m "Oh Wanda..."
        m "Where did I go wrong with this family"
        w "Easy babe"
        w "She's a grown up, she can decide for herself"
        scene smas77 with dissolve
        m "{i}(I wonder if [bname] has something to do with this, he kept asking me to allow her){/i}"
        scene smas78 with dissolve
        "Hey who's your little friend baby"
        w "Hi honey..."
        w "Where's Eva?"
        "She left"
        "Won't you introduce me to your friend?"
        scene smas79 with dissolve
        w "Ah so what's your name?"
        m "Kelly"
        scene smas80 with dissolve
        "You're so beautiful Kelly"
        scene smas81 with dissolve
        w "Honey! My rules! It's either you and me"
        w "Or me and her"
        menu:
            "You and her":
                scene smas81 with dissolve
                w "Ready to pleasure me?"
                m "Yes mistress"
                m "Let me take my suit away"
                scene smas82 with dissolve
                w "..."
                scene smas83 with dissolve
                w "Ahhh"
                "Enough Wanda"
                "My time now"
                $ persistent.unlock_84 = True
                scene mwp with fade
                "Ahh"
                "..."
                w "Yes baby"
                "Ahh"
                "...."
                pass

            "Me and you":
                scene wpm00 with fade
                w "Ahh"
                scene wpm02 with dissolve
                w "Oh my God, that's hot"
                scene wpm16 with dissolve
                w "You're seeing this kelly?"
                scene wpm21 with dissolve
                m "Ahhh"
                "..."
                pass

        scene black
        "LATER ON"
        scene bna15a with fade
        m "Hi honey"
        b "Oh finally"
        m "I'm sorry I left you alone"
        m "I'll be back"
        scene bna17a with fade
        b "Can I get you something to drink?"
        m "Yes, wine please"
        scene bna18a with dissolve
        m "So how was your afternoon?"
        b "Normal"
        b "Here's your wine"
        scene bna19a with dissolve
        b "I have a request"
        m "What is it?"
        menu:
            "Can you, give me a shower?":
                m "Sure baby, Let's go"
                b "Finish your wine first"
                m "I'll continue later, let it aerate, better"
                scene jdm3_37a with fade
                b "Again"
                scene jdm3_38a with dissolve
                m "Just relax baby"
                scene jdm3_39a with dissolve
                m "We don't want this small peenie weenie to get wet"
                b "Hey"
                scene jdm3_40 with dissolve
                m "Hahaha"
                b "Please stop it"
                b "It's not true"
                scene jdm3_41 with dissolve
                m "I'm sorry"
                m "We're done"
                scene jdm3_42 with dissolve
                m "How does my big boy feel now"
                b "{i}(Damn, such times make me feel shit){/i}"
                b "{i}(The way I think about her){/i}"
                b "{i}(All the evil thoughts){/i}"
                m "Why silent all of a sudden"
                b "Nothing, I was thinking how ungrateful I am"
                b "Thank you so much"
                scene jdm3_50 with dissolve
                "..."
                scene jdm3_50a with dissolve
                "..."
                scene jdm3_50b with dissolve
                b "Mmm"
                scene jdm3_50c with dissolve
                m "Ahh"
                scene jdm3_51a with dissolve
                m "Mmm"
                scene jdm3_52a with dissolve
                b "Mm"
                scene jdm3_53a with dissolve
                m "Mghhm"
                scene jdm3_54a with dissolve
                m "..."
                scene jdm3_55a with dissolve
                m "..."
                scene jdm3_56a with vpunch
                m "Aggh"
                scene jdm3_57a with fade
                m "I'm so tired, I will go to bed"
                b "Good night"
                jump newday
                
    elif askcherylforhelp ==2 and jendidgo ==1:
        $ jenvisitmasquerade = 1
        $ persistent.unlock_79 = True
        scene myt6 with fade
        b "Whoa! Nice uniform"
        b "Let's have some fun"
        s "Sorry mister, this is not for you"
        s "I'm going out"
        b "I can come with you"
        scene myt7 with dissolve
        s "No civilian person, not allowed"
        b "What the fuck, I'll just follow you"
        s "They won't let you in, you need a pass"
        b "A pass you said!? Hmm Ok"
        s "Bye"
        scene smas with fade
        b "{i}(Interesting place){/i}"
        b "{i}(Glad that Cheryl got me this pass){/i}"
        scene smas1 with dissolve
        s "[bname]! What are you doing here?"
        scene smas2 with dissolve
        b "I told you I will come"
        scene smas3 with dissolve
        s "Come with me"
        scene smas4 with fade
        "I don't want to come here anymore"
        "Enough! Tell your friend to chaperone his wife if he's so protective of her"
        "I don't like this whole thing"
        scene smas5 with dissolve
        "Ok just calm down"
        "I'll take care of it"
        "You just calm down and don't make a scene"
        scene smas4 with dissolve
        "I'm out"
        scene smas6 with fade
        s "[bname] why did you come?"
        s "You can't be here those are not your average people to hang out with"
        s "It's really dangerous"
        s "They are all big guns"
        b "So what! I'm a big gun too"
        scene smas7 with dissolve
        s "Stay here and don't mix up with people"
        s "Ok!"
        b "Huh"
        menu:
            "Follow [sname]":
                scene smas8 with dissolve
                b "{i}(I'll follow [sname]){/i}"
                scene smasq13b with dissolve
                b "{i}(Nice){/i}"
                scene smasq13 with fade
                s "Mmm"
                scene smasq14 with dissolve
                "..."
                scene smasq15 with dissolve
                "..."
                scene smasq19 with dissolve
                "..."
                scene smasq16 with dissolve
                "..."
                scene smasq17 with dissolve
                "..."
                scene smasq18 with dissolve
                "Hey do you care to swap?"
                "No, I don't you can both do the young girl"
                scene smasq20b with dissolve
                "I know you prefer her bastard"
                "I'm out"
                scene smas63 with fade
                "Who are you!"
                b "I was just watching"
                "You men are full of shit"
                b "Hey that's so unfair"
                play sound "sounds/mobilering.wav"
                b "Huh"
                scene smas64 with dissolve
                b "{i}([mname]){/i}"
                menu:
                    "Take the call":
                        stop sound
                        jump smasw
                    "Ignore it":
                        stop sound
                        "Let me guess"
                        "Your mom"
                        scene smas65 with dissolve
                        b "How did you..."
                        b "No, not my mom"
                        b "Yes"
                        scene smas66 with dissolve
                        "Not your mom huh!"
                        scene smas67 with dissolve
                        "Mmm"
                        scene smas68 with vpunch
                        "..."
                        scene smas69 with dissolve
                        b "Oh god, nice"
                        "Sit on the bed, I'll give you an amazing experience"
                        scene smasbbj02 with dissolve
                        b "Ahh"
                        scene smasbbj04 with dissolve
                        "..."
                        b "Yes"
                        scene smasbbj09 with dissolve
                        b "Fucking nice"
                        "..."
                        scene smas70 with dissolve
                        "I can feel it throbbing"
                        scene smas71 with dissolve
                        "..."
                        scene smas72 with dissolve
                        b "Oh yes!"
                        scene smas8 with fade
                        b "That was awesome"
                        scene mclub8 with fade
                        b "{i}(I wonder what [mname] wanted){/i}"
                        scene mclub7 with dissolve
                        m "Hey sweetheart"
                        b "Hey"
                        b "Sorry I couldn't answer your call, I was out and the music was loud"
                        m "No worries"
                        m "Wanda wanted to see if I'm home"
                        m "I'm so tired, I will go to sleep early"
                        b "Ah alright, sweet dreams"
                        jump newday
                        
                
            "Stay around":
                scene smas8 with fade
                b "{i}(What to do now?){/i}"
                jump smasw

    if masqueradeaccepted ==0 and askcherylforhelp <2:
        $ askcherylforhelp = 1
        scene smasquerade with fade
        b "Huh! What is this?"
        s "..."
        scene smasquerade1 with dissolve
        s "Secret!"
        b "Is this a kind of party?"
        s "I won't tell you?"
        s "Good night, I'm returning late"
        scene smasquerade2 with dissolve
        b "Huh! She left?"
        b "{i}(Is this, the masquerade thing?){/i}"
        b "{i}(But [mname] didn't approve this){/i}"
        b "Whatever!"
        b "{i}(I SHOULD INVITE CHERYL AND ASK HER FOR HELP TOMORROW){/i}"
        scene bna15a with fade
        m "Hi honey"
        b "Oh finally"
        m "I'm sorry I left you alone"
        m "I'll be back"
        scene black
        "MEANWHILE"
        scene smasq with fade
        "MUSIC"
        "CHATTER"
        scene smasq1 with dissolve
        s "So you won't show your face"
        scene smasq2 with dissolve
        "No, the rules are if you want you can"
        "But if not, it's your right to keep masks on"
        s "Ok"
        "Shall we go?"
        scene smasq3 with dissolve
        "Yeah true"
        "Are you married?"
        "No"
        scene smasq4 with dissolve
        "..."
        scene smasq5 with dissolve
        "..."
        scene smasq9 with fade
        "mm excuse me, can we join you?"
        scene smasq10 with dissolve
        "What do you say?"
        s "Hell yeah"
        "You girls start together while we undress"
        scene smasq11 with dissolve
        s "Mmm"
        scene smasq12 with dissolve
        "Enough, come let's go to the hall"
        scene smasq13 with fade
        s "Mmm"
        scene smasq14 with dissolve
        "..."
        scene smasq15 with dissolve
        "..."
        scene smasq19 with dissolve
        "..."
        scene smasq16 with dissolve
        "..."
        scene smasq17 with dissolve
        "..."
        scene smasq18 with dissolve
        "Hey do you care to swap?"
        "No, I don't you can both do the young girl"
        scene smasq20 with dissolve
        "I know you prefer her bastard"
        "Hey guys can we join you?"
        "If [sname] accepts"
        scene smasq21 with fade
        "May I stay here?"
        "What do you say monica?"
        scene smasq22 with dissolve
        "She can join us"
        scene smasq23 with dissolve
        "Mmm"
        scene smasq24 with dissolve
        "..."
        "Mmm"
        scene smasq26 with dissolve
        "..."
        scene black
        "..."
        scene smasq27 with fade
        "Let's destroy this bitch"
        s "Yes, I love dirty talk"
        scene smasq28 with dissolve
        s "Wait"
        scene smsqan with dissolve
        "Look at the bitch"
        scene smsqan1 with dissolve
        "Hell yeah"
        "She's enjoying it"
        scene black
        "BACK TO [bname]"
        pass

    else:
        scene bna15a with fade
        m "Hi honey"
        b "Oh finally"
        m "I'm sorry I left you alone"
        m "I'll be back"
        pass
    scene bna17a with fade
    b "Can I get you something to drink?"
    m "Yes, wine please"
    scene bna18a with dissolve
    m "So how was your afternoon?"
    if joshvisitpool == 1:
        b "I went to Joshua's"
        m "Mm nice, did you enjoy?"
        b "Yes, Wanda was nice, surprisingly"
        m "Yes she is good"
        m "Just be nice to her, and respectful"
        pass
    else:
        b "Normal"
        pass
    b "Here's your wine"
    if bstarmovie ==1:
        $ bstarmovie = 2
        b "And... I've got something for you"
        b "It's there near the tv"
        scene bmanipulate24 with dissolve
        m "What is it [bname]"
        b "Jewelry"
        m "Are you serious?"
        scene bmanipulate24 with dissolve
        m "What is it [bname]"
        b "Jewelry"
        m "Again?"
        m "My God"
        scene bmanipulate25 with dissolve
        b "Put it on, what are you waiting for?"
        scene bmanipulate26a with dissolve
        m "Oh my God [bname]"
        m "You make me cry again"
        scene bmanipulate27a with dissolve
        m "I love you honey"
        m "Let's go out and celebrate"
        m "I'll change and we go"
        b "Emm actually I want something else"
        scene bmanipulate28a with dissolve
        m "What do you want?"
        m "Anything for my baby"
        b "I want to record a film for us"
        m "Of course honey, get your camera"
        b "No, it's with Jonas"
        b "I already informed him"
        m "Ok tell me the date, so I can do it"
        b "Now, he can accomodate us"
        scene bmanipulate29a with dissolve
        m "Now? Are you sure?"
        b "Yes"
        scene bmanipulate28a with dissolve
        m "You're a naughty boy"
        m "I'll get ready and we go"
        jump mel_m_porn



    elif buyjewelry ==2 and escortrequest == 2:
        b "I've got something for you"
        $ buyjewelry = 3
        $ persistent.unlock_59 = True
        b "It's there near the tv"
        scene bmanipulate24 with dissolve
        m "What is it [bname]"
        b "Jewelry"
        m "Are you serious?"
        scene bmanipulate25 with dissolve
        b "Put it on, what are you waiting for?"
        scene bmanipulate26 with dissolve
        m "Oh my God [bname]"
        m "This is expensive! How did you manage to buy this?"
        b "Nah it's nothing"
        b "I managed from my daily work"
        scene bmanipulate27 with dissolve
        m "I love you honey"
        m "Let's go out and celebrate"
        m "I'll change and we go"
        m "You also get ready"
        scene bmanipulate28 with fade
        b sur "Oh my god!"
        scene bmanipulate29 with dissolve
        m "Thank you, come on let's move"
        scene bmanipulate30 with dissolve
        m "I have a reserveration under [mname]"
        "Please follow me"
        scene bmanipulate31 with fade
        m "Honey, she's presenting you the wine"
        scene bmanipulate32 with dissolve
        b "Oh sorry"
        b "What do I do?"
        m "Check the label and nod signaling her to start serving"
        b "Ah alright, yes good, you can pour"
        b "I'll go to the toilet, where is it?"
        "To the right at the end"
        b "Thanks"
        scene bmanipulate33 with dissolve
        m "I'm sorry, it's his first time"
        "No worries ma'am"
        scene bmanipulate34 with dissolve
        b "Good evening to you sir"
        b "I'm [bname]"
        b "The coast is clear"
        p "Good evening, got it thank you"
        scene bmanipulate35 with dissolve
        p "Good evening, my name is Pedro"
        p "And I noticed how beautiful you are"
        m "Oh thank you"
        p "I'd like to invite you on a yacht journey with me"
        m "Ermm I don't know"
        p "Don't answer me now, here's my business card"
        p "Take your time and when you decide"
        p "All you have to do is ring and my chauffeur will come and take you"
        scene bmanipulate36 with dissolve
        m "Thanks"
        scene bmanipulate37 with dissolve
        m "..."
        $ escortrequest = 3
        scene bmanipulate38 with fade
        b "Sorry it took me so long"
        m "No problem babe"
        b "Babe!?"
        m "Yes you're my babe tonight"
        m "And always"
        m "Cheers"
        scene bmanipulate39 with dissolve
        b "Cheers"
        b "To a beautiful night"
        m "And let's order food I'm hungry"
        b "Yeah"
        m "After we can go dancing"
        m "It feels like a great night, and full of good luck"
        b "I was thinking maybe we can visit Wanda"
        b "You know, to show her that you also have better jewelry"
        m "No babe, I don't care, I don't want it for attention"
        m "I want it from someone I love, to feel good about myself"
        b "That means a lot, thank you"
        scene black
        "LATER THAT NIGHT"
        scene bmanipulate40 with fade
        m "You know what, I'm already drunk"
        m "And you're right, let's go to your place"
        m "And Call Elaine"
        b "Cool, can she get her boyfriend with her?"
        m "Yes no problem if Rob comes"
        scene bmanipulate41 with dissolve
        b "Hey Elaine"
        b "Are you working?"
        m "I'll be back [bname]"
        m "Prepare the wine"
        scene bmanipulate42 with dissolve
        b "Listen, can you bring Rob with you?"
        e "{i}(Sure){/i}"
        b "It's going to be a good night"
        e "{i}(You mean sex?){/i}"
        b "Yes"
        e "{i}(Then definitely I'm not bringing Rob){/i}"
        b "What the fuck!"
        b "Ok much better"
        m "What happened?"
        scene bmanipulate43 with dissolve
        b "She's not coming"
        m "What to do! Let's celebrate alone"
        scene bmanipulate44 with fade
        m "I'm in the mood for a dance, let's finish this drink first"
        b "Ok cool"
        m "Bottoms up!"
        scene bmanipulate45 with fade
        b "Wow you're smoking!"
        m "Yes it's my last cigarette"
        b "Ah that's why you wanted Elaine"
        m "Come on, take your shirt away"
        scene bmanipulate46 with dissolve
        m "The key to dancing is passion"
        m "It's not very hard, passion and harmony"
        b "Ok got it"
        scene bmanipulate47 with dissolve
        b "Like this!"
        m "Mmm"
        scene bmanipulate48 with dissolve
        m "Good, I think I better give you a dance show"
        m "Then we go to my room"
        scene bmanipulate49 with dissolve
        m "Stop staring like this"
        scene bmanipulate50 with dissolve
        b "Come on! Stop teasing me"
        scene bmanipulate51 with dissolve
        b "Mmm"
        scene bmanipulate52 with dissolve
        b "Nice"
        b "Let's record a movie together"
        m "Hmmm"
        scene bmanipulate53 with dissolve
        m "You want to film this don't you"
        b "Indeed"
        menu:
            "Take her to her room":
                scene bmanipulate69 with fade
                m "Ah"
                m "Do me doggy [bname]"
                scene bmanangled
                play sound "sounds/bmanangledwav.wav"
                "..."
                m "Ahhh"
                "..."
                "...."
                stop sound fadeout 1.0
                scene bmanipulate70 with dissolve
                m "More!"
                scene bmanipulate71 with dissolve
                m "Say you love me!"
                b "I love you"
                m "No matter what happened!"
                b "Always, no matter"
                m "Sure?"
                b "Yes, come here, let me show you how much I want you"  
                scene bmanipulate72 with dissolve
                "..."
                scene bmanipulate73 with dissolve
                m "Mmm"
                m "Enough give me your sweet cock"
                scene bmanipulate74 with dissolve
                "..."
                scene bmanipulate75 with dissolve
                m "Uhh"
                "..."
                scene bmanipulate76 with fade
                m "You taste like wine"
                b "Did you swallow all?"
                m "What do you think?"
                b "Hehe"
                m "Can we sleep together tonight?"
                b "Of course"
                b "Let's go"
                scene black
                "..."
                jump newday

            "Do it here":
                b "Let me fix the camera"
                scene bmanipulate54 with dissolve
                b "Done"
                m "Mmmm"
                scene bmanipulate55 with dissolve
                m "Ahh"
                b "Let's get on the floor"
                scene bmanipulate56 with dissolve
                m "Yes here"
                scene bmanipulate57 with dissolve
                m "Mhmm"
                scene bmanipulate58 with dissolve
                b "Ahh"
                scene bmanipulate59 with dissolve
                b "Come kiss me"
                scene bmanipulate60 with dissolve
                m "Ah"
                scene bmanipulate61 with dissolve
                m "...."
                scene bmanipulate62 with hpunch
                m "Ahhhh"
                scene bmanipulate63 with dissolve
                m "I can't anymore [bname]"
                m "Full my mouth"
                scene bmanipulate64 with fade
                m "Mmm"
                scene bmanipulate65 with dissolve
                b "Ahhh so warm"
                scene bmanipulate66 with dissolve
                b "Ohh yess"
                scene bmanipulate67 with dissolve
                b "Fuck"
                scene bmanipulate68 with dissolve
                m "You taste like wine"
                b "Did you swallow all?"
                m "What do you think?"
                b "Hehe"
                m "Can we sleep together tonight?"
                b "Of course"
                b "Let's go"
                scene black
                "..."
                jump newday



        

    elif escortrequest ==1:
        play sound "sounds/doorbell.wav"
        $ persistent.unlock_25 = True
        b "Huh"
        stop sound
        b "That's..."
        m "I'll open that"
        $ escortrequest = 2
        scene bmanipulate with dissolve
        m "Thank you"
        b "Oh they delivered so quick?"
        scene bmanipulate1 with dissolve
        m "It's from you?"
        b "Yes, I wrote a note, didn't they put it inside?"
        m "I'll go check and try it"
        b "Alright, can't wait to see it on you"
        scene bna17b with dissolve
        m "[bname]! come"
        scene bmanipulate2 with fade
        m "So?"
        b "So? Do you like it?"
        scene bmanipulate3 with dissolve
        m "Of course I do"
        b "Glad you like it"
        scene bmanipulate4 with dissolve
        b "But you look better without it"
        scene bmanipulate5 with dissolve
        m "[bname] again?"
        b "I think I'm in love with you"
        m "[bname] you're my ..."
        scene bmanipulate6 with dissolve
        m "..."
        scene bmanipulate7 with dissolve
        b "And I want to love you every minute of the day"
        scene bmanipulate8 with dissolve
        m "Ah"
        scene bmanipulate9 with dissolve
        b "I love this"
        menu:
            "Doggy on the floor":
                scene bmanfoc with fade
                m "Ah"
                "..."
                m "Ahaha [bname]"
                m "Mm"
                "..."
                m "Ah"
                "..."
                m "Oh God yes"
                b "I'm done"
                scene bmanipulate22 with fade
                b "Can I ask you a question?"
                m "I know what it is"
                m "[bname] yes I do love you"
                m "But in a different way"
                b "Ok, but the question was something else"
                m "What is it?"
                b "Would you accept going on a yacht trip with someone"
                scene bmanipulate23 with dissolve
                m "What!?"
                b "There's a rich guy who saw your videos and wants you to go with him on a trip to the maldives"
                m "Are you serious?"
                b "Yes I am, why?"
                m "Please leave"
                b "{i}(Fuck, she won't accept in this version){/i}"
                b "{i}(I'll go to sleep){/i}"
                jump newday

            "Take her to the bed":
                pass
        scene bmanipulate10 with fade
        b "I love you"
        scene bmanipulate11 with dissolve
        m "Mmm"
        scene bmanipulate12 with dissolve
        m "Ahhhh"
        scene bmanipulate13 with dissolve
        m "[bname]"
        scene bmanipulate14 with dissolve
        m "Enough"
        scene bmanipulate15 with fade
        m "Mmm"
        scene bmanipulate16 with dissolve
        b "Ah"
        scene bmanipulate17 with dissolve
        m "..."
        scene bmanipulate18 with fade
        b "Can I ask you a question?"
        m "I know what it is"
        m "[bname] yes I do love you"
        m "But in my own way"
        b "Ok, but the question was something else"
        scene bmanipulate19 with dissolve
        m "What is it?"
        b "Would you accept going on a yacht trip with someone"
        scene bmanipulate20 with dissolve
        m "What!?"
        b "There's a rich guy who saw your videos and wants you to go with him on a trip to the maldives"
        scene bmanipulate21 with dissolve
        m "Are you serious?"
        b "Yes I am, why?"
        m "Please leave"
        b "{i}(Fuck, she won't accept in this version){/i}"
        b "{i}(I'll go to sleep){/i}"
        jump newday

    else:
        pass
    scene bna19a with dissolve
    b "I have a request"
    m "What is it?"
    menu:
        "Can you, give me a shower?":
            m "Sure baby, Let's go"
            b "Finish your wine first"
            m "I'll continue later, let it aerate, better"
            if bandageremove ==1:
                scene jdm3_37a with fade
                b "Again"
                scene jdm3_38a with dissolve
                m "Just relax baby"
                scene jdm3_39a with dissolve
                m "We don't want this small peenie weenie to get wet"
                b "Hey"
                scene jdm3_40 with dissolve
                m "Hahaha"
                b "Please stop it"
                b "It's not true"
                scene jdm3_41 with dissolve
                m "I'm sorry"
                m "We're done"
                scene jdm3_42 with dissolve
                m "How does my big boy feel now"
                b "{i}(Damn, such times make me feel shit){/i}"
                b "{i}(The way I think about her){/i}"
                b "{i}(All the evil thoughts){/i}"
                m "Why silent all of a sudden"
                b "Nothing, I was thinking how ungrateful I am"
                b "Thank you so much"
                scene jdm3_50 with dissolve
                "..."
                scene jdm3_50a with dissolve
                "..."
                scene jdm3_50b with dissolve
                b "Mmm"
                scene jdm3_50c with dissolve
                m "Ahh"
                scene jdm3_51a with dissolve
                m "Mmm"
                scene jdm3_52a with dissolve
                b "Mm"
                scene jdm3_53a with dissolve
                m "Mghhm"
                scene jdm3_54a with dissolve
                m "..."
                scene jdm3_55a with dissolve
                m "..."
                scene jdm3_56a with vpunch
                m "Aggh"
                scene jdm3_57a with fade
                m "I'm so tired, I will go to bed"
                b "Good night"
                jump newday
            else:
                pass
            scene jdm3_37 with fade
            b "Again"
            scene jdm3_38 with dissolve
            m "Just relax baby"
            scene jdm3_39 with dissolve
            m "We don't want this small peenie weenie to get wet"
            b "Hey"
            scene jdm3_40 with dissolve
            m "Hahaha"
            b "Please stop it"
            b "It's not true"
            scene jdm3_41 with dissolve
            m "I'm sorry"
            m "We're done"
            scene jdm3_42 with dissolve
            m "How does my big boy feel now"
            b "{i}(Damn, such times make me feel shit){/i}"
            b "{i}(The way I think about her){/i}"
            b "{i}(All the evil thoughts){/i}"
            m "Why silent all of a sudden"
            b "Nothing, I was thinking how ungrateful I am"
            b "Thank you so much"
            scene jdm3_50 with dissolve
            m "..."
            scene bna20a with fade
            b "I'm sorry for being rude earlier"
            m "Don't be sorry honey"
            scene bna21a with dissolve
            m "I love you no matter what"
            m "And that's not the wine speaking"
            b "I love you too"
            scene bna22a with dissolve
            "..."
            scene bna21a with dissolve
            m "[bname] you should go to sleep"
            b "I can't I really want to test myself"
            b "This thing is worrying me"
            m "Baby you're just paranoid"
            if mrel >=160:
                scene bna21b with dissolve
                m "[bname]?"
                b "I'm sick of this situation"
                m "Which situation?"
                b "Why do I have to keep asking you about this"
                b "Why can't we make it normal"
                scene bna24a with dissolve
                m "Mmm"
                scene bna25a with dissolve
                m "Ahhh"
                scene bna26a with dissolve
                m "What are you doing?"
                scene bna23b with dissolve
                m "[bname] No, please stop"
                b "Why?"
                m "It's not good for you"
                b "But I am good"
                m "I said no"
                menu:
                    "Stop":
                        b "Ok sorry"
                        scene bna23c with dissolve
                        m "I'm so tired, I will go to bed"
                        b "{i}(Fuck){/i}"
                        b "{i}(That's it here, I'll go to sleep){/i}"
                        jump newday
                    "Don't":
                        m "What are you doing?"
                        scene bna27a with dissolve
                        b "This"
                        $ persistent.unlock_13 = True
                        scene bna28a with dissolve
                        m "Hold me, I'll fall"
                        scene bna28c with dissolve
                        m "Don't worry"
                        scene bna29a with dissolve
                        m "Ahhhhh"
                        scene bna30a with dissolve
                        b "Ahhhh"
                        scene bna30c with dissolve
                        m "..."
                        scene bna23c with fade
                        m "I'm so tired, I will go to bed"
                        b "{i}(That's it, I'll go to sleep){/i}"
                        jump newday
            else:
                scene bna21b with dissolve
                m "[bname]?"
                scene bna23a with dissolve
                m "[bname] I told you stop"
                b "Ok sorry"
                "YOU DON'T HAVE ENOUGH POINTS, 160 NEEDED"
                scene bna23c with dissolve
                m "I'm so tired, I will go to bed"
                b "{i}(Fuck){/i}"
                b "{i}(That's it here, I'll go to sleep){/i}"
                jump newday
            

        "I'm not feeling well":
            b "I'm still not getting it up"
            m "That again"
            b "Yeah"
            m "All right, I'll finish my glass of wine, and will take a look at it"
            scene bnah0 with dissolve
            m "Undress yourself"
            menu:
                "Take the lead":
                    $ persistent.unlock_27 = True
                    scene bnah11 with dissolve
                    m "Mmm"
                    scene bnah12 with dissolve
                    m "..."
                    scene bnah11 with dissolve
                    m "Mmm"
                    b "Enough"
                    scene bnah13 with hpunch
                    m "Mm"
                    scene bnah14 with dissolve
                    b "Oh"
                    scene bnah15 with dissolve
                    m "Ahhh [bname]"
                    play sound "sounds/mobilering.wav"
                    m "Huh!"
                    scene bnah16 with dissolve
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
                    scene black
                    "..."
                    jump wandavisit

                "Let her take the lead":
                    pass
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
            scene bnah5a with dissolve
            b "Fuck!"
            b "{i}(I filled her throat with cum){/i}"
            scene bnah6a with dissolve
            m "..."
            b "Come to this side"
            scene bnah9 with dissolve
            m "Mmm"
            scene bnah10 with dissolve
            m "Gulp"
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

    scene bna19b with dissolve
    m "I'm so tired, I will go to bed"
    b "{i}(Fuck){/i}"
    b "{i}(That's it here, I'll go to sleep){/i}"
    jump newday
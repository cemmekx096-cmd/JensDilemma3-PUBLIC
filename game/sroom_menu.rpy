

label sroom_menu:
    if Hour >=9 and Hour <11:
        scene door with fade
        b "{i}([sname] door is locked){/i}"
        b "{i}(I wonder what is she doing?){/i}"
        call screen gnav

    elif Hour ==11:
        $ Hour += 1
        scene door with fade
        b "{i}(Looks like the door is open){/i}"
        menu:
            "Knock":
                play sound "sounds/knock.ogg"
                s "Who is it?"
                b "It's me"
                $ srel += 5
                s "Come in, it's open"
                scene sroom_ava with fade
                b "Hi [sname]"
                "..."
                b "[sname]!?"
                scene sroom_av1a with dissolve
                s "Huh [bname] sorry"
                s "I was studying"
                s "How are you?"
                b "A little better"
                s "Can you help me?"
                b "Of course"
                s "I can't do this equation"
                b "Let me see"
                scene sroom_av2a with dissolve
                s "This one"
                scene sroom_av3a with dissolve
                "..."
                scene sroom_av4a with dissolve
                b "Hmmm"
                b "Yeah"
                s "Yeah what?"
                s "I'll do it for you"
                scene sroom_av2 with dissolve
                b "This is how you do it?"
                scene sroom_av5a with dissolve
                show screen srelup
                s "Thank you"
                hide screen srelup
                b "You're welcome"
                s "Now let me finish this"
                if joshuacorrupted == 3 and snameacceptjoshua == 0:
                    menu:
                        "Ask her if she can help corrupting Joshua":
                            $ persistent.unlock_9 = True
                            b "Hey, can I ask for help?"
                            s "No, I'm not gonna blow you"
                            b "No no, it's not that"
                            b "I need your help with Joshua"
                            b "Remember when you came while we're playing a pc game?"
                            s "Yes I do, What is it about?"
                            b "Well I think he has the hots for you"
                            b "And if you repeat that with some teasing he's going to..."
                            b "Well let's say I need to weaken him a little bit"
                            s "Hmm"
                            s "I'll do that on one condition"
                            b "What do you want?"
                            s "If you can convince mom to allow me to go for that weekend pool party at aunt Cheryl's"
                            b "Easy, consider it done"
                            s "Ok. Consider teasing Joshua is done as well"
                            $ snameacceptjoshua = 1
                            b "Great, thank you"
                            pass
                        "Leave":
                            pass
                else:
                    pass
                b "Sure"
                pass
                
            "Enter":
                scene sroom_av5 with hpunch
                s "[bname]!! What's wrong?"
                s "Are you ok?"
                b "Yeah, what are you doing?" 
                scene sroom_av6 with dissolve
                s "Seriously!"
                b "What?"
                s "You scared me, I thought you are in pain"
                scene sroom_av7 with dissolve
                b "No"
                b "Do you need help with this?"
                s "No, I can manage"
                b "Ok, as you wish"
                pass
                
        scene door with fade
        b "{i}(...){/i}"
        call screen gnav


    elif Hour >=12 and Hour <13:
        scene door with fade
        b "{i}(The door is locked){/i}"
        menu:
            "Knock":
                $ Hour += 1
                play sound "sounds/knock.ogg"
                s "Who is it?"
                b "It's me"
                s "Wait"
                scene sroom_c with fade
                b "Hi [sname]"
                "..."
                b "[sname]!?"
                s "Wait!"
                b "You seem to be busy these days"
                scene sroom_c1 with dissolve
                s "Sorry, what did you want?"
                menu:
                    "Can you lend me some money?":
                        s "I can give you 100$ for a foot massage"
                        b lau "Really?"
                        s "Why are you laughing?"
                        b "Nothing"
                        menu:
                            "Ok":
                                b "Let's do it"
                                scene sroom_c2 with fade
                                s "Show me what you've got"
                                scene sroom_c3 with dissolve
                                s "Not bad"
                                scene sroom_c4 with dissolve
                                s "Mmm"
                                menu:
                                    "Kiss her feet":
                                        scene sroom_c7 with dissolve
                                        s "Nice"
                                        show screen scorr
                                        $ scorr += 5
                                        scene sroom_c8 with dissolve
                                        hide screen scorr
                                        s "You're tickling me"
                                        b "Mmm"
                                        b "Isn't it nice?"
                                        scene sroom_c9_ with dissolve
                                        s "You're such a good boy [bname]"
                                        scene sroom_c10 with dissolve
                                        s "Do you want please me more?"
                                        b "Ye..Yes!"
                                        scene sroom_c11 with dissolve
                                        s "Take off your clothes"
                                        scene sroom_c12 with dissolve
                                        s "Yes"
                                        scene sroom_c13 with dissolve
                                        s "Mmm"
                                        scene sroom_c12 with dissolve
                                        s "Enough, you can go now"
                                        pass

                                    "Continue the massage":
                                        b "Turn on your back let me do the heels"
                                        scene sroom_c5 with dissolve
                                        "..."
                                        scene sroom_c6 with dissolve
                                        b "..."
                                        s "I guess that's enough"
                                        pass

                                scene sroom_c1 with fade
                                s "Thank you [bname]"
                                s "Here's your 100"
                                $ mny += 100
                                b "Thanks"
                                scene door with fade
                                b "{i}(I wonder where is she getting the money from){/i}"
                                "..."
                                call screen gnav
                            "No":
                                s "Ok, then leave"
                                b "Bye"
                                scene door with fade
                                b "{i}(...){/i}"
                                "..."
                                call screen gnav

                    "Ask her if she can help corrupting Joshua" if joshuacorrupted == 3 and snameacceptjoshua == 0:
                        b "Hey, can I ask for help?"
                        $ persistent.unlock_9 = True
                        s ang "No, I'm not gonna blow you"
                        b "No no, it's not that"
                        b "I need your help with Joshua"
                        b "Remember when you came while we're playing a pc game?"
                        s "Yes I do, What is it about?"
                        b "Well I think he has the hots for you"
                        b "And if you repeat that with some teasing he's going to..."
                        b "Well let's say I need to weaken him a little bit"
                        s "Hmm"
                        s "I'll do that on one condition"
                        b "What do you want?"
                        s "If you can convince mom to allow me to go for that weekend pool party at aunt Cheryl's"
                        b "Easy, consider it done"
                        s "Ok. Consider teasing Joshua is done as well"
                        $ snameacceptjoshua = 1
                        b "Great, thank you"
                        call screen gnav

                    "Ask for more help with Joshua" if colaspike>=4 and gymwithwanda == 1 and smorehelpwithjoshua==0:
                        $ smorehelpwithjoshua = 1
                        b "Hey, can I ask for more help with Joshua?"
                        s ang "What do you want this time?"
                        b "I think we need to step it up in the toilet"
                        s "Like what?"
                        b "Well, tease him more"
                        s "I don't get it"
                        b "Be romantic, I don't know"
                        b "Maybe a hug?"
                        s "Ok"
                        s "I'll do that but I need something in return"
                        b "What do you want?"
                        s "I need you to convince mom to allow me to go to a ball masque"
                        b "Easy, consider it done"
                        s "She didn't agree when I asked her, so you have to use your all of your convincing skills"
                        b "Sure"
                        b "Wait, what's that?"
                        s "It's a masquerade ball"
                        s "It's pronounced ball maskay"
                        b "And since when you go to such things"
                        s "I don't know, it's just for fun"
                        b "{i}(Hmm interesting twist of events){/i}"
                        b "{i}(We will figure this out in future versions){/i}"
                        b "Alright, I'll convince her"
                        s "Consider making Joshua wetting himself done then"
                        call screen gnav

                    "Ask her if she can help corrupting Joshua" if snametoiletjoshua ==1:
                        b "Hey, can I ask for help one more time?"
                        s ang "No, I'm not gonna blow you"
                        b "No no, it's not that"
                        b "I need your help with Joshua"
                        b "Remember when you came while we're playing a pc game?"
                        s "Yes I do, What is it about?"
                        b "Well I need more help"
                        s "Hmm"
                        s "What is it about this time?"
                        b "Well, every time I am at his place, he accompanies me to the bathroom"
                        b "I need to lure him into somthing"
                        b "So he stops escorting me"
                        b "As if I am some criminal"
                        s "I don't get it"
                        b "Look, just do this for me, I can't clearly explain it"
                        s "Ok"
                        s "I'll do that on one condition"
                        b "What do you want?"
                        s "If you can convince mom to allow me to go for another party"
                        b "Easy, consider it done"
                        s "Ok. Consider teasing Joshua is done as well"
                        $ snametoiletjoshua = 2
                        b "Great, thank you"
                        call screen gnav

                    "Do you want to go the beach?":
                        if srel >= 105:
                            s "What about your skin thing?"
                            b "What's about it?"
                            s sur "What's?!!"
                            s "Do you think you can \"what's\" go and \"what's\" swim?"
                            b "Ah yeah"
                            b "Well I can get some sun at least"
                            s "I don't know, I can't be responsible for that"
                            s "Ask [mname]"
                            scene bsbeach0a with fade
                            b "Ahem"
                            m "Yes [bname]"
                            b "Is it ok if I go swim with [sname]"
                            if bandageremove ==1:
                                m "Ah to the beach?"
                                if persistent.patch_enabled:
                                    b "No at aunt Cheryl's"
                                    pass
                                else:
                                    b "No at Cheryl's place"
                                    pass
                                m "Oh"
                                if mcorr >= 30:
                                    m "I was thinking if you can help me do something on the laptop"
                                    b "Hmm"
                                    menu:
                                        "Refuse politely and go with [sname]":
                                            b "Ahh, sorry, I already promised [sname]"
                                            b "We can do it another time"
                                            $ mrel -= 5
                                            show screen mreldw
                                            scene bsbeach1b with dissolve
                                            m sad "Ok"
                                            hide screen mreldw
                                            m "Enjoy"
                                            jump cbspool

                                        "Yeah sure":
                                            b "I'll go tell [sname] to go alone and will bring my laptop"
                                            jump mlaptophelp

                                else:
                                    #
                                    scene bsbeach2b with dissolve
                                    m "Ok fine, but don't make a habit of it"
                                    b "And don't stay long"
                                    "RAISE HER CORRUPTION POINTS TO 30"
                                    jump cbspool

                            else:
                                pass
                            m "[bname] you can't swim"
                            m "And which beach are you planning to go to, you'll get sand in your scar"
                            if mrel <150:
                                b "I'm sorry, yeah, I mean to sit on the pool just to get some sun"
                                m "Where?"
                                if persistent.patch_enabled:
                                    b "At aunt Cheryl's"
                                    pass
                                else:
                                    b "At Cheryl's place"
                                    pass
                                scene bsbeach1b with dissolve
                                m "..."
                                scene bsbeach2b with dissolve
                                m "You can't get in the sun with this"
                                m "Wait few more days, then we'll see"
                                m "Maybe we go together to the beach"
                                scene hall_d with fade
                                b "{i}(Dang!){/i}"
                                "RAISE YOUR POINTS WITH [mname] TO 150"
                                call screen gnav
                            else:
                                b "I'm sorry, yeah, I mean to sit on the pool just to get some sun"
                                m "Where?"
                                if persistent.patch_enabled:
                                    b "At aunt Cheryl's"
                                    pass
                                else:
                                    b "At Cheryl's place"
                                    pass
                                scene bsbeach2b with dissolve
                                m "Ok fine, but don't make a habit of it"
                                b "And don't stay more than one hour"
                                jump cbspool

                        else:
                            s "No, sorry, not in the mood"
                            b "Whatever"
                            b "Bye"
                            scene door with fade
                            b "{i}(...){/i}"
                            "RAISE YOUR POINTS WITH HER TO 105"
                            call screen gnav

    elif Hour ==13:
        $ Hour += 1
        scene door with fade
        b "{i}(Looks like the door is open){/i}"
        scene sroom_av8 with fade
        b "Hey there"
        b "What are you doing?"
        scene sroom_av9 with dissolve
        s "[bname]! Can't you see I'm reading"
        s "Please"
        b "Ok Sorry"
        "..."
        scene sroom_av10 with dissolve
        s "Stop being annoying"
        scene sroom_av11 with dissolve
        s "Please [bname]"
        s "Please leave"
        menu:
            "I'll leave on one condition":
                s "What is it?"
                scene sroom_av15 with dissolve
                "..."
                b "Come on, we did it many times already"
                s "I'm not in the mood right now"
                b "It's only one kiss"
                scene sroom_av16 with dissolve
                s "You pervert"
                s "You never change, even with your condition"
                scene sroom_av17 with dissolve
                "..."
                if srel >= 105:
                    b "{i}(Hmm){/i}"
                    b "{i}(Maybe...){/i}"
                    scene sroom_av18 with dissolve
                    b "{i}(Cool, no reaction){/i}"
                    menu:
                        "Pull it":
                            scene sroom_av24 with dissolve
                            "..."
                            scene sroom_av25 with hpunch
                            b "Ouch!"
                            s "Get out"
                            b sad "Calm down, I'm leaving"
                            scene door with fade
                            b "{i}(...){/i}"
                            "..."
                            call screen gnav
                            
                        "Do nothing":
                            pass
                    scene sroom_av19 with dissolve
                    s "Happy"
                    b "Hehehe yeah"
                    s "Now let me read please"
                    b "Yes cool"
                    scene door with fade
                    b "{i}(...){/i}"
                    "..."
                    call screen gnav
                else:
                    scene sroom_av19 with dissolve
                    s "Let me read please"
                    b "OK"
                    scene door with fade
                    b "{i}(...){/i}"
                    "RAISE YOUR POINTS TO 105"
                    call screen gnav
                        
                
                
            "Tease her":
                b "{i}(Hmm){/i}"
                scene sroom_av12 with dissolve
                s "What now [bname]?"
                b "I'm going to..."
                menu:
                    "Tickle her feet":
                        scene sroom_av13 with dissolve
                        b "..."
                        show screen sreldw
                        $ srel -= 1
                        scene sroom_av14 with hpunch
                        hide screen sreldw
                        s "My God [bname]"
                        s "Please go"
                        if persistent.patch_enabled:
                            s "Or else I'll call mom"
                            pass
                        else:
                            s "Or else I'll call [mname]"
                            pass
                            
                        b "Hahahah"
                        b "I'm going"
                        pass
                        
                    "Pull her bottoms down":
                        scene sroom_av22 with hpunch
                        b "Wow"
                        scene sroom_av15a with vpunch
                        s "OUT!!"
                        b "I'm leaving"
                        scene door with fade
                        b "{i}(...){/i}"
                        "..."
                        call screen gnav
                            
                            
                            

                
            "Leave":
                b "I'm going"
                pass
            

        scene door with fade
        b "{i}(...){/i}"
        call screen gnav
        
    elif Hour >13 and Hour <19:
        if Hour ==16 and sbmbname ==2:
            $ sbmbname = 3
            $ Hour += 1
            scene sfo with fade
            b "So what is it about?"
            $ persistent.unlock_23 = True
            s "It's a request for my fansonly page"
            b sur "You have a fansonly page?"
            s "Yes"
            b "What a family!"
            s "Look who's talking"
            s "It was your idea"
            b "Me!?"
            s "Wait for me in the living room"
            menu:
                "Request 1":
                    scene sfo1 with fade
                    b "Hahaha serious?"
                    s "Hmmm"
                    scene sfo2 with dissolve
                    s "Duh!"
                    s "Move the table while I set up the camera"
                    s "And can you take off your bandage?"
                    s "We don't want people to identify you"
                    b "Yes I have a small sticker on anyway"
                    s "Ok that won't show"
                    scene sfo3 with fade
                    s "Hey peeps, it's been..."
                    b "Ugh wow, this is so hot maybe I won't be able to hold"
                    scene sfo4 with dissolve
                    s "Shut the fuck [bname]"
                    s "Now I have to repeat"
                    s "Don't speak"
                    b "Ok"
                    scene sfo3 with dissolve
                    s "Hey peeps, this video shows you the right way to serve your princess"
                    s "And there's only one princess"
                    s "It's me Kamiko!"
                    s "First you kiss her hands"
                    scene sfo5 with dissolve
                    s "Hmm"
                    scene sfo6 with dissolve
                    s "That wasn't enough"
                    s "Maybe her feet would do?"
                    scene sfo7 with dissolve
                    s "Bad doggy"
                    s "Come here"
                    scene sfo8 with dissolve
                    s "Yes lick your princess"
                    scene sfo9 with dissolve
                    s "Mhhmm"
                    scene sfo10 with fade
                    s "Thank you peeps"
                    s "And don't forget to vote for the next request"
                    scene sfo11 with dissolve
                    b "That was it? No sex?"
                    s "Maybe next time [bname]"
                    s "Let's see the request"
                    b "Fuck!"
                    s "Please let me edit this video and then we will see"
                    b "Grrr..."
                    b "{i}(...){/i}"
                    call screen gnav

                "Request 2":
                    scene sfo1 with fade
                    $ persistent.unlock_41 = True
                    b "Oh Merry Christmas"
                    b "You cut your hair?"
                    scene sfo12 with dissolve
                    s "It's a wig"
                    s "What? Don't you like it?"
                    b "I do, I do..."
                    s "Put this mask on while I setup the camera"
                    b "Okay"
                    scene sfo14 with fade
                    s "Mmm"
                    #ring"
                    scene sfo15 with dissolve
                    z "Hi"
                    s "Ah, cool, you decided to come"
                    scene sfo16 with dissolve
                    s "Oh you look better in real life"
                    "Thank you"
                    b "Who is it?"
                    s "Another influencer, we're doing a collab"
                    b "Influencer! Yeah right"
                    b "What exactly is your influence?"
                    s "Shut up, let's go to my room"
                    scene sfo17 with fade
                    s "I'll setup the webcam"
                    b "Can I remove the mask?"
                    b "I need to see this beauty"
                    menu:
                        "Zoey is a female":
                            s "Yes"
                            scene sfo18a with fade
                            b "What a beautiful lady!"
                            scene sfo19a with dissolve
                            b "Mmm"
                            z "Let's get on the bed"
                            scene sfo21a with fade
                            b "Yeah"
                            scene sfo22a with dissolve
                            b "You're so hot"
                            s "Ok now I'll be giving you both instructions"
                            scene sfo23a with dissolve
                            s "Yes slowly"
                            scene sfo24a with dissolve
                            z "Ah"
                            scene sfo25a with dissolve
                            b "Fuck!"
                            scene sfo26a with dissolve
                            b "..."
                            scene sfo27a with dissolve
                            z "Mmmm"
                            scene sfo28a with fade
                            s "That was awsome Zoey"
                            s "We should do more collabs"
                            z "Definitely"
                            b "{i}(...){/i}"
                            call screen gnav

                        "Zoey is a transgender/male":
                            s "No, you can't remove your mask"
                            scene sfo18 with fade
                            b "Mmm nice ass"
                            scene sfo19 with dissolve
                            s "Wow"
                            scene sfo20 with dissolve
                            b "What?"
                            z "Nothing, Let's get on the bed"
                            scene sfo21 with fade
                            b "Yeah"
                            scene sfo22 with dissolve
                            b "You're so hot"
                            scene sfo23 with dissolve
                            z "Open his mouth"
                            scene sfo24 with dissolve
                            b "What is it?"
                            s "I don't think this is a good idea Zoey"
                            b "What the fuck is it?"
                            s "She has a huge dildo"
                            b "That's it I'll remove this fucking mask"
                            scene sfo25 with dissolve
                            b "What the fuck!"
                            menu:
                                "Fuck her":
                                    scene sfo29 with fade
                                    z "Ahh"
                                    scene sfo26 with dissolve
                                    b "Ugggh"
                                    scene sfo27 with dissolve
                                    z "Ahhhh"
                                    scene sfo28 with dissolve
                                    b "Take it bitch"
                                    scene sfo30 with dissolve
                                    z "Aooh"
                                    scene sfo28a with fade
                                    s "That was awsome Zoey"
                                    s "We should do more collabs"
                                    z "Definitely"
                                    b "{i}(...){/i}"
                                    call screen gnav
                                    
                                "Watch her with [sname]":
                                    scene zfs with fade
                                    s "Ahh"
                                    b "..."
                                    s "So big!"
                                    scene sfo31 with dissolve
                                    z "Shut up"
                                    scene sfo32 with hpunch
                                    s "Ohhh"
                                    scene sfo33 with fade
                                    s "That was awsome Zoey"
                                    s "We should do more collabs"
                                    z "Definitely"
                                    b "{i}(...){/i}"
                                    call screen gnav
                "Request 3":
                    scene sfo1 with fade
                    b "Nice"
                    s "Hmmm"
                    scene sfo34 with dissolve
                    b "So what is it about this time?"
                    b "We have a request, but in the toilet"
                    b "In the toilet?"
                    s "Yes while I pee"
                    scene sfo11 with dissolve
                    b "No no no, I'm not doing this"
                    s "[bname] this fan pays a lot of money for videos"
                    s "It's just a clip, I won't be peeing for real"
                    scene sfo34 with dissolve
                    b "What do I get in return?"
                    s "Let's film it, and you won't be disappointed"
                    scene sfo35 with fade
                    b "You speak like professional business people"
                    s "..."
                    b "What are you thinking about?"
                    s "Trying to find a place for the phone"
                    b "You mean a recording angle?"
                    s "Yes"
                    b "Why don't you hang it near on top of the toilet door"
                    s "Good idea, start undressing while I do it"
                    scene sfo36 with fade
                    s "That should do it"
                    b "I'm done undressing"
                    scene sfo37 with dissolve
                    s "Ok just a sec"
                    scene sfo38 with dissolve
                    s "Get out, You come when I tell you"
                    scene sfo39 with fade
                    s "You can come"
                    b "Did you just pee?"
                    s "Did you hear any drops?"
                    b "No!"
                    s "Then come, you idiot"
                    b "Ok"
                    s "On your knees and kiss my pussy first"
                    scene sfo40 with dissolve
                    $ persistent.unlock_46 = True
                    s "Ahhh"
                    scene sfo41 with dissolve
                    s "Ummh"
                    scene sfo42 with dissolve
                    s "Ohhh I love it baby"
                    scene sfo43 with dissolve
                    s "Ahh yes"
                    s "Fuck me baby"
                    scene sfo44 with fade
                    s "Slow"
                    scene sfo45 with dissolve
                    s "Mmm"
                    scene sfo46 with dissolve
                    s "Ahh"
                    scene sfo47 with dissolve
                    s "Ahhh"
                    s "Are you done baby?"
                    b "Almost"
                    s "Give me in my mouth"
                    scene sfo48 with dissolve
                    s "You deserve it for licking my pee"
                    scene sfo49 with hpunch
                    b "Ah"
                    scene sfo50 with fade
                    b "Aren't you going to dress up?"
                    s "No I want to shower first"
                    s "I'm not dirty like you"
                    if josh_r_photos >=1:
                        b "Where's my payment?"
                        s "I'll think about something in the next version"
                        b "Can I click few photos of you in the bathtub?"
                        b "I promised to show Joshua something"
                        s "..."
                        s "Ok but no face"
                        b "You can put the face mask"
                        b "It'll be more realistic"
                        scene sfo51 with fade
                        b "Ok"
                        b "Now out of the water"
                        scene sfo52 with dissolve
                        b "Great"
                        scene sfo53 with fade
                        s "Enough for now"
                        s "Go"
                        call screen gnav
                    else:
                        b "Yeah right"
                        b "Where's my payment?"
                        s "I'll think about something in the next version"
                        s "Go now"
                        call screen gnav

                "Request 4":
                    scene sfo1 with fade
                    b "Wow"
                    s "Hmmm"
                    scene sfo54 with dissolve
                    b "Olga!"
                    scene sfo1 with dissolve
                    b "Hahaha"
                    s "Who's Olga"
                    b "No one, you look like a russian soldier"
                    b "So what's the request about today?"
                    s "Nothing, I need to take a few shoots in this"
                    b "So no recording?"
                    s "No"
                    b "Shall we start?"
                    s "Yes"
                    scene sfo55 with dissolve
                    s "Come closer"
                    scene sfo56 with dissolve
                    s "Now take without my face"
                    b "Ok"
                    s "You know!, No need just take it with the face"
                    s "I will cover it"
                    scene sfo57 with dissolve
                    b "Wow"
                    s "Now take the last one, on the couch"
                    scene sfo58 with dissolve
                    b "Cool"
                    s "Done"
                    scene sfo59 with dissolve
                    s "And stop saying cool, it's retarded"
                    b "Why is everyone bullying me now?"
                    b "But why do you need such photos anyway?"
                    s "..."
                    scene sfo60 with dissolve
                    s "I am a very important member of the underground"
                    b "Underground what?"
                    scene sfo61 with dissolve
                    s "Secret!"
                    s "Bye"
                    b "{i}(Could it be for her mysterious parties?){/i}"
                    b "{i}(This girl is getting really suspicious){/i}"
                    call screen gnav
                    


        else:
            pass
        scene door with fade
        b "{i}(The door is locked){/i}"
        call screen gnav


    elif Hour >=19 and Hour <20:
        $ Hour += 1
        scene door with fade
        b "{i}(Looks like the door is open){/i}"
        menu:
            "Knock":
                play sound "sounds/knock.ogg"
                if sscall ==0:
                    b "Hmm"
                    b "{i}(I'll enter){/i}"
                    $ sscall = 1
                    scene sroom_scall with fade
                    if persistent.patch_enabled:
                        s "Yes dad"
                        pass
                    else:
                        s "Yes stewart"
                        pass
                    "..."
                    s "Not that much..."
                    scene sroom_scall1 with dissolve
                    s "Ok, thanks"
                    s "You too, bye"
                    b "Hmm"
                    scene sroom_scall2 with dissolve
                    s "Yes?"
                    b "Who are you talking to?"
                    if persistent.patch_enabled:
                        s "Dad"
                    else:
                        s "Stewart"
                        pass
                    
                    b "You're calling him frequently"
                    s "I didn't call him"
                    b "Ah really?"
                    s "He called"
                    scene sroom_scall3 with dissolve
                    s "What's your problem [bname]!?"
                    s "Whether he called or not?!"
                    if persistent.patch_enabled:
                        b "Nothing... I'm gonna tell mom"
                        pass
                    else:
                        b "Nothing... I'm gonna tell [mname]"
                        pass
                    s "Go on! Tell her"
                    b "We'll see"
                    s "She doesn't even care about him, you moron!"
                    scene sroom_scall4 with dissolve
                    b "Whatever!"
                    scene door with fade
                    b "{i}(...){/i}"
                    call screen gnav
                else:
                    pass
                s "Who is it?"
                b "It's me"
                s "Come in, it's open"
                scene sroom_st with fade
                b "Still studying?"
                scene sroom_st1 with dissolve
                s "No, I'm done"
                s "I'll go for dinner"
                s "See you"
                b "Ok"
                scene door with fade
                b "{i}(...){/i}"
                call screen gnav
                    
            "Enter":
                if sscall ==0:
                    $ sscall = 1
                    scene sroom_scall with fade
                    if persistent.patch_enabled:
                        s "Yes dad"
                        pass
                    else:
                        s "Yes stewart"
                        pass
                    "..."
                    s "Not that much..."
                    scene sroom_scall1 with dissolve
                    s "Ok, thanks"
                    s "You too, bye"
                    b "Hmm"
                    scene sroom_scall2 with dissolve
                    s "Yes?"
                    b "Who are you talking to?"
                    if persistent.patch_enabled:
                        s "Dad"
                    else:
                        s "Stewart"
                        pass
                    
                    b "You're calling him frequently"
                    s "I didn't call him"
                    b "Ah really?"
                    s "He called"
                    scene sroom_scall3 with dissolve
                    s "What's your problem [bname]!?"
                    s "Whether he called or not?!"
                    if persistent.patch_enabled:
                        b "Nothing... I'm gonna tell mom"
                        pass
                    else:
                        b "Nothing... I'm gonna tell [mname]"
                        pass
                    s "Go on! Tell her"
                    b "We'll see"
                    s "She doesn't even care about him, you moron!"
                    scene sroom_scall4 with dissolve
                    b "Whatever!"
                    scene door with fade
                    b "{i}(...){/i}"
                    call screen gnav
                else:
                    pass
                s "Who is it?"
                b "It's me"
                s "Come in, it's open"
                scene sroom_st with fade
                b "Still studying?"
                scene sroom_st1 with dissolve
                s "No, I'm done"
                menu:
                    "What's new with your movies?":
                        b "Are you filming new stuff?"
                        s "Yeah, and no you can't watch any"
                        s "I don't have them"
                        b "Err I wasn't going to ask"
                        s lau "Yeah right"
                        b "Come on, show me"
                        s ang "I said I don't have them"
                        b "Please!"
                        if srel >= 130:
                            s "Ah, alright I'll show you what I have"
                            s "Go wait for me in the hall"
                            scene wmws0 with fade
                            s "No one should ever know about this clip"
                            b "Why do you care anyway?"
                            b "[mname] is doing the same, she won't mind"
                            s "It's because of the girl with me"
                            s "Anyways you won't every find the file"
                            scene wmws with dissolve
                            s "And... Play"
                            b "..."
                            scene wmws1 with fade
                            "..."
                            scene wmws2 with dissolve
                            b "What's that?"
                            scene wmws3 with dissolve
                            b "It's not a movie"
                            scene wmws0 with dissolve
                            b "That's only photography"
                            s "That's all what I've got"
                            b "Fine whatever"
                            scene hall_night with fade
                            b "{i}(Cheater){/i}"
                            call screen gnav

                        else:
                            s ang "I, DON'T, HAVE, THEM!"
                            s ang "Leave me alone, please"
                            b "{i}(Damn){/i}"
                            call screen gnav

                    "Wanna take some photos?":
                        s "You just want to drool over"
                        s "Knowing that you can't perform"
                        b "{i}(...){/i}"
                        call screen gnav
                    
        
    elif Hour >=21:
        scene door with fade
        b "{i}(It's locked){/i}"
        call screen gnav
        
    elif Hour >21:
        scene door with fade
        b "{i}(The door is locked){/i}"
        b "{i}(I should go to sleep){/i}"
        jump newday
        
    else:
        scene door with fade
        b "{i}(The door is locked){/i}"
        call screen gnav
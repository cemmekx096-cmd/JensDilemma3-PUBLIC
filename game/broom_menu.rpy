

label broom_menu:
    if Hour >=9 and Hour <18:
        scene broom_day with fade
        b "Hmmm"
        b "What to do?"
        menu:
            "Call Melinda to follow up on your porn movie with [mname]" if bmmovie == 2:
                scene callelaine with dissolve
                b "Hello"
                scene mporn_19 with dissolve
                $ bmmovie = 3
                ml "Hi [bname]"
                b "{i}(Sorry to disturb you, but is there any update?){/i}"
                b "{i}(About my role in the movie?){/i}"
                ml "Just go with her this Sunday"
                ml "And we hope it works"
                ml "It all depends on her answer"
                ml "If she accepts, Jonas have a scenario and will find actors to join in"
                b "{i}(Alright){/i}"
                b "{i}(Fingers crossed, thanks){/i}"
                scene broom_day with fade
                b "{i}(Great, can't wait){/i}"
                call screen gnav

            "Call Melinda to check what happened with Pedro" if jendidgo == 1:
                scene callelaine with dissolve
                b "Hello"
                scene mporn_19 with dissolve
                ml "Hi [bname]"
                b "{i}(So how was it with Pedro?){/i}"
                ml "He was very happy"
                ml "But he said that at some points she was rude"
                b "{i}(It's her first time doing this){/i}"
                b "{i}(Let's give her some time){/i}"
                ml "Yes"
                ml "Listen [bname] I'm a little busy now"
                ml "Let's talk another time"
                b "Yes, but don't forget me"
                ml "Of course"
                b "I'll make you happy don't worry"
                scene broom_day with fade
                b "{i}(Great, can't wait){/i}"
                call screen gnav

            "Check the porn site" if siteunlocked ==1:
                $ Hour += 1
                jump watchmporn

            "Study" if bstudied <2:
                $ Hour += 1
                $ bstudy += 1
                $ bstudied += 1
                $ brains += 1
                scene bcourse with fade
                b "Hmm good"
                scene broom_day with fade
                "..."
                call screen gnav
                
            "Exercise" if bexercise <2:
                if bandageremove ==0:
                    b "I cannot do exercises now"
                    scene broom_day with fade
                    "..."
                    call screen gnav
                elif bandageremove ==1:
                    scene bexer with fade
                    $ Hour += 1
                    $ bexercise += 1
                    $ physique += 1
                    "..."
                    if day==7:
                        scene bexerms with dissolve
                        m "[bname]!"
                        b "Yes?"
                        scene bexerms1 with dissolve
                        b "I was working out"
                        m "Good"
                        b "Yes, see?"
                        if physique >=10:
                            scene bexers4 with dissolve
                            m "Hmm"
                            scene bexerms2 with dissolve
                            m "Good"
                            show screen mrelup
                            m "Keep it up"
                            hide screen mrelup
                            $ mrel += 5
                            b "Thanks"
                            b "What did you want?"
                            m "I forgot"
                            m "What do you say we go to the gym together As before"
                            b "Sure"
                            m "Let's go during weekdays"
                            scene black with fade
                            "..."
                            jump broom_menu     
                        else:
                            scene bexers3 with dissolve
                            m "Looks the same to me"
                            scene black with fade
                            "..."
                            jump broom_menu

                    elif Hour==11:
                        scene bexerm with dissolve
                        m "[bname]!"
                        b "Huh"
                        scene bexerm1 with dissolve
                        b "I was working out"
                        b "I decided to take care of my body"
                        m "It's good"
                        b "Yes, see?"
                        if physique >=10:
                            scene bexers4 with dissolve
                            m "Hmm"
                            scene bexerm2 with dissolve
                            m "Good"
                            show screen mrelup
                            m "Keep it up"
                            hide screen mrelup
                            $ mrel += 5
                            b "Thanks"
                            b "What did you want?"
                            m "I forgot"
                            b "If you remember tell me"
                            m "Sure"
                            m "Why don't you come with me to the gym?"
                            menu:
                                "Yes":
                                    if wandagym == 3:
                                        m "I'll call Wanda if she wants to join"
                                        jump bmwjgym
                                    elif wandagym == 2:
                                        b "Maybe you can convince Wanda to send Joshua"
                                        m "I think I can do that"
                                        $ wandagym = 3
                                        jump bmwjgym
                                    else:
                                        jump bmgym
                                "Not today":
                                    b "Sorry I'm tired today"
                                    scene black with fade
                                    "..."
                                    jump broom_menu 

                        else:
                            scene bexers3 with dissolve
                            m "Looks the same to me"
                            scene black with fade
                            "..."
                            jump broom_menu
                    else:
                        scene bexer2 with dissolve
                        s "Looking after yourself, not bad eh!"
                        b "Huh!"
                        b "Yes, there's nothing wrong with that"
                        b "You can't rat on me"
                        scene bexers2 with dissolve
                        s "Show me"
                        b "Show you what?"
                        s "Your progress"
                        if physique >=10:
                            scene bexers4 with dissolve
                            s "Hmm"
                            scene bexers5 with dissolve
                            s "Not bad"
                            show screen srelup
                            s "Keep it up"
                            hide screen srelup
                            $ srel += 5
                            b "Thanks"
                            b "I think you should join me in the gym sometime"
                            s ang "Why? What's wrong with me? I'm perfect"
                            b "Yes but you have to maintain it"
                            s "Not this time [bname]"
                            b "Alright, I'll wait"
                            jump broom_menu
                        else:
                            scene bexers3 with dissolve
                            s "Hehe still the same"
                            scene black with fade
                            "..."
                            jump broom_menu
########################################################################gym

            "Check what you stole from the hospital":
                scene broom_medicine with fade
                b "{i}(I hide it inside the drawer){/i}"
                scene broom_medicine1 with dissolve
                b "{i}(My baby, you'll be useful when the time is right){/i}"
                menu:
                    "Inject yourself" if binjected ==0 and banesthetic >0:
                        scene broom_medicine2 with dissolve
                        b "{i}(Maybe the time is now){/i}"
                        $ binjected = 1
                        b "{i}(Let's try it for the day){/i}"
                        show screen anotify
                        b "{i}(That nursing course came in handy){/i}"
                        $ banesthetic -= 1
                        hide screen anotify
                        b "{i}(Let's rock!){/i}"
                        scene broom_day with fade
                        "..."
                        call screen gnav
                        

                    "Not needed now":
                        scene broom_day with fade
                        "..."
                        call screen gnav
            "Check Joshua cam recording" if josh_hidden_cam == 1:
                scene broom_camera1 with dissolve
                b "Hmm let's see"
                if firsttimecam ==0:
                    scene jhiddencam with dissolve
                    $ firsttimecam = 1
                    b "{i}(Cool, he set it up){/i}"
                    b "{i}(What an idiot, very bad angle){/i}"
                    scene jhiddencam1 with dissolve
                    b "Nothing"
                    scene jhiddencam1 with dissolve
                    b "Nothing"
                    b "Fast forward"
                    scene jhca with dissolve
                    b "Aha bingo"
                    scene jhca with dissolve
                    b "Nice girl"
                    b "Fast forward"
                    scene jhiddencam1 with dissolve
                    b "Nothing"
                    b "{i}(This idiot probably put it in the wrong shower){/i}"
                    b "I'll check another time"
                    scene broom_night with fade
                    "..."
                    call screen gnav

                elif firsttimecam >= 1 and firsttimecam <=2:
                    scene jhiddencam1 with dissolve
                    $ firsttimecam += 1
                    b "Nothing"
                    scene jhiddencam2 with dissolve
                    b "{i}(Damn, someone just closed the door){/i}"
                    b "Jackpot!"
                    scene jhiddencam3 with dissolve
                    b "{i}(I need to save this separately){/i}"
                    scene jhiddencam1 with fade
                    b "Ah she left"
                    b "I'll check another time"
                    scene broom_night with fade
                    "..."
                    call screen gnav

                elif firsttimecam >2 and persistent.unlock_65 == False:
                    scene jhiddencam1 with dissolve
                    $ firsttimecam += 1
                    b "Nothing"
                    scene jhiddencam2 with dissolve
                    b "{i}(Damn, again){/i}"
                    scene jhiddencam3 with dissolve
                    b "{i}(Is this Wanda){/i}"
                    scene jhiddencam4 with dissolve
                    b "Wow"
                    scene jhcw with dissolve
                    $ persistent.unlock_65 = True
                    b "Holy crap"
                    "..."
                    "..."
                    scene jhiddencam1 with fade
                    b "Damn, that's all of it"
                    b "I'll check another time"
                    scene broom_night with fade
                    "..."
                    call screen gnav

                elif firsttimecam >2 and wandashower ==0 :
                    $ firsttimecam += 1
                    $ wandashower = 1
                    b "Nothing"
                    scene jhiddencam2 with dissolve
                    $ persistent.unlock_76 = True
                    b "{i}(Hmmm){/i}"
                    scene jhiddencam5 with dissolve
                    "..."
                    scene jhiddencam6 with dissolve
                    "..."
                    scene jhiddencam4 with fade
                    "..."
                    scene jhcaw with dissolve
                    "..."
                    "...."
                    "....."
                    scene jhiddencam7 with dissolve
                    b "{i}(Wow){/i}"
                    scene jhiddencam8 with dissolve
                    b "{i}(Hmmm){/i}"
                    scene jhiddencam1 with fade
                    b "Damn, that's it!?"
                    b "I'll check another time"
                    scene broom_night with fade
                    "..."
                    call screen gnav

                elif firsttimecam >2 and persistent.unlock_76 == True and persistent.unlock_77 == False:
                    scene jjhiddencam with dissolve
                    $ persistent.unlock_77 = True
                    b "..."
                    scene jjhiddencam1 with dissolve
                    b "{i}(This idiot doesn't know that I can see the cam){/i}"
                    scene jjhiddencam2 with dissolve
                    "..."
                    scene jjhiddencam3 with dissolve
                    b "{i}(She saw him){/i}"
                    b "{i}(I wish I have audio to hear what they're talking){/i}"
                    scene jjhiddencam4 with dissolve
                    j "Ermm sorry"
                    j "I wanted to shower"
                    scene jjhiddencam5 with dissolve
                    ja "I thought you fell down"
                    ja "You can come and take a shower"
                    j "{i}(That's a good idea, I can send her away, no questions asked){/i}"
                    j "{i}(Especially from mom){/i}"
                    scene jjhiddencam6 with dissolve
                    b "{i}(Holy crap!){/i}"
                    scene jjhiddencam7 with dissolve
                    j "Come on get out"
                    ja "Wait"
                    j "What is it?"
                    ja "Something from the floor"
                    ja "A splinter"
                    ja "Can you try and remove it for me"
                    scene jjhiddencam8 with dissolve
                    j "Huh!"
                    j "Okay"
                    scene jjhiddencam9 with dissolve
                    b "What the fuck are they doing!?"
                    scene jjhiddencam10 with dissolve
                    "..."
                    scene jjhiddencam11 with dissolve
                    j "There's nothing"
                    ja "Hahaha"
                    ja "I prank you, there's no splinter"
                    j "Oh gosh"
                    scene jjhiddencam12 with dissolve
                    "..."
                    scene jjhiddencam13 with dissolve
                    b "{i}(She left, and the idiot is masturbating){/i}"
                    scene broom_night with fade
                    "..."
                    call screen gnav

                elif firsttimecam >2 and jfjaney == 0:
                    scene jjhiddencam with dissolve
                    b "..."
                    scene jjhiddencam1 with dissolve
                    b "{i}(This idiot doesn't know that I can see the cam){/i}"
                    scene jjhiddencam2 with dissolve
                    "..."
                    scene jjhiddencam3 with dissolve
                    b "{i}(She saw him){/i}"
                    b "{i}(I wish I have audio to hear what they're talking){/i}"
                    scene jjhiddencam4 with dissolve
                    j "Ermm sorry"
                    j "I wanted to shower"
                    scene jjhiddencam5 with dissolve
                    ja "I thought you fell down"
                    ja "You can come and take a shower"
                    j "{i}(That's a good idea, I can send her away, no questions asked){/i}"
                    j "{i}(Especially from mom){/i}"
                    scene jjhiddencam6 with dissolve
                    b "{i}(Holy crap!){/i}"
                    scene jjhiddencam7 with dissolve
                    j "Come on get out"
                    ja "Wait"
                    j "What is it?"
                    ja "Something from the floor"
                    ja "A splinter"
                    ja "Can you try and remove it for me"
                    scene jjhiddencam8 with dissolve
                    j "Huh!"
                    j "Okay"
                    scene jjhiddencam9 with dissolve
                    b "What the fuck are they doing!?"
                    scene jjhiddencam10 with dissolve
                    "..."
                    scene jjhiddencam11 with dissolve
                    j "There's nothing"
                    ja "Hahaha"
                    ja "I prank you, there's no splinter"
                    j "Oh gosh"
                    scene jjhiddencam12 with dissolve
                    "..."
                    scene jjhiddencam13 with dissolve
                    b "{i}(She left, and the idiot is masturbating){/i}"
                    scene broom_night with fade
                    "..."
                    call screen gnav


                elif firsttimecam >2 and jfjaney == 1:
                    scene jjhiddencam with dissolve
                    b "..."
                    scene jjhiddencam1 with dissolve
                    b "{i}(This idiot doesn't know that I can see the cam){/i}"
                    scene jjhiddencam2 with dissolve
                    "..."
                    scene jjhiddencam3 with dissolve
                    b "{i}(She saw him){/i}"
                    b "{i}(I wish I have audio to hear what they're talking){/i}"
                    scene jjhiddencam4 with dissolve
                    j "Ermm sorry"
                    j "I wanted to shower"
                    scene jjhiddencam5 with dissolve
                    ja "I thought you fell down"
                    ja "You can come and take a shower"
                    j "{i}(That's a good idea, I can send her away, no questions asked){/i}"
                    j "{i}(Especially from mom){/i}"
                    scene jjhiddencam6 with dissolve
                    b "{i}(Holy crap!){/i}"
                    scene jjhiddencam7 with dissolve
                    j "Come on get out"
                    ja "Wait"
                    j "What is it?"
                    ja "Something from the floor"
                    ja "A splinter"
                    ja "Can you try and remove it for me"
                    scene jjhiddencam8 with dissolve
                    j "Huh!"
                    j "Okay"
                    scene jjhiddencam9 with dissolve
                    b "What the fuck are they doing!?"
                    scene jjhiddencam10 with dissolve
                    "..."
                    scene jjhiddencam11 with dissolve
                    j "There's nothing"
                    ja "Hahaha"
                    ja "I prank you, there's no splinter"
                    j "Oh gosh"
                    scene jjhiddencam12 with dissolve
                    "..."
                    scene jjhiddencam13 with dissolve
                    b "{i}(She left, and the idiot is masturbating){/i}"
                    scene jjhiddencam14 with dissolve
                    ja "What are you doing?"
                    j "You're still here?"
                    ja "Yes I was drying up"
                    ja "What are you doing?"
                    j "Ah! Showering!"
                    scene jjhiddencam15 with dissolve
                    ja "Hahaha no, you're only washing your peepee"
                    ja "Stinky peepee hahaha"
                    scene jjhiddencam16 with dissolve
                    j "{i}(I should do what [bname] always tell me){/i}"
                    j "{i}(What would he do if it was him){/i}"
                    scene jjhiddencam17 with dissolve
                    j "You are also stinky"
                    ja "Not true"
                    ja "Mom says I smell like flowers"
                    j "You wanna bet who's more stinky?"
                    scene jjhiddencam18 with dissolve
                    b sur "..."
                    scene jjhiddencam19 with dissolve
                    b sur "..."
                    scene jjhiddencam20 with dissolve
                    ja "So do I smell like flowers?"
                    j "Yes but that's the body wash you used for showering"
                    ja "I win then"
                    j "No, not fair, I smell better than you"
                    j "Come smell for yourself"
                    ja "Phew ok"
                    scene jjhiddencam21 with dissolve
                    ja "I'm already smelling it here"
                    j "Oh yeah!"
                    j "Come closer"
                    scene jjhiddencam23 with hpunch
                    $ persistent.unlock_81 = True
                    j "Like this!"
                    ja "Ouch! My hair"
                    scene jjhiddencam22 with dissolve
                    ja "Please"
                    j "{i}(She might tell mom){/i}"
                    j "{i}(I should end this){/i}"
                    j "So you admit I smell better"
                    ja "Yes you do"
                    scene jjhiddencam24 with dissolve
                    b "{i}(Holy crap!){/i}"
                    scene jjhiddencam26 with dissolve
                    ja "I lied"
                    ja "You stink!"
                    j "Whatever"
                    scene jjhiddencam27 with dissolve
                    ja "..."
                    scene jjhiddencam25 with dissolve
                    b "Hmm"
                    b "{i}(Nothing more...){/i}"
                    b "{i}(I will as usual pretend I didn't see this){/i}"
                    scene broom_night with fade
                    "..."
                    call screen gnav



            "Return to your room screen":
                scene broom_day with fade
                "..."
                call screen gnav

    elif Hour >=18 and Hour <21:
        $ Hour += 1
        scene broom_night with fade
        b "Hmmm"
        b "What to do now?"
        menu:
            "Check Joshua cam recording" if josh_hidden_cam == 1:
                scene broom_camera1 with dissolve
                b "Hmm let's see"
                if firsttimecam ==0:
                    scene jhiddencam with dissolve
                    $ firsttimecam = 1
                    b "{i}(Cool, he set it up){/i}"
                    b "{i}(What an idiot, very bad angle){/i}"
                    scene jhiddencam1 with dissolve
                    b "Nothing"
                    scene jhiddencam1 with dissolve
                    b "Nothing"
                    b "Fast forward"
                    scene jhca with dissolve
                    b "Aha bingo"
                    scene jhca with dissolve
                    b "Nice girl"
                    b "Fast forward"
                    scene jhiddencam1 with dissolve
                    b "Nothing"
                    b "{i}(This idiot probably put it in the wrong shower){/i}"
                    b "I'll check another time"
                    scene broom_night with fade
                    "..."
                    call screen gnav

                elif firsttimecam >= 1 and firsttimecam <=2:
                    scene jhiddencam1 with dissolve
                    $ firsttimecam += 1
                    b "Nothing"
                    scene jhiddencam2 with dissolve
                    b "{i}(Damn, someone just closed the door){/i}"
                    b "Jackpot!"
                    scene jhiddencam3 with dissolve
                    b "{i}(I need to save this separately){/i}"
                    scene jhiddencam1 with fade
                    b "Ah she left"
                    b "I'll check another time"
                    scene broom_night with fade
                    "..."
                    call screen gnav

                elif firsttimecam >2 and persistent.unlock_65 == False:
                    scene jhiddencam1 with dissolve
                    $ firsttimecam += 1
                    b "Nothing"
                    scene jhiddencam2 with dissolve
                    b "{i}(Damn, again){/i}"
                    scene jhiddencam3 with dissolve
                    b "{i}(Is this Wanda){/i}"
                    scene jhiddencam4 with dissolve
                    b "Wow"
                    scene jhcw with dissolve
                    $ persistent.unlock_65 = True
                    b "Holy crap"
                    "..."
                    "..."
                    scene jhiddencam1 with fade
                    b "Damn, that's all of it"
                    b "I'll check another time"
                    scene broom_night with fade
                    "..."
                    call screen gnav

                elif firsttimecam >2 and wandashower == 1 :
                    $ wandashower = 1
                    $ firsttimecam += 1
                    b "Nothing"
                    scene jhiddencam2 with dissolve
                    $ persistent.unlock_76 = True
                    b "{i}(Hmmm){/i}"
                    scene jhiddencam5 with dissolve
                    "..."
                    scene jhiddencam6 with dissolve
                    "..."
                    scene jhiddencam4 with fade
                    "..."
                    scene jhcaw with dissolve
                    "..."
                    "...."
                    "....."
                    scene jhiddencam7 with dissolve
                    b "{i}(Wow){/i}"
                    scene jhiddencam8 with dissolve
                    b "{i}(Hmmm){/i}"
                    scene jhiddencam1 with fade
                    b "Damn, that's it!?"
                    b "I'll check another time"
                    scene broom_night with fade
                    "..."
                    call screen gnav

                elif firsttimecam >2 and persistent.unlock_76 == True:
                    scene jjhiddencam with dissolve
                    $ persistent.unlock_77 = True
                    b "..."
                    scene jjhiddencam1 with dissolve
                    b "{i}(This idiot doesn't know that I can see the cam){/i}"
                    scene jjhiddencam2 with dissolve
                    "..."
                    scene jjhiddencam3 with dissolve
                    b "{i}(She saw him){/i}"
                    b "{i}(I wish I have audio to hear what they're talking){/i}"
                    scene jjhiddencam4 with dissolve
                    j "Ermm sorry"
                    j "I wanted to shower"
                    scene jjhiddencam5 with dissolve
                    ja "I thought you fell down"
                    ja "You can come and take a shower"
                    j "{i}(That's a good idea, I can send her away, no questions asked){/i}"
                    j "{i}(Especially from mom){/i}"
                    scene jjhiddencam6 with dissolve
                    b "{i}(Holy crap!){/i}"
                    scene jjhiddencam7 with dissolve
                    j "Come on get out"
                    ja "Wait"
                    j "What is it?"
                    ja "Something from the floor"
                    ja "A splinter"
                    ja "Can you try and remove it for me"
                    scene jjhiddencam8 with dissolve
                    j "Huh!"
                    j "Okay"
                    scene jjhiddencam9 with dissolve
                    b "What the fuck are they doing!?"
                    scene jjhiddencam10 with dissolve
                    "..."
                    scene jjhiddencam11 with dissolve
                    j "There's nothing"
                    ja "Hahaha"
                    ja "I prank you, there's no splinter"
                    j "Oh gosh"
                    scene jjhiddencam12 with dissolve
                    "..."
                    scene jjhiddencam13 with dissolve
                    b "{i}(She left, and the idiot is masturbating){/i}"
                    scene broom_night with fade
                    "..."
                    call screen gnav


                    

            "Study" if bstudied <2:
                $ Hour += 1
                $ bstudy += 1
                $ bstudied += 1
                $ brains += 1
                scene bcourse with fade
                b "Hmm good good"
                scene broom_night with fade
                "..."
                call screen gnav

            "Check the porn site" if siteunlocked ==1:
                $ Hour += 1
                jump watchmporn
            

            "Check what you stole from the hospital":
                scene broom_medicine with fade
                b "{i}(I hide it inside the drawer){/i}"
                scene broom_medicine1 with dissolve
                b "{i}(My baby, you'll be useful when the time is right){/i}"
                menu:
                    "Inject yourself" if binjected ==0 and banesthetic >0:
                        scene broom_medicine2 with dissolve
                        b "{i}(Maybe the time is now){/i}"
                        $ binjected = 1
                        b "{i}(Let's try it for the day){/i}"
                        show screen anotify
                        b "{i}(That nursing course came in handy){/i}"
                        $ banesthetic -= 1
                        hide screen anotify
                        b "{i}(Let's rock!){/i}"
                        scene broom_night with fade
                        "..."
                        call screen gnav
                        

                    "Not needed now":
                        scene broom_night with fade
                        "..."
                        call screen gnav


            "Call Melinda and thank her for the movie" if melinda_daughters == 1:
                scene callelaine with fade
                b "Hi"
                ml "{i}(Hi [bname]){/i}"
                b "I want to thank you for the movie with [mname]"
                ml "{i}(No need to thank me, I enjoyed it as well){/i}"
                ml "{i}(Say why don't you come visit me and meet my daughters, Ann and Rhonda){/i}"
                ml "{i}(They're here for the day){/i}"
                b "Sure"
                ml "{i}(I'll send you the address){/i}"        
                scene rsnbathe2 with fade
                b "Wow"
                scene rsnbathe3 with dissolve
                ml "Hi [bname]"
                ml "That's Rhonda my daughter"
                scene rsnbathe4 with dissolve
                b "Hi Rhonda"
                rh "Hi"
                ml "[bname] Would you like to drink something"
                b "Yes wine please"
                ml "What about you Rhonda"
                rh "Nothing"
                ml "I'll be back"
                scene rsnbathe5 with dissolve
                rh "You look familiar"
                rh "Are you a friend of my brother?"
                b "I don't think so, I don't know"
                b "Who's your brother"
                rh "Daniel, do you know him?"
                scene rsnbathe6 with dissolve
                b "Daniel!"
                b "{i}(I knew it){/i}" 
                ml "Here's your drink [bname]"
                scene rsnbathe7 with dissolve
                b "Thank you"
                b "Aren't you drinking?"
                ml "No, I've got to go soon"
                ml "I have an important appointment"
                b "Ah I see"
                rh "I'm leaving also"
                scene rsnbathe8 with dissolve
                ml "Rhonda!"
                ml "You can't leave, stay a bit with [bname]"
                rh "Yeah right"
                scene rsnbathe9 with dissolve
                ml "Sorry [bname] Ann also left earlier"
                b "No problem, another time"
                b "I'll go now"
                b "{i}(Well, that was a short one){/i}"
                jump broom_menu


            "Call Melinda and ask about Pedro" if escortrequest ==3 and bstarmovie ==0:
                scene callelaine with fade
                b "Hey, how did it go with Pedro?"
                "..."
                ml "{i}(It was perfect, they agreed on a date next month){/i}"
                b "Oh next month! Too bad!"
                b "Okay and what about our movie agreement"
                ml "{i}(Let's discuss it){/i}"
                ml "{i}(Can you visit me?){/i}"
                b "Of course"
                scene melcall1 with fade
                ml "Hi [bname]"
                ml "Please have a seat"
                scene bmelanone3 with dissolve
                b "You promised if things work out with Pedro"
                b "I'll get to have my own movie"
                ml "Yes true"
                m "What's on your mind for the movie"
                menu:
                    "I want to have a movie with you":
                        scene bmelanone10 with dissolve
                        ml "I like your confidence"
                        b "Yeah"
                        ml "You know I can't show on porn movies"
                        b "Why not, a lot of important managers do star in their own movies"
                        b "Like that Daniela Storm, right?"
                        ml "I can't [bname]"
                        ml "But I can have it with you right now right here"
                        b "Ok"
                        b "Let's do it"
                        b "What if I bring [mname] with us?"
                        ml "Still I won't accept"
                        ml "But if you want, we can pretend to film something"
                        ml "That's if you can convince her"
                        b "Hmm"
                        b "I'll think about it"
                        ml "Ok"
                        scene bmelanone4a with dissolve
                        ml "Why don't you go first take a shower, I'll change and wait for you here"
                        scene bmelanone22 with fade
                        b "Wow"
                        ml "Come here"
                        scene bmelanone23 with dissolve
                        ml "..."
                        scene bmelanone24 with dissolve
                        ml "Not bad!"
                        ml "I know your favorite"
                        scene bmelanone25 with dissolve
                        ml "Everyone wants to titfuck Melinda"
                        scene bmelanone26 with dissolve
                        ml "Mmm yes"
                        scene bmelanone27 with dissolve
                        ml "Yess!"
                        b "They're fucking warm"
                        scene bmelanone28 with dissolve
                        b "Ahhh"
                        scene bmelanone29 with dissolve
                        b "Ahhh"
                        ml "..."
                        scene bmelanone30 with dissolve
                        ml "Mmm"
                        scene bmelanone31 with fade
                        b "Thank you... So..."
                        b "About convincing [mname]"
                        b "I have an idea"
                        ml "What is it?"
                        b "We say there's a filming for me and her"
                        b "And then you join us"
                        b "We just need to do a scenario"
                        b "Something like she's the maid and you acting as my mother"
                        b "You catch us having sex, and you decide to teach us both a lesson of sex"
                        ml "And what makes you think"
                        ml "She's going to flake out and let you down in the middle of the filming?"
                        b "Easy, another big gift will let her turn a blind eye"
                        ml "You demands seem to be growing day after day"
                        ml "But I'm going to give this one"
                        ml "What do you want to gift her?"
                        b "A bracelet maybe?"
                        ml "Ok fine"
                        scene broom_night with fade
                        $ bstarmovie = 1
                        b "{i}(Great){/i}"
                        $ mny += 1000
                        b "{i}(That Melinda is really nice, she even gave me $1000){/i}"
                        b "{i}(Now all I have to do is go to the main hall and wait for [mname]){/i}"
                        call screen gnav

                    "I want to have a movie with Rowena":
                        b "But I don't know if I can convince her"
                        "THIS OPTION IS NOT YET READY FOR THIS VERSION"
                        scene bmelanone10 with dissolve
                        ml "Until then, come here"
                        b "Yeah"
                        b "Can we do a movie together?"
                        ml "You know I can't show on porn movies"
                        b "Why not, a lot of important managers do star in their own movies"
                        b "Like that Daniela Storm, right?"
                        ml "I can't [bname]"
                        ml "But I can have it with you right now right here"
                        b "Ok"
                        b "What if I bring [mname] with us?"
                        ml "Still I won't accept"
                        ml "But if you want, we can pretend to film something"
                        ml "That's if you can convince her"
                        b "Hmm"
                        b "I'll think about it"
                        ml "Ok"
                        scene bmelanone4a with dissolve
                        ml "Why don't you go first take a shower, I'll change and wait for you here"
                        scene bmelanone22 with fade
                        b "Wow"
                        ml "Come here"
                        scene bmelanone23 with dissolve
                        ml "..."
                        scene bmelanone24 with dissolve
                        ml "Not bad!"
                        ml "I know your favorite"
                        scene bmelanone25 with dissolve
                        ml "Everyone wants to titfuck Melinda"
                        scene bmelanone26 with dissolve
                        ml "Mmm yes"
                        scene bmelanone27 with dissolve
                        ml "Yess!"
                        b "They're fucking warm"
                        scene bmelanone28 with dissolve
                        b "Ahhh"
                        scene bmelanone29 with dissolve
                        b "Ahhh"
                        ml "..."
                        scene bmelanone30 with dissolve
                        ml "Mmm"
                        scene bmelanone31 with fade
                        b "Thank you... So..."
                        b "About convincing [mname]"
                        b "I have an idea"
                        ml "What is it?"
                        b "We say there's a filming for me and her"
                        b "And then you join us"
                        b "We just need to do a scenario"
                        b "Something like she's the maid and you acting as my mother"
                        b "You catch us having sex, and you decide to teach us both a lesson of sex"
                        ml "And what makes you think"
                        ml "She's going to flake out and let you down in the middle of the filming?"
                        b "Easy, another big gift will let her turn a blind eye"
                        ml "You demands seem to be growing day after day"
                        ml "But I'm going to give this one"
                        ml "What do you want to gift her?"
                        b "A bracelet maybe?"
                        ml "Ok fine"
                        scene broom_night with fade
                        $ bstarmovie = 1
                        b "{i}(Great){/i}"
                        $ mny += 1000
                        b "{i}(That Melinda is really nice, she even gave me $1000){/i}"
                        b "{i}(Now all I have to do is go to the main hall and wait for [mname]){/i}"
                        call screen gnav



            "Call Melinda maybe she can help buying jewelry" if buyjewelry ==1 and escortrequest ==2 :
                scene callelaine with fade
                b "Hi, what's up"
                "..."
                scene melcall with dissolve
                ml "[bname]! Long time"
                b "There's something I wanted to ask you about"
                ml "What is it?"
                b "I prefer to say it in person, can I visit you?"
                scene melcall1 with fade
                ml "Hi [bname]"
                ml "Please have a seat"
                scene bmelanone3 with dissolve
                ml "The reason I called you is that I figured out a way"
                b "To make [mname] accept the request of the wealthy client"
                ml "You mean the maldives trip?"
                b "Yes"
                ml "Interesting"
                ml "And what is that way?"
                b "I just need to get her some good jewelry"
                ml "Are you sure, that's all it takes"
                b "Nothing is 100 percent sure, but I'm confident it might"
                ml "Ok, I'll give you what you want, and if you succeed"
                scene bmelanone10 with dissolve
                ml "I'll have you star in your own movie"
                b "You mean, I'll be on my own?"
                ml "Yes, you'll be the star"
                b "Cool"
                ml "Let's get the jewelry here, so you can give her when you return"
                b "Now?"
                b "I thought I can get the money and buy it myself"
                ml "No, it's better I choose something"
                ml "You don't know what to get"
                ml "I'll call my driver and tell him what to buy"
                b "Alright"
                $ buyjewelry = 2
                scene broom_night with fade
                $ persistent.unlock_58 = True
                b "{i}(Now all I have to do is go to the main hall and wait for [mname]){/i}"
                call screen gnav
                        


            "Call Melinda" if escortrequest ==0 and persistent.unlock_19 == True:
                scene callelaine with fade
                b "Hey I want to thank you for giving me a role in the movie"
                scene melcall with dissolve
                ml "[bname]! Long time"
                ml "Can you visit me? There's something Important I want to tell you"
                b "Ok sure"
                scene melcall1 with fade
                ml "...Yes it is still the top ranked movie clip"
                ml "Thanks to you"
                ml "Have a seat"
                scene bmelanone3 with dissolve
                ml "The reason I called you is that I have a proposal for [mname]"
                b "Oh this..."
                ml "Listen first"
                b "Ok"
                ml "One of my elite clients is interested in her"
                ml "And wants her to travel with him for a couple of days to the Maldives"
                ml "On his yacht"
                b "I think she won't accept"
                ml "How do you know?"
                ml "He's going to pay her 75 grand"
                ml "For 3 days"
                ml "And I know that she's planning to buy a car"
                ml "He's might take care of that, you never know"
                b sur "Huh, how do you know?! I don't even know about it"
                b "Oh wow, I need to figure how to ask her this"
                ml "Great"
                scene bmelanone4 with dissolve
                ml "Here's something you will need"
                ml "Buy her a gift and then ask her about it"
                ml "Buy a bikini that she will think about places where to use it"
                $ escortrequest = 1
                $ mny += 2000
                b "I see"
                b "Ok thanks"
                ml "You can go now"
                ml "Don't tell her the request came through me"
                b "Of course"
                scene broom_night with fade
                b "{i}(Interesting){/i}"
                scene broom_camera1 with dissolve
                b "{i}(Let's get this thing){/i}"
                b "{i}(Nice, they're going to deliver real quick){/i}"
                $ mny -= 1000
                call screen gnav

            "Return to your room screen":
                scene broom_night with fade
                "..."
                call screen gnav


    elif Hour >=21:
        scene broom_night with fade
        b "{i}(I should go to sleep){/i}"
        jump newday

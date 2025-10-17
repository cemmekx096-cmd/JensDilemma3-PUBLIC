

label mroom_menu:
    if Hour ==9:
        $ Hour += 1
        scene door with fade
        b "{i}(The door is locked){/i}"
        b "{i}(Maybe I can check the stairs){/i}"
        scene mstairs with fade
        "..."
        scene checkstairs with fade
        b "{i}(She's not here){/i}"
        b "{i}(I'll get back inside){/i}"
        scene hall_d with fade
        "..."
        call screen gnav

    elif Hour >=10 and Hour <=11 and day ==1:
        $ Hour += 1
        scene door with fade
        b "{i}(The door is open){/i}"
        b "Are you there?"
        m "Yes come in!"
        if mrel >=130:
            scene mroom_ironing1 with fade
            m "Yes dear?"
            b "{i}(Damn it, I need to fuck now){/i}"
            menu:
                "I think I'm still numb down there":
                    m "Hmm"
                    scene mroom_ironing2 with dissolve
                    m "Ok let me finish, and I'll take a look"
                    b "Ok"
                    m "Meanwhile, undress and sit on the bed"
                    scene mroom_ironing3_ with fade
                    m "Done"
                    scene mroom_ironing4_ with dissolve
                    m "Let's see"
                    if binjected ==0:
                        scene mroom_ironing5a_ with dissolve
                        m "..."
                        scene mroom_ironing5_ with dissolve
                        m "Doesn't look like numb at all"
                        m "You're just paranoid honey, go take nap"
                        b "{i}(Fuck!){/i}"
                        pass
                    else:
                        scene mroom_ironing5a_ with dissolve
                        m "Hmm"
                        m "Lay on your back"
                        scene mlhj_bg with fade
                        b "Ahh, I can't feel anything"
                        scene mroom_ironing6 with dissolve
                        m "I don't know dear, but I think it became harder than usual"
                        scene mlhj_bg with dissolve
                        b "No, it's not"
                        b "I feel like I am having a different penis"
                        m "Relax dear, we will visit the doctor soon"
                        m "You're just paranoid honey, go take nap"
                        b "{i}(Fuck!){/i}"
                        pass


                    scene hall_d with fade
                    "..."
                    call screen gnav

        else:
            scene mroom_ironing with fade
            m "Yes dear?"
            menu:
                "I think I'm still numb down there":
                    m "Dear give it few days"
                    b "Ok if you say so"
                    m "Anyway we have to visit the doctor soon for your stitches"
                    m "Don't worry honey, you'll be ok I'm sure"
                    b "Right"
                    scene hall_d with fade
                    "..."
                    call screen gnav


    elif Hour >=10 and Hour <=11 and day ==7:
        $ Hour += 1
        scene door with fade
        b "{i}(The door is open){/i}"
        b "Are you there?"
        m "Yes come in!"
        if mrel >=130:
            scene mroom_ironing1 with fade
            m "Yes dear?"
            b "{i}(Damn it, I need to fuck now){/i}"
            menu:
                "Do you need help?" if bandageremove ==1:
                    m "No honey, I'm ok, it's my duty"
                    m "Just go and relax"
                    scene mroom_ironing27 with dissolve
                    b "No, you should relax"
                    scene mroom_ironing28 with dissolve
                    m "[bname] you're going to tear it"
                    b "I won't"
                    m "Wait please"
                    m "Let me teach you how to do it"
                    scene mroom_ironing29 with dissolve
                    m "You see this hook here?"
                    scene mroom_ironing30 with dissolve
                    b "Yes I do"
                    m "That's what we usually undo before removing it"
                    m "You can go now"
                    b "What?"
                    scene mroom_ironing31 with dissolve
                    b "Not so fast"
                    m "[bname]!"
                    scene mroom_ironing32 with dissolve
                    m "No!"
                    m "Enough!"
                    scene mroom_ironing33 with dissolve
                    m "Sto...p"
                    m "Ahh"
                    scene mroom_ironing34 with dissolve
                    m "..."
                    b "Come here"
                    scene mroom_ironing35 with dissolve
                    m "..."
                    scene mroom_ironing36 with dissolve
                    m "Ahh"
                    scene mroom_ironing37 with dissolve
                    m "[bname] let me manage the rythm please"
                    scene ironanim with dissolve
                    m "Mmm"
                    m "..."
                    b "What is this?"
                    b "Faster!"
                    m "Mmm"
                    scene ironanimf with dissolve
                    b "..."
                    m "Ahhh"
                    b "Get down"
                    scene ironendanim with fade
                    m "..."
                    scene ironendanim300 with dissolve
                    m "..."
                    scene ironendanim340 with dissolve
                    m "Mmm"
                    scene ironendanim300 with dissolve
                    b "I'm about to explode"
                    scene ironendanim240 with dissolve
                    b "In your mouth"
                    scene ironendanim000 with dissolve
                    b "Keep it open!"
                    scene ironendanim060 with dissolve
                    b "Ahhh"
                    scene ironendanim081 with dissolve
                    b "Mmm"
                    scene ironendanim090 with dissolve
                    b "Mmhhm"
                    scene black
                    scene hall_d with fade
                    b "..."
                    call screen gnav

                "I think I'm still numb down there":
                    m "Hmm"
                    scene mroom_ironing2 with dissolve
                    m "Ok let me finish, and I'll take a look"
                    b "Ok"
                    m "Meanwhile, undress and sit on the bed"
                    scene mroom_ironing3 with fade
                    m "Done"
                    scene mroom_ironing4 with dissolve
                    m "Let's see"
                    if binjected ==0:
                        scene mroom_ironing5a with dissolve
                        m "..."
                        scene mroom_ironing5 with dissolve
                        m "Doesn't look like numb at all"
                        m "You're just paranoid honey, go take nap"
                        b "{i}(Fuck!){/i}"
                        pass
                    else:
                        scene mroom_ironing5a with dissolve
                        m "Hmm"
                        m "Lay on your back"
                        scene mlhj with fade
                        b "Ahh, I can't feel anything"
                        m "I don't know dear, but I think it became harder than usual"
                        scene mlhj with dissolve
                        b "No, it's not"
                        b "I feel like I am having a different penis"
                        if mrel >=150:
                            m "Ok, move over"
                            scene mlbj
                            play sound "sounds/msucking.mp3"
                            b "Ahh"
                            b "{i}(Yeah suck it){/i}"
                            stop sound
                            play sound "sounds/msucking.mp3"
                            b "Mmm"
                            b "It's not going to work"
                            b "Oh"
                            stop sound
                            scene mroom_ironing7 with dissolve
                            m "Your moans are saying otherwise"
                            b "Can we do it standing?"
                            scene mroom_ironing8 with dissolve
                            m "Mhhm"
                            b "What?"
                            m "I don't know [bname] but... it's better to see the doctor for such things"
                            m "We can't keep testing this"
                            b "I don't know... He's going to give me medicine and same shit"
                            b "If you don't want to, it's ok"
                            b "I'll wait few more days"
                            m "No, it's fine"
                            scene mroom_ironing9 with dissolve
                            b "Mm"
                            scene mroom_ironing10 with dissolve
                            b "{i}(She's fucking teasing me){/i}"
                            scene mroom_ironing11 with dissolve
                            b "..."
                            scene mroom_ironing12 with dissolve
                            m "..."
                            scene mroom_ironing13 with dissolve
                            m "Ugh"
                            scene mroom_ironing12 with dissolve
                            m "..."
                            b "{i}(Fuck she's choking){/i}"
                            b "Ahh fuck!"
                            scene mroom_ironing14 with hpunch
                            b "Ahhh"
                            scene mroom_ironing15 with fade
                            m "You see, you're ok"
                            m "Why don't you go take a nap"
                            pass
                        else:
                            m "Relax dear, we will visit the doctor soon"
                            m "You're just paranoid honey, go take a nap"
                            b "{i}(Fuck!){/i}"
                            pass


                    scene hall_d with fade
                    "..."
                    call screen gnav

        else:
            scene mroom_ironing with fade
            m "Yes dear?"
            menu:
                "I think I'm still numb down there":
                    m "Dear give it few days"
                    b "Ok if you say so"
                    m "Anyway we have to visit the doctor soon for your stitches"
                    m "Don't worry honey, you'll be ok I'm sure"
                    b "Right"
                    scene hall_d with fade
                    "..."
                    call screen gnav



    elif Hour >=10 and Hour <=11 and day !=7:
        $ Hour += 1
        scene door with fade
        b "{i}(The door is open){/i}"
        b "Are you there?"
        m "Yes come in!"
        if mrel >=130:
            scene mroom_ironing with fade
            m "Yes dear?"
            b "{i}(Damn it, I need to fuck now){/i}"
            menu:
                "You look tired, do you need help?" if bandageremove ==1:
                    m "Hmm"
                    scene mroom_ironing16 with dissolve
                    m "No honey, I'm Ok"
                    b "Let me finish this for you"
                    scene mroom_ironing17a with dissolve
                    b "Done"
                    m "Thank you honey"
                    scene mroom_ironing18a with dissolve
                    show screen mrelup
                    $ mrel += 5
                    m "..."
                    hide screen mrelup
                    m "Here my eyes"
                    b "Hehe"
                    m "Please go, I'm tired"
                    m "I need to get some rest"
                    if janeyseduction >= 2:
                        b "Can I click few photos of you?"
                        scene mroom_ironing19a with dissolve
                        m "Photos?"
                        m "What do you mean?"
                        b "Do you remember the website you told me about?"
                        m "Ah yes"
                        b "For that reason, I need to take few test photos"
                        m "Ok"
                        m "How do you want to take them?"
                        $ janeyseduction = 3
                        b "Nothing fancy, just pretend you are sleeping"
                        b "And put something light"
                        scene mroom_ironing21a with fade
                        m "Did you start?"
                        b "{i}(I did, but won't tell her){/i}"
                        b "Not yet"
                        m "Ok tell me so I know what to hide and how to pose"
                        b "You can start, I'll click"
                        scene mroom_ironing22a with dissolve
                        b "Nice"
                        scene mroom_ironing23a with dissolve
                        m "[bname] what are you doing?"
                        m "Not from here"
                        b "I didn't click"
                        m "Enough, leave"
                        b "Ok"
                        b "{i}(I took more photos than I expected, cool){/i}"
                        scene hall_d with fade
                        "THAT'S ALL FOR THE PHOTOS HERE"
                        call screen gnav
                    else:
                        pass
                    scene hall_d with fade
                    "..."
                    call screen gnav

                "I think I'm still numb down there":
                    m "Hmm"
                    scene mroom_ironing16 with dissolve
                    m "Ok let me finish, and I'll take a look"
                    b "Ok"
                    m "Meanwhile, undress and sit on the bed"
                    scene mroom_ironing17 with fade
                    m "Let's see it"
                    if binjected ==0:
                        scene mroom_ironing18 with dissolve
                        m "Hmm"
                        m "Doesn't look like numb at all"
                        m "You're just paranoid honey, go take nap"
                        b "{i}(Fuck! I forgot to inject myself){/i}"
                        pass
                    else:
                        m "Hmm"
                        m "Lay on your back"
                        scene mlhj_bg with fade
                        play sound "sounds/mitshard.mp3"
                        m "Mhm"
                        b "Ahh, I can't feel anything"
                        stop sound
                        scene mroom_ironing6 with dissolve
                        #origin
                        m "I don't know dear, but I think it became harder than usual"
                        scene mroom_ironing19 with dissolve
                        b "No, it's not"
                        b "I feel like I am having a different penis"
                        if mrel >=150:
                            m "Ok, move over"
                            scene mlbj with fade
                            play sound "sounds/msucking.mp3"
                            m "..."
                            stop sound fadeout 2.0
                            m "..."
                            play sound "sounds/msucking.mp3"
                            m "..."
                            stop sound fadeout 2.0
                            m "..."
                            scene mroom_ironing20 with dissolve
                            b "Ahh"
                            b "Mmm"
                            b "It's not going to work"
                            b "Oh"
                            m "Your moans are saying otherwise"
                            b "Can we do it another way?"
                            if mcorr >= 25:
                                m "I'll try one more time"
                                m "Stay as you are"
                                scene mroom_ironing20a with dissolve
                                b "Mmm"
                                b "I like this"
                                scene mroom_ironing21 with dissolve
                                b "Ahh"
                                scene mroom_ironing22 with dissolve
                                m "Ahh no movement [bname]"
                                m "Stay... As you are I said!"
                                scene mroom_ironing23 with dissolve
                                m "Hands off, let me take care of this"
                                scene mroom_ironing25 with dissolve
                                b "Ahh"
                                scene mroom_ironing26 with dissolve
                                b "Ahh"
                                scene mroom_ironing24 with fade
                                m "Mmm"
                                m "Finally you're getting back to normal"
                                scene hall_d with fade
                                "..."
                                call screen gnav
                            else:
                                "INCREASE CORRUPTION TO 25 POINTS AT LEAST"
                                pass
                            m "I don't know [bname] but... it's better to see the doctor for such things"
                            m "We can't keep testing this"
                            b "I don't know... He's going to give me medicine and same shit"
                            m "Give it few days more"
                            b "Ok"
                            scene mroom_ironing15_ with fade
                            m "You see, you're ok"
                            m "Why don't you go take a nap"
                            pass
                        else:
                            m "Relax dear, we will visit the doctor soon"
                            m "You're just paranoid honey, go take a nap"
                            b "{i}(Fuck!){/i}"
                            "RAISE YOUR POINTS TO 150"
                            pass


                    scene hall_d with fade
                    "..."
                    call screen gnav

        else:
            scene mroom_ironing with fade
            m "Yes dear?"
            menu:
                "I think I'm still numb down there":
                    m "Dear give it few days"
                    b "Ok if you say so"
                    m "Anyway we have to visit the doctor soon for your stitches"
                    m "Don't worry honey, you'll be ok I'm sure"
                    b "Right"
                    scene hall_d with fade
                    "..."
                    call screen gnav


    elif Hour ==12:
        if day !=7:
            $ Hour += 1
            scene door with fade
            b "{i}(The door is locked){/i}"
            b "{i}(Maybe I can check the stairs){/i}"
            scene mstairs with fade
            "..."
            scene checkstairs with fade
            b "{i}(She's not here){/i}"
            b "{i}(I'll get back inside){/i}"
            scene hall_d with fade
            "..."
            call screen gnav

        else:
            $ Hour += 1
            scene door with fade
            b "{i}(Looks like the door is open){/i}"
            menu:
                "Knock":
                    play sound "sounds/knock.ogg"
                    m "Who is it?"
                    b "It's me"
                    m "Enter"
                    stop sound
                    scene mroom_enter with fade
                    b "Sorry! I wanted to ask you something"
                    scene mroom_enter1 with dissolve
                    m "What is it?"
                    b "Eh it was..."
                    b "Is there anything I can do to help?"
                    scene mroom_entera with dissolve
                    $ mrel += 5
                    show screen mrelup
                    m "No honey, I don't want you to anything"
                    hide screen mrelup
                    m "Just go and chill"
                    b "Ok"
                    scene door with fade
                    b "{i}(...){/i}"
                    call screen gnav
                    
                "Enter":
                    scene mroom_knock with hpunch
                    m "[bname]!!?"
                    $ mrel -= 5
                    show screen mreldw
                    m "What's wrong?"
                    hide screen mreldw
                    b "Sorry"
                    b "I wanted to ask if there's anything I can help with"
                    m "No honey, I don't want you to anything"
                    m "Just go and chill"
                    b "Ok"
                    scene door with fade
                    b "{i}(...){/i}"
                    call screen gnav
                    scene door with fade
                    b "{i}(...){/i}"
                    call screen gnav



#########################

    elif Hour >12 and Hour <=21:
        if day !=7:
            if Hour == 14:
                $ Hour += 1
                scene door with fade
                b "{i}(The door is unlocked){/i}"
                play sound "sounds/knock.ogg"
                m "Come in"
                scene mvaina with dissolve
                m "Yes dear"
                m "How do you feel?"
                b "Bored"
                menu:
                    "Tell her about Melinda's request" if mellastrequest == 1:
                        b "There's something I want to tell you"
                        $ mellastrequest = 2
                        $ persistent.unlock_78 = True
                        scene mvaina1 with dissolve
                        m "What is it?"
                        b "There's a... gentleman who wants to get to know you"
                        scene mvaina3 with dissolve
                        m "Stop right there"
                        m "I don't want to know"
                        b "But"
                        scene mvaina4 with dissolve
                        m "What are you?"
                        m "My manager, doing soliciting!?"
                        b "But you lose nothing"
                        b "And he's offering a lot"
                        b "Just this time and then we're done with all this life"
                        scene mvaina5 with dissolve
                        m "Hmm"
                        m "Just go please"
                        b "Alright, but think about it"
                        scene hall_d with fade
                        b "{i}(I hope she does){/i}"
                        call screen gnav

                    "Continue":
                        pass

                "..."
                if snameacceptjoshua == 1 and snamecherylparty ==0:
                    b "There's something I want to ask you"
                    m "What is it?"
                    b "Did [sname] tell you about the party she's invited to?"
                    m "Yes and it's a no!"
                    b "I think you're making a mistake"
                    b "It's better if she keeps asking you, rather than sneaking without telling you"
                    b "Think about it, you're out most of the time"
                    b "And you won't be able to do this forever"
                    b "Plus you don't want her to rebel"
                    b "Just be on her side, and contain her"
                    scene mvaina1 with dissolve
                    m "You know, you're right"
                    m "I'll tell her I changed my mind"
                    b "Great"
                    $ snamecherylparty = 1
                    scene hall_d with fade
                    b "One promise fulfilled"
                    call screen gnav

                elif smorehelpwithjoshua ==1 and masqueradeaccepted ==0:
                    b "There's something I wanted to ask you"
                    m "What is it?"
                    b "Did [sname] tell you about the tanqueray?"
                    m "What's tanqueray?"
                    b "I don't remember but it's a tanqueray ball something something..."
                    m "Are you trying to be funny?"
                    b "No"
                    b "Why asking?"
                    m "It's called masquerade"
                    m "And my answer is no, I don't want her to go to such parties"
                    b "But why!?"
                    b "Do you want her sneaking out rather than asking you"
                    scene mvaina2 with dissolve
                    m "Tell her she can try sneaking"
                    b "Come on! Please"
                    m "No, I said No!"
                    scene hall_d with fade
                    b "Damn it"
                    b "{i}(I wonder what's with this masquerade){/i}"
                    call screen gnav

                else:
                    pass
                scene mvaina1 with dissolve
                m "I know, it's tough"
                m "But it's just a temporary period"
                m "Are you hungry?"
                m "I'll prepare something for you before I leave"
                m "Wait for me in the kitchen"
                scene hall_d with fade
                "..."
                call screen gnav

            else:
                scene door with fade
                b "{i}(The door is locked){/i}"
                call screen gnav
        else:
            if Hour >=17 and Hour<=18:
                $ Hour += 1
                scene door with fade
                b "{i}(The door seems to be open){/i}"
                "IF YOU COME TO THIS LOCATION AT THIS TIME"
                "YOU TRIGGER THE EVENT WHERE [mname] GOES OUT"
                "MAYBE YOU WANT TO KEEP HER AT HOME INSTEAD?"
                menu:
                    "Enter":
                        scene mroom_ent_outa with fade
                        b "{i}(Wow){/i}"
                        m "Yes [bname]?"
                        b "Sorry"
                        m "What is it?"
                        b "Nothing, are you going out?"
                        m "Yes darling"
                        b "Ok"
                        b "I'll leave you to get ready"
                        scene mroom_ent_out1 with dissolve
                        b "..."
                        m "I won't be late honey"
                        m "It's just for a couple of hours"
                        menu:
                            "Can I invite someone?":
                                b "So you can have peace of mind"
                                m "That's a good idea, they'll look after you?"
                                m "Elaine maybe?"
                                menu:
                                    "Yes Elaine":
                                        m "Great, I'll call her"
                                        jump elainebs
                                    "Is it possible Cheryl?":
                                        scene mroom_ent_out2a with dissolve
                                        m "Does it have to be her?"
                                        b "I mean, why not"
                                        m "Alright, but make sure she leaves before I come"
                                        m "And don't make a habit of it"
                                        jump cherylbs
                                    "The neighbors?":
                                        m "Ok sounds good"
                                        jump neighbs
                                    "Joshua":
                                        m "See if his mom allows him"
                                        b "Ok I'll call him now"
                                        jump joshuavisit

                            "Ok I'll wait for you":
                                scene mroom_ent_out3 with dissolve
                                b "Ok I'll wait for you"
                                jump waitform

                    "Knock":
                        play sound "sounds/knock.ogg"
                        m "Yes!"
                        b "It's me"
                        stop sound
                        m "Enter"
                        scene mroom_ent_outa with fade
                        b "{i}(Wow){/i}"
                        m "Yes [bname]?"
                        b "Sorry"
                        m "What is it?"
                        b "Nothing, are you going out?"
                        m "Yes darling"
                        b "Ok"
                        b "I'll leave you to get ready"
                        scene mroom_ent_out1 with dissolve
                        b "..."
                        m "I won't be late honey"
                        m "It's just for a couple of hours"
                        menu:
                            "Can I invite someone?":
                                b "So you can have peace of mind"
                                m "That's a good idea, they'll look after you?"
                                m "Elaine maybe?"
                                menu:
                                    "Yes Elaine":
                                        m "Great, I'll call her"
                                        jump elainebs
                                    "Is it possible Cheryl?":
                                        scene mroom_ent_out2a with dissolve
                                        m "Does it have to be her?"
                                        b "I mean, why not"
                                        m "Alright, but make sure she leaves before I come"
                                        m "And don't make a habit of it"
                                        jump cherylbs
                                    "The neighbors?":
                                        m "Ok sounds good"
                                        jump neighbs
                                    "Joshua":
                                        m "See if his mom allows him"
                                        b "Ok I'll call him now"
                                        jump joshuavisit


                            "Ok I'll wait for you":
                                scene mroom_ent_out3 with dissolve
                                $ Hour -= 1
                                b "Ok I'll wait for you"
                                jump waitform


                    "No need to enter or knock, I'll get back to the scene where I came from":
                        scene door with fade
                        b "{i}(Yes better not to){/i}"
                        call screen gnav
                        
            else:
                scene door with fade
                b "{i}(The door is locked){/i}"
                call screen gnav


    elif Hour >21:
        scene door with fade
        b "{i}(I should go to sleep){/i}"
        jump newday


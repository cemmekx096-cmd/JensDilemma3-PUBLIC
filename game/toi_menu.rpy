

label toi_menu:
    if Hour ==9:
        scene toidoor with fade
        b "Who's in?"
        s "[bname] it's me"
        menu:
            "Can I enter?":
                $ Hour += 1
                b "I need to pee"
                s "Wait"
                scene toid_s with dissolve
                s "Come in, is everything alright?"
                b "Yes just wanted to pee"
                s "Ok help yourself, I was just about to shower"
                scene toid_s1 with dissolve
                s "You guys will never learn to sit"
                scene toid_s2 with dissolve
                b "I usually sit, it's better"
                b "But not with such circumstances"
                s "Eek, ok"
                if janeyseduction == 2:
                    b "Mm can I ask a favor?"
                    $ persistent.unlock_51 = True
                    s  "What is it now?"
                    s "Ok, make it quick"
                    b "I'll pretend to hide in the laundry room"
                    $ janeyseduction = 3
                    scene toid_s6 with dissolve
                    b "Perfect"
                    s "Ok enough"
                    b "One more please"
                    b "At the mirror if you can"
                    scene toid_s7 with fade
                    b "Perfect"
                    s "Please go now, let me finish properly"
                    menu:
                        "Grab her" if bandageremove ==1:
                            scene toid_s8 with dissolve
                            s "Hey!"
                            s "Stop it"
                            scene toid_s9 with dissolve
                            s "Stop! I said"
                            b "You're acting all weird recently"
                            b "like you are some sort of celebrity"
                            s "Get out before I call [mname]"
                            pass
                        
                        "Continue":
                            pass
                    b "See you later"
                    scene toidoor with dissolve
                    "..."
                    call screen gnav


                if joshuacorrupted == 3 and snameacceptjoshua == 0:
                    menu:
                        "Ask her if she can help corrupting Joshua":
                            $ persistent.unlock_9 = True
                            b "Hey, can I ask for help?"
                            scene toid_s4 with dissolve
                            s "No, I'm not gonna blow you"
                            b "No no, it's not that"
                            b "I need your help with Joshua"
                            b "Remember when you came while we're playing a pc game?"
                            scene toid_s2 with dissolve
                            s "Yes... What is it about?"
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

                elif snametoiletjoshua ==1:
                    menu:
                        "Ask her if she can help corrupting Joshua":
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

                        "Leave":
                            pass
                else:
                    pass
                if scorr >=20 and josh_r_photos >=1:
                    scene toid_s5 with dissolve
                    b "Can I take some photos of you?"
                    s "For Joshua?"
                    b "Yes"
                    s "Ok, make it quick"
                    b "I'll pretend to hide here"
                    scene toid_s6 with dissolve
                    b "Perfect"
                    s "Ok enough"
                    b "One more please"
                    b "At the mirror if you can"
                    scene toid_s7 with fade
                    b "Perfect"
                    s "Please go now, let me finish properly"
                    pass

                else:
                    pass
                b "See you later"
                scene toidoor with dissolve
                "..."
                call screen gnav

            "Leave":
                scene toidoor with dissolve
                "..."
                call screen gnav


    elif Hour >=10 and Hour <=11:
        $ Hour += 1
        scene toi_d with fade
        b "{i}(No one here){/i}"
        b "{i}(And I don't want to use the toilet now){/i}"
        call screen gnav



    elif Hour >=12 and Hour <14:
        if Hour ==12 and day !=7:
            $ Hour += 1
            scene toidoor with fade
            b "Huh!"
            b "Who's in?"
            m "Hey!"
            b "Sorry but can I come in?"
            b "I need to use the toilet"
            m "Ok just a moment, don't enter yet"
            b "Ok"
            "..."
            m "You can come in now"
            if mrel >=120:
                scene toi_d_mshowerud2a with dissolve
                m "Honey are you ok?"
                menu:
                    "Looks like you want to tell me something" if jendidgo == 1:
                        m "Yes"
                        b "What is it?"
                        scene jendecisiontoilet with dissolve
                        m "I'm thinking about life"
                        b "Why? What's wrong with our life?"
                        m "I'm thinking to stop this porn star"
                        b "What!? No!!"
                        $ persistent.unlock_71 = True
                        $ jenlastmovie = 1
                        menu:
                            "Try to change her mind":
                                b "But why?"
                                m "I've made up my mind"
                                m "No why's!"
                                b "What's disturbing you?"
                                b "What can I do to change your mind?"
                                m "Nothing"
                                scene jendecisiontoilet1 with dissolve
                                m "I appreciate what you're trying to do [bname] but"
                                m "I'm done, seriously"
                                b "I don't want you to be sad"
                                scene jendecisiontoilet2 with dissolve
                                m "..."
                                b "Please change your mind"
                                m "I don't want [bname]"
                                scene jendecisiontoilet4 with dissolve
                                b "Please"
                                scene jendecisiontoilet5 with dissolve
                                m "..."
                                scene jendecisiontoilet6 with dissolve
                                m "..."
                                scene jendecisiontoilet7 with dissolve
                                "..."
                                scene jendecisiontoilet8 with fade
                                m "Ahhh"
                                scene jendecisiontoilet9 with dissolve
                                m "..."
                                scene jendecisiontoilet10 with dissolve
                                m "I won't change my mind [bname]"
                                pass
                            "Say nothing and continue":
                                pass
                        scene mhall_noona1 with fade
                        b "{i}(Damn that's bad news){/i}"
                        call screen gnav

                    "I wanted to pee, but":
                        m "But what?"
                        b "I don't know, this numbness down there is worrying me"
                        m "Let me see"
                        scene toi_d_mshowerud2b with dissolve
                        if mrel >=130 and binjected ==1:
                            m "It looks fine"
                            b "But it doesn't come up"
                            m "Come here"
                            scene toi_d_mshowerud2c with dissolve
                            m "Let me see it"
                            scene toi_d_mshowerud2e with dissolve
                            m "..."
                            scene toi_d_mshowerud2f with dissolve
                            m "..."
                            scene toi_d_mshowerud2g with dissolve
                            m "..."
                            scene toi_d_mshowerud2j with dissolve
                            m "Ahh"
                            scene toi_d_mshowerud2k with dissolve
                            m "Mmm"
                            scene toi_d_mshowerud2l with dissolve
                            m "Ah [bname]"
                            if persistent.patch_enabled:
                                s "mom are you in?"
                                pass
                            else:
                                s "[mname] are you in?"
                                pass
                            m "Huh!"
                            m "Get up"
                            scene toi_d_mshowerud2h with dissolve
                            s "I need to get something"
                            m "Yes honey, 2 more minutes please"
                            scene toi_d_mshowerud2i with dissolve
                            m "Time's up sweetheart, I think everything is ok"
                            b "..."
                            menu:
                                "I want to fuck now":
                                    scene toi_d_mshowerud2m with dissolve
                                    m "[bname]"
                                    if mrel >=140:
                                        m "That's risky"
                                        scene toi_d_mshowerud2n with dissolve
                                        $ persistent.unlock_15 = True
                                        b "Shh"
                                        scene toi_d_mshowerud2o with dissolve
                                        m "Ahh"
                                        scene toi_d_mshowerud2q with dissolve
                                        m "Mmm"
                                        scene toi_d_mshowerud2p with dissolve
                                        m "Ahh"
                                        b "You're so wet"
                                        scene toi_d_mshowerud2r with dissolve
                                        m "Fuck me slow"
                                        scene toi_d_mshowerud2s with dissolve
                                        m "Please"
                                        scene toi_d_mshowerud2t with dissolve
                                        m "[bname] I'm ..."
                                        scene toi_d_mshowerud2u with dissolve
                                        b "Me too"
                                        s "Huh"
                                        $ sbmbname = 1
                                        b "Get down"
                                        scene toi_d_mshowerud2v with dissolve
                                        m "Urghh"
                                        scene toi_d_mshowerud2w with dissolve
                                        b "Now, we can leave"
                                        pass
                                    else:
                                        m "No, please"
                                        m "It's risky, stop!"
                                        b "Damn, Ok"
                                        pass
                                "Continue":
                                    pass
                            scene room3 with fade
                            "..."
                            call screen gnav
                        else:
                            m "It looks fine"
                            b "But it doesn't come up"
                            m "It looks perfectly fine to me"
                            menu:
                                "Thanks for the compliment":
                                    b "You look drop dead gorgeous as well"
                                    show screen mcorr
                                    scene toi_d_mshowerud2d with dissolve
                                    m "..."
                                    hide screen mcorr
                                    $ mcorr += 5
                                    $ mrel += 5
                                    pass
                                "Ok":
                                    pass
                                
                            scene room3 with fade
                            "YOU NEED 130 POINTS OR MAYBE YOU FORGOT TO DO SOMETHING"
                            call screen gnav
                        
                    "Just wanted to pee":
                        scene toi_d_mshower1 with dissolve
                        b "..."
                        scene toi_d_mshowerud2a with dissolve
                        b "Thank you"
                        scene room3 with fade
                        "..."
                        call screen gnav
            else:
                pass
            scene toi_d_mshowerud2a with dissolve
            b "Hi"
            scene toi_d_mshower1 with dissolve
            b "Done"
            scene toi_d_mshowerud2a with dissolve
            b "Thank you"
            scene room3 with fade
            call screen gnav

        else:
            pass
        scene toi_d with fade
        b "{i}(No one is here){/i}"
        b "{i}(And I don't want to use the toilet now){/i}"
        call screen gnav


    elif Hour >=14 and Hour <=16:
        scene toi_d with fade
        b "{i}(No one here){/i}"
        b "{i}(And I don't want to use the toilet now){/i}"
        menu:
            "Do the laundry" if laundry == 0:
                $ Hour += 1
                $ laundry = 1
                b "{i}(Maybe I can do the laundry){/i}"
                jump laundry

            "Leave":
                "..."
                call screen gnav


    elif Hour ==17:
        scene toi_d with fade
        b "Hmm"
        menu:
            "I need to shower":
                b "{i}(Damn I forgot I cannot){/i}"
                scene toi_d with fade
                b "{i}(Maybe later when [mname] is here, she can brush my back){/i}"
                call screen gnav


    elif Hour >=18 and Hour <20:
        scene toi_n with fade
        b "{i}(No one here){/i}"
        b "{i}(And I don't want to use the toilet now){/i}"
        call screen gnav
        
    elif Hour ==20:
        "..."
        $ Hour += 1
        if day ==7:
            scene toidoor with fade
            "..."
            scene toidoor with vpunch
            m "Hey!"
            b "{i}(Shit){/i}"
            scene toi_m_n3a with dissolve
            m "[bname]?"
            b "Yeah sorry!"
            b "I didn't know"
            menu:
                "Can you give me a rub":
                    m "Of course, come in!"
                    m "Get undressed"
                    scene jdm3_37 with fade
                    b "Oh come on"
                    b "I'm not disabled"
                    scene jdm3_38 with dissolve
                    m "Maybe you are"
                    scene jdm3_39 with dissolve
                    m "Disabled under the belt"
                    scene jdm3_40 with dissolve
                    m "Hahaha"
                    b "It's not funny"
                    scene jdm3_41 with dissolve
                    m "Yes I'm sorry"
                    m "We're done"
                    scene jdm3_42 with dissolve
                    m "How does my big boy feel now"
                    b "{i}(Damn, such times make me feel shit){/i}"
                    b "{i}(The way I think about her){/i}"
                    b "{i}(All the evil thoughts){/i}"
                    m "Why silent all of a sudden"
                    b "Nothing, I was thinking how ungrateful I am"
                    b "Thank you"
                    scene jdm3_50 with dissolve
                    m "..."
                    call screen gnav
                        
                    
                "Leave":
                    scene toidoor with fade
                    b "Sorry"
                    call screen gnav

        else:
            scene toi_n with fade
            b "{i}(No one is here){/i}"
            call screen gnav
                
    elif Hour >=21:
        scene toi_n with fade
        b "{i}(No one is here){/i}"
        b "{i}(I should go to sleep){/i}"
        jump newday
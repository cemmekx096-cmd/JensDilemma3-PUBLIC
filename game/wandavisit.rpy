

label wandavisit:
    if today < datetime.date(2024, 12, 22):
        pass
    else:
        if christmas_withwanda_done == 0:
            $ christmas_withwanda_done = 1
            jump wandachristmas
        else:
            pass

    scene bna21c with fade
    m "Wanda! Please come in"
    $ persistent.unlock_1 = True
    scene bna22b with dissolve
    w "Hi [bname] how are you feeling?"
    menu:
        "Look at her cleavage":
            scene bna23d with dissolve
            $ wsusp += 1
            show screen wsuspup
            b "Better, thanks for asking"
            hide screen wsuspup
            pass
        "Focus on her eyes":
            scene bna24b with dissolve
            $ wsusp -= 1
            show screen wsuspdw
            b "Better, thanks for asking"
            hide screen wsuspdw
            pass
    m "Honey, why don't you take Joshua and play with your computer games"
    menu:
        "Sure":
            scene bna25b with dissolve
            b "Let's go"
            b "{i}(I need to find a way to hook this guy){/i}"
            pass
        "Convince Joshua to lurk and watch them" if persistent.unlock_36 == True:
            b "Come let's go"
            scene bna26d with dissolve
            m "Do you want to see my new dress?"
            scene bna26b with dissolve
            w "No [mname], not now"
            w "I don't want it to turn into our session from the gym"
            scene bna26d with dissolve
            b "{i}(I'm sure something is happening between them 2){/i}"
            b "Let's go Joshua"
    
    "..."        
    menu:
        "*Take him to your room to watch something*New*" if janeyseduction == 3:
            $ persistent.unlock_52 = True
            b "Let's go to my room"
            scene bna28b with fade
            b "I have something to show you"
            scene bna29f with dissolve
            j "Mmm"
            scene bna29e with dissolve
            j "..."
            scene bna30d with dissolve
            j "Ow!"
            if repeatjphotos ==0:
                $ repeatjphotos = 1
                b "Alright that's all, let's get back"
                b "{i}(NEXT time I'll kill him if he doesn't get me something){/i}"
                scene bna31b with fade
                m "Hey guys"
                w "Right on time, we should leave"
                scene bna32b with fade
                m "Good night"
                b "Good night"
                "TRY MORE OF THIS OPTION, IT'S LOADED"
                jump newday
            else:
                scene bna29g with dissolve
                j "Oh my God"
                b "Did you get me something?"
                j "What do you mean?"
                scene bna30e with dissolve
                if joshjaneyphotos ==0:
                    b "I mean I always show you photos"
                    b "And you never get me something in return"
                    b "Looks like you're taking advantage of me"
                    j "But it's not easy for me"
                    scene bna30f with dissolve
                    b "What's not easy? Getting some photos in the toilet?"
                    b "Or from the bedroom window?"
                    j "Ok Ok don't be angry"
                    j "I will try"
                    $ joshjaneyphotos = 1
                    b "Alright, let's get back"
                    scene bna31b with fade
                    m "Hey guys"
                    w "Right on time, we should leave"
                    scene bna32b with fade
                    m "Good night"
                    b "Good night"
                    jump newday
                elif joshjaneyphotos ==1:
                    b "I mean I always show you photos"
                    b "And you never get me something in return"
                    b "Looks like you're taking advantage of me"
                    j "It's not easy for me"
                    scene bna30f with dissolve
                    b "What's not easy? Getting some photos in the toilet?"
                    b "Or from the bedroom window?"
                    j "Ok Ok don't be angry"
                    j "I am trying"
                    $ joshjaneyphotos = 1
                    b "Alright, let's get back"
                    scene bna31b with fade
                    m "Hey guys"
                    w "Right on time, we should leave"
                    scene bna32b with fade
                    m "Good night"
                    b "Good night"
                    jump newday

                elif joshjaneyphotos ==2:
                    b "I mean I always show you photos"
                    b "And you never get me something in return"
                    b "Looks like you're taking advantage of me"
                    scene bna30g with dissolve
                    j "I've got something"
                    j "Here on my phone"
                    scene bna30h with dissolve
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
                    scene bna28b with dissolve
                    b "Wow, that was something"
                    b "Have you tried something with her?"
                    j "No"
                    b "Come on!"
                    scene bna28f with dissolve
                    j "No"
                    j "I can't, she's..."
                    b "She's what?"
                    scene bna28g with dissolve
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
                    scene bna28b with dissolve
                    j "Like what?"
                    b "Maybe you can visit me during the days?"
                    j "No, mom won't accept"
                    b "I'll see what I can do about that"
                    b "Let's get back to them"
                    scene bna31b with fade
                    m "Hey guys"
                    w "Right on time, we should leave"
                    scene bna32b with fade
                    b "Do you think, you can convince Wanda to let Joshua visit me during the days?"
                    m "Maybe"
                    b "Great"
                    m "What for?"
                    b "Just to continue the game, much better when we're in no rush"
                    m "Okay"
                    $ joshjaneyphotos = 3
                    m "Good night"
                    b "Good night"
                    "JOSHUA WILL VISIT AT 11:00 DURING WEEKDAYS MAKE SURE YOU ARE NOT BUSY WITH SOMETHING ELSE"
                    jump newday

                elif joshjaneyphotos ==3 and buyjewelry <=2:   
                    scene bna30g with dissolve
                    b "So do you have anything?"
                    j "The same on my phone"
                    b "Let me see"
                    scene bna30h with dissolve
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
                    scene bna31b with fade
                    m "Hey guys"
                    w "Right on time, we should leave"
                    scene bna32b with fade
                    m "Good night"
                    b "Good night"
                    jump newday


                elif buyjewelry ==3:
                    scene bna30g with dissolve
                    b "So do you have anything?"
                    j "Yes I have something new"
                    b "Let me see"
                    scene bna30h with dissolve
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
                    scene jstj5 with dissolve
                    b "I can never be bored with this"
                    b "..."
                    menu:
                        "Man if  only she's living in my house":
                            j "What would you do?"
                            scene jstj6 with dissolve
                            b "I would ram my cock into her sweet hairy pussy"
                            scene bna30d with dissolve
                            $ jcorr += 1
                            show screen jcorr
                            j "Oh wow"
                            hide screen jcorr
                            pass
                        "Let's get back":
                            pass
                    b "Let's get back to them"
                    scene bna31b with fade
                    m "Hey guys"
                    w "Right on time, we should leave"
                    scene bna32b with fade
                    m "Good night"
                    b "Good night"
                    "THAT WAS ALL HERE"
                    jump newday



        "What do you want to do?" if persistent.unlock_37 == True:
            j "Let's go to your room"
            b "Do you want to drink cola with me?"
            j "Can I?"
            scene bna26c with dissolve
            w "Uh huh"
            scene bna25c with dissolve
            b "Hmm"
            scene bna28d with fade
            "WHILE YOU ARE CHATTING"
            s "Hey [bname]"
            scene bna33b with dissolve
            s "Oh sorry I didn't know Joshua is here"
            scene bna34b with dissolve
            s "I wanted to ask you something but it's fine"
            s "I'll go take a bath first"
            scene jbst1 with dissolve
            j "Oh God I think I need to use the bathroom again"
            j "My stomach is rumbling suddenly"
            if unlock43 == 0:
                scene jbst22a with fade
                $ unlock43 = 1
                j "Huh"
                j "..."
                j "{i}(Oh my God){/i}"
                scene jbst11 with fade
                "..."
                scene jbst12 with dissolve
                j "{i}(I'm done){/i}"
                scene jbst22a with dissolve
                j "{i}(It's better I leave){/i}"
                scene jbst23a with dissolve
                s "{i}(What an idiot, he left){/i}"
                s "{i}(I'll try something more next time){/i}"
                scene jbst19 with fade
                b "Hey man, you came quick this time?"
                j "Yes my stomach feels better"
                scene jbst20 with dissolve
                b "{i}(Hmmm){/i}"
                j "I think it's time to go"
                b lau "Alright, let's get back"
                scene bna31b with fade
                m "Hey guys"
                w "Right on time, we should leave"
                scene bna32b with fade
                m "What's wrong with him, he look all flushed"
                b "I have no idea"
                m "Well, whatever"
                m "Good night"
                b "Good night"
                scene jbst21 with fade
                b "Hey, what happened?"
                s "He simply left"
                b "Did he do something?"
                s "No"
                b "Damn"
                s "I'll do something else next time"
                b "Thanks for tonight"
                s "You owe me one"
                s "Go ask [mname] about my masquerade"
                b "Sure"
                jump newday
            else:
                pass
            scene jbst22 with fade
            j "Huh"
            j "..."
            scene jbst23 with dissolve
            j "..."
            scene jbst24 with dissolve
            j "{i}(I'll take this){/i}"
            scene jbst25 with dissolve
            j "Huh"
            scene jbst26 with dissolve
            j "..."
            scene jbst11 with fade
            "..."
            scene jbst12 with dissolve
            j "{i}(I'm done){/i}"
            j "{i}(Shall I take another look?){/i}"
            scene jbst27 with dissolve
            "..."
            scene jbst28 with dissolve
            $ persistent.unlock_43 = True
            j "{i}(...){/i}"
            scene jbst29 with dissolve
            j "{i}(It's better I leave){/i}"
            scene jbst19 with fade
            b "Hey man, you came quick this time?"
            j "Yes my stomach feels better"
            scene jbst20 with dissolve
            b "{i}(Hmmm){/i}"
            if josh_r_photos ==0:
                j "Ermm [bname], do you have any new photos on your phone?"
                $ josh_r_photos = 1
                b "I have but probably you've seen then"
                j "Ok"
                b "Don't worry, I'll take new ones, and will share with you"
                j "Alright"
                pass
            else:
                pass

            j "I think it's time to go"
            b lau "Alright, let's get back"
            scene bna31b with fade
            m "Hey guys"
            w "Right on time, we should leave"
            scene bna32b with fade
            m "What's wrong with him, he look all flushed"
            b "I have no idea"
            m "Well, whatever"
            m "Good night"
            b "Good night"
            scene jbst21 with fade
            b "Hey, what happened?"
            s "Happy now?"
            b "Oh my god, he looks destroyed"
            b "Did he do something?"
            s "No, he just slurped some words, turned and left"
            b "I think we need to make you helpless"
            b "Maybe put a mask on and pretend to do yoga or meditate"
            b "We need an inviting pose, so he can have the confidence"
            b "But that's for next version"
            s "Ok"
            b "Thanks for tonight"
            s "You owe me one"
            s "Go ask [mname] about my masquerade"
            b "Sure"
            jump newday

        "Sit and talk" if joshuatoilet >= 2 and smorehelpwithjoshua ==1 and masqueradeaccepted ==0:
            b "Do you want to drink cola with me?"
            j "Can I?"
            scene bna26c with dissolve
            w "Uh huh"
            scene bna25c with dissolve
            b "Hmm"
            scene bna28d with fade
            "WHILE YOU ARE CHATTING"
            s "Hey [bname]"
            scene bna33b with dissolve
            s "Oh sorry I didn't know Joshua is here"
            scene bna34b with dissolve
            s "I wanted to ask you something but it's fine"
            s "I'll go take a bath first"
            b "Yes [sname] take a bath first and then I'll check your phone"
            s "Ok I'll go now"
            scene jbst2a with dissolve
            b "Joshua you know where the bathroom is in case you need to"
            scene jbst1 with dissolve
            j "Oh God yes I think I need to"
            j "My stomach is rumbling suddenly"
            scene jbst6 with fade
            j "Where is the..."
            scene jbst7 with dissolve
            j "Ahhh"
            scene jbst8 with dissolve
            j "Sorry!"
            scene jbst9 with dissolve
            j "I'm so sorry, I needed to use the toilet"
            j "And [bname] showed me the way to this one"
            j "I... I didn't know it's the one..."
            j "I'm really sorry"
            s "Joshua chill, you can use it"
            j "But"
            s "Well you have two options"
            s "Either wait till I finish, or use it now"
            s "Is it ok?"
            s "Don't worry"
            s "I need time to finish, and you're hidden in there anyway"
            scene jbst10 with fade
            j "Ahhh"
            scene jbst11 with dissolve
            j "Ahh"
            s "What's wrong?"
            scene jbst12 with dissolve
            j "My stomach..."
            scene jbst13 with dissolve
            j "Oh my God [sname]"
            scene jbst14a with dissolve
            s "Oh my god"
            j "You said you're not going to come here"
            scene jbst15b with dissolve
            s "Are you okay?"
            j "Please, I'm not comfortable with this"
            s "Okay, I'll get you some meds"
            scene jbst15a with dissolve
            s "Here"
            scene jbst15b with dissolve
            s "Take this"
            j "..."
            j "Thanks"
            scene jbst12 with fade
            j "I'm done"
            s "Are you feeling better?"
            j "Yes thanks, that was good"
            scene jbst18a with dissolve
            $ persistent.unlock_37 = True
            j "Oh!"
            s "What?"
            j "I'm..."
            scene jbst18b with dissolve
            s "Come on, haven't you seen a naked girl before?"
            scene jbst18c with dissolve
            j "Ehh"
            j "I got to go"
            #scene jbst19a with dissolve
            #s "Don't you want to feel them?"
            scene jbst19 with fade
            b "Hey man, what took you so long?"
            j "My stomach was acting up"
            scene jbst20 with dissolve
            b "{i}(Hehehe I wonder what did she do to him){/i}"
            j "I think it's time to go"
            b lau "Alright, let's get back"
            scene bna31b with fade
            m "Hey guys"
            w "Right on time, we should leave"
            scene bna32b with fade
            m "What's wrong with him, he look all flushed"
            b "I have no idea"
            m "Well, whatever"
            m "Good night"
            b "Good night"
            scene jbst21 with fade
            b "Hey, what happened?"
            s "Happy now?"
            b "Oh my god, he looks destroyed"
            b "Did he do something?"
            s "No, he just slurped some words, turned and left"
            b "I think we need to make you helpless"
            b "Maybe put a mask on and pretend to do yoga or meditate"
            b "We need an inviting pose, so he can have the confidence"
            b "But that's for next version"
            s "Ok"
            b "Thanks for tonight"
            s "You owe me one"
            s "Go ask [mname] about my masquerade"
            b "Sure"
            jump newday

        "Sit and talk" if joshuatoilet >= 2 and colaspike<4:
            if colaspike >= 1 and colaspike <=3:
                if colaspike ==1:
                    $ colaspike = 2
                else:
                    pass
                b "Do you want to drink cola with me?"
                j "Can I?"
                scene bna26c with dissolve
                w "Uh huh"
                scene bna25c with dissolve
                b "Hmm"
                scene bna28d with fade
                "WHILE YOU ARE CHATTING"
                s "Hey [bname]"
                scene bna33b with dissolve
                s "Oh sorry I didn't know Joshua is here"
                scene bna34b with dissolve
                s "I wanted to ask you something but it's fine"
                s "I'll go take a bath first"
                b "Yes [sname] take a bath first and then I'll check your phone"
                s "Ok I'll go now"
                scene jbst2a with dissolve
                b "Joshua you know where the bathroom is in case you need to"
                scene jbst1 with dissolve
                j "Oh God yes I think I need to"
                j "My stomach is rumbling suddenly"
                scene jbst6 with fade
                j "Where is the..."
                scene jbst7 with dissolve
                j "Ahhh"
                scene jbst8 with dissolve
                j "Sorry!"
                scene jbst9 with dissolve
                j "I'm so sorry, I needed to use the toilet"
                j "And [bname] showed me the way to this one"
                j "I... I didn't know it's the one..."
                j "I'm really sorry"
                s "Joshua chill, you can use it"
                j "But"
                s "Well you have two options"
                s "Either wait till I finish, or use it now"
                s "Is it ok?"
                s "Don't worry"
                s "I need time to finish, and you're hidden in there anyway"
                scene jbst10 with fade
                j "Ahhh"
                scene jbst11 with dissolve
                j "Ahh"
                s "Are you ok?"
                scene jbst12 with dissolve
                j "No, my stomach is killing me"
                scene jbst13 with dissolve
                j "Oh my God [sname]"
                scene jbst14 with dissolve
                j "You said you're not going to come here"
                s "Relax, I'll get you some medicine for your upset stomach"
                s "Your moans scared me"
                s "Sit tight, I'll get it for you"
                j "{i}(Oh thanks God she's leaving){/i}"
                scene jbst15 with dissolve
                s "Now where did I keep this thing?"
                scene jbst16 with dissolve
                s "{i}(Poor boy){/i}"
                if colaspike ==3:
                    $ colaspike = 4
                    scene jbst15a with dissolve
                    j "Ahh"
                    pass
                else:
                    pass
                scene jbst17 with dissolve
                s "Here drink this"
                j "Uh...Thank you"
                s "I'll continue my shower now"
                scene jbst18 with fade
                j "Thank you"
                s "Glad that you are ok"
                scene jbst19 with fade
                b "Hey man, what took you so long?"
                j "My stomach was acting up"
                scene jbst20 with dissolve
                b "{i}(Hehehe I wonder what did she do to him){/i}"
                $ persistent.unlock_22 = True
                j "I think it's time to go"
                b lau "Alright, let's get back"
                scene bna31b with fade
                m "Hey guys"
                w "Right on time, we should leave"
                scene bna32b with fade
                m "What's wrong with him, he look all flushed"
                b "I have no idea"
                m "Well, whatever"
                m "Good night"
                b "Good night"
                scene jbst21 with fade
                b "Hey, what happened?"
                s "Happy now?"
                if colaspike ==4:
                    b "No, I want you to stop doing this"
                    s "Why? I thought you wanted to tease him"
                    b "I did, but it's enough, I need to teach him a lesson"
                    s "Ok"
                    s "But you still owe me one"
                    b "Sure, good night"
                    jump newday
                else:
                    pass
                b "Oh my god, he looks destroyed"
                s "That was easy baby, next time bring some tougher nut"
                b "Yeah, thanks for tonight"
                s "You owe me one"
                b "Sure, good night"
                jump newday
            elif colaspike == 4:
                b "Do you want to drink cola with me?"
                j "Can I?"
                scene bna26c with dissolve
                w "Uh huh"
                scene bna25c with dissolve
                b "Hmm"
                scene bna28d with fade
                "WHILE YOU ARE CHATTING"
                s "Hey [bname]"
                scene bna33b with dissolve
                s "Oh sorry I didn't know Joshua is here"
                scene bna34b with dissolve
                s "I wanted to ask you something but it's fine"
                s "I'll go take a bath first"
                b "Yes [sname] take a bath first and then I'll check your phone"
                s "Ok I'll go now"
                scene jbst2a with dissolve
                b "Joshua you know where the bathroom is in case you need to"
                scene jbst1 with dissolve
                j "Oh God yes I think I need to"
                j "My stomach is rumbling suddenly"
                scene jbst6a with fade
                j "Huh"
                j "{i}(No one is here){/i}"
                scene jbst12 with fade
                j "Ah God"
                scene jbst20a with fade
                j "Shall we go?"
                b "{i}(Aha, empty handed eh!?){/i}"
                b "Yes let's go"
                if wandagym == 2:
                    scene black
                    "MEANWHILE"
                    scene bna42 with fade
                    $ wandagym = 3
                    w "Yes true"
                    m "And he should gain some weight"
                    w "I've tried, his dad equipped a home gym, just for him"
                    w "Still he barely uses it"
                    m "You know what? [bname] was telling me if you allow him to train with him"
                    m "Maybe this can give him an incentive"
                    scene bna43 with dissolve
                    w "That's not a bad idea"
                    w "We can train all together"
                    scene bna42 with dissolve
                    m "Yes, it's much better if we're all there, he wouldn't want to miss out"
                    w "But we're going to be too many in our small room"
                    m "We can go to our public gym"
                    w "Ok, sounds good enough"
                    m "I'll call you when we go"
                    b "We're back"
                    scene bna31b with dissolve
                    m "Hey guys"
                    w "Right on time, we should leave"
                    scene bna32b with fade
                    m "Good night"
                    b "Good night"
                    jump newday
                else:
                    scene bna31b with fade
                    m "Hey guys"
                    w "Right on time, we should leave"
                    scene bna32b with fade
                    m "Good night"
                    b "Good night"
                    jump newday



            else:
                pass
            scene bna26b with dissolve
            w "My darling is so innocent and timid"
            m "Don't worry Wanda, [bname] is also..."
            m "I wouldn't say innocent, but he's a good boy"
            #scene jbst with dissolve
            scene bna28b with dissolve
            #alien away
            b "So, do you play any sports?"
            b "Apart from the regular gym"
            j "No, just the gym at home"
            j "And I do it only because my mom pushes me to do it"
            if snametoiletjoshua ==0:
                "AFTER CHATTING FOR A WHILE"
                b "{i}(Hmm I've got an idea){/i}"
                $ snametoiletjoshua = 1
                b "{i}(Maybe I can show him that it's ok to visit the bathroom alone){/i}"
                #scene jbst1 with dissolve
                scene bna28b with dissolve
                b "You can use the bathroom if you want to, it's the last door down the corridor"
                j "I don't need to"
                b "Just saying in case you're shy to ask"
                j "Oh yes, thank you"
                j "I think it's time to go"
                b "Alright, let's get back"
                scene bna31b with fade
                m "Hey guys"
                w "Right on time, we should leave"
                scene bna32b with fade
                m "Good night [bname]"
                b "Good night"
                jump newday
            elif snametoiletjoshua ==1:
                #scene jbst1 with dissolve
                scene bna28b with dissolve
                b "You know where the bathroom is in case you need"
                j "No, thanks, I'm still ok"
                b "Just saying"
                j "Oh thank you"
                j "I think it's time to go"
                b "Alright, let's get back"
                b "{i}(Damn, I think I need to ask [sname] for help){/i}"
                scene bna31b with fade
                m "Hey guys"
                w "Right on time, we should leave"
                scene bna32b with fade
                m "Good night [bname]"
                b "Good night"
                jump newday

            elif snametoiletjoshua ==2:
                scene bna28b with dissolve
                "WHILE YOU ARE CHATTING"
                s "Hey [bname]"
                scene bna33b with dissolve
                s "Oh sorry I didn't know Joshua is here"
                scene bna34b with dissolve
                s "I wanted to ask you something but it's fine"
                s "I'll go take a bath first"
                b "Yes [sname] take a bath first and then I'll check your phone"
                s "Ok I'll go now"
                scene jbst2 with dissolve
                b "Joshua you know where the bathroom is in case you need to"
                #scene jbst1 with dissolve
                #render original jbst2 on alien
                scene bna28b with dissolve
                j "Oh no, thanks, I'm still ok"
                $ persistent.unlock_17 = True
                b lau "Just saying hehehe"
                j "I think it's time to go"
                b "Alright, let's get back"
                b "{i}(What a loser){/i}"
                scene bna31b with fade
                m "Hey guys"
                w "Right on time, we should leave"
                scene bna32b with fade
                m "Good night [bname]"
                b "Good night"
                scene jbst3 with fade
                s "..."
                play sound "sounds/door_openc.wav"
                s "{i}(That must be Joshua){/i}"
                stop sound
                scene jbst4 with dissolve
                s "Oops sorry"
                scene jbst5 with dissolve
                s "You?!"
                b "Yes, I came to tell you abort mission"
                b "They left"
                b "He's an idiot"
                s "Ok"
                $ colaspike = 1
                b "Thanks anyway"
                scene jbst4 with dissolve
                s "I have an idea"
                b "What is it?"
                s "Why don't you put castor oil in his drink"
                s "You offer him cola and few drops will do the job"
                b "And what does it do?"
                s "It's a natural laxative"
                s "Here I have some, I use it for my acne"
                s "Just keep it in the kitchen"
                b "Cool thanks"
                b "Good night"
                jump newday
                
            else:
                #scene jbst1 with dissolve
                scene bna28b with dissolve
                b "You know where the bathroom is in case you need"
                j "No, thanks, I'm still ok"
                b "Just saying hehehe"
                j "Oh thank you"
                j "I think it's time to go"
                b "Alright, let's get back"
                scene bna31b with fade
                m "Hey guys"
                w "Right on time, we should leave"
                scene bna32b with fade
                m "Good night [bname]"
                b "Good night"
                jump newday

        "Play a computer game together":
            scene bna26b with dissolve
            w "My darling is so innocent and timid"
            m "Don't worry Wanda, [bname] is also..."
            m "I wouldn't say innocent, but he's a good boy"
            pass
    scene bna27b with dissolve
    b "You did good!"
    j "Thanks"
    if joshuacorrupted ==0:
        b "{i}(Now is the time){/i}"
        $ joshuacorrupted = 1
        b "Let me see what else we can play"
        b "Do you like going to the beach?"
        j "Yes, but I'm sorry I can't join you, you know, my mom and stuff"
        j "We usually stay at the pool at home, or our yacht"
        b "Ok I understand"
        b "But beach is nice, you don't know what you're missing"
        j "It's not that I've never been to the beach, but recently I have not"
        b "Let me show you some photos from our beach last year"
        scene bna29c with dissolve
        b "Here"
        scene bna30b with dissolve
        j "That's..."
        j "That's...[sname]?"
        b "Yes"
        b "{i}(It seems he has a thing for [sname]){/i}"
        b "{i}(Bingo){/i}"
        scene bna29c with dissolve
        b "This was last week"
        scene bna30b with dissolve
        b "I have plenty like that if you want to see"
        scene bna28b with dissolve
        j "Can I?"
        b "{i}(You pervert){/i}"
        b "Yes..."
        j "I mean... No"
        j "It's late now..."
        b "Alright as you wish"
        j "Maybe next time"
        scene bna31b with fade
        m "Hey guys"
        w "Right on time, we should leave"
        scene bna32b with fade
        m "Good night [bname]"
        b "Good night"
        "NOW YOU CAN VISIT THEM ON SUNDAY"
        jump newday

    elif joshuacorrupted ==1:
        b "Let me see what else we can play"
        j "Did you go to the beach?"
        b "{i}(Hmm interesting){/i}"
        b "Yes, but I didn't take photos"
        b "We did some before leaving home"
        scene bna29b with dissolve
        $ joshuacorrupted = 2
        b "Here"
        scene bna30b with dissolve
        j "Ah nice"
        b "Yes"
        scene bna29b with dissolve
        b "This was just before we went to the beach, she wanted to check on something and I snapped this photo to show her"
        scene bna30b with dissolve
        b "I have plenty like that if you want to see"
        scene bna28b with dissolve
        j "It's late now..."
        b "Alright as you wish"
        j "Maybe next time"
        b "Well you should also try with Miss Wanda, and..."
        j "She's going to kill me, if I only ask"
        b "You never know, or maybe you can do it without..."
        scene bna31b with fade
        m "Hey guys"
        w "Right on time, we should leave"
        scene bna32b with fade
        m "Good night [bname]"
        b "Good night"
        jump newday
    else:
        b "Let me see what else we can play"
        j "Did you go to the beach?"
        b "{i}(Hmm interesting){/i}"
        b "Yes, but I didn't take photos"
        b "We did some before leaving home"
        scene bna29d with dissolve
        b "Here"
        scene bna30b with dissolve
        j "Ah nice"
        b "Yes"
        scene bna29d with dissolve
        b "This was just before we went to the beach, she wanted to check on something and I snapped this photo to show her"
        scene bna30b with dissolve
        b "I have plenty like that if you want to see"
        scene bna28b with dissolve
        j "It's late now..."
        b "Alright as you wish"
        j "Maybe next time"
        b "Well you should also try with Miss Wanda, and..."
        j "She's going to kill me, if I only ask"
        b "You never know, or maybe you can do it without..."
        if joshuacorrupted == 2:
            s "[bname]! Are you here?"
            s "My phone is acting weird"
            scene bna33b with dissolve
            $ persistent.unlock_8 = True
            s "Oh hi, I didn't know you had someone"
            $ joshuacorrupted = 3
            s "How are you"
            j "I'm"
            j "And you"
            s "I'm good, [bname] when you finish can you check what's wrong with my phone"
            scene bna34b with dissolve
            b "Of course, just give me a minute"
            b "{i}(Wow, he's taken by her){/i}"
            b "{i}(Good timing [sname]){/i}"
            pass
        else:
            if joshuacorrupted == 3 and snameacceptjoshua == 1:
                s "[bname]! Are you here?"
                b "Yes?"
                if sjosh ==0:
                    scene bna35b with dissolve
                    s "My phone again, please"
                    b "I'll do it after we finish"
                    $ sjosh += 1
                    b "{i}(Hmm){/i}"
                    pass
                elif sjosh ==1:
                    scene bna35b with dissolve
                    s "My phone again, please"
                    b "I'll do it after we finish"
                    $ sjosh += 1
                    s "Ok I'll wait here"
                    b "Ok"
                    scene bna37 with dissolve
                    "..."
                    scene bna38 with dissolve
                    b "{i}(Hmm){/i}"
                    scene bna39 with dissolve
                    s "Say Josh, do you have a girlfriend?"
                    j "No"
                    s "Ah too bad, I was thinking maybe us four can hang out"
                    j "Erm.."
                    s "Ok guys, see you later"
                    scene bna28b with dissolve
                    b "Hey I have something for you"
                    scene bna40 with dissolve
                    j "What's that?"
                    b "Panties of [sname]"
                    scene bna41 with dissolve
                    $ persistent.unlock_10 = True
                    j "What for?"
                    b "Guys stuff, you know"
                    j "Oh yes I get it"
                    b "Take it and let's go"
                    j "I'll hide it in my pocket"
                    pass
                else:
                    scene bna35b with dissolve
                    s "My phone again, please"
                    b "I'll do it after we finish"
                    $ sjosh += 1
                    s "Ok I'll wait here"
                    b "Ok"
                    scene bna37 with dissolve
                    "..."
                    scene bna38 with dissolve
                    b "{i}(Hmm){/i}"
                    scene bna39 with dissolve
                    s "Say Josh, do you have a girlfriend?"
                    j "No"
                    s "Ah too bad, I was thinking maybe us four can hang out"
                    j "..."
                    s "Ok guys, see you later"
                    b "Bye"
                    scene bna28b with dissolve
                    b "Joshua?"
                    j "Yes"
                    scene bna29c with dissolve
                    b "Who do you think is more hot in this photo?"
                    j "Umm, [mname]"
                    b "Hmm interesting"
                    b "I thought you like [sname]"
                    j "I don't know, but I think [mname] is more pretty"
                    b "I think your mom is much more pretty and hot"
                    j "What!? No, ew, she's gross and fat"
                    b "Do you think so?"
                    j "Yes, I think it's time to go"
                    pass

            else:
                pass
        scene bna31b with fade
        m "Hey guys"
        w "Right on time, we should leave"
        scene bna32b with fade
        m "Good night [bname]"
        b "Good night"
        jump newday


label wandapool:
    scene wvisit0 with fade
    $ persistent.unlock_2 = True
    "..."
    scene wvisit1 with dissolve
    w "[mname]! Glad to see you"
    j "Hi [bname]"
    w "I was just preparing lunch"
    m "Oh ok, I think we came at the wrong time"
    w "No, not at all"
    w "We'll have a quick drink and snack and we go to the pool"
    scene wvisit2 with fade
    w "So, yes, that's what it is basically"
    j "I'll show you how to do it"
    b "..."
    if jendidgo == 1:
        $ persistent.unlock_74 = True
        w "Let's have coffee or drinks at the pool"
        w "The boys can swim if they want"
        scene wvisit40 with fade
        ja "Yes, I'm also fan of hers"
        m "And what about Taylor?"
        scene wvisit41 with dissolve
        m "Do you like her?"
        ja "No"
        b "{i}(What the hell!){/i}"
        b "{i}(She's all normal and discussing now){/i}"
        scene wvisit42 with dissolve
        b "Joshua!"
        b "How come Janey is all normal and discusssing stuff now?"
        b "I thought you said she had this mental thing"
        j "It's because she has just got her weekly treatment"
        j "She's at her best just after the treatment"
        b "Ah that makes sense"
        b "And she gets that weekly?"
        j "Yes, she can't be doing it more often, it's not safe"
        b "Okay fair enough"
        b "Let's swim"
        scene wvisit43 with dissolve
        "..."
        scene wvisit25 with dissolve
        menu:
            "Let's scare them":
                j "Yes sure"
                b "Go under water pretending to do the challenge"
                b "I'll count for you"
                b "What the hell!"
                scene wvisit44 with dissolve
                b "Where did they go?"
                j "Janey where are you all going?!"
                scene wvisit45 with dissolve
                ja "We will come back, just going to change for swimming"
                scene wvisit25 with dissolve
                b "Okay let's wait then"
                scene wvisit53j with fade
                w "Josh, please leave this pool for us"
                w "You can swim in the other pool"
                scene wvisit54j with dissolve
                b "Joshua, which ass do you like more?"
                j "I don't know"
                b "Let me rephrase it for you"
                scene wvisit55j with dissolve
                b "Who's more sexy"
                scene wvisit56 with dissolve
                j "[mname]!"
                b "You naughty boy"
                j "What about you?"
                b "Me?"
                scene wvisit55j with dissolve
                b "Hmmm"
                b "I like the ones that are hard to get"
                j "So? Who?"
                b "Wanda!"
                j "Ewww"
                b "Janey"
                j "No no no"
                scene wvisit57j with fade
                w "Janey, don't you want to swim?"
                ja "In a moment"
                w "You're so lucky you have short hair"
                m "It's your fault, you should have tied it"
                w "True"
                w "Do you think they are still swimming?"
                m "Yes why?"
                w "Ok time to get out of the water"
                scene wvisit58j with dissolve
                b "Oh my god"
                b "Joshua come"
                j "What?"
                menu:
                    "Come closer for a better look":
                        scene wvisit59j with dissolve
                        b "{i}(I have to fuck this ass){/i}"
                        scene wvisit60j with dissolve
                        b "..."
                        scene wvisit61j with dissolve
                        ja "..."
                        ja "Joshua!"
                        scene wvisit62j with dissolve
                        w "Huh"
                        m "What's going on!?"
                        j "Uhh we thought you're done"
                        m "That's creepy"
                        w "Stand up young man!"
                        scene wvisit63j with dissolve
                        w "Go change both!"
                        w "Your swimming is done!"
                        scene wvisit64 with fade
                        b "Stop whining"
                        j "I'm the one who's going to get punished"
                        scene wvisit22 with fade
                        "..."
                        scene hall_d with fade
                        "..."
                        call screen gnav

                    "Let's wait for them to shower" if josh_hidden_cam == 1:
                        j "And then what?"
                        b "Mmm"
                        b "We can watch the camera live"
                        j "Oh really!"
                        scene wvisit56 with dissolve
                        j "Good idea"
                        scene wvisit65j with dissolve
                        w "Josh honey"
                        w "We will go change"
                        b "Come"
                        menu:
                            "Proceed with watching the camera":
                                scene jpool20 with dissolve
                                b "Ready!"
                                j "Can you record this?"
                                b "Err"
                                b "No, just watch live"
                                scene wvisit66 with fade
                                w "Go ahead first, I'll wait for you"
                                scene wvisit67 with dissolve
                                "..."
                                scene wvisit68 with dissolve
                                m "..."
                                scene wvisit69 with dissolve
                                "..."
                                scene wvisit70 with dissolve
                                "..."
                                scene wvisit71 with dissolve
                                "..."
                                scene wvisit72 with dissolve
                                j "Oh my God!"
                                b "Don't cum in your pants"
                                scene wvisit73 with dissolve
                                b "Aha, they're done, let's get ready"
                                scene hall_d with fade
                                "..."
                                call screen gnav
                            "Talk to Janey*":
                                scene wvisit66j with dissolve
                                b "{i}(Holy crap){/i}"
                                scene wvisit67j with dissolve
                                "..."
                                b "Hi Janey"
                                scene wvisit68j with dissolve
                                ja "..."
                                b "{i}(What the hell){/i}"
                                b "Come Joshua"
                                scene wvisit72 with dissolve
                                b "Good that Janey left"
                                b "Let's watch the camera"
                                j "Can you record this?"
                                b "Err"
                                b "No, just watch live"
                                scene wvisit69j with fade
                                b "Ahh seems they're done"
                                scene wvisit70j with dissolve
                                j "Oh Sad"
                                b "Hang on, there's a shadow coming"
                                scene wvisit71j with dissolve
                                b "Cool"
                                scene wvisit72j with dissolve
                                "..."
                                scene wvisit73j with dissolve
                                b "..."
                                scene wvisit74j with dissolve
                                $ persistent.unlock_80 = True
                                b "You should totally fuck this one"
                                scene wvisit75j with dissolve
                                $ jfjaney = 1
                                j "You think so?"
                                b "Yeah, the best time is when she's not on medication"
                                scene wvisit76j with dissolve
                                b "Of course"
                                scene wvisit77j with dissolve
                                "..."
                                scene wvisit78j with dissolve
                                b "We should fuck her both"
                                b "I mean the best time is when she's not on medication"
                                scene wvisit75j with dissolve
                                j "Huh"
                                b "Easy when she's not on medication"
                                scene wvisit79j with dissolve
                                b "Ahh she's done"
                                b "See you next time"
                                scene hall_d with fade
                                "..."
                                call screen gnav
                                

                                
                                

            "Let's do something naughty":
                j "What's on your mind?"
                b "When we get out of water"
                b "We pull  each other shorts"
                j "Hmm, scary but we can try if you say so"
                scene wvisit46 with dissolve
                b "Where did they go?"
                j "Janey where are you all going?!"
                ja "They went to see Mrs [mname] new car"
                scene wvisit25 with dissolve
                b "Let's do it"
                b "Now that Wanda isn't here, you don't have to be scared"
                b "Remove my shorts while I don't look"
                scene wvisit47 with dissolve
                ja "Watch out! Behind you!!"
                b "What's behind me?"
                scene wvisit48 with dissolve
                b "What!"
                ja "Huh!"
                scene wvisit49 with dissolve
                ja "..."
                scene wvisit50 with dissolve
                "..."
                scene wvisit51 with hpunch
                ja "You are one disrespectful boy!"
                b "Ouch!"
                j "Hahaha"
                b "Why me? Not him!!?"
                scene wvisit52 with dissolve
                b "What the hell!"
                j "Pull it up [bname]"
                j "They're coming"
                scene wvisit53 with dissolve
                w "Josh, you can both continue swimming in the other pool"
                scene wvisit54 with dissolve
                b "Joshua, which ass do you like more?"
                j "I don't know"
                b "Let me rephrase it for you"
                scene wvisit55 with dissolve
                b "Who's more sexy"
                scene wvisit56 with dissolve
                j "[mname]!"
                b "You naughty boy"
                j "What about you?"
                b "Me?"
                scene wvisit55 with dissolve
                b "Hmmm"
                b "I like the ones that are hard to get"
                j "So? Who?"
                b "Wanda!"
                j "Ewww"
                scene wvisit57 with fade
                w "You're so lucky you have short hair"
                m "It's your fault, you should have tied it"
                w "True"
                w "Do you think they are still swimming?"
                m "Yes why?"
                w "Ok time to get out of the water"
                scene wvisit58 with dissolve
                b "Oh my god"
                b "Joshua come"
                j "What?"
                b "Let's get a closer look"
                scene wvisit59 with dissolve
                b "{i}(I have to fuck this ass){/i}"
                scene wvisit60 with dissolve
                b "..."
                scene wvisit61 with dissolve
                "..."
                scene wvisit62 with dissolve
                w "Huh"
                m "What's going on!?"
                j "Uhh we thought you're done"
                m "That's creepy"
                j "Stand up young man!"
                scene wvisit63 with dissolve
                w "Go change both!"
                w "Your swimming is done!"
                scene wvisit64 with fade
                b "Stop whining"
                j "I'm the one who's going to get punished"
                scene wvisit22 with fade
                "..."
                scene hall_d with fade
                "..."
                call screen gnav

    else:
        pass
    scene wvisit6 with fade
    if wsusp <5 and bandageremove ==1:
        $ persistent.unlock_34 = True
        w "[bname] now that you removed your bandages you can swim if you want"
        b "Cool thanks"
        scene wvisit23 with fade
        j "Let's dip"
        scene wvisit24 with dissolve
        #splash
        b "..."
        scene wvisit25 with dissolve
        b "Hey let's scare them"
        b "I'm going to go under water pretending to do a challenge and you pretend you're counting"
        b "Make sure your counts are fake, like 150 and plus"
        b "So that they think it's been like 3 minutes underwater"
        j "Ok got it"
        menu:
            "Do it yourself":
                scene wvisit26 with dissolve
                b "Hey Joshua, count for me"
                b "I'm going to do a breath holding challenge"
                scene wvisit25 with dissolve
                b "I'll go now"
                scene wvisit34 with dissolve
                b "..."
                j "150, 151"
                scene wvisit35 with dissolve
                m "[bname] knock it off"
                menu:
                    "Get out":
                        scene wvisit25 with dissolve
                        b "It won't work"
                        b "[mname] knows me"
                        scene wvisit26 with dissolve
                        w "Enough pool for you guys"
                        w "Go change your clothes"
                        w "And play something"
                        scene wvisit21 with fade
                        j "This was crazy"
                        b "Yes"
                        b "Next time we do more"
                        w "Joshua! Are you there?"
                        scene wvisit20 with dissolve
                        j "Ah they're calling us"
                        b "Yes, maybe it's time to go"
                        scene wvisit22 with fade
                        "..."
                        scene hall_d with fade
                        "..."
                        call screen gnav

                    "Stay more":
                        scene wvisit34 with dissolve
                        b "..."
                        j "170, 171"
                        scene wvisit36 with dissolve
                        m "[bname] Get out! Now!"
                        scene wvisit37 with dissolve
                        m "Joshua help me get him out"
                        scene wvisit38 with dissolve
                        m "Oh God"
                        b "I'm Ok come on!"
                        m ang "Stand up!"
                        scene wvisit39 with dissolve
                        m "Go change"
                        scene wvisit26 with fade
                        m "This is insane"
                        w "Yeah kids"
                        scene wvisit21 with fade
                        j "This was crazy"
                        b "Yes"
                        w "Joshua! Are you there?"
                        scene wvisit20 with dissolve
                        j "Ah they're calling us"
                        b "Yes, maybe it's time to go"
                        scene wvisit22 with fade
                        "..."
                        scene hall_d with fade
                        "..."
                        call screen gnav

            "Suggest he does it":
                b "Maybe it's better you do it"
                j "Ok"
                scene wvisit26 with dissolve
                b "Hey Joshua"
                b "Let's do a breath holding challenge"
                b "I'm going to count for you"
                scene wvisit25 with dissolve
                b "Ok man, clear to go"
                b "Whatever happens don't get out of the water until I come down to you"
                j "Ok"
                scene wvisit27 with dissolve
                b "149, 150"
                w "Hey!!"
                scene wvisit28 with dissolve
                w "Get out of the water this moment"
                w "Oh My God!"
                w "[bname] take him out!"
                b "He's doing the challenge, he's fine don't worry"
                scene wvisit29 with dissolve
                #splash
                b "..."
                scene wvisit30 with fade
                w "Go change your clothes"
                w "No more swimming for you today"
                scene wvisit31 with dissolve
                w "Can you believe this!?"
                m "Emm Wanda, I think you need to change your swimsuit"
                scene wvisit33 with dissolve
                w "Oh my God"
                m "Don't worry, it started drying anyway"
                m "God you're tense"
                m "Take it easy"
                m "Come let me massage your shoulders"
                scene wvisit21 with fade
                j "This was crazy"
                b "Hehe yes"
                j "I'm gonna be grounded for sure"
                w "Joshua! Are you there?"
                scene wvisit20 with dissolve
                j "Ah they're calling us"
                b "Yes, maybe it's time to go"
                scene wvisit22 with fade
                "..."
                scene hall_d with fade
                "..."
                call screen gnav



    else:
        w "Joshua"
        w "Why don't you show [bname] around the house, and then you can play something together"
        j "Ok mom"
        pass
    scene wvisit5 with dissolve
    b "Mmm"
    w "Thank you for coming [mname]"
    w "And for wearing one of my swimsuits"
    w "I'm surprised it fit you"
    scene wvisit4 with dissolve
    m "We're almost the same size"
    w "I'm fat"
    m "No you're not, you're extremely hot"
    w "Thank you"
    scene wvisit3 with dissolve
    b "{i}(Damn, why can't we sit with them){/i}"
    b "{i}(This Wanda is a control freak){/i}"
    b "{i}(She made [mname] wear her bikini, just so her son doesn't see flesh){/i}"
    j "Here comes my sister"
    scene wvisit7 with dissolve
    b "Hmm"
    b "{i}(Well well well){/i}"
    scene wvisit4a with dissolve
    b "Hi"
    b "{i}(Is she retarded?! She didn't answer){/i}"
    j "She's very shy"
    j "Let's leave them alone, I'll show you the place"
    scene wvisit8 with dissolve
    ja  "Hi miss [mname]"
    m "Hi Janey"
    scene wvisit9 with dissolve
    ja "Mom, may I swim with you?"
    w "Sure"
    ja "Thanks"
    scene wvisit10 with dissolve
    j "Nice view, isn't it?"
    scene wvisit11 with dissolve
    b "Indeed"
    menu:
        "Sneak at them":
            scene wvisit12 with dissolve
            ja "I'm done"
            w "Ok sweetie"
            w "You can swim now, but use the ring"
            ja "Ok"
            scene wvisit13 with dissolve
            m "..."
            scene wvisit14 with dissolve
            b "Damn!"
            j "Oh dear God!!"
            $ wsusp += 1
            scene wvisit15 with dissolve
            show screen wsuspup
            w "Hmm"
            hide screen wsuspup
            b "{i}(Fuck, this woman sense is out of this world){/i}"
            pass
            
        "Don't":
            scene wvisit12 with dissolve
            ja "I'm done"
            w "Ok sweetie"
            w "You can swim now, but use the ring"
            ja "Ok"
            pass
    
    scene wvisit16 with dissolve
    m "This pool is nice"
    w "Or as the kids these day say, 'Awesome'"
    m "Yes"
    scene wvisit17 with dissolve
    w "I'll get into the water"
    w "Serve yourself some punch"
    scene wvisit17a with dissolve
    w "..."
    scene wvisit18 with fade
    j "And here is our gym"
    b "Ah that's you you brought me to the roof"
    scene wvisit19 with dissolve
    b "{i}(They have their own gym at home! Fuck it){/i}"
    scene wvisit20 with dissolve
    b "So how do you spend your days?"
    j "Reading, tv, gym"
    j "Pool, praying"
    b lau "Praying!"
    j "Yeah I know, boring"
    j "But my mom, you know"
    b "No girlfriend?"
    scene wvisit21 with dissolve
    j "Nah"
    b "Ah yes you told me"
    j "The only girls I know is my mom and sister"
    b "Which is why you have to do something about it"
    w "Joshua! Are you there?"
    scene wvisit20 with dissolve
    j "Ah they're calling us"
    b "Yes, maybe it's time to go"
    scene wvisit22 with fade
    "..."
    scene hall_d with fade
    "..."
    call screen gnav
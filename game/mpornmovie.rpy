


label mpornmovie:
    scene jdm3_2 with fade
    jn "Hey happy to see you again after the summer break"
    m "Thanks, I'm happy to see you too"
    scene jdm3_3 with dissolve
    jn "You know the way to the makeup room"
    m "Sure, but ermm"
    m "I need to review the script if that's ok"
    m "Haven't had enough time to memorize it"
    jn "Don't worry dear, it's too short this time"
    jn "[bname] you can't join us today"
    jn "Sorry, this is a very delicate movie today"
    jn "I appreciate your understanding"
    b "Yeah..."
    if bmmovie ==1:
        b "{i}(Maybe I can call Melinda?){/i}"
        b "{i}(And ask if I can have a role in [mname]'s movie){/i}"
        menu:
            "Call her now":
                scene mporn_0 with dissolve
                $ bmmovie = 2
                b "Hey I was wondering if..."
                scene mporn_2 with fade
                b "{i}(If I can have a role in one of the movies){/i}"
                scene mporn_2a with dissolve
                ml "Hmm let me guess... With [mname]"
                b "{i}(Hehe yes){/i}"
                scene mporn_2 with dissolve
                ml "Let me see what I can do"
                scene mporn_3 with fade
                jn "Hi Ma'am"
                jn "Yes sure for next week"
                pass
            "No":
                pass

    else:
        pass
    scene mporn_1 with fade
    jn "And action"
    m "Hi sir"
    m "I was cleaning the bedroom"
    "Julia..."
    "You seem like a good girl"
    m "Yes sir"
    m "I do my best sir"
    m "My family needs my help"
    "Interesting"
    scene mporn_4 with dissolve
    "You are a beautiful woman Julia"
    "I wonder why someone like you is working as a maid"
    m "Sir... I..."
    "Drop the stance, you can be at ease"
    m "I'm sorry sir"
    scene mporn_5 with dissolve
    m "Sir I come from a poor family"
    "And"
    m "And my mom needs treatment"
    m "That's why"
    "I am willing to help you with that..."
    "Lots of money"
    "On one condition"
    scene mporn_6 with dissolve
    m "Huh"
    "Come here"
    scene mporn_7 with dissolve
    m "Yes sir"
    scene mporn_8 with dissolve
    "Yes suck it"
    m "Mmm"
    scene mporn_9 with dissolve
    m "Uhh"
    scene mporn_10 with dissolve
    "Lay here"
    scene mporn_11 with dissolve
    m "Mmm"
    scene mporn_12 with dissolve
    m "Ahhh"
    scene mporn_13 with dissolve
    m "Slowly sir, please"
    scene mporn_14 with dissolve
    m "Ahhh"
    jn "Cut, that was perfect"
    scene mporn_15 with dissolve
    jn "Guys let's prepare for the finishing cut scene"
    scene mporn_16 with fade
    jn "Action"
    scene mporn_17 with dissolve
    m "Gulp"
    scene mporn_18 with fade
    b "So how was it?"
    m "I'm tired [bname]"
    call screen gnav


label bmporn:
    scene jdm3_2 with fade
    #$bmmovie = 4
    jn "Hey happy to see you"
    m "Thanks you too"
    scene jdm3_3 with dissolve
    jn "Mm, we have a slight change today"
    m "What's wrong?"
    jn "The actor didn't show up so..."
    m "So no filming today?"
    jn "Well the reason I didn't inform you was..."
    jn "I... Have a great story and script, but we need one more actor"
    m "What is it Jonas?"
    jn "Well... It's a mom swinging story, but..."
    jn "Will you allow [bname] to take a role in it?"
    scene jdm3_3a with dissolve
    m "What?!!"
    jn "We are short for one male, and he fits in very well"
    scene jdm3_3b with dissolve
    m "No way!"
    jn "We're going to change his looks and pay him for this"
    if mcorr >= 40:
        scene jdm3_3c with dissolve
        $ persistent.unlock_19 = True
        m "Hmm"
        jn "I take that as a yes"
        jn "Don't worry you won't even know him"
        jn "Meet me in the studio when you read the script"
        b "Come on, this is not so bad"
        scene jdm3_3d
        m "Yeah right, now it's all over the world"
        scene bmporn1 with fade
        jn "ACTION!"
        scene bmporn2 with dissolve
        m "Hi sweetie"
        m "No good afternoon? No kiss?"
        ch "Good afternoon"
        scene bmporn3 with dissolve
        m "Hey, what's wrong?"
        m "Come back here, don't run"
        ch "I'm sorry I just tripped at school today"
        scene bmporn4 with dissolve
        m "What is that? Tripping?"
        m "That's it, I'm calling your principal"
        m "What's the name of the kid who did this?"
        ch "Tony"
        m "I'm calling your principal"
        scene bmporn5 with dissolve
        m "Hi is Principal Stepney available"
        if persistent.patch_enabled:
            m "This is Jenna, Chris roadwreck mother"
            pass
        else:
            m "This is Jenna, Chris roadwreck guardian"
            pass

        m "He just came in with a bruise on his face and a black eye"
        m "And he's saying some kid had done this to him"
        m "..."
        m "I think the kid name is Tony"
        m "Umm I... I mean I would like to speak with his mother"
        m "Yeah, exactly, this is completely unacceptable"
        m "Uh huh"
        m "Thank you Mr Stepney"
        jn "Cut! Perfect"
        scene bmporn6 with fade
        b "Yeah I kicked his ass, what a jerk!"
        i "Yes totally unacceptable"
        b "Ah I got to go"
        scene bmporn7 with dissolve
        i "Indeed"
        i "I'll deal with it"
        i "Thank you"
        scene bmporn8 with dissolve
        i "Oh My God!"
        i "Are you serious Tony!?"
        i "Bullying another kid"
        play sound "sounds/doorbell.wav"
        scene bmporn9 with dissolve
        i "Are you expecting someone?"
        stop sound
        scene bmporn10 with fade
        m "This is what your kid did to my kid"
        i "Emm yeah, please come in"
        scene bmporn11 with dissolve
        m "And you must be Tony?"
        b "..."
        scene bmporn12 with dissolve
        m "You really are a rude boy"
        m "Take Chris and apologize to him"
        m "It's time for you to make amends"
        scene bmporn11 with dissolve
        m "Or else"
        i "Please go Tony, please take Chris and go"
        jn "Cut! Awesome!"
        jn "Let's take [bname] and Chris shots"
        scene bmporn13 with fade
        b "Look man I'm sorry"
        b "I regret doing this to you"
        b "I'm saying this because you're a nice guy"
        if persistent.patch_enabled:
            b "Not because of your mom asking me"
            pass
        else:
            b "Not because of your guardian asking me"
            pass
        b "She's a bitch"
        b "Did you see how she almost pierce my eyes with her nails!?"
        ch "I know, she does the same to me"
        ch "Trust me this is nothing"
        ch "My dad left us because of her behavior"
        b "..."
        b "I have an idea"
        ch "What's on your mind?"
        b "Let's give her some of her own medicine"
        b "Let's bully the hell out of her"
        ch "She's not easy, you're going to regret it"
        b "Just follow my lead"
        scene bmporn14 with dissolve
        m "You have to be more firm"
        i "I know"
        m "Be tough now, reap it later"
        i "Yes"
        i "Here they come"
        b "You know..."
        scene bmporn15 with dissolve
        b "I said sorry to Chris, just because he's a nice guy"
        if persistent.patch_enabled:
            b "But I feel more sorry for him because he has a bitch of a mom"
            pass
        else:
            b "But I feel more sorry for him because he has a bitch of a guardian"
            pass
        scene bmporn16 with dissolve
        i "Huh!"
        i "Dany Oh my"
        scene bmporn15 with dissolve
        b "I may be a bully for fun"
        b "But you.. Because of you Chris needs therapy"
        b "Because you're the real bitch bully"
        scene bmporn17 with dissolve
        play sound "sounds/slap.mp3"
        b "Ahh"
        stop sound
        scene bmporn18 with dissolve
        m "You want bully! You'll get bully"
        scene bmporn19 with dissolve
        m "How about now?"
        b "You're a bitch"
        scene bmporn20 with dissolve
        jn "Cut, perfect"
        jn "Take Chris scene now"
        jn "And you [bname], come record your voice over"
        jn "Saying 'Huh! Did she just sit on my dick?'"
        jn "We will add it to the last scene"
        scene bmporn21 with fade
        jn "Action!"
        if persistent.patch_enabled:
            ch "Mom that doesn't look like a punishment!"
            pass
        else:
            ch "This doesn't look like a punishment!"
            pass
        scene bmporn22 with dissolve
        m "Huh!"
        scene bmporn23 with dissolve
        m "Agh"
        scene bmporn24 with dissolve
        b "Come here"
        m "What for?"
        b "We need to teach her a lesson and heal you"
        ch "Ah later"
        scene bmporn25 with dissolve
        m "Huh"
        jn "Cut, we messed up the match cut with that chalkboard"
        jn "Anyway leave it, they won't notice"
        jn "Let's move to the other shot"
        scene bmporn26 with dissolve
        jn "Action"
        i "Mmm"
        scene bmporn27 with dissolve
        b "Bitch"
        scene bmporn28 with dissolve
        b "Nice ass bitch"
        scene bmporn29 with dissolve
        m "Hey"
        m "You're not half of a man"
        m "I dare you to do it"
        b "Oh! Really!?"
        scene bmporn32 with dissolve
        m "Ah"
        scene bmporn33 with dissolve
        m "What the hell"
        scene bmporn30 with dissolve
        m "Ahh"
        scene bmporn31 with dissolve
        m "Ah more you idiot!"
        scene bmporn34 with dissolve
        i "Chris!"
        scene bmporn35 with dissolve
        i "Yes Chris, fuck the mom of your bully"
        scene bmporn36 with dissolve
        m "Ahh"
        m "Yes"
        scene bmporn37 with dissolve
        m "You're such a bully Tony"
        scene bmporn38 with dissolve
        m "Mmmm"
        b "Get up"
        scene bmporn40 with dissolve
        b "Oh yes bitch"
        m "..."
        jn "Cut!"
        scene bmporn39 with dissolve
        jn "This was great, thank you everyone"
        scene mporn_18 with fade
        b "Wow, that was really nice"
        m "Yeah"
        m "Now, please go to sleep"
        m "We're not mentioning this anymore"
        b "But why?"
        m "I said no more"
        b "{i}(Damn){/i}"
        call screen gnav



    else:
        m "I said No way!"
        scene jdm3_3 with dissolve
        m ang "let's go [bname]"
        scene mporn_18 with fade
        b "Why did you say no?"
        m "I don't want to talk about it"
        b "{i}(Damn){/i}"
        "RAISE HER CORRUPTION POINTS TO 40"
        call screen gnav



label bmporn1:
    scene jdm3_2 with fade
    jn "Hey happy to see you"
    m "Thanks you too"
    scene jdm3_3 with dissolve
    jn "Mm, we have a slight change today"
    m "What's wrong?"
    jn "The actor didn't show up so..."
    m "Again!?"
    jn "Well to be honest, the last movie was a great success"
    jn "[bname] was great and... We need him again"
    scene jdm3_3e with dissolve
    m "Oh my God"
    jn "We are short for one male, and he fits in very well"
    scene jdm3_3b with dissolve
    m "No way!"
    jn "He's a great success"
    if mcorr >= 40:
        $ persistent.unlock_28 = True
        scene jdm3_3c with dissolve
        m "Hmm"
        b "Come on, we're great actors, it runs in our blood"
        scene jdm3_3d
        m "Yeah right"
        scene bmporn41 with fade
        jn "Action"
        "..."
        m "Hmm"
        m "That's weird"
        scene bmporn42 with dissolve
        b "Hi, what time are we going home"
        m "I'm still finalizing the test results"
        b "Oh Ok"
        scene bmporn43 with dissolve
        m "Tell me Billy, isn't it weird that all my students passed the test"
        m "Even this stupid [bname] who hasn't attended all the semester"
        scene bmporn44 with dissolve
        b "Ah!"
        m "Do you have any idea how this happened?"
        scene bmporn45 with dissolve
        b "Achew"
        b "Sorry I'm not feeling alright"
        b "I guess I'll walk home"
        m "Ok see you there"
        scene bmporn46 with dissolve
        m "Hey Billy, still not feeling well?"
        b "Yes not so"
        scene bmporn47 with dissolve
        m "I think you're absolutely fine"
        b "No... I'm not"
        m "Stop the bullshit Billy"
        scene bmporn47a with dissolve
        m "I've had a conversation with a couple of the boys"
        m "that got a full marks on that test"
        m "And it turns out, you've sold them the copy of the test"
        m "Doing a side hustle aren't you?"
        b "... I'm..."
        m "Well let's see what your father says about that"
        scene bmporn48 with dissolve
        b "What?! Wait, no!"
        m "Hi honey, yes I'm OK"
        m "Billy has something to tell you"
        scene bmporn49 with dissolve
        b "Hey dad, yeah"
        b "I'm good, how are you"
        b "..."
        b "Listen, I just want to tell you"
        b "That I love you and can't wait for you to return home safe"
        scene bmporn50 with dissolve
        m "..."
        b "See you, bye"
        scene bmporn51 with dissolve
        m "Give me the phone!!"
        b "He closed"
        b "Wait!"
        scene bmporn52 with dissolve
        m "Billy? Are you looking at my cleavage?"
        b "And your hand is on my penis"
        scene bmporn53 with dissolve
        m "Hmm"
        scene bmporn51 with dissolve
        m "No, that's my phone"
        b "I know what you want"
        scene bmporn54 with dissolve
        m "Huh Billy!"
        scene bmporn55 with dissolve
        m "No! Please"
        b "Why?! We both want it"
        m "You want it also?"
        m "Oh crap"
        m "I mean I don't want it"
        scene bmporn56 with dissolve
        b "Don't worry"
        b "Dad won't be home till tomorrow"
        scene bmporn57 with dissolve
        b "You want your phone, don't you?"
        m "Yes"
        b "Well"
        scene bmporn58 with dissolve
        b "Here it is"
        m "Huh"
        scene bmporn58a with dissolve
        m "..."
        scene bmporn59 with dissolve
        m "Ahh"
        scene bmporn60 with dissolve
        m "Mmm"
        scene bmporn61 with dissolve
        m "Oh"
        scene bmporn62 with dissolve
        m "Yes [bname]"
        jn "Cut!"
        scene bmporn63 with dissolve
        jn "His name is Billy here"
        m lau "Sorry"
        jn "It's fine, let's move to the next cut"
        scene bmporn64 with dissolve
        jn "Action!"
        m "Billy!"
        m "Where did you learn all this"
        m "And don't tell me sex ed"
        b "Hmmm"
        scene bmporn65 with dissolve
        m "Ohh"
        "GROANS"
        scene bmporn66 with dissolve
        m "Oh"
        scene bmporn67 with dissolve
        m "Ahhh"
        scene bmporn68 with fade
        b "Ohh yes"
        scene bmporn70 with fade
        jn "That was great, you two are natural winners"
        scene mporn_18 with fade
        b "Wow, that was really nice"
        m "Yeah"
        m "Now, please go to sleep"
        m "We're not mentioning this anymore"
        b "But why?"
        m "I said no more"
        b "{i}(Damn){/i}"
        call screen gnav


    else:
        m "No thanks"
        scene jdm3_3 with dissolve
        m ang "let's go [bname]"
        scene mporn_18 with fade
        b "Why did you say no?"
        m "I don't want to talk about it"
        b "{i}(Damn){/i}"
        "RAISE HER CORRUPTION POINTS TO 40"
        call screen gnav


label mpornmovie1:
    define wb = Character("Bald Worker")
    define wa = Character("Worker")
    $ persistent.unlock_30 = True
    scene mporn86b with fade
    m "Thank you"
    scene mporn86a with fade
    m "Yes honey, I'll be waiting for you"
    m "Ah"
    m "No, I didn't notice the workers, I just woke up"
    m "Yes honey, I know it's 6 pm"
    m "But sorry, I had to entertain you and your guests till late yesterday"
    m "Ok honey"
    m "Mwah"
    scene mporn87 with fade
    m "Hmm"
    m "{i}(The idiot is working late){/i}"
    m "{i}(Let's check on their work){/i}"
    m "Hmm"
    scene mporn88 with dissolve
    m "{i}(I'd better change first){/i}"
    scene mporn89 with dissolve
    "Phew man, that was some real work"
    scene mporn90 with dissolve
    m "Is the pool ready?"
    wb "Yes ma'am"
    scene mporn91 with dissolve
    m "Doesn't look like the water is getting warm"
    wb "The heater takes time, we just started it"
    wb "You can try it in 10 minutes"
    m "You bet I will"
    scene mporn92 with fade
    wa "Do you think she will come back?"
    wb "Man I'm tired with these bitches"
    wb "I don't care"
    wa "Then let's go it's late, we will send him the bill"
    scene mporn93 with dissolve
    wb "Yeah let's move"
    wa "Wait"
    wa "Here she comes"
    scene mporn94 with fade
    m "This is not warm"
    wa "It is"
    m "Are you fucking kidding me?"
    wa "We don't care, we're leaving and will send the bill by mail"
    scene mporn95 with dissolve
    m "Listen you idiot!"
    m "You can fool my stupid husband, but you can't fool me"
    wa "Ma'am please be respectful"
    m "Yeah, what are you going to do about it?"
    m "You little sissy BITCH!!"
    scene mporn96 with dissolve
    wa "Shut the fuck"
    wa "You know what? We can get our payment from you"
    m "Hey"
    scene mporn97 with dissolve
    wb "Hmm"
    scene mporn98 with dissolve
    m "What!"
    scene mporn99 with dissolve
    m "Take your hand"
    wa "Keep holding her, let me undress myself"
    scene mporn100 with dissolve
    m "Stop!!"
    scene mporn101 with dissolve
    m "I'll kill you both"
    wb "You won't say that after we're done with you"
    wb "It's been ages since we fucked a hot bitch"
    scene mporn102 with dissolve
    wa "Hey! My hair bitch!"
    scene mporn103 with dissolve
    play sound "sounds/mgroan.mp3"
    m "Ahhh"
    stop sound
    scene mporn104 with dissolve
    m "You're a fucking idiot!"
    scene mporn105 with dissolve
    play sound "sounds/mmoanang.mp3"
    wb "Keep talking shit"
    wa "Put her down"
    stop sound
    scene mporn106 with dissolve
    m "Ahh"
    scene mporn107 with dissolve
    m "..."
    scene mporn108 with dissolve
    m "Mmm"
    scene mporn109 with dissolve
    m "Ahhhh"
    scene mporn110 with dissolve
    m "Ptoo"
    wb "Shit!"
    wb "Turn her"
    scene mporn111 with dissolve
    m "Ah"
    scene mporn112 with dissolve
    m "Aaaah"
    scene mporn113 with dissolve
    m "Oh God!"
    scene mporn114 with dissolve
    wa "Quiet!!"
    scene mporn115 with dissolve
    m "Aah"
    scene mporn116 with dissolve
    wb "Turn bitch, I'm done"
    scene mporn117 with fade
    m "..."
    #sound
    scene mporn118 with dissolve
    jn "Cut, that was great"
    scene mporn119 with dissolve
    jn "We still need to shoot the behind the scenes and consent disclaimer"
    jn "That this was done with the consent of everyone, and no one was forced"
    wb "Cool"
    scene mporn120 with fade
    m "Hahaha"
    scene black
    "..."
    scene mporn_18 with fade
    b "How was your day?"
    m "It.. It was ok"
    b "Cool, tell me about it"
    m "[bname] I'm tired please"
    b "Ok but please tell me later"
    m "Ok later"
    call screen gnav



label bmporn2:
    scene jdm3_2 with fade
    $ bmporn2done = 1
    jn "Hey happy to see you"
    m "Thanks you too"
    scene jdm3_3 with dissolve
    jn "Mm, we have a great script today"
    m "Yeah, as always"
    jn "Hey don't be so sarcastic, our movies are the best"
    m "It's true because you have me"
    jn "It's with two young men"
    jn "And...[bname] is one of them"
    scene jdm3_3e with dissolve
    m "Oh my God"
    jn "Come on, we will change his looks again"
    scene jdm3_3c with dissolve
    m "Hmm"
    b "Come on, we're great actors, it runs in the family"
    scene jdm3_3d
    m "That's not comforting [bname]"
    scene bmporn71 with fade
    b "It was on of these normal days"
    scene bmporn72 with fade
    m "Hmmm I guess Sonya's son is up for a little adventure again"
    m "Let's tease the boy"
    scene bmporn73_ with dissolve
    m "I feel bad for him waiting all day on the window for just a peek"
    scene bmporn73 with dissolve
    b "What the hell!"
    scene bmporn74 with dissolve
    b "Parker?! What are you doing"
    b "Get your ass over here"
    scene bmporn75 with dissolve
    m "Oh God!"
    scene bmporn76 with fade
    b "You idiot"
    m "Oh my God"
    scene bmporn77 with dissolve
    m "You knocked him out!"
    b "I'll kill this pervert if I see him one more time peeking at our pool"
    m "Go to your room!"
    scene bmporn78 with fade
    m "Don't worry dear"
    m "The ice won't let bruises"
    "You know Miss Jenna, I wish my mom was like you"
    "Supportive and caring"
    m "Don't worry sweetie, things will be ok"
    "I got to go, she's gonna see me on your pool and it's gonna be hell"
    m "Is she that bad?"
    "Yes, I mean I am already 19 but she still treats me like a young boy"
    "I wish I can trade her for you"
    scene bmporn79 with dissolve
    m "I think I have an idea"
    "You do?"
    m "You want to teach your mom a lesson"
    m "And I want to teach my son a lesson"
    "Yes"
    scene bmporn80 with dissolve
    "Hmm"
    scene bmporn81 with dissolve
    m "Lose your shirt"
    scene bmporn82 with dissolve
    m "Don't think about your mom"
    m "Just enjoy the moment"
    scene bmporn83 with dissolve
    "..."
    scene bmporn84 with dissolve
    "..."
    scene bmporn85 with fade
    "MEANWHILE"
    b "Let's see if this idiot left"
    scene bmporn86 with dissolve
    b ang "What the fuck!"
    scene bmporn87 with dissolve
    m "Oh Honey, the food is on the kitchen counter"
    b "What the fuck, bitch!"
    b "I'll tell you what you deserve"
    scene bmporn88 with dissolve
    "Take it easy man, I didn't even want to do this"
    b "Shut the fuck up"
    b "And come here"
    scene bmporn89 with dissolve
    m "Why honey? Why!?"
    b "Shut up bitch"
    scene bmporn90 with dissolve
    m "Mmm"
    b "Bring her here"
    scene bmporn91 with dissolve
    b "You like his cock bitch?"
    scene bmporn92 with dissolve
    m "Ahh"
    scene bmporn93 with dissolve
    m "Please!"
    scene bmporn94 with dissolve
    m "Mmhm"
    scene bmporn95 with dissolve
    m "Traffic light"
    jn "Cut"
    scene bmporn96 with dissolve
    m "Ahh"
    jn "[bname] we said cut!"
    jn "She said the safeword"
    jn "Are you ok [mname]?"
    scene bmporn97 with fade
    jn "Cut scene to the ending"
    jn "Action!"
    scene bmporn98 with dissolve
    m "Give it to me boys"
    scene bmporn99 with dissolve
    b "Ahh"
    jn "Cut!"
    jn "That was great"
    jn "And [bname] you should be easy on your emotions"
    b "Ok"
    scene mporn_18 with fade
    b "Wow, that was really nice"
    m "Yeah"
    m "Now, please go to sleep"
    m "We're not talking about this"
    b "But why?"
    m "I said no more"
    b "{i}(Damn){/i}"
    call screen gnav


label mpornmovie2:
    scene jdm3_2 with fade
    jn "Hey happy to see you"
    m "Thanks you too"
    scene jdm3_3 with dissolve
    jn "Mm, we have a great script today"
    m "Yeah, as always"
    jn "Hey don't be so sarcastic, our movies are the best"
    m "It's true because you have me"
    jn "[bname] you can watch"
    jn "If [mname] is ok with it"
    b "Yes"
    jn "But you be quiet"
    m "I don't care, by now he can do whatever he wants"
    jn "Let's go then"
    m "Ok"
    jn "To the roof please"
    jn "We'll setup a night scene"
    scene mpornmovers0 with dissolve
    jn "Action"
    m "I wonder if the movers are done"
    scene mpornmovers with dissolve
    m "Hmm"
    scene mpornmovers1 with dissolve
    m "I see you're almost done"
    scene mpornmovers2 with dissolve
    "I'm completely done"
    m "And where are your guys?"
    "They just left"
    "I'm going as well"
    m "Well there's something more I want you to do"
    scene mpornmovers3 with dissolve
    m "For me"
    "Woah ma'am I'm married"
    scene mpornmovers4 with dissolve
    m "So what?"
    "No!"
    scene mpornmovers5 with dissolve
    m "Relax!"
    scene mpornmovers6 with dissolve
    m "Oh my God"
    scene mpornmovers7 with dissolve
    "..."
    "Can you deal with this?"
    scene mpornmovers8 with dissolve
    m "You seem so confident"
    scene mpornmovers9 with dissolve
    "You have asked for it"
    scene mpornmovers10 with vpunch
    m "Ughh"
    scene mpornmovers11 with dissolve
    m "..."
    scene mpornmovers13 with dissolve
    "Get down"
    scene mpornmovers12 with dissolve
    m "Mmm"
    scene mpornmovers14 with dissolve
    "Yes worship that cock"
    m "..."
    "Enough"
    scene mpornmovers15 with dissolve
    m "Mmm"
    scene mpornmovers16 with dissolve
    m "Ahh"
    "Turn"
    scene mpornmovers17 with dissolve
    m "..."
    scene mpornmovers18 with dissolve
    m "Ahh"
    play sound "sounds/mpornmoversound.mp3"
    scene mpmanim with dissolve
    m "Oh"
    "..."
    m "My"
    "..."
    m "God"
    "..."
    stop sound
    scene mpornmovers19 with dissolve
    m "Fucker!"
    scene mpornmovers20 with fade
    "Ahhh"
    scene mporn_18a with fade
    b ang "Looks like you are enjoying this"
    m "[bname] stop"
    m "Or I won't take you with me anymore"
    b ang "Gree"
    m "Stop!"
    b "{i}(Damn){/i}"
    call screen gnav


    

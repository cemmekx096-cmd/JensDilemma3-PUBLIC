


label maleescort:
    scene mclub8_call with dissolve
    b "Hi Elaine"
    b  "Where can I order a male stripper, escort, or something"
    e "{i}(Oh la la! I see someone wants to change sides){/i}"
    e "{i}(Is this your coming out?){/i}"
    b "No that's my second coming"
    e "{i}(What!? I don't get it){/i}"
    b "Look, I'm serious, I need to celebrate with [mname]"
    b "And I thought to try a threesome"
    e "{i}(It happens that I know a guy, who knows a guy){/i}"
    b "Cut it out and send someone"
    b "Not so expensive please"
    e "{i}(I'm sending you my g...){/i}"
    e "{i}(My friend){/i}"
    b "Ok cool, and how do they charge?"
    e "{i}(Don't worry, this time is on me){/i}"
    scene mclub8 with dissolve
    b "{i}(Cool){/i}"
    scene mclub_ge0 with fade
    m "What to put on?"
    scene black
    "..."
    scene mclub_me with fade
    b "Woah"
    scene mclub_me1 with dissolve
    b "Cheers"
    m "Whisky [bname]!!?"
    if persistent.patch_enabled:
        b "Mom we're celebrating"
        pass
    else:
        b "But we're celebrating"
        pass
    play sound "sounds/doorbell.wav"
    m "..."
    m "Are you expecting someone?"
    stop sound
    b "Yes I asked Elaine for something to celebrate"
    m "Ah, I see"
    m "I'll open to surprise her"
    scene mclub_me2 with dissolve
    m "Hi Elaine"
    m "Come in"
    scene mclub_me3 with dissolve
    m "Oh! I'm...I'm so sorry"
    scene mclub_me4 with dissolve
    ca "My name is Carlos"
    ca "I've been sent by Elaine for this party"
    b "Cool"
    scene mclub_me5 with dissolve
    m "[bname]! What is the meaning of that?"
    b "I... I thought we can get something new to spice up our life"
    scene mclub_me6 with dissolve
    m "Oh my God"
    scene mclub_me7 with dissolve
    ca "Relax, I'm a professional stripper"
    ca "I won't do anything without your consent"
    if mrel >=200 and mcorr >= 30:
        $ persistent.unlock_20 = True
        m "No"
        scene mclub_me11 with dissolve
        b "Oh come on"
        b "We're just celebrating, it's a one off"
        m "{i}(Maybe I can teach [bname] a lesson){/i}"
        scene mclub_me12 with dissolve
        show screen mcorr
        m "{i}(And this Carlos is a thing){/i}"
        hide screen mcorr
        $ mcorr += 5
        scene mclub_me13 with dissolve
        m "Let's see your show Carlos, I'll be the judge"
        m "If you do good, I'm all yours"
        scene mclub_me14 with fade
        ca "..."
        scene mclub_me15 with dissolve
        "..."
        scene mclub_me16 with dissolve
        m "Oh"
        scene mclub_me17 with dissolve
        ca "Man, come here"
        menu:
            "Go 'Risky'":
                ca "So my lady, which one do you prefer?"
                scene mclub_me18 with dissolve
                b "..."
                ca "Hmm, impressive, very impressive size"
                scene mclub_me19 with dissolve
                ca "Would you like if we have some fun together first?"
                menu:
                    "No":
                        b "No, leave me alone!"
                        scene mclub_me20 with dissolve
                        m "Hahaha"
                        pass

            "Go but stay far at a distance from him":
                scene mclub_me18 with dissolve
                b "..."
                ca "Hmm, impressive, very impressive size"
                pass

        scene mclub_me21 with dissolve
        ca "Come here milady"
        scene mclub_me22 with fade
        ca "Yeah"
        scene mclub_me23 with dissolve
        m "..."
        scene mclub_me24 with dissolve
        m "[bname]"
        m "Are you sure you want to do this?"
        b "Yes... It's fun"
        m "..."
        scene mclub_me25 with dissolve
        m "Mmm"
        scene mclub_me26 with dissolve
        m "Ahh"
        scene mclub_me27 with dissolve
        ca "How do you want to do this [bname]"
        menu:
            "You watch first":
                scene mclub_me28 with dissolve
                m "What is he doing?"
                b "Watching your ass"
                m "Tell him to undress me and kiss it"
                scene mclub_me29 with dissolve
                b "You heard the lady man"
                scene mclub_me30 with dissolve
                m "Oh [bname]"
                m "You want to watch me getting licked and fucked by another man?"
                menu:
                    "No":
                        b "Maybe later, now let's take this suit off"
                        pass
                    "Yes":
                        m "Mhhm interesting"
                        $ persistent.unlock_49 = True
                        b "Come on, start"
                        scene mclub_me31a with dissolve
                        m "Mmm"
                        ca "Stand still, let me undress you"
                        scene mclub_me34a with dissolve
                        m "Give it to me"
                        ca "Patience"
                        play sound "sounds/mblowjob.mp3"
                        scene mescortanim with fade
                        m "Mmm"
                        m "Mmmm"
                        m "..."
                        m "..."
                        stop sound fadeout 1.0
                        scene mclub_me33a with fade
                        m "{i}(I can't believe I am sucking this guy's cock){/i}"
                        m "{i}(In front of [bname]){/i}"
                        m "{i}(Is he enjoying it!?){/i}"
                        menu:
                            "Enough":
                                b "Enough"
                                pass
                            "Now fuck her":
                                $ mcorr += 5
                                show screen mcorr
                                scene mclub_me56 with dissolve
                                hide screen mcorr
                                m "..."
                                scene mclub_me57 with dissolve
                                m "Mmmm"
                                b "Enough"
                                pass
                        scene mclub_me33 with dissolve
                        m "Mmm"
                        scene mclub_me34 with dissolve
                        ca "Patience"
                        scene mclub_me35 with dissolve
                        m "{i}(The excitement is killing me){/i}"
                        b "Enough, get down"
                        scene mclub_me36 with dissolve
                        m "Mmm"
                        scene mclub_me37 with dissolve
                        b "Come, get up"
                        scene mclub_me38 with fade
                        m "Mmm you know how to please a woman Carlos"
                        b "{i}(Bitch){/i}"
                        b "Let's do this properly"
                        scene mclub_me39 with dissolve
                        play sound "sounds/mgrunt.wav"
                        m "Ahh [bname]"
                        scene mclub_me40 with dissolve
                        stop sound
                        m "Take it easy, what's wrong with you?"
                        scene mclub_me41 with dissolve
                        b "Easy, right?!"
                        scene mclub_me42 with dissolve
                        play sound "sounds/mpant.wav"
                        m "Mhhmm"
                        b "Shut her mouth with your cock"
                        scene mclub_me43 with dissolve
                        stop sound
                        play sound "sounds/mgag1.wav"
                        ca "Ahhh"
                        scene mclub_me44 with dissolve
                        m "Mmm"
                        ca "I want her ass"
                        m "Mhmm"
                        stop sound
                        scene mclub_me45 with dissolve
                        m "..."
                        scene mclub_me46 with dissolve
                        ca "Fuck yeah"
                        b "Wait for me"
                        scene mclub_me48 with dissolve
                        m "[bname]!"
                        scene mclub_me47 with dissolve
                        m "Uh"
                        scene mclub_me49 with dissolve
                        m "..."
                        scene mclub_me49a with dissolve
                        m "Ohhh"
                        b "Are you sore yet bitch?"
                        scene mclub_me50 with dissolve
                        m "Ahhh"
                        scene mclub_me51 with dissolve
                        m "..."
                        b "Turn quick!"
                        scene mclub_me52 with fade
                        m "..."
                        scene mclub_me53 with hpunch
                        m "Mmm"
                        scene mclub_me54 with dissolve
                        m "..."
                        ca "I'll go now"
                        m "Thank you Carlos"
                        b "See you"
                        scene mclub_me55 with fade
                        m "Come hug me [bname]"
                        b "Good night"
                        jump newday

            "Let's do this together":
                b "And let's take this suit off"
                pass

        scene mclub_me31 with dissolve
        m "Carlos?"
        scene mclub_me32 with dissolve
        m "Why don't you want to show it to me"
        m "Remove this"
        ca "Patience my dear"
        scene mclub_me33 with dissolve
        m "Mmm"
        scene mclub_me34 with dissolve
        ca "Patience"
        scene mclub_me35 with dissolve
        m "{i}(The excitement is killing me){/i}"
        b "Enough, get down"
        scene mclub_me36 with dissolve
        m "Mmm"
        scene mclub_me37 with dissolve
        b "Come, get up"
        scene mclub_me38 with fade
        m "Mmm you know how to please a woman Carlos"
        b "{i}(Bitch){/i}"
        b "Let's do this properly"
        scene mclub_me39 with dissolve
        play sound "sounds/mgrunt.wav"
        m "Ahh [bname]"
        scene mclub_me40 with dissolve
        stop sound
        m "Take it easy, what's wrong with you?"
        scene mclub_me41 with dissolve
        b "Easy, right?!"
        scene mclub_me42 with dissolve
        play sound "sounds/mpant.wav"
        m "Mhhmm"
        b "Shut her mouth with your cock"
        scene mclub_me43 with dissolve
        stop sound
        play sound "sounds/mgag1.wav"
        ca "Ahhh"
        scene mclub_me44 with dissolve
        m "Mmm"
        ca "I want her ass"
        m "Mhmm"
        stop sound
        scene mclub_me45 with dissolve
        m "..."
        scene mclub_me46 with dissolve
        ca "Fuck yeah"
        b "Wait for me"
        scene mclub_me48 with dissolve
        m "[bname]!"
        scene mclub_me47 with dissolve
        m "Uh"
        scene mclub_me49 with dissolve
        b "Are you sore yet bitch?"
        scene mclub_me50 with dissolve
        m "Ahhh"
        scene mclub_me51 with dissolve
        m "..."
        b "Turn quick!"
        scene mclub_me52 with fade
        m "..."
        scene mclub_me53 with hpunch
        m "Mmm"
        scene mclub_me54 with dissolve
        m "..."
        ca "I'll go now"
        m "Thank you Carlos"
        b "See you"
        scene mclub_me55 with fade
        m "Come hug me [bname]"
        b "Good night"
        jump newday


    else:
        scene mclub_me8 with dissolve
        m "No! Please leave"
        ca "Ok, have a good evening"
        scene mclub_me9 with dissolve
        m "I'll deal with you tomorrow"
        scene mclub_me10 with dissolve
        b "{i}(I screwed up, should have worked on my relationship and corruption points){/i}"
        b "{i}(I'll go to sleep now){/i}"
        jump newday



label girlescort:
    scene mclub8_call with dissolve
    b "Hi Elaine"
    b  "Where can I order a girl stripper, escort, or something"
    e "{i}(Ouch, and why you don't want me?){/i}"
    b "I need to celebrate with [mname]"
    e "{i}(Ouch again, right in my heart){/i}"
    b "Look I'm serious, I just want to surprise her"
    e "{i}(Hmm let me see){/i}"
    b "Not so expensive please"
    e "{i}(Don't worry, this time is on me){/i}"
    b "Cool, thank you"
    e "{i}(You're gonna love this one){/i}"
    scene mclub8 with dissolve
    b "{i}(Cool){/i}"
    scene mclub_ge0 with fade
    m "What to put on?"
    scene black
    "..."
    scene mclub_me with fade
    b "Woah"
    scene mclub_me1 with dissolve
    b "Cheers"
    m "Whisky [bname]!!?"
    if persistent.patch_enabled:
        b "Mom we're celebrating"
        pass
    else:
        b "But we're celebrating"
        pass
    play sound "sounds/doorbell.wav"
    m "..."
    m "Are you expecting someone?"
    stop sound
    b "Yes I asked Elaine for something to celebrate"
    m "Ah, I see"
    m "I'll open to surprise her"
    scene mclub_me2 with dissolve
    m "Hi Elaine"
    m "Come in"
    scene mclub_ge with dissolve
    m "Oh! I'm...I'm so sorry"
    scene mclub_ge1 with dissolve
    "Hi"
    "My name is Faye"
    fa "I've been sent by Elaine for this party"
    b "Cool"
    scene mclub_ge2 with dissolve
    m "[bname]! What is the meaning of that?"
    b "I... I thought we can get something new to spice up our life"
    scene mclub_ge3 with dissolve
    m "Oh my God"
    fa "Relax, I'm a professional dancer"
    if mrel >=200 and mcorr >= 30:
        m "No"
        $ persistent.unlock_21 = True
        scene mclub_ge4 with dissolve
        b "Oh come on"
        b "We're just celebrating, it's a one off"
        fa "Yes, just a celebration"
        m "{i}(Maybe I can teach [bname] a lesson){/i}"
        m "Mhm"
        m "Ok let's see your moves"
        scene mclub_ge5 with fade
        fa "Do you have a chair or something?"
        scene mclub_ge6 with dissolve
        b "I'll get you a chair"
        m "{i}(There's something odd with this girl){/i}"
        scene mclub_ge7 with dissolve
        fa "Thank you for the chair sweetheart"
        fa "Whoops!"
        scene mclub_ge8 with dissolve
        fa "Mmm"
        scene mclub_ge9 with dissolve
        fa "like what you see?"
        scene mclub_ge10 with dissolve
        fa "Why don't you come here?"
        scene mclub_ge11 with dissolve
        fa "Undress yourself"
        fa "Oh aren't you a cutie"
        fa "I'll undress first, so you can feel at ease"
        scene mclub_ge12 with dissolve
        "CHOOSE FAYE'S GENDER"
        menu:
            "Female":
                scene mclub_ge13 with dissolve
                m "{i}(Look at those ugly boobs){/i}"
                m "{i}(Pay some money and get a good surgeon, bitch!){/i}"
                m "{i}(An it seems nobody taught the bitch to match makeup and clothes?){/i}"
                scene mclub_ge14 with dissolve
                b "Mmm"
                scene mclub_ge15 with dissolve
                b "{i}(Hot!){/i}"
                scene mclub_ge16 with dissolve
                fa "So how do we do this?"
                b "Why don't you take care of [mname] while I take the chair away"
                scene mclub_ge17 with dissolve
                fa "You're such a gorgeous woman"
                scene mclub_ge18 with dissolve
                fa "By the way, who's the young guy?"
                m "..."
                fa "You don't wanna answer"
                scene mclub_ge19 with dissolve
                fa "I'm a good girl"
                fa "I'll take care of you"
                scene mclub_ge20 with dissolve
                m "..."
                scene mclub_ge21 with dissolve
                m "Mmmm"
                b "Cool"
                scene mclub_ge22 with dissolve
                fa "Come let's have some fun"
                scene mclub_ge23 with dissolve
                m "This looks more like your celebraton"
                b "Hmm"
                scene mclub_ge24 with dissolve
                b "Mmm"
                scene mclub_ge25 with dissolve
                b "She's good"
                m "Mmm"
                b "Enough sucking"
                scene mclub_ge26 with dissolve
                fa "Ah"
                scene mclub_ge27 with dissolve
                m "Ahhh.."
                b "Come here"
                scene mclub_ge28 with fade
                b "Ahh fuck"
                scene mclub_me10 with fade
                b "{i}(What a night){/i}"
                b "{i}(I'll go to sleep now){/i}"
                jump newday
                
            "Transgender":
                scene mclub_ge13 with dissolve
                m "{i}(Look at those ugly boobs){/i}"
                m "{i}(Pay some money and get a good surgeon, bitch!){/i}"
                m "{i}(An it seems nobody taught the bitch to match makeup and clothes?){/i}"
                scene mclub_ge14 with dissolve
                b "Mmm"
                scene fayeanim with dissolve
                b "Cool"
                b "Wait a minute!"
                scene mclub_ge15t with dissolve
                b sur "Oh my fucking crap!"
                scene mclub_me20 with dissolve
                m "Hahahaha"
                m "{i}(Karma's got you bitch! Fascinated by her){/i}"
                m "{i}(Thinking she's a girl, and Kaboom!){/i}"
                scene mclub_ge16t with dissolve
                m "{i}(Hot ass){/i}"
                scene mclub_ge17t with dissolve
                m "Let's lose this bra"
                b "What?!"
                m "Stop saying what and clear the floor mess"
                m "Take the chair to wherever you brought it from"
                scene mclub_ge18t with dissolve
                m "So is it real?"
                fa "Hahaha"
                scene mclub_ge19t with dissolve
                fa "Of course it is real"
                m "But do you feel anything?"
                scene mclub_ge20t with dissolve
                m "Oh my God, it's huge"
                m "Is it natural?"
                fa "Do you want to touch it?"
                m "Ermm"
                fa "It won't bite, come"
                scene mclub_ge21t with dissolve
                fa "By the way, who's the young guy?"
                m "Ah yes.."
                m "Erm and your ass is it real?"
                m "Or some brazilian operation"
                fa "Hahaha, I am brazilian, I don't need a brazilian lift"
                fa "I'm the real deal"
                fa "What about the guy? Who is he?"
                m "Sorry I totally zoned out"
                m "Yes, he's... He's a friend of my son"
                fa "Ah you are such a cute vixen"
                scene mclub_ge22t with dissolve
                fa "See all natural"
                scene mclub_ge23t with dissolve
                fa "I sense that you are a shy woman despite giving the impression that you aren't"
                fa "Take that corset away"
                scene mclub_ge24t with dissolve
                b "Ohh"
                scene mclub_ge25t with dissolve
                m "Ahh"
                scene mclub_ge26t with dissolve
                b "{i}(I guess I'll watch for a bit){/i}"
                scene mclub_ge27t with dissolve
                fa "Mmmmhm"
                scene mclub_ge28t with fade
                b "{i}(Bitch looking at me){/i}"
                scene mclub_ge29t with dissolve
                fa "Ahh"
                b "Alright, my turn now"
                scene mclub_ge30t with dissolve
                fa "Come get your turn on this one"
                m "Yes why not [bname]"
                menu:
                    "No let's take her both":
                        scene mclub_ge30ta with dissolve
                        fa "Good idea"
                        scene mclub_ge31ta with dissolve
                        m "Mmm"
                        scene mclub_ge32ta with dissolve
                        m "Oh"
                        fa "Come here baby"
                        scene mclub_ge33ta with dissolve
                        m "Huh"
                        scene mclub_ge34ta with dissolve
                        fa "Come get it"
                        scene mclub_ge35ta with dissolve
                        m "Ugh"
                        scene mclub_ge36ta with dissolve
                        m "[bname]"
                        "SHE MUTTERED"
                        b "Make her kiss your feet"
                        scene mclub_ge37ta with dissolve
                        m "..."
                        scene mclub_ge38ta with dissolve
                        fa "{i}(Mmmm I want this boy to suck my cock){/i}"
                        scene mclub_ge39ta with dissolve
                        fa "Ahhh"
                        scene mclub_ge40ta with dissolve
                        fa "Ahhh"
                        menu:
                            "Tell [mname] to suck Faye":
                                scene mclub_ge41ta with fade
                                fa "Ahh yess"
                                scene mclub_ge42ta with dissolve
                                fa "I know deep inside you want to be in her place"
                                fa "The curiosity is killing you"
                                fa "Here's my number in case you overcome your fears"
                                menu:
                                    "Take it":
                                        b "Ok"
                                        $ fayenumber = 1
                                        scene mclub_me10 with fade
                                        b "{i}(What a night){/i}"
                                        b "{i}(I'll go to sleep now){/i}"
                                        jump newday

                                    "No thanks":
                                        b "No, it's not going to happen"
                                        b "Thanks"
                                        scene mclub_me10 with fade
                                        b "{i}(What a night){/i}"
                                        b "{i}(I'll go to sleep now){/i}"
                                        jump newday

                    "Carry on, I'll watch more":
                        pass
                b "You know what, I've enjoyed watching you, carry on"
                scene mclub_ge31t with dissolve
                fa "God you're so hot"
                fa "Let me put a condom first"
                scene mclub_ge32t with dissolve
                m "Oh lord"
                scene mclub_ge33t with dissolve
                m "..."
                fa "Let's get to the couch"
                scene mclub_ge34t with dissolve
                m "Make it slow please"
                b "{i}(Bitch pretending to be new to this){/i}"
                fa "Don't worry gorgeous, I know"
                scene mclub_ge35t with dissolve
                m "Mmm"
                scene mclub_ge36t with dissolve
                m sad "Oh"
                scene mclub_ge35t with dissolve
                m sad "..."
                scene mclub_ge36t with dissolve
                m sad "Oh"
                scene mclub_ge35t with dissolve
                m sad "..."
                scene mclub_ge36t with dissolve
                m sad "Oh dear"
                scene mclub_ge37t with dissolve
                m "Ahhhhhh"
                scene mclub_ge38t with dissolve
                fa "Ahh yess"
                fa "Good night guys"
                b "My turn"
                scene mclub_ge39t with dissolve
                b "{i}(I think it's better to leave her alone){/i}"
                b "{i}(I'll go to sleep now){/i}"
                jump newday



    else:
        scene mclub_ge4 with dissolve
        m "No! Please leave"
        fa "Ok, have a good evening"
        scene mclub_me9 with dissolve
        m "I'll deal with you tomorrow"
        scene mclub_me10 with dissolve
        b "{i}(I screwed up, should have worked on my relationship and corruption points){/i}"
        b "{i}(I'll go to sleep now){/i}"
        jump newday
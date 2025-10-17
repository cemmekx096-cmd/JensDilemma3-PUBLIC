


label bvisitm:
    $ Hour += 4
    scene mclub with fade
    play sound "sounds/clapping.mp3"
    "Yeah!!"
    "..."
    scene mclub1 with dissolve
    "..."
    scene mclub2 with dissolve
    m "Huh"
    b "{i}(She saw me){/i}"
    stop sound fadeout 1.0
    scene mclub3 with dissolve
    b "Cool yeah!"
    scene mclub4 with dissolve
    b "Oh wow"
    scene mdc
    m "..."
    play sound "sounds/cheer.mp3"
    m "..."
    "Yeah"
    m "..."
    "..."
    stop sound fadeout 1.0
    if mellastrequest >= 1:
        scene mclub5_edit with fade
        play sound "sounds/clapping.mp3"
        b "Awesome"
        "..."
        "Oh God!!"
        scene mclub31 with dissolve
        "..."
        stop sound
        pass
    else:
        scene mclub5 with fade
        play sound "sounds/clapping.mp3"
        b "Awesome"
        "..."
        "Oh God!!"
        stop sound
        pass
    scene mclub6 with fade
    b "Are you done?"
    m "Yes"
    m "That was it for tonight"
    b "Ah, no other shows?"
    m "No more, and I've got good money tonight"
    scene mclub7 with fade
    b "How much did you get?"
    m "A lot"
    b "Cool, let's celebrate"
    m "Yes, good idea, prepare some drinks I'm going to change into something more comfy"
    b "Yeah put something nice"
    scene mclub8 with dissolve
    b "{i}(Maybe I can call){/i}"
    menu:
        "A male stripper":
            jump maleescort

        "A girl escort":
            jump girlescort

        "Don't call anyone":
            pass

    scene mclub9 with fade
    b "Woah"
    scene mclub10 with dissolve
    b "Cheers"
    m "Whisky [bname]!!?"
    if persistent.patch_enabled:
        b "Mom we're celebrating"
        pass
    else:
        b "But we're celebrating"
        pass
    m "All right"
    scene mclub11 with dissolve
    b "{i}(What is she doing?){/i}"
    scene mclub12 with dissolve
    m "{i}(Oh [mname] what's going on with you){/i}"
    m "{i}(How the hell I have been dragged into this...){/i}"
    if persistent.patch_enabled:
        m "{i}(With my own son){/i}"
        pass
    else:
        m "{i}(With a guy who's the age of my son){/i}"
        m "{i}(Even younger){/i}"
        pass
    "..."
    if mrel >= 180:
        scene mclub14 with dissolve
        $ persistent.unlock_14 = True
        m "{i}(The damage is already done){/i}"
        scene mclub15 with dissolve
        m "..."
        scene mclub16 with dissolve
        m "..."
        scene mclub17 with dissolve
        m "Undress yourself"
        scene mclub18 with dissolve
        m "{i}(For the first time I see [bname] scared){/i}"
        menu:
            "I'll play him a little bit" if mcorr >= 20 and bandageremove ==1:
                $ persistent.unlock_68 = True
                m "{i}(It's my turn to play){/i}"
                m "I said undress yourself"
                b lau "Undress me"
                scene mplaydom with vpunch
                b "Ouch!"
                m "Undress"
                scene mplaydom1 with fade
                b "What now?"
                b "Are you serious?"
                scene mplaydom2 with dissolve
                b "Ahhh"
                m "Damn I am"
                scene mplaydom3 with dissolve
                m "Stay as you are"
                scene mplaydom4 with dissolve
                m "You like it huh!"
                scene mplaydom5 with dissolve
                m "No moving I said"
                scene mplaydom6 with dissolve
                m "No touching also"
                scene mplaydom7 with dissolve
                m "..."
                scene mplaydom8 with dissolve
                b "Please let me control the thrust"
                scene mplaydom7 with dissolve
                m "No"
                scene mplaydom8 with dissolve
                b "I'll explode"
                m "Noo!"
                scene mplaydom9 with dissolve
                b "Ahhh"
                scene mplaydom10 with dissolve
                m "Happy!?"
                b "Not so"
                b "Good night"
                jump newday

            "Normal love":
                pass
        scene mclub19 with dissolve
        m "Wait, let me take off my body"
        scene mclub20 with dissolve
        m "Ohh"
        scene mclub21 with dissolve
        m "Ahh"
        menu:
            "Anal":
                scene mclub22 with dissolve
                m "[bname] not there"
                scene mclub23 with dissolve
                m "Ahh"
                scene mclub24 with dissolve
                m "Ahhh"
                scene mclub25 with hpunch
                m "[bname]! Ahhh!"
                scene mclub26 with dissolve
                m "..."
                scene mclub27 with dissolve
                m "[bname]!!"
                menu:
                    "Cum in":
                        scene mclub28 with hpunch
                        m "Uhhh"
                        scene mclub29 with dissolve
                        b "Good night b..."
                        b "Babe"
                        jump newday
                    "Cum in her mouth":
                        scene mclub30 with fade
                        m "Ahhh"
                        b "Good night b..."
                        b "Babe"
                        jump newday

            "Help her ride it":
                b "Come on top"
                scene mclubr with dissolve
                m "..."
                m "Put it in"
                m "Be gentle, you're so big honey"
                scene mclubra with dissolve
                m "Ahh"
                scene mclubr1 with dissolve
                m "Ahh"
                b "I'm close"
                scene mclubr2 with dissolve
                b "Ahhh fuck"
                scene mclubr3 with dissolve
                m "Nice"
                scene mclubr4 with fade
                m "Going to sleep?"
                b "Yes"
                m "I'll go out to meet some friends"
                m "Good night"
                jump newday
        
    else:
        m "{i}(No, I can't do that){/i}"
        scene mclub13 with dissolve
        m "Good night"
        b "What?"
        b "{i}(What the fuck!){/i}"
        "GET YOUR POINTS TO HIGHER THAN 180"
        jump newday



label jmasha:
    m "{i}(I should check on them){/i}"
    m "{i}(Come on [mname] just a quick peek I promise){/i}"
    scene cnd27a with dissolve
    "..."
    scene cnd29b with dissolve
    m "{i}(Time to return to my room){/i}"
    if mcorr >=35:
        m "{i}(Or maybe I can){/i}"
        scene mascnd2ma with dissolve
        m "{i}(Wow she's good at sucking){/i}"
        m "{i}(If she can take my baby's big cock){/i}"
        m "{i}(God what am I doing?){/i}"
        m "{i}(Oh they're coming close){/i}"
        scene mascnd3ma with dissolve
        nd "Baby it's painful"
        scene mascnd4ma with dissolve
        m "Ahh"
        scene cnd27c with dissolve
        m "{i}(I'll get something to drink){/i}"
        pass
    else:
        "RAISE HER CORRUPTION POINTS TO 35"
        scene cnd27c with dissolve
        m "{i}(Or maybe I'll get a glass of water){/i}"
        scene cnd27ba with dissolve
        b "..."
        scene cnd27ca with dissolve
        m "..."
        scene cnd27da with dissolve
        "..."
        scene cnd27ea with dissolve
        m "{i}(What am I doing!){/i}"
        scene cnd27fa with dissolve
        m "{i}(I should go){/i}"
        scene halln_m_in11a with fade
        "YOU NEED 35 CORRUPTION POINTS WITH [mname]"
        jump newday

    scene cnd27bc with dissolve
    nd "Oh God miss [mname], I'm..."
    scene cnd27db with dissolve
    nd "I'm so sorry"
    m "Oh why are you leaving, the night is still early?"
    b "Masha, your shirt"
    menu:
        "[mname] will let her go":
            scene cnd30ba with fade
            m "I'm sorry dear, I just wanted to drink water"
            b "Say sorry to him"
            scene cnd31ba with dissolve
            b "..."
            scene cnd32ba with dissolve
            b "What do you want now?"
            scene cnd33ba with dissolve
            m "..."
            scene cnd334ba with dissolve
            "..."
            scene cnd335ba with dissolve
            menu:
                "Fuck her in this position":
                    $ persistent.unlock_83 = True
                    scene cnd336ba with dissolve
                    "..."
                    scene mhher with dissolve
                    "YOU CAN PRESS H"
                    "..."
                    m "Ahhh"
                    "..."
                    m "[bname] yes"
                    scene cnd337ba with dissolve
                    m "Mmm"
                    scene cnd338ba with fade
                    b "I'm going to sleep"
                    jump newday
                "Throat fuck":
                    scene mtf with fade
                    b "Yes"
                    b "Bitch!"
                    m "..."
                    b "Ahh"
                    scene cnd339ba with dissolve
                    b "Are you okay?"
                    m "Haa yes"
                    b "I'm going to sleep"
                    jump newday

        "[mname] will stop her":
            m "Stop!"
            scene cnd340ba with fade
            nd "I'm really sorry"
            m "..."
            m "Don't worry"
            m "There's nothing wrong with love"
            m "And you are a beautiful girl"
            scene cnd341ba with dissolve
            m "I'm very happy that you are my son's girlfriend"
            m "But"
            m "You don't sneak at nights"
            m "And do these things in the main hall"
            m "What I want you to do now"
            m "Go to his room"
            m "And do whatever you want like two normal adults"
            scene cnd342ba with dissolve
            nd "Hmm"
            nd "No it's fine"
            m "Go on, I can see the smile that you're trying to hide"
            m "Just go both of you"
            scene cnd343ba with dissolve
            nd "Your mom is nice"
            b "Yes and it seems she likes you"
            b "{i}(Which gives me an idea for another time){/i}"
            nd "Do you think so?"
            b "Yes"
            b "It's not talking time"
            scene cnd344ba with dissolve
            b "{i}(Maybe I can have a threesome with both of them){/i}" 
            $ mashamname = 1
            b "{i}(But this needs preparation){/i}"
            scene black
            "..."
            jump newday 
            
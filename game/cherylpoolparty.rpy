

label cherylpoolparty:
    $ persistent.unlock_61 = True
    scene cpp with dissolve
    c "Hey [sname]"
    scene cpp1 with dissolve
    c "Here"
    scene cpp2 with dissolve
    b "{i}(I feel I know this guy){/i}"
    scene cpp3 with dissolve
    b "{i}(I've seen him somewhere){/i}"
    c "There's someone I want you to meet"
    scene cpp4 with dissolve
    c "Pedro, this is my niece"
    c "[sname] meet my friend Pedro"
    scene cpp5 with dissolve
    b "{i}(I need to choose who to hang out with...){/i}"
    scene cpp6 with dissolve
    b "{i}(Damn, they both left with him){/i}"
    b "{i}(Bitches){/i}"
    scene cpp5 with dissolve
    b "{i}(Who to choose?){/i}"
    menu:
        "New girl":
            scene cpp7 with dissolve
            b "Hi"
            b "{i}(What the hell is wrong with her face){/i}"
            "Who are you?"
            b "I'm [bname]"
            "Yeah, nice to meet you"
            b "I'm a friend of Cheryl"
            b "What's that on your face?"
            "It's blush my dear"
            b "Oh I see"
            b "Would you like a drink?"
            "Yes, anyway this thing is boring"
            scene cpp8 with fade
            "Cheers"
            b "So..."
            b "You seem not enjoying this"
            scene cpp9 with dissolve
            "No, I'm not"
            b "Why?"
            "I'm an escort, I was invited to this party"
            "And no one is interested in sex"
            b "Hell, I am interested"
            "But I charge my dear"
            b "How much is it?"
            "$1000"
            b "Damn"
            menu:
                "Ok" if mny >=1000:
                    "Let's go to the room"
                    $ mny -= 1000
                    scene cpp10 with dissolve
                    "Undress and follow me to the couch"
                    b "Aren't you gonna give me some love first"
                    "I don't do that honey"
                    "Only fucking"
                    scene cpp11 with dissolve
                    b "Alright, you wanna play this game?"
                    scene cpp12 with dissolve
                    "Ahh"
                    scene cpp13 with hpunch
                    "Hah!"
                    scene cpp14 with dissolve
                    b "..."
                    scene cpp15 with dissolve
                    b "Get up!"
                    scene cpp16 with dissolve
                    b "Yes bitch"
                    scene cpp17 with dissolve
                    b "Ahhh"
                    scene cpp18 with dissolve
                    b "Thank you"
                    scene cpp19 with fade
                    b "{i}(What the hell!){/i}"
                    b "{i}(Where is everybody?){/i}"
                    menu:
                        "Search for Rowena":
                            scene cppran with dissolve
                            b "{i}(Oh my....){/i}"
                            a "Ahhh"
                            b "{i}(She's more of a bitch than [sname]){/i}"
                            a "Ah"
                            a "..."
                            scene cpp20 with dissolve
                            a "Mmmm"
                            scene cpp21 with dissolve
                            a "Oh My God"
                            b "{i}(I better leave){/i}"
                            scene cpp19 with fade
                            "..."
                            scene cpp30 with fade
                            b "Aha! Here's comes everybody"
                            b "Shall we go"
                            c "It was lovely seeing you darling"
                            s "You too, mwah"
                            b "Come on let's go"
                            jump broom_menu 

                        "Search for [sname]":
                            scene cpp22 with fade
                            b "{i}(Holy crap){/i}"
                            scene cpp23 with dissolve
                            b "..."
                            scene cpp24 with dissolve
                            b "..."
                            scene cpp25 with dissolve
                            b "..."
                            scene cpp26 with dissolve
                            p "Ahh"
                            scene cpp27 with dissolve
                            p "Mmm"
                            scene cpp26 with dissolve
                            p "Cheryl your niece is a pro cock sucker"
                            scene cpp28 with dissolve
                            b "{i}(Damn it, that bitch is getting destroyed){/i}"
                            scene cpp29 with dissolve
                            b "{i}(I'm out of here){/i}"
                            scene cpp19 with fade
                            "..."
                            scene cpp30 with fade
                            b "Aha! Here's comes everybody"
                            b "Shall we go"
                            c "It was lovely seeing you darling"
                            s "You too, mwah"
                            b "Yes indeed!"
                            b "Come on let's go"
                            jump broom_menu 

                "Go check where are the others":
                    scene cpp19 with fade
                    b "{i}(What the hell!){/i}"
                    b "{i}(Where is everybody?){/i}"
                    menu:
                        "Search for Rowena":
                            scene cppran with dissolve
                            b "{i}(Oh my....){/i}"
                            a "Ahhh"
                            b "{i}(She's more of a bitch thank [sname]){/i}"
                            a "Ah"
                            a "..."
                            scene cpp20 with dissolve
                            a "Mmmm"
                            scene cpp21 with dissolve
                            a "Oh My God"
                            b "{i}(I better leave){/i}"
                            scene cpp19 with fade
                            "..."
                            scene cpp30 with fade
                            b "Aha! Here's comes everybody"
                            b "Shall we go"
                            c "It was lovely seeing you darling"
                            s "You too, mwah"
                            b "Come on let's go"
                            jump broom_menu 

                        "Search for [sname]":
                            scene cpp22 with fade
                            b "{i}(Holy crap){/i}"
                            scene cpp23 with dissolve
                            b "..."
                            scene cpp24 with dissolve
                            b "..."
                            scene cpp25 with dissolve
                            b "..."
                            scene cpp26 with dissolve
                            p "Ahh"
                            scene cpp27 with dissolve
                            p "Mmm"
                            scene cpp26 with dissolve
                            p "Cheryl your niece is a pro cock sucker"
                            scene cpp28 with dissolve
                            b "{i}(Damn it, that bitch is getting destroyed){/i}"
                            scene cpp29 with dissolve
                            b "{i}(I'm out of here){/i}"
                            scene cpp19 with fade
                            "..."
                            scene cpp30 with fade
                            b "Aha! Here's comes everybody"
                            b "Shall we go"
                            c "It was lovely seeing you darling"
                            s "You too, mwah"
                            b "Yes indeed!"
                            b "Come on let's go"
                            jump broom_menu 



        "Rowena":
            scene cpp31 with dissolve
            b "Hey, let's have a drink and explore the place"
            a "Okay"
            scene cpp32 with dissolve
            "..."
            scene cpp33 with fade
            a "This place is huge and empty"
            b "Yes an empty palace"
            b "I couldn't ask for more"
            a "Scary"
            scene cpp34 with dissolve
            b "Relax"
            a "I am but still the silence"
            scene cpp35 with dissolve
            b "The silence of the lambs"
            b "Omg you're such a cutie petite"
            b "Take that glass away"
            scene cpp36 with dissolve
            a "Mmm"
            scene cpp37 with dissolve
            a "MMm"
            scene cpp39 with dissolve
            b "You're such a doll"
            b "I want you Rowena"
            b "For me only"
            a "Are you sure? with all the girls you've been with"
            b "Which girls?"
            a "Your girls"
            a "Ah"
            b "I'm a one woman only man"
            b "And that woman is you"
            scene cpp40 with dissolve
            a "Ugh stop lying"
            scene cpp41 with dissolve
            a "Slowly [bname]"
            scene cpp42 with dissolve
            a "Ahhh"
            b "Fuck you're so tight"
            scene cpp43 with dissolve
            a "Ohhh"
            b "I'm not gonna last long"
            b "Change position"
            scene cpp44 with dissolve
            a "Mmhmm"
            b "..."
            scene cpp45 with dissolve
            b "I'll go now"
            scene cpp19 with fade
            b "{i}(I wonder where is [sname]){/i}"
            scene cpp22 with fade
            b "{i}(Holy crap){/i}"
            scene cpp23 with dissolve
            b "..."
            scene cpp24 with dissolve
            b "..."
            scene cpp25 with dissolve
            b "..."
            scene cpp26 with dissolve
            p "Ahh"
            scene cpp27 with dissolve
            p "Mmm"
            scene cpp26 with dissolve
            p "Cheryl your niece is a pro cock sucker"
            scene cpp28 with dissolve
            b "{i}(Damn it, that bitch is getting destroyed){/i}"
            scene cpp29 with dissolve
            b "{i}(I'm out of here){/i}"
            scene cpp19 with fade
            "..."
            scene cpp30 with fade
            b "Aha! Here's comes everybody"
            b "Shall we go"
            c "It was lovely seeing you darling"
            s "You too, mwah"
            b "Yes indeed!"
            b "Come on let's go"
            jump broom_menu 





label laundry:
    scene lndry with dissolve
    "..."
    scene lndry1 with fade
    b "{i}(Let's do this){/i}"
    menu:
        "Iron [sname] clothes":
            scene lndry2 with dissolve
            b "Easy"
            b "Time to go"
            $ srel += 5
            b "Huh"
            s "[bname]?"
            scene lndry6 with dissolve
            b "I just finished the laundry"
            b "And was ironing your clothes"
            s "Ok, thank you"
            show screen srelup
            b "Ok"
            hide screen srelup
            scene lndry3 with fade
            "..."
            call screen gnav

        "Iron [mname] clothes":
            scene lndry2 with dissolve
            b "Easy"
            b "Time to go"
            $ mrel += 5
            b "Huh"
            m "What are you doing honey?"
            scene lndry8 with dissolve
            b "I just finished the laundry"
            b "And was ironing your clothes"
            scene lndry8a with dissolve
            m "Leave everything please, just don't disturb yourself"
            m "You should be recovering"
            show screen mrelup
            b "Ok"
            hide screen mrelup
            scene lndry3 with fade
            "..."
            call screen gnav

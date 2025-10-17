


label joshuaday:
    $ joshuadaydone = 1
    $ Hour += 1
    play sound "sounds/doorbell.wav"
    scene jday with fade
    stop sound
    b "Hey, you managed to come"
    j "Yeah"
    j "But I cannot stay more than 2 hours"
    b "It's fine"
    b "Come let's go to my room"
    scene jday1 with fade
    j "That's not your room? Where's your laptop"
    b "Just hide under the bed and wait here"
    j "Huh"
    b "Just wait under the bed, maybe you'll get something"
    scene jday2 with dissolve
    j "Are you sure about this?"
    b "Just get your hands back and you're good"
    b "Now just stay here"
    b "I'll go talk to [sname]"
    b "See if she's going to the beach"
    call screen gnav
    
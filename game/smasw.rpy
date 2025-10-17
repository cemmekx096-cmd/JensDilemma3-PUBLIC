

label smasw:
    scene smas9 with fade
    w "{i}(Yes, that's a good idea){/i}"
    scene smas10 with dissolve
    m "Oh Hi Wanda"
    "..."
    m "I still have 2 hours of duty"
    m "You can wait for me [bname] is there"
    m "I'll call him anyway"
    scene smas11 with fade
    b "I'm out with my friends"
    m "{i}(Go home now, Wanda is coming){/i}"
    m "{i}(She wants to see me){/i}"
    b "Ok Ok I'll go back home"
    scene black
    "20 MINUTES LATER"
    scene smas12 with fade
    w "Hi [bname]"
    w "I know you're alone, but I wanted to see [mname]"
    b "Yes she called me"
    b "No worries at all"
    scene smas13 with dissolve
    w "So, how was your evening?"
    scene smas14 with dissolve
    b "Boring, I went out for a while, then I came back"
    scene smas15 with dissolve
    b "Where is Joshua, why didn't he come with you?"
    scene smas16 with dissolve
    "..."
    scene smas15 with dissolve
    w "Joshua was sleeping when I left"
    w "I didn't want to disturb him"
    w "You know what!? We can go now and bring him with us"
    b "{i}(That's weird, she's being overly nice with me){/i}"
    b "{i}(Maybe she wants to get fucked){/i}"
    b "{i}(Let's see where this goes){/i}"
    w "What, it seems you don't like"
    b "No no, of course I do like"
    w "I'll give you a ride of your life"
    b "{i}(Hmm interesting){/i}"
    scene smas17 with dissolve
    b "Oh"
    w "Wheeee!"
    scene smas18 with dissolve
    b "This..."
    b "Is..."
    b "So fast"
    w "Don't worry, we will get the other car for Joshua"
    scene smas19 with dissolve
    w "Joshua!"
    w "What are you hanging without a shirt!"
    w "Change and let's go"
    scene smas20 with fade
    "..."
    scene smas21 with dissolve
    w "[bname] may I get a glass of wine"
    b "Of course I'll get you one"
    scene smas22 with dissolve
    w "Thank you"
    b "{i}(She's so nice today){/i}"
    b "{i}(Maybe I'll get my chance){/i}"
    scene smas23 with dissolve
    m "Hey Wanda!"
    w "[mname] you came early"
    m "Yes, I'll change first"
    scene smas24 with fade
    m "Guys go play"
    m "Give us some alone time"
    menu:
        "We'll do for a lambo ride with Ms Wanda":
            if wsusp <8:
                w "Of course dear"
                $ wandaride = 1
                w "I'll come and take you during day time"
                b "Cool"
                pass

            else:
                w "We'll see about it later"
                b "Ok"
                pass

        "Continue":
            pass
    scene smas25 with fade
    j "So what do we do now?"
    b "Do you have new shots on your phone"
    scene smas26 with fade
    w "I can't stand his whims and desires anymore"
    w "I'm thinking not to go to these masked parties"
    m "You definitely should do what you feel is right"
    w "Can I ask you a favor?"
    m "Of course"
    w "I think you should join me one of these nights"
    m "Did he ask you to invite me?"
    w "No, I just want you to see what I'm suffering"
    w "Let's make it fun, we will pretend you're some random event guest"
    m "Sounds good, but are you ok with it!"
    w "No I'm not, we can just play along"
    w "Regardless of that you definitely should join me"
    w "There's something you should be aware of"
    scene smas26a with dissolve
    m "Something like what?"
    w "You will know when you're there"
    m "Ok"
    $ jenvisitmasquerade = 2
    scene smas26 with dissolve
    m "Say, maybe you can stay here tonight"
    w "I don't know [mname]"
    m "Why not, it could be fun"
    m "I'll give you a nightie, and Joshua some shorts"
    scene smas27 with dissolve
    w "I can't, I have an appointment early in the morning"
    w "But Joshua can stay"
    m "That will get [bname] happy"
    w "All right, I should go now"
    w "Let's go inform Joshua"
    scene smas26 with dissolve
    w "One request [mname]"
    w "Please keep an eye on them, you know the kids at this age"
    m "Don't worry about it, I'll take care of it"
    scene smas28 with fade
    w "Honey I decided that you can sleep here tonight"
    w "Here is some money in case you need anything"
    w "I'll be here by 8:00 after my appointment"
    j "Ok mom"
    scene smas29 with dissolve
    j "Cool"
    b "Who do you want to watch?"
    b "[mname] will have her shower by now"
    b "We can hide in there"
    b "[sname] is easier, we give her some money and she does whatever I want"
    menu:
        "[mname]":
            b "Let's go hide before she gets into the shower"
            scene smas30 with fade
            b "Shh keep quiet"
            scene smas31 with dissolve
            "..."
            scene smas32 with dissolve
            "..."
            scene smas33 with dissolve
            "..."
            scene smas34 with dissolve
            b "She's gone to the tub"
            b "Slowly get your head out and watch"
            scene smas35 with dissolve
            j "..."
            scene smas36 with dissolve
            j "..."
            scene smas37 with dissolve
            b "Hey get back in, she's about to finish"
            scene smas38 with dissolve
            j "..."
            scene smas39 with dissolve
            j "..."
            scene smas34 with dissolve
            b "She's gone"
            scene smas40 with fade
            b "Stay if you want to rub one out"
            j "Ok I'll shower and then where do I go?"
            b "Come to my room, you'll be sleeping there"
            j "Okay"
            scene smas56 with fade
            b "I wonder what's taking this idiot so long"
            scene smas58 with dissolve
            b "Finally here you are"
            j "Yes"
            b "Here change into this for sleeping"
            b "I'm gonna go sleep on the couch"
            j "Oh are you sure?"
            b "Yes"
            b "Good night"
            scene smas59 with fade
            b "Hey"
            b "Can I sleep here?"
            scene smas60 with dissolve
            m "Hmm"
            b "Come on! I don't want to sleep with Joshua"
            m "But no funny business"
            b "Ok"
            scene smas61 with dissolve
            "..."
            scene smas62 with dissolve
            m "Good night"
            scene black with fade
            jump newday

        "[sname] {i}Fantasy Choice{/i}":
            b "How much money do you have?"
            j "1000"
            b "Give me 500 I'll find a way for you to fuck [sname]"
            j "Oh"
            scene smas25 with dissolve
            j "What do I tell my mom about the money?"
            b "Oh my, does she ask you?"
            j "She's gonna ask what did I buy"
            b "Tell her you lost it"
            j "Okay"
            b "I'll go now make a deal with [sname]"
            b "Stay here, I'll be back"
            scene smas41 with fade
            b "Come on [sname]"
            b "He needs your help"
            b "I'll do whatever you want"
            scene smas42 with fade
            s "[bname] told me you know how to fix my phone"
            j "Do I?"
            b "..."
            s "Come with me, I really need it fixed"
            b "Go with her Joshua"
            scene smas43 with fade
            s "Take the phone"
            s "I need to get something"
            scene smas44 with dissolve
            s "..."
            scene smas45 with dissolve
            j "..."
            scene smas46 with dissolve
            j "Huh"
            scene smas47 with dissolve
            s "Relax babe"
            scene smas48 with dissolve
            j "Huh"
            s "Come"
            scene smas49 with dissolve
            s "I like slim fit guys"
            scene smas50 with dissolve
            j "Uhh"
            scene smas51 with dissolve
            j "Ffff"
            scene smas52 with dissolve
            j "Mmm"
            scene smas53 with dissolve
            j "..."
            scene smas54 with dissolve
            s "Mmm"
            scene smas53 with dissolve
            s "Ahhh"
            scene smas54 with dissolve
            s "..."
            scene smas55 with dissolve
            s "Don't come babe"
            scene smas56 with fade
            b "I wonder how this idiot is doing"
            scene smas57 with dissolve
            s "[bname] I just came to tell you"
            s "Joshua will stay in my room"
            b "Are you sure it's safe"
            s "Yes it is, he messed up and started crying"
            b sur "Oh jeez"
            b "Make sure no one finds out"
            s "Who cares"
            b "Oh come on!"
            s "Don't worry I'll sneak him out early in the morning"
            b "Ok"
            scene smas56 with dissolve
            b "Alright, time to sleep"
            jump newday


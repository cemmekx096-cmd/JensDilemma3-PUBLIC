
init -3 python:
    persistent.patch_installed = False
init -1 python:
    if persistent.patch_installed and not persistent.patch_first_time:
        persistent.patch_enabled = True
        persistent.patch_first_time = True
    elif not persistent.patch_installed:
        persistent.patch_first_time = False
        persistent.patch_enabled = False



define b = Character('[bname]', image = 'bchar')
define s = Character('[sname]', image = 'schar')
define m = Character('[mname]', image = 'mchar')
define d = Character("Stewart")
define e = Character("Elaine", color="#F7DED9")
define c = Character("Cheryl", color="#FFC000")
define r = Character("Rob")
define a = Character("Rowena", color="#ff00ea")
define mb = Character("Adam")
define n = Character("Katy")
define nd = Character("Masha")
define ml = Character('Melinda', image = 'melchar')
define dn = Character("Daniel")
define jn = Character("Jonas")
define w = Character('Wanda', image = 'wchar')
define j = Character("Joshua")
define ja = Character("Janey")
define ca = Character("Carlos")
define fa = Character("Faye")
define ch = Character("Chris")
define i = Character("Ida")
define z = Character("Zoey")
define p = Character("Pedro")
define rh = Character("Rhonda")
define ka = Character("Karl")



default mrel = 100
default srel = 100
default mny = 2000
default wk = 0
default scorr = 10
default mcorr = 0
default binjected = 0
default banesthetic = 200
default wsusp = 10
default joshuacorrupted = 0
default nadiajoin = 0
default snameacceptjoshua = 0
default snametoiletjoshua = 0
default snamecherylparty = 0
default sjosh = 0
default joshuatoilet = 0
default fayenumber = 0
default wandagym = 0
default jcorr = 0
default josh_r_photos = 0
default repeatjphotos = 0
default joshjaneyphotos = 0
default joshuadaydone = 0
default bmporn2done = 0
default smorehelpwithjoshua = 0
default masqueradeaccepted = 0
default mcherylrecording = 0
default gymwithwanda = 0
default christmas_withwanda_done = 0
default buyjewelry = 0
default bstarmovie = 0
default today = datetime.date.today()
default unlock43 = 0
default bmmovie = 0
default joshvisitpool = 0
default janeyseduction = 0
default cherylpoolparty = 0
default melinda_daughters = 0
default sbmbname = 0
default jaydeb = 0
default colaspike = 0
default bandageremove = 0
default escortrequest = 0
default melcallivan = 0
default siteunlocked = 0
default cwatch = 0
default dwashed = 0
default event1 = 0
default asksabtbreasts = 0
default ndvisit = 0
default brains = 0
default physique = 0
default lingeriechoice1 = 0
default lingeriechoice2 = 0
default mrobevidence = 0
#lt
default sscall = 0
default bstudied = 0
default event1_adv = 0
default aphro = 0
default srbname = 0 ### s reports bname
default costumeandwig = 0
default jenjealous = 0
default danm = 0
default money_cheat = 0
default gym = 0
default jmasturbate = 0
default mnamemoney = 0
default bexercise = 0
default bstudy = 0
default bworked = 0
default toiletcleaned = 0
default sworkvisited = 0
default event_s = 0
default slaundry = 0
default dishes = 0
default laundry = 0
default Hour = 16
default dayname = 0
default day = 0
default event2 = 0
default event3 = 0
default mtalk = 0
default condom_found = 0
default ndsnamestays = 0
default sat_m_event = 0 # 2 is sex scene in the club
default sundaytemp = 0 # resets to 0 with sex scene in the club
default bshirt = 0
default scalet = 0
default sbmb = 0
default topshelfchecked = 0
default alonewithm_hotel = 0
default melconvincem = 0
default smovie = 0
default smovieseen = 0
default ndevent = 0
default moviewithsname = 0
default mpaybackstewart = 0
default hardacrebdsm = 0
default money_cheat_discovered = 0
default mhair = 0
default jonascall = 0
default mgluteimprove = 0
default mnamenotavailable = 0
default mfirstmovie = 0
default brememberstudioname = 0
default bnamebodyguard = 0
default msecondmovie = 0
default elainemlesb = 0
default josh_hidden_cam = 0
default firsttimecam = 0
default bmljosh = 0
default jendidgo = 0
default sleepingpills = 0
default jenlastmovie = 0
default mellastrequest = 0
default askcherylforhelp = 0
default wandashower = 0
default movieplusone = 0
default wandaride = 0
default jenvisitmasquerade = 0
default mashamname = 0
default jfjaney = 0

label splashscreen:
    scene black
    with Pause(1)
    show text "THE CONTENT FROM OR THROUGH THIS GAME ARE PROVIDED “AS-IS,” “AS AVAILABLE,” AND ALL WARRANTIES, EXPRESSED OR IMPLIED, ARE DISCLAIMED (INCLUDING BUT NOT LIMITED TO THE DISCLAIMER OF ANY IMPLIED WARRANTIES OF MERCHANTABILITY AND FITNESS FOR A PARTICULAR PURPOSE). IT MAY CONTAIN BUGS, ERRORS, PROBLEMS OR OTHER LIMITATIONS. THE OWNER OF THIS GAME ASSUMES NO LIABILITY OR RESPONSIBILITY FOR ANY ERRORS OR OMISSIONS.\n\nWARNING. This game contains sexually oriented adult material intended for individuals 18 years of age or older. If you are not yet 18, if adult material offends you, or if you are accessing this game from any country or locale where adult material is prohibited by law, PLEASE LEAVE NOW! SEXUAL ACTIVITY IN THIS GAME IS A FANTASY, IT ISN'T REALITY, THIS GAME IS NOT ADVOCATING THAT YOU REENACT ANYTHING FROM ITS CONTENT. ALL CHARACTERS PORTRAYED IN THIS GAME ARE AT LEAST 18 YEARS OLD. If you understand and accept these terms, you may ENTER."
    with Pause(25)
    hide text with dissolve
    show text "The people in this game are all in possession of a recent and valid STD test. We do not promote unprotected sex"
    show text "SerialNumber Presents..." with dissolve
    with Pause(10)
    hide text with dissolve
    with Pause(1)
    #10lt
    menu:

        "I am 18 years old or above ":
            jump agecheck

        "I am below 18 years old":
            jump agecheck1
            
label agecheck:
    scene black
    with Pause(1)
    show text "Jen's Dilemma Chapter 3" with dissolve
    with Pause(9)
    hide text with dissolve
    with Pause(1)
    menu:
        "(c) 2024 SerialNumberComics, All Rights Reserved":
            play sound "sounds/introtwo.mp3"
            scene ch3main with fade
            "Enjoy playing"
            stop sound fadeout 3.0
            return
    
label agecheck1:
    "YOU CAN'T PLAY IF YOU'RE YOUNGER THAN 18"
    $ renpy.quit()
    

label start:
    scene jenny with fade
    "PRESS ENTER IF YOU WANT TO KEEP THE ORIGINAL NAME"
    $ mname = renpy.input("Enter main Female character name")
    $ mname = mname.strip()
    if mname == "":
        $ mname="Jenny"
    scene ivan with fade
    $ bname = renpy.input("Enter main Male character name")
    $ bname = bname.strip()
    if bname == "":
        $ bname="Ivan"
    scene nadia with fade
    $ sname = renpy.input("Enter secondary Female character name")
    $ sname = sname.strip()
    if sname == "":
        $ sname="Nadia"
    scene jdm3_1 with dissolve
    m "I want you to come with me"
    b "Where to?"
    m "I have a shooting"
    m "And I could use your support"
    b "Of course!"
    m "Let's go, and take that grin away please"
    scene jdm3_2 with fade
    jn "How's our star today?"
    m "Good, a little anxious"
    jn "There's no need to be, you're great"
    scene jdm3_3 with dissolve
    jn "Shall we go?"
    m "Yes"
    scene jdm3_4 with fade
    jn "Ok guys, so we're just waiting for Wanda"
    jn "She's going to be here any minute"
    scene jdm3_5 with dissolve
    w "Hey guys, sorry I'm late"
    b "{i}(Wow!){/i}"
    jn "Cool, let's proceed"
    jn "If anyone of you wants to review the script, do it now please"
    jn "Otherwise let's get into action"
    scene jdm3_6 with dissolve
    jn "[bname] you can stay during this cut, but keep your mouth shut!"
    b "Shtoom"
    scene mporn63 with fade
    #music
    "Late in that evening, when most employees have left"
    "But Jenna a diligent and ambitious employee was still at her desk"
    scene mporn64 with dissolve
    "..."
    scene mporn65 with dissolve
    w "Hmmm"
    w "Pretending to work?"
    w "Bitch!"
    scene mporn66 with dissolve
    m "..."
    scene mporn67 with dissolve
    m "Look Wanda"
    m "I'm sorry if being the most succesful employee and being Mr Johnson's favourite is adding to you insecurities"
    w "My husband hired you because you're a bitch"
    scene mporn68 with dissolve
    m "Huh! Me! Look at yourself"
    w "Wanda leaves fuming"
    scene mporn69 with fade
    m "{i}(Haa! Finally I'm done){/i}"
    m "{i}(I'll put the files back and leave){/i}"
    jn "Cut, that was great, in one take, you girls are perfect"
    jn "Let's head to the other location"
    jn "[bname] stay here please"
    b "Fuck!"
    scene mporn70 with fade
    # music
    m "..."
    scene mporn71 with dissolve
    "..."
    scene mporn72 with dissolve
    m "Leave me alone! Will you!!"
    scene mporn73 with hpunch
    m "Ahh"
    w "I'll show you who's bitch"
    scene mporn74 with dissolve
    m "You'll be in big trouble"
    scene mporn75 with hpunch
    w "Your big overused pussy"
    w "That's what's gonna be in trouble"
    scene mporn76 with dissolve
    m "You're nuts"
    scene mporn77 with dissolve
    w "You're fucking my husband right?"
    scene mporn78 with dissolve
    m "..."
    scene mporn78a with hpunch
    w "I asked you a question bitch!"
    m "I..."
    scene mporn78b with dissolve
    m "Never did"
    w "Hmm, you're so wet already"
    w "Seems you like to be dominated"
    scene mporn79 with dissolve
    w "Mmmm"
    scene mporn80 with dissolve
    m "Ahh"
    w "If you want to keep working in this company"
    w "Then you'll have to be my slut"
    scene mporn81 with dissolve
    w "Understand bitch?"
    scene mporn81a with dissolve
    w "Do you understand!?!"
    m "Yes"
    scene mporn81b with dissolve
    w "Good girl"
    w "You like it huh!?"
    scene mporn81c with dissolve
    w "Seems you do"
    scene mporn82 with dissolve
    w "..."
    scene mporn83 with dissolve
    m "Uhh"
    scene mporn84 with dissolve
    w "Mmmm"
    scene mporn85 with dissolve
    w "You like that bitch"
    m "Yes"
    w "Turn"
    scene mpornanim
    m "Ahh"
    w "Yes bitch"
    scene mporn86 with dissolve
    m "Mhhm"
    jn "Cut! Awesome"
    scene jdm3_7 with fade
    b "How was Wanda, did you get along?"
    m "Yes she's cool, we exchanged numbers and decided to meet up some time"
    m "She has a son around your age also"
    b "Maybe him and me can be friends also"
    m "Thanks God this stalker didn't show up today"
    m "I'll beat his ass if he shows up"
    scene jdm3_8 with dissolve
    m "You'll do nothing"
    m "Just ignore him"
    b "You'll see, I'll destroy him"
    m "[bname]"
    m "I didn't bring you to fight him, just seeing you with me is enough to shoo him"
    m "Just get us a taxi, please!"
    "Hey beautiful"
    scene jdm3_9 with dissolve
    b "You piece of shit!"
    scene jdm3_10 with dissolve
    play sound "sounds/pistolsound.mp3"
    m "[bname] oh my god!"
    stop sound
    scene black
    play sound "sounds/ambulace.mp3"
    "..."
    "..."
    stop sound fadeout 3.0
    scene jdm3_11 with fade
    m ",,,"
    scene jdm3_12 with fade
    b "Ahh! What happened?"
    "No no, don't move"
    scene jdm3_13 with dissolve
    "Finally you woke up"
    b "What happened? Why I can't feel my lower body"
    "It's the anesthetic"
    b "What's that?"
    "It's sort of a pain killer, to stop you from feeling the pain of the operation"
    "That bottle over there, we used it during the operation"
    scene jdm3_14 with dissolve
    b "Which operation?"
    scene jdm3_13 with dissolve
    "We took the bullet out"
    b "I can't feel my penis!! What happened?!"
    "Hahaha, don't worry it's still there, fully functional"
    "Once the anesthetic effect will go, it will be back to normal"
    "Look, why don't you just relax, we will take you out in few minutes"
    scene jdm3_15 with fade
    "Time to take you to your room"
    scene jdm3_16 with fade
    "Here we go"
    m "Oh God"
    "He's going to be ok"
    "2 days and he goes home"
    scene black
    play sound "sounds/backhome.mp3"
    "FEW DAYS LATER"
    scene jdm3_17 with fade
    stop sound fadeout 3.0
    s lau "Hey You!"
    m "..."
    scene jdm3_18 with dissolve
    b "Wow"
    scene jdm3_19 with dissolve
    b "Thanks"
    s "That GO was meant as asking you to leave"
    b "Of course, I know"
    e "No hug for me sweetie?"
    m "Elaine, he can't hug anyone now"
    m "Let's go change [bname]"
    scene jdm3_20 with fade
    m "Easy"
    b "But I don't want to change!"
    m "You have to put something loose, as the doctor said"
    b "But I don't mind it"
    b "I'm fine like this"
    scene jdm3_21 with dissolve
    m "Nonsense, I'll help you change"
    if persistent.patch_enabled:
        b "Wow mom, it seems you put on weight"
        pass
    else:
        b "Wow, seems you put on weight"
        pass
    scene jdm3_22 with dissolve
    m "And you mister, have lost a lot of weight"
    b "But seriously you've gained weight"
    m "I know"
    m "Once you get better, we'll go to the gym and you're gonna rock me"
    b "{i}(You bet I will){/i}"
    scene jdm3_23 with dissolve
    m "Don't be late"
    m "[sname] ordered your favourite food from doordawdle"
    b "Ok"
    b "By the way, who's this guy in there?"
    m "That's, Joshua, the son of Wanda"
    b "Oh, alright"
    scene jdm3_24 with fade
    m "Hi honey, your pizza is there"
    m "And Elaine prepared some shuba salad for you"
    e "Yeah, that's very healthy, it's good for you"
    b "Ok thanks"
    b "I'll sit on the kitchen counter"
    scene jdm3_25 with dissolve
    b "Bleergh"
    b "What is that shit?"
    scene jdm3_26 with dissolve
    b "Fuck!"
    e "Hahaha it's herrings, that's my favorite"
    m "Eat the pizza honey, just leave the salad"
    scene jdm3_27 with dissolve
    b "It's fine, I'm already full"
    e "Come have some wine"
    m ang "No! Just come and sit with us"
    b "{i}(Maybe I can get close to this guy, his mom is so hot){/i}"
    scene jdm3_28 with dissolve
    b "Hey, do you want to play some computer game with me?"
    scene jdm3_29 with dissolve
    j "Mom, can I go with him?"
    w "..."
    scene jdm3_30 with dissolve
    w "Sure honey, go"
    scene jdm3_31 with dissolve
    w "And behave! [bname] is still in pain"
    j "Sure mom"
    scene jdm3_32 with dissolve
    j "What's the name?"
    b "Thunder gate"
    j "You're lucky, you can play these things"
    j "My mom says no violence allowed"
    j "You're mom is cool, I wish my mom was like that"
    j "Besides she's never in the mood"
    j "Although they both work in the same restaurant but your mom doesn't seem to complain about standing on her feet the whole day"
    b "Yeah"
    scene jdm3_33 with dissolve
    b "Wait what?"
    b "Which restaurant?"
    j "Where they met, mom told me they work together in the restaurant"
    j "My mom is the manager there"
    scene jdm3_34 with dissolve
    b "Ah right, I got confused"
    scene jdm3_32 with dissolve
    b "{i}(His mom is one tough bitch){/i}"
    b "{i}(And she does porn! Hehehe){/i}"
    b "{i}(But probably his internet is rigged by her){/i}"
    b "{i}(So he will never know){/i}"
    b "{i}(But that doesn't make sense! What if I showed him her porn now?){/i}"
    j "What are you thinking about?"
    b "Ehh"
    b "Thinking which game to play next"
    b "What kind of games do you like to try?"
    j "Well, I think we better go back to the hall"
    b "Ok maybe next time you visit me and we play"
    j "Yeah I hope so, but I wouldn't promise you"
    j "My mom won't let me come by myself"
    b "Then bring her along"
    j "Yes, maybe that's a good idea"
    b "Don't worry, I'll also ask mom to invite her more often"
    j "Cool"
    scene jdm3_35 with fade
    w "How was it?"
    j "We played a game"
    b "{i}(Poor guy, he's getting his ass beaten){/i}"
    if persistent.patch_enabled:
        b "Mom your eyes look tired"
        pass
    else:
        b "[mname] your eyes look tired"
        pass
    scene jdm3_36 with dissolve
    m "No, I'm perfectly fine dear"
    scene black
    "LATER THAT NIGHT"
    scene jdm3_37 with fade
    b "I can walk alone"
    m "Yes but you can't bath"
    b "I can"
    m "Haven't you heard the doctor?"
    m "You can't let the scar get wet"
    m "Now stand up here while I give you a rub"
    b "I can do this myself"
    m "No! I owe you this, you saved my life"
    scene jdm3_38 with dissolve
    b "You didn't put any water"
    m "I did, just enough water on the brush"
    m "Turn"
    scene jdm3_39 with dissolve
    m "You need to shave [bname]"
    m "But don't do it today"
    b "That's not a problem"
    b "But what's bothering me is that I feel numb down there"
    b "And it kinda shrank"
    scene jdm3_40 with dissolve
    m "Oh thanks god for that"
    b "It's not funny"
    scene jdm3_41 with dissolve
    m "Come on, It's the anesthetia effect"
    m "And the operation itself, affects your body and muscles"
    b "After 3 days?"
    m "Keep checking it, if it stays like that for 2 more days, we will go to the doctor"
    b "Ok"
    scene jdm3_42 with fade
    b "I swear I'm not disabled"
    m "Maybe in some areas you are"
    b "Cut it out please"
    m "You get dressed up, I'll use the toilet"
    scene jdm3_43 with dissolve
    b "What's with this wanda?"
    b "She's too tough on her kid"
    m "Really [bname]?! You want to have small talk with me now?"
    m "While I'm on the john!?"
    b "It's fine, I don't mind it?"
    scene jdm3_44 with dissolve
    m "Yes but I do, I'm self conscious"
    b "And you know what he told me?"
    b "She said she works in a restaurant"
    b "And that's where you two met"
    scene jdm3_45 with dissolve
    m "[bname] we don't discuss the private life of people"
    m "With anyone, including among us"
    b "No, I didn't say anything"
    b "But how is she going to hide it if he sees her movies online"
    m "She's not what you think she is"
    m "Just, please, let me finish what I'm doing"
    m "And I'll tell you her story"
    b "Ok"
    m "Wait outside"
    scene jdm3_46 with fade
    b "{i}(Huh! She says we don't discuss private life and now she wants to tell me about Wanda){/i}"
    scene jdm3_47 with dissolve
    m "Sorry I had to take a quick shower"
    m "Good night sweetie"
    b "Wait, you promised to tell me about Wanda"
    scene jdm3_48 with dissolve
    m "Wanda doesn't star in porn movies"
    m "It was a personal thing, not for publication"
    b "And... Why?"
    m "She comes from a wealthy conservative and religious family"
    m "But she married the wrong guy"
    m "For her, marriage is for life"
    b "Ok... so? What has that got to do with the movie?"
    m "It was her husband request"
    m "He's very rich and has some sort of fetish"
    m "And it happens he knows the owner of the studio"
    b "{i}(Melinda! That's interesting){/i}"
    scene jdm3_49 with dissolve
    m "You see, her and me have an almost identical life"
    m "Except me, I didn't raise you well"
    m "And you became a pervert"
    b "Come on, I am not"
    b "I'm just a man with hormones"
    m "For that, there are plenty of women out there"
    b "What do you mean?"
    m "Good night"
    #NO T MORE VARIETY HERE? 
    $ dayname = (_("Monday"))
    $ day = 0
    $ wk = 0
    jump newday


    



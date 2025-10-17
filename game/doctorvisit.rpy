

label doctorvisit:
    scene docvisit0 with fade
    $ persistent.unlock_29 = True
    m "Grab a cab please"
    scene docvisit with fade
    "Everything looks good"
    scene docvisit1 with dissolve
    "He can remove the bandage"
    scene docvisit2 with dissolve
    "But [bname] if there's still drainage"
    "You can can keep a sticker bandage on it"
    scene docvisit with dissolve
    b "Ok cool"
    $ bandageremove = 1
    scene docvisit3 with fade
    m "Happy now?"
    m "You can take it off"
    b "Nah, it's still draining sometimes, but let's see"
    "NOW YOU WILL SEE HIM WITHOUT THE BANDAGE IN NEW SCENES"
    call screen gnav
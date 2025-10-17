

label map_menu:
    if Hour >=9 and Hour <18:
        scene cityd with fade
        b "{i}(Nah, I can't go out){/i}"
        call screen gnav

    elif Hour >=18 and wk <2:
        scene cityn with fade
        b "{i}(Nah, I can't go out){/i}"
        call screen gnav

    elif Hour >=18 and wk >=2:
        scene cityn with fade
        b "{i}(Maybe I can try to go out and visit [mname]'s work){/i}"
        call screen citynight




screen citynight():
    imagemap:
        ground "cityn.jpg"
        hover "cityn.jpg"
        idle "cityn.jpg"
        hotspot (454, 110, 228, 217) action Jump("bvisitm")

        textbutton "RETURN" action Jump("broom_menu") xalign 0.30 yalign 0.90


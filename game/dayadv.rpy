


label dayadv:
    menu:
        "Advance 1 Hour":
            $ Hour +=1
            "TIME ADVANCED BY ONE HOUR"
            if Hour >=21:
                $ Hour =21
                jump broom_menu
            else:
                "..."
                call screen gnav
            
        "Advance 2 Hours":
            $ Hour +=2
            "TIME ADVANCED BY TWO HOURS"
            if Hour >=21:
                $ Hour =21
                jump broom_menu
            else:
                "..."
                call screen gnav

            
            
        "Advance 3 Hours":
            $ Hour +=3
            "TIME ADVANCED BY THREE HOURS"
            if Hour >=21:
                $ Hour =21
                jump broom_menu
            else:
                call screen gnav

            
        "Advance 4 Hours":
            $ Hour +=4
            "TIME ADVANCED BY FOUR HOURS"
            if Hour >=21:
                $ Hour =21
                jump broom_menu
            else:
                jump broom_menu

            
        "Advance till the end of day":
            $ Hour =21
            jump newday
            
        "Return":
            call screen gnav
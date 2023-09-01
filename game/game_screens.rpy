screen select_level():
    hbox:
        xalign 0.5
        ypos 10
        spacing 30

        button:
            xysize (600, 960)
            background Solid("#5decff")

            text "Beginner" size 40 xalign 0.5 yalign 0.5:
                idle_color "#000000"
                hover_color "#757575"

            action Return("beginner")

        button:
            xysize (600, 960)
            background Solid("#f4ff5d")

            text "Professional" size 40 xalign 0.5 yalign 0.5:
                idle_color "#000000"
                hover_color "#757575"

            action Return("professional")

        button:
            xysize (600, 960)
            background Solid("#ff3df5")

            text "Expert" size 40 xalign 0.5 yalign 0.5:
                idle_color "#000000"
                hover_color "#757575"

            action Return("expert")

    text "Please select a level of expertise." xalign 0.5 yalign 0.95

screen work_screen():
    if phone_ringing or anything_in_inbox:
        frame:
            xysize (800, 50)
            xalign 0.5

            if phone_ringing:
                text "Your Phone is ringing." xalign 0.5 yalign 0.5

            elif anything_in_inbox:
                text "You have new email in your inbox." xalign 0.5 yalign 0.5
    frame:
        xysize (1920, 230)
        yalign 1.0

        grid 2 3:
            xpos 40
            yalign 0.5

            xspacing 40

            textbutton _("Examine inbox") text_size 40 action Return("examine")
            textbutton _("Answer the Phone") text_size 40 action Return("phone")
            textbutton _("Work") text_size 40 action Return("work")
            textbutton _("Phone Apps") text_size 40 action Return("phone")
            textbutton _("Settings") text_size 40 action ShowMenu("preferences")
            textbutton _("Leave Office") text_size 40 action Return("leave")

        add clock:
            xalign 0.95
            yalign 0.5

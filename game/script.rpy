label start:

    "Welcome to AI Saga."
    $ first_name = renpy.input("Please enter your first name:", default="Eleanor", allow="abcdefghijklmnopqrstuvwxyzABCSEFGHIJKLMNOPQRSTUVWXYZ")
    $ last_name = renpy.input("Please enter your last name:", default="Watson", allow="abcdefghijklmnopqrstuvwxyzABCSEFGHIJKLMNOPQRSTUVWXYZ")
    $ nick_name = renpy.input("Please enter your nick name:", default="Nell", allow="abcdefghijklmnopqrstuvwxyzABCSEFGHIJKLMNOPQRSTUVWXYZ")

    menu:
        "Male":
            $ gender = "male"

        "Female":
            $ gender = "female"

    call screen select_level
    $ difficulty = _return

    "Welcome to AI Saga Office [first_name]. You will be working your day to day work here."

label work_desk:
    scene desk
    call screen work_screen

    if _return == "examine":
        jump examining_the_box

    elif _return == "phone":
        jump answer_the_phone

    elif _return == "work":
        jump start_working

    elif _return == "phone":
        jump check_phone

    elif _return == "leave":
        jump take_a_break

label day_ends:
    "Your day has come to an end."

    $ event_list = ["event_a", "event_b", "event_c", "event_d", "event_e", "event_f", "event_g"]
    $ event_seen_today = []

    $ anything_in_inbox = False
    $ phone_ringing = False

    "New day has begun."
    $ clock.set_time(9, 0)

    jump work_desk

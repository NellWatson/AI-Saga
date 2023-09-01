label examining_the_box:
    if anything_in_inbox:
        "There was something in the inbox. You checked it out."

        $ anything_in_inbox = False
        $ clock.add_time(h=1, m=0)

    else:
        "There is nothing new in your inbox."
        $ clock.add_time(h=0, m=30)

    $ _value = renpy.random.randint(0, 100)
    if _value < chance_for_event and event_list:
        $ chosen_event = renpy.random.sample(event_list, k=1)
        $ event_seen_today.append(chosen_event[0])
        $ event_list.remove(chosen_event[0])

        jump expression chosen_event[0]

    else:
        jump work_desk

label answer_the_phone:
    if phone_ringing:
        "You answer the phone."

        $ phone_ringing = False
        $ clock.add_time(h=0, m=30)

    else:
        "Your phone is not ringing."

        $ clock.add_time(h=0, m=10)

    $ _value = renpy.random.randint(0, 100)
    if _value < chance_for_event and event_list:
        $ chosen_event = renpy.random.sample(event_list, k=1)
        $ event_seen_today.append(chosen_event[0])
        $ event_list.remove(chosen_event[0])

        jump expression chosen_event[0]

    else:
        jump work_desk

label start_working:
    "You tidy up some files and work for a bit."
    $ clock.add_time(h=2, m=0)

    $ _value = renpy.random.randint(0, 100)
    if _value < chance_for_event and event_list:
        $ chosen_event = renpy.random.sample(event_list, k=1)
        $ event_seen_today.append(chosen_event[0])
        $ event_list.remove(chosen_event[0])

        jump expression chosen_event[0]

    else:
        jump work_desk

label check_phone:
    "You check your social media apps."
    $ clock.add_time(h=0, m=30)

    $ _value = renpy.random.randint(0, 100)
    if _value < chance_for_event and event_list:
        $ chosen_event = renpy.random.sample(event_list, k=1)
        $ event_seen_today.append(chosen_event[0])
        $ event_list.remove(chosen_event[0])

        jump expression chosen_event[0]

    else:
        jump work_desk

label take_a_break:
    "You took a break."

    $ clock.add_time(h=1, m=30)
    "You get back to office."

    jump work_desk

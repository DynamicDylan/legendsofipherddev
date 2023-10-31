init python:
    gallery = Gallery()

    gallery.button("CG_SettlersJournal1")
    gallery.unlock_image("CG_SettlersJournal1")

    gallery.button("CG_SettlersJournal2")
    gallery.unlock_image("CG_SettlersJournal2")

    gallery.button("CG_SettlersJournal3")
    gallery.unlock_image("CG_SettlersJournal3")

    gallery.button("CG_SettlersJournal4")
    gallery.unlock_image("CG_SettlersJournal4")




screen Album:
    tag menu
    hbox:
        xalign 0.5
        yalign 0.5
        spacing 30

        grid 2 2:
            add gallery.make_button(name="CG_SettlersJournal1",unlocked="CGs/album/SettlersJournal1.png",locked="CGs/album/lock.png")
            add gallery.make_button(name="CG_SettlersJournal2",unlocked="CGs/album/SettlersJournal2.png",locked="CGs/album/lock.png")
            add gallery.make_button(name="CG_SettlersJournal3",unlocked="CGs/album/SettlersJournal3.png",locked="CGs/album/lock.png")
            add gallery.make_button(name="CG_SettlersJournal4",unlocked="CGs/album/SettlersJournal4.png",locked="CGs/album/lock.png")
        textbutton "Return" action Return()
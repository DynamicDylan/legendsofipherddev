
label start:
 
    python:
        domname = renpy.input("What is your name?")
        domname = domname.strip()

        if not domname:
             domname = "Domenic"

voice "audio/voice/narrator/start_cc24ba58.mp3"
n "Excellent you have chosen to be [domname]"

voice "audio/voice/narrator/start_61caf43e.mp3"
n "That is a wonderful name"

n "You will enter the Legends of Ipherd"

n "Will you be a Hero or Villian of GREAT porportions?"

n "I don't know but you'll have to make a choice"

n "Good luck [domname] may your adventure be fruitful and welcome to the Legends of Ipherd"

menu:
    "Make the choice"
    "Bad Guy":
        if  domname in "Domenic Ó Maolagáin":
            jump DomBad
        else:
            jump Villian
    "Good Guy":
        if domname in "Domenic Ó Maolagáin":
            jump DomGood
        else:
            jump Hero
label DomBad:
n "All stories have a beginning. This is how the tale all began."

n "Back in 1869 when Ipherd was first settled the settlers brought their beliefs"

n "For those who don't know belief has power."

n "This power was orignally kind and good, but some power can turn rotten"

n "I shall now show you a page from a Settler's Journal circa 1869."

scene CG_SettlersJournal1 with fade

pause

n "These pages will be the key to your story whichs begins now!"

scene CG_Ipherd5YearsAgo with fade

"It was my 18th Birthday when it all began."
"I was  enjoying it like any other person my age."
"Which means I was dreading paying taxes and the possibility of being drafted should there ever be war."
"The gifts I recieved were nothing strange, except one that is."
"It was a gift from my grandfather Atticus."
"My grandfather was a little odd sure, because he collected old and unusual things."
"It was a book bound in a finely dyed leather. The color of the book a shade of red while the pages looked like aged parchment."
"I opened it to the first page and read the text there. It talked of an old country and Gods."
"I scoffed at the idea that gods could do anything, but I turned to my Grandfather and said"

dom "Thank you for the thoughtful gift Grandpa Atticus."

show atticus with fade
ti "Your welcome [domname]. This book has been passed from Ó Maolagáin to Ó Maolagáin since the town's founding."

ti "Tradition states it is passed on to the next Son on their 18th Birthday."

ti "It is a shame your father isn't here to pass it on to you, but he died doing his duty."

ti "So I have held on to this since he left. Hopefully you will find this book useful."

ti "There is one warning I must give however."

ti "Do not go hunting for legends even if it seems fun."
hide atticus with dissolve

"That was the last time I seen my Grandfather alive. Two weeks later he was found dead in his home."
"The autopsy said it was a large quantity of poison that did him in. The warning and mysterious death,"
"It sparked my curiosity, but it would have to wait until I returned from college for me to truly explore the information inside the book"
return

#Label Villian w/Custom Name here

label Villian:
n "All stories have a beginning. This is how the tale all began."

n "Back in 1869 when Ipherd was first settled the settlers brought their beliefs"

n "For those who don't know belief has power."

n "This power was orignally kind and good, but some power can turn rotten"

n "I shall now show you a page from a Settler's Journal circa 1869."

scene CG_SettlersJournal1 with fade

pause

n "These pages will be the key to your story whichs begins now!"

scene CG_Ipherd5YearsAgo with fade

"It was my 18th Birthday when it all began."
"I was  enjoying it like any other person my age."
"Which means I was dreading paying taxes and the possibility of being drafted should there ever be war."
"The gifts I recieved were nothing strange, except one that is."
"It was a gift from my grandfather Atticus."
"My grandfather was a little odd sure, because he collected old and unusual things."
"It was a book bound in a finely dyed leather. The color of the book a shade of red while the pages looked like aged parchment."
"I opened it to the first page and read the text there. It talked of an old country and Gods."
"I scoffed at the idea that gods could do anything, but I turned to my Grandfather and said"

dom "Thank you for the thoughtful gift Grandpa Atticus."

show atticus with fade
ti "Your welcome [domname]. This book has been passed down our family since the town's founding."

ti "Tradition states it is passed on to the next Son on their 18th Birthday."

ti "It is a shame your father isn't here to pass it on to you, but he died doing his duty."

ti "So I have held on to this since he left. Hopefully you will find this book useful."

ti "There is one warning I must give however."

ti "Do not go hunting for legends even if it seems fun."
hide atticus with dissolve

"That was the last time I seen my Grandfather alive. Two weeks later he was found dead in his home."
"The autopsy said it was a large quantity of poison that did him in. The warning and mysterious death,"
"It sparked my curiosity, but it would have to wait until I returned from college for me to truly explore the information inside the book"
n "It is now time to select your Major you shall now have four choices to choose from"
menu:
    "Choose a Major"
    "English":
        jump englishe
    "Math":
        jump mathe
    "Communications":
        jump communicationse
    "History":
        jump historye


label englishe:
n "So this is the choice huh?"
scene CG_english with fade
return
label mathe:
n "Math Really?"
scene CG_math with fade
return
label communicationse:
n "Finding a Job might be hard"
scene CG_comm with fade
return
label historye:
n "This will be useful"
scene CG_history with fade

return

#Label Hero route Domenic

label DomGood:
n "All stories have a beginning. This is how the tale all began."

n "Back in 1869 when Ipherd was first settled the settlers brought their beliefs"

n "For those who don't know belief has power."

n "This power was orignally kind and good, but some power can turn rotten"

n "I shall now show you a page from a Settler's Journal circa 1869."

scene CG_SettlersJournal1 with fade

pause

n "These pages will be the key to your story whichs begins now!"

scene CG_Ipherd5YearsAgo with fade

"It was my 18th Birthday when it all began."
"I was  enjoying it like any other person my age."
"Which means I was dreading paying taxes and the possibility of being drafted should there ever be war."
"The gifts I recieved were nothing strange, except one that is."
"It was a gift from my grandfather Atticus."
"My grandfather was a little odd sure, because he collected old and unusual things."
"It was a book bound in a finely dyed leather. The color of the book a shade of red while the pages looked like aged parchment."
"I opened it to the first page and read the text there. It talked of an old country and Gods."
"I scoffed at the idea that gods could do anything, but I turned to my Grandfather and said"

dom "Thank you for the thoughtful gift Grandpa Atticus."

show atticus with fade
ti "Your welcome [domname]. This book has been passed from Ó Maolagáin to Ó Maolagáin since the town's founding."

ti "Tradition states it is passed on to the next Son on their 18th Birthday."

ti "It is a shame your father isn't here to pass it on to you, but he died doing his duty."

ti "So I have held on to this since he left. Hopefully you will find this book useful."

ti "There is one warning I must give however."

ti "Do not go hunting for legends even if it seems fun."
hide atticus with dissolve

"That was the last time I seen my Grandfather alive. Two weeks later he was found dead in his home."
"The autopsy said it was a large quantity of poison that did him in. The warning and mysterious death,"
"It sparked my curiosity, but it would have to wait until I returned from college for me to truly explore the information inside the book"
return

#Label Hero Route Custom

label Hero:

n "All stories have a beginning. This is how the tale all began."

n "Back in 1869 when Ipherd was first settled the settlers brought their beliefs"

n "For those who don't know belief has power."

n "This power was orignally kind and good, but some power can turn rotten"

n "I shall now show you a page from a Settler's Journal circa 1869."

scene CG_SettlersJournal1 with fade

pause

n "These pages will be the key to your story whichs begins now!"

scene CG_Ipherd5YearsAgo with fade

"It was my 18th Birthday when it all began."
"I was  enjoying it like any other person my age."
"Which means I was dreading paying taxes and the possibility of being drafted should there ever be war."
"The gifts I recieved were nothing strange, except one that is."
"It was a gift from my grandfather Atticus."
"My grandfather was a little odd sure, because he collected old and unusual things."
"It was a book bound in a finely dyed leather. The color of the book a shade of red while the pages looked like aged parchment."
"I opened it to the first page and read the text there. It talked of an old country and Gods."
"I scoffed at the idea that gods could do anything, but I turned to my Grandfather and said"

dom "Thank you for the thoughtful gift Grandpa Atticus."

show atticus with fade
ti "Your welcome [domname]. This book has been passed down our family since the town's founding."

ti "Tradition states it is passed on to the next Son on their 18th Birthday."

ti "It is a shame your father isn't here to pass it on to you, but he died doing his duty."

ti "So I have held on to this since he left. Hopefully you will find this book useful."

ti "There is one warning I must give however."

ti "Do not go hunting for legends even if it seems fun."
hide atticus with dissolve

"That was the last time I seen my Grandfather alive. Two weeks later he was found dead in his home."
"The autopsy said it was a large quantity of poison that did him in. The warning and mysterious death,"
"It sparked my curiosity, but it would have to wait until I returned from college for me to truly explore the information inside the book"

n "It is now time to select your Major you shall now have four choices to choose from"
menu:
    "Choose a Major"
    "English":
        jump english
    "Math":
        jump math
    "Communications":
        jump communications
    "History":
        jump history

label english:
n "So this is the choice huh?"
scene CG_english with fade
return
label math:
n "Math Really?"
scene CG_math with fade
return
label communications:
n "Finding a Job might be hard"
scene CG_comm with fade
return
label history:
n "This will be useful"
scene CG_history with fade
n "Nothing Here yet"
return

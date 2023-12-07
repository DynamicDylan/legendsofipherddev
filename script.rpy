define dom = Character(_("[domname]"), color="#FF0000")
define ti = Character (_("Atticus"), color="#FFD700")
define n = Character(_("Narrator"), color="#87CEEB")
define f = Character(_("Felix"), color="#39993A")
define m = Character(_("Melinda"), color="#734f96")
define h = Character(_("Hans"), color="#FFFFFF")
label start:
 
    python:
        domname = renpy.input("What is your name?")
        domname = domname.strip()

        if not domname:
             domname = "Domenic"

n "Excellent you have chosen to be [domname]"


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
scene CG_dorm with fade

"I set off to college and started to unpack things into my Dorm room"
"There wasn't much for me to unpack considering I would only be here for four or so months before the semester ends"
scene CG_campus with fade
"I journeyed outside to to the rest of campus and stumbled upon my first interaction with an interesting person"
show hans with fade
h "Hello there."
h "Its nice to meet you I am Hans what is your name?"
dom "My name is [domname] its nice to meet you Hans"
"Hans walked away" 
hide hans with dissolve
"I didn't see him again that day"
"I returned to the dorm room after exploring campus"
scene CG_dorm_hall with fade
"By the time I finally returned to the dorm room I had met a most curious person in the hallway."
show felix with fade
f "What's up dude? I'm your next door neighbor Felix its nice to meet you"
dom "Well its nice to meet you too Felix, I am [domname]. It looks like I will be rooming next to you for the next four months"
f "Four months? Well, thats only if you or I move out my guy. I hope we will be rooming next to each other for the next four years."
"Internally I scoffed at that I hope to graduate early and investigate into the book Grandfather Atticus had given me."
dom "Well, we'll see won't we"
"I said as I made a hasty escape into my room seeing as I had been inching towards the door as I talked."
hide felix with dissolve
scene CG_dorm_night with fade
"It was finally night so it was time to hit the hay and prepare for classes the next day."
play movie "audio/sfx/ipherdburns.webm"
play sound "audio/sfx/burn.mp3"

"What a strange dream I will think on it in the morning."

scene CG_dorm with fade

"I awoke bright and early and I had forgotten the dream little did I know that dream was a bad omen of things to come"
menu:
    "Choose where to go today"
    "Outside":
        jump outside
    "Class":
        jump Class
    "Library":
        jump librari
    "Archives":
        jump Archives

label outside:
scene CG_campus
show hans with fade
"Today I went outside and skipped class it was liberating although skipping class was likely bad for my grade"
"While I wandered around campus I met that strange man named Hans again"
h "Hello again [domname]. How are you today?"
dom "I am fine and how are you Hans?"
h"I'm doing great why aren't you in class?"
dom "Classes were canceled for me today. Might I ask the same of you?"
h"I'm a graduate student doing special a special history Project for one of my Professors"
h"So I have permission to go to the archives and look for imformation"
h "I have gotten into old towns and their history I'm currently researching a small place called Ipherd have you heard of it?"
h"If not the town was founded back in the 1800s by some French Dutch settlers who had strange beliefs"
h "Its one of the oldests towns in the state if you can believe that"
"I let hans continue to talk learning a surprising amount about my small town from what seemed like an impassioned person. This got me thinking about the book I had in my possession perhaps I should look into it more"
dom "That's very interesting Hans perhaps we should talk about it sometime as I am from Ipherd born and raised."
"We shook hands agreeing at a later date and I wandered off in search of one of the campus dining facilities"
hide hans with dissolve
scene CG_dfac
play sound "audio/sfx/diningnoise.mp3"

"I entered the dining hall no one familar in sight. I sighed a breath of relief honestly the social interactions take too much out of me"
"I grabbed some Col Dylan's Chicken from the CDFC and sat down"
"Fried chicken is so bad for me but it tastes so good I won't lie."
"As I was eating some young woman came up to me. I silently raised an eyebrow there goes a peaceful lunch"
show melinda with fade
dom "Is there something I can help you with miss...?"
m "My name is Melinda, thanks for asking. I noticed you weren't in class today. The Professor had a bulletin board with pictures and names so we could identify each other"
"I silently decided then and there to probably drop that class after going to a few because man that was creepy."
dom "So what if I wasn't in class I was getting aqquainted with the campus. The fact we have classes the day after getting here is a major flaw in the system"
m "I didn't say it was a bad thing I just wanted to come up and talk to you about what you missed."
dom "Also the fact you recognized me means you must have stared at my picture for a while"
"She didn't know what to say looking slightly off to one side. I continued to eat my lunch while pointedly staring directly at her."
m "Th-That doesn't matter what matters is what you missed. Here is a copy of the syllabus I picked up for you"
dom "I am touched at your kind heartedness. Please feel free to have a seat and eat with me when you get your food."
"I made this offer hoping she would reject it. While she seemed kind ulterior motives are not unsual for classmates being 'friendly' sometimes."
m "That's quite kind of you I'll be right back."
hide melinda with dissolve
"Drat my plan backfired. Oh well, how bad could it be to get to know one of my classmates?"
"The answer was very as melinda was coming back I spotted a very familiar shock of blonde hair coming with her."
"Oh boy, I muttered under my breath. She had brought Felix with her. I could feel my social battery draining like an Orange Product specifically their UPhone."
show melinda at right with fade 
show felix at left with fade 
"I cringed as that sat down knowing talking here would be exhausting"
dom "Well, hello again Felix and Melinda. I'm so glad you both could join me"
"This was an obvious lie said with a customer service smile"
m "I hope you don't mind I invited him we have been friends since Kindergarten and when I saw him in line I kind of just extended an invite"
dom "It's no problem. It's fine I know Felix because we live in the same dorm together."
f "Dom dude how are you? How was the first day you enjoying the campus life"
"I was not infact enjoying the campus life this lunch felt like it was going to take an eternity to get through."
dom "Yes, I found a quite plesant person while I was out exploring today and we discussed the history of Ipherd."
f "Ipherd? Never heard of it but did you hear..."
"Felix then proceeded to inform us of the people who were found with guns in the dorms last night. The only reason they were found out is because they had accidentally shot themselves"
"One would think that a prestigious university like Vall State would inform its students of potential threats. They really need to work on communication on this campus."
m "No, I hadn't heard of this but now that I know I think the Campus should work on its communication"
dom "That was exactly what I was thinking. Only learning about it a day or so later isn't bad but what if it had been a News outlet to inform the student body first rather than the University?"
f "Yeah, well the university does have bad communication have you ever checked your email settings. Their daily communications email is full of junk you don't care about."
f "Honestly unless you change the settings yourself you only get that type of garbage."
"Talking to these two turned out to be more informative than I thought I quickly ate the rest of my lunch and enjoyed the time I spent with them rather than quickly leaving."
dom "Do you want to learn about Ipherd?"
"I asked this as I was well versed in some of the towns history not as much as I wanted but Felix did seem curious"
f "Sure thing man."
m "It's a good way to get to know you."
"The way Melinda said that was a little weird but I shrugged it off and started telling them all I knew about the town."
stop sound
scene CG_dorm_night with fade

"After talking with Felix and Melinda today I feel as though I might really enjoy the university life"
"Though its time to go to bed"
scene burningipherd with fade
show book with fade 
play sound "audio/sfx/laughter.mp3"
pause(5.0)
hide book with dissolve
"It was another bright and sunny morning"
"Well, what to do today?"
return

label librari:
"Well, I had decided to go to class and after class had ended I meandered my way over to the library"
"The library was quite old I pulled out what I thought was one of my textbooks but instead I had pulled out the old journal"
"The following was on the page"
scene CG_SettlersJournal2 with fade

pause
return

label Archives:
n "Not Written"
return
label Class:
n "not written"
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
scene CG_history with fade
"I had chosen history as my major although the classes were boring to sit through."

"I met two people who would eventually help me in magnificent ways. Their names were Felix and Melinda."

"These two were my best friends during college. In fact, I remember the day I met them well."

"I had the choice to study alone or go to the library."

menu:
    "What should I do"
    "Study Alone":
        jump alone
    "Go to the Library":
        jump library

label alone:
return
label library:
return


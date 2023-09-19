
# region: helper functions
import re
import copy

def replace_tags(message: str, current_user: str, handles:set):
  tags: list = re.findall(r"@[\w._-]+(?<!.[._-]$)", message)
  for tag in tags:
    handles.add(tag[1:])
    message = message.replace(tag, f'<a href="#{tag[1:]}_profile_{current_user}" class="tag" rel="nofollow">{tag}</a>')
  # print(current_user, handles)
  return message

def create_message(user:str, handle:str, time:str, message:str, handles:set):
  html_lines.append(f"""
      <p class="post"><b><a href="#{handle}_profile_{user}" rel="nofollow">{handle}</a></b> {time}<br/>
        {replace_tags(message, user, handles)}
      </p>""")

def insert_header(link):
  html_lines.append(f"""
    <a name="{link}" id="{link}" rel="nofollow"></a>
    <div class="page">
      <h1 class="header">
        <a class="logo" href="#{link}" rel="nofollow">Penstagram<sub><sub>2.0</sub></sub></a>
      </h1>""")

def insert_navbar(user: str):
  html_lines.append(f"""
    </div>
    <div>
      <ul class="bar">
        <li><a href="#{user}" rel="nofollow">__home__</a></li>
        <li><a href="#{user}_foryou" rel="nofollow">__for you__</a></li>
        <li><a href="#{user}_notifications" rel="nofollow">__notifications__</a></li>
        <li><a href="#{user}_messages" rel="nofollow">__messages__</a></li>
      </ul>
    </div>""")

def create_profile(user, handle):
    display, location, date, bio, following, followers = profiles[handle]
    html_lines.append(f"""
    <a id="{handle}_profile_{user}" name="{handle}_profile_{user}"></a>
    <div class="page">
      <h1 class="header">
        <a class="logo" href="#{user}" rel="nofollow">Penstagram<sub><sub>2.0</sub></sub></a>
      </h1>
      <h4>
        {display}<br />@{handle}<br />{'<a href="#fake_button" class="edit_button" rel="nofollow">Edit profile</a>'
         if handle == users[user] else ""}
      </h4>
      <p class="bio">__pin__: {location} | __calendar__: {date}<br />
        {replace_tags(bio, user, profiles_to_create[user])}
        <br />
        <br />
        {following} Following | {followers} Followers
      </p>
    </div>
    <div>
      <ul class="bar">
        <li><a href="#{user}" rel="nofollow">__home__</a></li>
        <li><a href="#{user}_foryou" rel="nofollow">__for you__</a></li>
        <li><a href="#{user}_notifications" rel="nofollow">__notifications__</a></li>
        <li><a href="#{user}_messages" rel="nofollow">__messages__</a></li>
      </ul>
    </div>""")
# endregion: helper functions

# region: initialize html, create head, and start body
html_lines = ["""<html>

<head>
  <link rel="stylesheet" href="penstagram.css">
</head>

<body>
  <p class="disclaimer"><b>Note from the <i>Penstagram 2.0</i> Development Team: For the best user experience, 
  it is highly recommended that you turn on "Show Creator's Style".</b></p>
"""]

users = {
  "eda": "BADGIRLCOVEN",
  "darius": "goo-daddy",
  "raine": "rainey.day"
}
# endregion: initialize html, create head, and start body

# region: user select page
html_lines.append(f"""  <div class="main">
    <a name="login" id="login" rel="nofollow"></a>
    <div class="page">
      <h1 class="header">Penstagram<sub><sub>2.0</sub></sub></h1>
      <h3>SELECT PROFILE</h3>
      <ul>""")

for name in users:
  html_lines.append(f"""
        <li><a href="#{name}">{users[name]}</a></li>""")

html_lines.append("""
      </ul>
    </div>
    <div>
      <ul class="bar"></ul>
    </div>""")
# endregion: user select page

# region: feed data
feeds = {
  "eda": [
    ["BADGIRLCOVEN", "10:09 AM", "Third mug of appleblood downed. Time to rob some schmucks blind."],
    ["rainey.day", "10:11 AM", "Eda, you realize these are monitored, right?"],
    ["BADGIRLCOVEN", "10:12 A M", "don't care."],
    ["goodWitchLuzura", "11:26 AM", "amity ur so pretty"],
    ["goops", "12:03 PM", "Finally changed my display name so people know who I am."],
    ["goodWitchLuzura", "12:19 PM", "@em_ira @bestBlight which one of you stoll my scroll? - Amity"],
    ["em_ira", "12:20 PM", "We'll give it back if you promise not to tell Dad that we snuck out to meet Jerbo and Viney."],
    ["goodWitchLuzura", "12:20 PM", "I wouldn't do that, anyway. - Amity"],
    ["bestBlight", "12:21 PM", "hey mittens, catch lol"],
    ["WitchChick128", "12:22 PM", "Thank you."],
    ["veeeeeee", "12:25 PM", ":3"],
    ["MashPit", "12:25 PM", "Nearly got eaten a few minutes ago, but fought em off. RIP bozo, never stood a chance."],
    ["BADGIRLCOVEN", "12:26 PM", "y do i keep getting notis from all you kids."],
    ["BADGIRLCOVEN", "12:28 PM", "screw this time for apple blood #4."],
    ["HOOOOOOOOOT", "6:66 PM", "SOULS OF THE DAMNED ARE YUMMY HOOT HOOT"],
  ],
  "darius": [
    ["goo-daddy", "9:21 AM", "Never trust a man who says a dead body is talking to him and him alone.\
      Unless it's me. Always trust me."],
    ["rainey.day", "9:35 AM", "Just had a very relaxing tea with my breakfast. Time to start the day!"],
    ["RAISEDBYDIREWOLVES", "10:21 AM", "saw a cool rock :)"],
    ["RULERZREACHF4N", "11:07 AM", "h0w .aer yoi gyus sp good at tyipng"],
    ["Hello_willow", "11:07 AM", "You'll get better with time, Hunnybun."],
    ["RULERZREACHF4N", "11:09 AM", "thanks, Captain"],
    ["chilly.lily", "11:30 AM", "New ink review dropping tomorrow!"],
    ["rainey.day", "11:36 AM", "I want to try something."],
    ["rainey.day", "11:38 AM", "01001111 01001000 00100000 01010100 01001001 01010100 01000001 \
     01001110 00100000 01010100 01001000 01001001 01010011 00100000 01001001 01010011 00100000 \
     01000001 01010111 01000110 01010101 01001100"],
  ],
  "raine": [
    ["rainey.day", "2:07 AM", "Just did a line of rosin powder. Let's get this money, bards."],
  ]
}
# endregion: feed data

# region: for you data
for_you = {
  "eda": [
    ["goodWitchLuzura", "7:53 AM", "sometimes you need to let out some stress by stomping a colonizer's face in."]
  ],
  "darius": [
    ["chilly.lily", "9:00 AM", "Join myself and @HOOOOOOOOOT today at noon as we unveil the newest wing of the\
     @SNMH - Balusters Through The Ages: From Deadwardian Until Present Day."]
  ],
  "raine": [
    ["BADGIRLCOVEN", "6:39 PM", "need me some bard booty."]
  ]
}
# endregion: for you data

# region: trending data
trending = {
  "eda": [
    ["bestBlight", "3:09 AM", "NEW VID OUT NOW! TOP 10 WAYS TO SNEAK OUT OF THE CONFORMATORIUM: \
     <a title='mew.tube/dQw4w9WgXcQ' href='https://www.youtube.com/watch?v=dQw4w9WgXcQ'>mew.tube/dQw4w9WgXcQ</a>"],
  ],
  "darius": [
    ["", "", ""]
  ],
  "raine": [
    ["", "", ""]
  ],
}
# endregion: trending data

# region: news data
news = {
  "eda": [
    ["", "", ""]
  ],
  "darius": [
    ["", "", ""]
  ],
  "raine": [
    ["", "", ""]
  ],
}
# endregion: news data

# region: sports data
sports = {
  "eda": [
    ["", "", ""]
  ],
  "darius": [
    ["", "", ""]
  ],
  "raine": [
    ["", "", ""]
  ],
}
# endregion: sports data

# region: notifications data
notifications = {
  "eda": [],
  "darius": [],
  "raine": [],
}
# endregion: notifications data

# region: messages data
messages = {
  "eda": [],
  "darius": [],
  "raine": [],
}
# endregion: messages data

profiles_to_create = dict()

profiles = {
  "BADGIRLCOVEN": ["Owl Lady", "Owl Shack", "Scab. 2017", "Formerly wanted criminal, now Headmaster at @UWM", "12", "31.4k"],
  "goo-daddy": ["Darius D.", "noyb", "Jaw. 2017", "Abominations > People", "35", "20.6k"],
  "rainey.day": ["Raine Whispers", "The Owl House", "Fea. 2020", "Hello!", "1", "16.3k"],
  "goodWitchLuzura": ["<i>Luz</i>", "Flip-flopping CT and the BI", "Jaw. 2021", 
  "Sweet Potato of @WitchChick128<br/> @veeeeeee's sister.<br/>the reports of my death were minorly exaggerated", "73", "98k"],
  "goops": ["Gus Porter", "UWM Branch 19", "Sep. 2017", "Founder of the DR-HR Exchange Program", "306", "1.5k"],
  "em_ira": ["The Older Blight Twin", "Your Mom's Bedroom", "Parch 2016", 
             "<i>Waiting for mom to kick the bucket so I can let her down one last time.</i>", "305", "4.8k"],
  "bestBlight": ["Ed", "Rent-free in your head", "Parch 2016", "Doing stupid things so you don't have to. \
                 SUBCRIBE TO MY MEWTUBE OR ELSE.", "478", "11.3k"],
  "WitchChick128": ["Mittens", "Bonesborough", "Ath. 2017", "Sweet potato of @goodWitchLuzura \
                 Younger sibling of @em_ira and @bestBlight.", "289", "19k"],
  "veeeeeee": ["Vee Noceda (she/her)", "La Casa Noceda", "Dis. 2021", "Sometimes a snake, sometimes a human, \
               always adorable.<br/>Sister of @goodWitchLuzura", "51", "6.2k"],
  "MashPit": ["Masha (they/them)", "Gravesfield, CT", "Dis. 2021", "Ich weiss nicht, etwas auf Deutsch.<br/>\
              Partner of @veeeeeee Noceda", "9", "428"],
  "HOOOOOOOOOT": ["hootsifer", "Papa Titan's Eye Socket", "The Dawn of Time", "there is no beginning. there is no end. \
                  there is only hoot.", "-1", "Infinite"],
  "chilly.lily": ["Lilith Clawthorne", "Clavicus, Left Arm", "Scab. 2018", "Lead Historian at @SNMH \
                  | Occasional ink connoisseur", "51", "21.7k"],
  "SNMH": ["The Supernatural Museum of History", "200 W. Bronchial Rd.", "Saw. 2021", "Where history comes to life! \
           Lead historian: @chilly.lily", "10", "13k"],
  "RAISEDBYDIREWOLVES": ["Eberwolf the Huntsman", "Yes", "Dis. 2019", ">:3", "2", "29"],
  "RULERZREACHF4N": ["Hunter Park-Deamonne-Noceda-Clawthorne-Whispers", "carving palismen", "Awk. 2021",
                     "R.I.P Flapjack - Thank you for finding me.", "5", "4.6K"],
  "Hello_willow": ["Willow Park", "Bonseborough, The Chest", "Scab. 2019", "Captain of the @EmeraldEntrails \
                   Hexside Class of '22.", "17", "29.4k"],
  "UWM": ["<i>The</i> University of Wild Magic", "The Tree", "Fea. 2022", "Official account of the University \
          of Wild Magic, the only college worth a hoot. Home of the Owls.", "62", "31k"],
  "EmeraldEntrails": ["The Sea of Green", "The Pitch", "Gna. 2021", "The OFFICIAL account for the Emerald \
                      Entrails Flyer Derby Team. Captained by @Hello_willow", "5", "20k"],
}

for user in users:
# region: generating html for feeds
  html_lines.append(f"\n\n\t\t<!-- FEED FOR {user.upper()} -->\n")
  profiles_to_create[user] = set()
  insert_header(user)
  html_lines.append("""
      <p>
        <a href="#login" class="switch_profile" rel="nofollow">SWITCH PROFILE</a>
      </p>""")

  feed: list[list[str]] = feeds[user]
  for handle, time, message in feed:
    profiles_to_create[user].add(handle)
    html_lines.append(f"""
      <p class="post"><b><a href="#{handle}_profile_{user}" rel="nofollow">{handle}</a></b> {time}<br/>
        {replace_tags(message, user, profiles_to_create[user])}
      </p>""")

  insert_navbar(user)
  
  html_lines.append(f"\n\n\t\t<!-- END FEED FOR {user.upper()} -->\n")
# endregion: generating html for feeds

  sections: list[list[str, object]] = [["For You", for_you], ["Trending", trending], ["News", news], ["Sports", sports]]
  for section, data in sections:
    html_lines.append(f"\n\n\t\t<!-- {section.upper()} FOR {user.upper()} -->\n")
    link = f"{user}_{section.replace(' ', '')}"
    insert_header(link)
    html_lines.append(f"""      <div>
        <ul class="bar">
          <li><a href="#{user}_foryou">For You</a></li>
          <li><a href="#{user}_trending">Trending</a></li>
          <li><a href="#{user}_news">News</a></li>
          <li><a href="#{user}_sports">Sports</a></li>
        </ul>
      </div>""")
    for handle, time, message in data[user]:
      profiles_to_create[user].add(handle)
      create_message(user, handle, time, message, profiles_to_create[user])
    insert_navbar(user)
    html_lines.append(f"\n\n\t\t<!-- END {section.upper()} FOR {user.upper()} -->\n")
  
# region: generating html for notifications
  link = f"{user}_notifications"
  html_lines.append(f"\n\n\t\t<!-- NOTIFICATION FOR {user.upper()} -->\n")
  insert_header(link)
  for handle, time, message in notifications[user]:
    profiles_to_create[user].add(handle)
    create_message(user, handle, time, message, profiles_to_create[user])
  insert_navbar(user)
  html_lines.append(f"\n\n\t\t<!-- END NOTIFICATIONS FOR {user.upper()} -->\n")
# endregion: generating html for notifications
  
# region: generating html for messages
  link = f"{user}_messages"
  html_lines.append(f"\n\n\t\t<!-- MESSAGES FOR {user.upper()} -->\n")
  insert_header(link)
  for handle, time, message in messages[user]:
    profiles_to_create[user].add(handle)
    create_message(user, handle, time, message, profiles_to_create[user])
  insert_navbar(user)
  html_lines.append(f"\n\n\t\t<!-- END MESSAGES FOR {user.upper()} -->\n")
# endregion: generating html for messages

# region: generate profiles

for user in users:
  html_lines.append(f"\n\n\t\t<!-- USER PROFILES FOR {user.upper()} -->\n")
  current_profiles = copy.deepcopy(profiles_to_create)
  for handle in current_profiles[user]:
    if handle:
      try:
        create_profile(user, handle)
      except KeyError:
        print(f"\t\tERROR: Missing profile for handle '{handle}' (User: {user})\n")
      new_handles = [profile for profile in profiles_to_create[user] if profile not in current_profiles[user]]
      for new_handle in new_handles:
        try:
          create_profile(user, new_handle)
        except KeyError:
          print(f"\t\tERROR: Missing profile for handle '{handle}' (User: {user})\n")

  html_lines.append(f"\n\n\t\t<!-- END USER PROFILES FOR {user.upper()} -->\n")
# endregion: generate profiles

# region: close remaining tags and write to penstagram_2.html

html_lines.append("""
</body>

</html>""")

for user in users:
  print(profiles_to_create[user])

with open("penstagram_2.html", "w") as file:
  file.writelines(html_lines)

# endregion: close remaining tags and write to penstagram2.html

# TODO:
# Finish filling feeds with data
# Create score generator for sports
# Make some fake DMs
# other shit idk
###########################################
# TODO:                                   #
# Finish filling feeds with data          #
# Create score generator for sports tab   #
# ~Make some fake DMs~                    #
# Fix dms being broken                    #
###########################################

import copy

from penstagram_feeds import feeds
from penstagram_helpers import *
from penstagram_messages import messages
from penstagram_notifications import notifications
from penstagram_trending import for_you, trending, news, sports

# region: initialize html, create head, and start body
html_lines = ["""<html>

<head>
  <link rel="stylesheet" href="penstagram.css">
</head>

<body>
  <p class="disclaimer"><b>Note from the <i>Penstagram 2.0</i> Development Team: For the best user experience, 
  it is highly recommended that you turn on "Show Creator's Style".</b></p>
"""]

username_of = {
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

for name in username_of:
  html_lines.append(f"""
        <li><a href="#{name}">{username_of[name]}</a></li>""")

html_lines.append("""
      </ul>
    </div>
    <div>
      <ul class="bar"></ul>
    </div>""")
# endregion: user select page

profiles_to_create = dict()

# region: generate html for users feed, notifications, etc.
for user in username_of:
  
  html_lines.append(f"\n\n\t\t<!-- FEED FOR {user.upper()} -->\n")
  profiles_to_create[user] = set()
  link = user
  insert_header(html_lines, link)
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
  insert_navbar(html_lines, user)  
  html_lines.append(f"\n\n\t\t<!-- END FEED FOR {user.upper()} -->\n")

  sections: list[list[str, object]] = [["For You", for_you], ["Trending", trending], ["News", news], ["Sports", sports]]
  for section, data in sections:
    html_lines.append(f"\n\n\t\t<!-- {section.upper()} FOR {user.upper()} -->\n")
    link = f"{user}_{section.replace(' ', '_').lower()}"
    insert_header(html_lines, link)
    html_lines.append(f"""      <div>
        <ul class="bar">
          <li><a href="#{user}_for_you">For You</a></li>
          <li><a href="#{user}_trending">Trending</a></li>
          <li><a href="#{user}_news">News</a></li>
          <li><a href="#{user}_sports">Sports</a></li>
        </ul>
      </div>""")
    for handle, time, message in data[user]:
      profiles_to_create[user].add(handle)
      create_post(html_lines, user, handle, time, message, profiles_to_create[user])
    insert_navbar(html_lines, user)
    html_lines.append(f"\n\n\t\t<!-- END {section.upper()} FOR {user.upper()} -->\n")
  
  link = f"{user}_notifications"
  html_lines.append(f"\n\n\t\t<!-- NOTIFICATION FOR {user.upper()} -->\n")
  insert_header(html_lines, link)
  for handle, time, message in notifications[user]:
    profiles_to_create[user].add(handle)
    create_post(html_lines, user, handle, time, message, profiles_to_create[user])
  insert_navbar(html_lines, user)
  html_lines.append(f"\n\n\t\t<!-- END NOTIFICATIONS FOR {user.upper()} -->\n")
  
  link = f"{user}_messages"
  html_lines.append(f"\n\n\t\t<!-- MESSAGES FOR {user.upper()} -->\n")
  insert_header(html_lines, link)
  for other_user in messages[user]:
    message_history = messages[user][other_user]
    print(other_user, messages[user][other_user])
    create_private_message(html_lines, profiles_to_create, user, other_user, message_history, link)
  insert_navbar(html_lines, user)
  html_lines.append(f"\n\n\t\t<!-- END MESSAGES FOR {user.upper()} -->\n")
# endregion: generate html for users feed, notifications, etc.

# region: generate profiles
for user in username_of:
  html_lines.append(f"\n\n\t\t<!-- USER PROFILES FOR {user.upper()} -->\n")
  current_profiles = copy.deepcopy(profiles_to_create)
  for handle in current_profiles[user]:
    if handle:
      try:
        create_profile(html_lines,username_of, profiles_to_create, user, handle)
      except KeyError:
        print(f"\t\tERROR: Missing profile for handle '{handle}' (User: {user})\n")
      # check for handles mentioned in profiles but not anywhere else (i.e., UWM and SNMH)
      new_handles = [profile for profile in profiles_to_create[user] if profile not in current_profiles[user]]
      for new_handle in new_handles:
        try:
          create_profile(html_lines, username_of, profiles_to_create, user, new_handle)
        except KeyError:
          print(f"\t\tERROR: Missing profile for handle '{handle}' (User: {user})\n")

  html_lines.append(f"\n\n\t\t<!-- END USER PROFILES FOR {user.upper()} -->\n")
# endregion: generate profiles

# region: close remaining tags and write to penstagram_2.html
html_lines.append("""
</body>

</html>""")

# have to use utf-8 encoding to handle the emojis
with open("penstagram_2.html", "w", encoding='utf-8') as file:
  file.writelines(html_lines)
# endregion: close remaining tags and write to penstagram2.html

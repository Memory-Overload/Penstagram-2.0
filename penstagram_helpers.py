import re
from penstagram_profiles import profiles

def replace_tags(message: str, user: str, handles: set):
  """Takes in a message and returns it with all handle mentions replaced with specific anchor tags added.
    ### Params
    - `message` is the base text of the post body.
    - `user` is the current logged in user profile.
    - `handles` is the set of known profile handles."""
  
  tags: list = re.findall(r"@[\w._-]+(?<!.[._-]$)", message)
  for tag in tags:
    handles.add(tag[1:])
    message = message.replace(tag, f'<a href="#{tag[1:]}_profile_{user}" class="tag" rel="nofollow">{tag}</a>')
  return message

def create_post(html_lines: list[str], user: str, handle: str, time: str, message: str, handles: set):
  """Adds a new post to the current page.
    ### Params
    - `html_lines` is the array that will be written to the final html file
    - `user` is the name of the current logged in user.
    - `handle` is the account name for the person making the post.
    - `time` is the time that the post was created.
    - `message` is the actual body of the message.
    - `handles` is the set of known profile handles."""
  
  html_lines.append(f"""
      <p class="post"><b><a href="#{handle}_profile_{user}" rel="nofollow">{handle}</a></b> {time}<br/>
        {replace_tags(message, user, handles)}
      </p>""")

def insert_header(html_lines: list[str], link: str):
  """Inserts a header containing the Pesntagram 2.0 logo at the top of the page.
    ### Params
    - `html_lines` is the array that will be written to the final html file
    - `link` is the name of the page that pressig the logo should return to."""
  
  html_lines.append(f"""
    <a name="{link}" id="{link}" rel="nofollow"></a>
    <div class="page">
      <h1 class="header">
        <a class="logo" href="#{link}" rel="nofollow">Penstagram<sub><sub>2.0</sub></sub></a>
      </h1>""")

def insert_navbar(html_lines: list[str], user: str):
  """Inserts a navbar at the bottom of the page containing links to Home, For You, Notifications, and Messages.
    ### Params
    - `html_lines` is the array that will be written to the final html file
    - `user` is the name of the current user profile."""

  html_lines.append(f"""
    </div>
    <div>
      <ul class="bar">
        <li><a href="#{user}" rel="nofollow">🏠</a></li>
        <li><a href="#{user}_for_you" rel="nofollow">🔎</a></li>
        <li><a href="#{user}_notifications" rel="nofollow">🔔</a></li>
        <li><a href="#{user}_messages" rel="nofollow">📧</a></li>
      </ul>
    </div>""")

def create_profile(html_lines: list[str], username_of: dict, profiles_to_create, user: str, handle: str):
  """Creates a profile page for the given handle.
    ### Params
    - `html_lines` is the array that will be written to the final html file
    - `user` is the current logged in user profile.
    - `handle` is the account that the page is being created for."""
  display, location, date, bio, following, followers = profiles[handle]
  html_lines.append(f"""
    <a id="{handle}_profile_{user}" name="{handle}_profile_{user}"></a>
    <div class="page">
      <h1 class="header">
        <a class="logo" href="#{user}" rel="nofollow">Penstagram<sub><sub>2.0</sub></sub></a>
      </h1>
      <h4>
        {display}<br />@{handle}<br />{'<a href="#fake_button" class="edit_button" rel="nofollow">Edit profile</a>'
         if handle == username_of[user] else ""}
      </h4>
      <p class="bio">📍: {location} | 📅: {date}<br />
        {replace_tags(bio, user, profiles_to_create[user])}
        <br />
        <br />
        {following} Following | {followers} Followers
      </p>
    </div>
    <div>
      <ul class="bar">
        <li><a href="#{user}" rel="nofollow">🏠</a></li>
        <li><a href="#{user}_for_you" rel="nofollow">🔎</a></li>
        <li><a href="#{user}_notifications" rel="nofollow">🔔</a></li>
        <li><a href="#{user}_messages" rel="nofollow">📧</a></li>
      </ul>
    </div>""")

def create_private_message(html_lines: list, profiles_to_create: dict, 
                           user: str, other_user: str, message_history: list[tuple], link: str):
  profiles_to_create[user].add(other_user)
  insert_header(html_lines, link)
  html_lines.append(f"""
    <h2><a href="#{other_user}_profile_{user}">{other_user}</a></h2><br/>
    <p>""")
  for side, message in message_history:
    html_lines.append(f"""
      <span class="{'right' if side else 'left'}_text">{replace_tags(message, user, profiles_to_create[user])}</span>""")
  html_lines.append("""
    </p>""")
  insert_navbar(html_lines, user)
  
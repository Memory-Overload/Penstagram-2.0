###########################################
# check mark for copy-pasting: ✓
# TODO:
# More fake DMs
# - Eda
# - Raine
# - Darius
# - Luz
# - Amity
# Flesh out news and trending feeds
# Make feeds for:
# - Gus
# - Willow
# - Hunter
# - Vee
# - Masha
###########################################

from penstagram_helpers import create_post, create_private_message, create_profile, insert_header, insert_navbar, replace_tags
from penstagram_notifications import notifications
from penstagram_feeds import feeds
from penstagram_messages import messages
from penstagram_trending import news, sports, for_you, trending

from copy import deepcopy

username_of = {
    "eda": "BADGIRLCOVEN",
    "darius": "goo-daddy",
    "raine": "rainey.day",
    "luz": "goodWitchLuzura",
    "amity": "WitchChick128",
}


def start_html(html_lines: list[str]):
    html_lines.append("""<html>

<head>
  <link rel="stylesheet" href="penstagram.css">
</head>

<body>
  <p class="disclaimer"><b>Note from the <i>Penstagram 2.0</i> Development Team: For the best user experience,
      it is highly recommended that you turn on "Show Creator's Style".</b></p>
  <div class="main">
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


def close_html(html_lines):
    html_lines.append("""
</body>

</html>""")


profiles_to_create: dict[str:set] = dict()


def generate_feed(html_lines: list[str], user: str):
    html_lines.append(f"\n\n\t\t<!-- FEED FOR {user.upper()} -->\n")
    profiles_to_create[user] = set()
    insert_header(html_lines, user, user)
    html_lines.append("""
      <p>
        <a href="#login" class="switch_profile" rel="nofollow">SWITCH PROFILE</a>
      </p>""")
    feed: list[list[str]] = feeds[user]
    for handle, time, message in feed:
        profiles_to_create[user].add(handle)
        html_lines.append(f"""
      <p class="post"><b><a href="#{handle}_profile_{user}" rel="nofollow">{handle}</a></b> {time}<br />
        {replace_tags(message, user, profiles_to_create[user])}
      </p>""")
    insert_navbar(html_lines, user)
    html_lines.append(f"\n\n\t\t<!-- END FEED FOR {user.upper()} -->\n")


def generate_sections(html_lines: list[str], user: str):
    sections: list[list[str, object]] = [["For You", for_you], [
        "Trending", trending], ["News", news], ["Sports", sports]]
    for section, data in sections:
        html_lines.append(
            f"\n\n\t\t<!-- {section.upper()} FOR {user.upper()} -->\n")
        link = f"{user}_{section.replace(' ', '_').lower()}"
        insert_header(html_lines, link, user)
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
            create_post(html_lines, user, handle, time,
                        message, profiles_to_create[user])
        insert_navbar(html_lines, user)
        html_lines.append(
            f"\n\n\t\t<!-- END {section.upper()} FOR {user.upper()} -->\n")


def generate_notifications(html_lines: list[str], user: str):
    link = f"{user}_notifications"
    html_lines.append(f"\n\n\t\t<!-- NOTIFICATION FOR {user.upper()} -->\n")
    insert_header(html_lines, link, link)
    for notification in notifications[user]:
        html_lines.append(f"""
      <p class="post">{replace_tags(notification, user, profiles_to_create[user])}</p><hr>""")
    insert_navbar(html_lines, user)
    html_lines.append(
        f"\n\n\t\t<!-- END NOTIFICATIONS FOR {user.upper()} -->\n")


def generate_messages(html_lines: list[str], user: str):
    link = f"{user}_messages"
    messages_link = f"{user}_messages"
    html_lines.append(f"\n\n\t\t<!-- MESSAGES FOR {user.upper()} -->\n")
    insert_header(html_lines, link, link)
    html_lines.append("""
      <h2>Select a conversation.</h2>""")
    for other_user in messages[user]:
        html_lines.append(f"""
        <h4><a href="#{other_user}_convo_{user}">{other_user}</a></h4><hr>""")
    insert_navbar(html_lines, user)
    for other_user in messages[user]:
        link = f"{other_user}_convo_{user}"
        insert_header(html_lines, link, messages_link)
        message_history = messages[user][other_user]
        create_private_message(
            html_lines, profiles_to_create, user, other_user, message_history)
        insert_navbar(html_lines, user)
    html_lines.append(f"\n\n\t\t<!-- END MESSAGES FOR {user.upper()} -->\n")


def generate_profiles(html_lines: list[str], user: str):
    html_lines.append(f"\n\n\t\t<!-- USER PROFILES FOR {user.upper()} -->\n")
    current_profiles = deepcopy(profiles_to_create)
    for handle in current_profiles[user]:
        if handle:
            try:
                create_profile(html_lines, username_of,
                               profiles_to_create, user, handle)
            except KeyError:
                print(
                    f"\t\tERROR: Missing profile for handle '{handle}' (User: {user})\n")
    # check for handles mentioned in profiles but not anywhere else
    new_handles = profiles_to_create[user] - current_profiles[user]
    for new_handle in new_handles:
        try:
            create_profile(html_lines, username_of,
                           profiles_to_create, user, new_handle)
        except KeyError:
            print(
                f"\t\tERROR: Missing profile for handle '{handle}' (User: {user})\n")
    html_lines.append(
        f"\n\n\t\t<!-- END USER PROFILES FOR {user.upper()} -->\n")


def write_to_html(html_lines):
    # have to use utf-8 encoding to handle the emojis
    with open("penstagram_2.html", "w", encoding='utf-8') as file:
        file.writelines(html_lines)


def main():
    html_lines = []
    start_html(html_lines)
    for user in username_of:
        generate_feed(html_lines, user)
        generate_sections(html_lines, user)
        generate_notifications(html_lines, user)
        generate_messages(html_lines, user)
        generate_profiles(html_lines, user)
    close_html(html_lines)
    write_to_html(html_lines)


if __name__ == "__main__":
    main()

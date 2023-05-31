import re

current_user = "raine"

posts = [
    ["rainey.day", "Just did a line of rosin powder. Let's get this money, bards.", "2:07 AM"],
    ["skara4real", "Hot take: Violas are better than violins in every aspect.", "8:24 AM"],
    ["_derwin", "@skara4real Incorrect, it is a known fact that bassoons are the best.", "8:29 AM"],
    ["FreeTheLemons", "@_derwin bro why are u beefing with a child. chill.", "8:31 AM"],
    ["FreeTheLemons", "also we should just accept that all instruments have value and are of equal worth. even if they sometimes sound like a dying ratworm.", "8:32 AM"],
    ["bo-lieve", "Yo @goops, can I get an expedited review of my DR-HR Exchange Program appilcation? Maybe show a little HAS nepotism?", "9:38 AM"],
    ["goops", "@bo-lieve I might be able to pull some strings.", "9:41 AM"],
    ["bo-lieve", "@goops Thank you so much :)", "9:42 AM"],
    ["goops", "@bo-lieve eh its no biggie", "9:42 AM"],
    ["rainey.day", "Sometimes, I wish I made it as an actor.", "10:14 AM"],
    ["rainey.day", "Wait, no. That's a horrible idea.", "10:14 AM"],
    ["rainey.day", "The trauma is still too strong.", "10:15 AM"],
    ["rainey.day", "The blood oranges. Oh Titan, the blood oranges.", "10:15 AM"],
    ["FreeTheLemons", "@rainey.day I'd pay like a bajillion snails to see you do The Monarch In Orange.", "10:17 AM"],
    ["rainey.day", "@FreeTheLemons did you not just see my posts? there is nothing you can do that will ever convince me to perform that play.", "10:19 AM"],
    ["rainey.day", "@FreeTheLemons Firstly: No. Secondly: I don't want to die just yet.", "10:20 AM"],
    ["FreeTheLemons", "@rainey.day Darn I thought maybe that would be fun.", "10:23 AM"],
    ["amberamberamber", "if @BADGIRLCOVEN is our mom, does that mean @KINGOFDEMONS is our brother???", "12:19 AM"],
    ["BADGIRLCOVEN", "that is not how that works. at all.", "12:20 AM"],
    ["BADGIRLCOVEN", "also, I ain't your mom. what I said back then? that was a joke.", "12:21 AM"],
    ["amberamberamber", "but what about you and @rainey.day", "12:21 AM"],
    ["BADGIRLCOVEN", "we haven't tied the knot yet, and probably never will. sorry to burst your bubble, kid.", "12:23 AM"],
    ["amberamberamber", "sad", "12:23 AM"],
    ["BADGIRLCOVEN", "so goes life.", "12:23 AM"],
    ["BADGIRLCOVEN", "i need some late night apple blood.", "12:28 AM"],
    ["steve", "steve", "3:00 AM"],
]

string: str = f"""
<a name="{current_user}" rel="nofollow" id="{current_user}"></a>
<div class="page">
  <h1 class="header">
    <a class="logo" href="#{current_user}" rel="nofollow">Penstagram<sub><sub>2.0</sub></sub></a>
  </h1>
  <p>
    <a href="#login" class="switch_profile" rel="nofollow">SWITCH PROFILE</a>
  </p>"""

for author, message, time in posts:
    tags: list = re.findall(r"@[\w._-]+(?<!.[._-]$)", message) # can't end with ., _, or -
    post_to_add = f"""
  <p class="post"><span class="post_author"><b><a href="#{author}_profile_{current_user}" rel="nofollow">{author}</a></b> {time}<br /></span>
    {message}
  </p>"""
    
    if tags:  # empty lists eval to falsey, but non-empty lists are truthy
        for tag in tags:
          post_to_add = post_to_add.replace(tag, f"""<a href="#{tag[1:]}_profile_{current_user}" class="tag" rel="nofollow">{tag}</a>""")
    string += post_to_add
string += f"""
</div>"""

print(string, end="")
import re

current_user = "eda"

posts = [
    ["", "@MARILYN.PLEASE.COME.BACK, @I.MISS.YOU, and @stan followed you.", ""],
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
string += """
</div>"""

print(f"{string}", end="")
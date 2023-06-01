import shared_functions

current_user: str = "mo"

posts = [
    # [author, message, time]
    ["MemoryOverload", "This is an example", "12:00 AM"],
    ["MemoryOverload", "Subscribe to @DanaTerrace", "12:00 AM"]
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
    post_to_add = f"""
  <p class="post"><span class="post_author"><b><a href="#{author}_profile_{current_user}" rel="nofollow">{author}</a></b> {time}<br /></span>
    {message}
  </p>"""
    string += shared_functions.replace_tags(post_to_add, current_user)
string += f"""
</div>"""

print(string, end="")

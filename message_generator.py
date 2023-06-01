import shared_functions

left_user: str = "Alabomdor_1"
right_user: str = "goo-daddy"
current_user: str = "darius"

messages = [
    # false = left text, true = right text
    [],
]

string: str = f"""
<a name="{left_user}_convo_{right_user}" id="{left_user}_convo_{right_user}" rel="nofollow"></a>
    <div class="page">
      <h1 class="header">
        <a class="logo" href="#{current_user}" rel="nofollow">Penstagram<sub><sub>2.0</sub></sub></a>
      </h1>
      <h2>{left_user}</h2>
      <hr>
      <p>"""
for side, message in messages:
    string += f"""
        <span class={"'right" if side else "'left"}_text'>
          {shared_functions.replace_tags(message, current_user)}
        </span>"""

string += f"""
      </p>
    </div>"""

print(string)

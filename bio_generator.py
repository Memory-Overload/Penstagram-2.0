import shared_functions

current_user = "raine"

bios = [
  # [name, handle, location, date, description, following, followers]
  [],
]

for name, handle, location, date, description, following, followers in bios:
  # convert @ mentions into actual tags to user profiles
  description = shared_functions.replace_tags(description, current_user)
  
  # __pin__ and __calendar__ represent 📌 and 📅, respectively
  # because python can't handle printing emojis.
  # cowards, honestly.
  # just remember to Ctrl+H and replace the standins with the emojis
  string: str = f"""
  <a name="{handle}_profile_{current_user}" rel="nofollow" id="{handle}_profile_{current_user}"></a>
  <div class="page">
    <h1 class="header">
      <a class="logo" href="#{current_user}" rel="nofollow">Penstagram<sub><sub>2.0</sub></sub></a>
    </h1>
    <h4>{name}<br />
        @{handle}<br />
    </h4>
    <p class="bio">__pin__: {location} | __calendar__: {date}<br />
      {description}<br />
      <br />
      {following} Following | {followers} Followers
    </p>
  </div>"""

  print(string)

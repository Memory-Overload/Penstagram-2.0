import shared_functions

current_user = "raine"

bios = [
    ["KING", "KINGOFDEMONS", "My dad's corpse", "Awf. 2021", "A squirmy lil fella", "2", "53k"],
    ["scare bear enthusiast", "skara4real", "a hole", "Ath. 2022", "flyer derby > grudgby. fight me over it.", "285", "2k"],
    ["niche penstagram microcelebrity", "amberamberamber", "in denial", "Dis. 2019", "she/her | making mewtube vids about life n stuff", "314", "5k"],
    ["derwin", "_derwin", "Not doxxing myself", "Dis. 2019", "Proving bard magic can be cool", "579", "403"],
    ["Lemons aka Katya (she/her)", "FreeTheLemons", "posting fic on OFW", "Dis. 2015", "writer of stories. i feed on angst.", "489", "11k"],
    ["Steve Tholomule", "steve", "The Heart", "Awk. 2016", "Yo. I'm Steve.", "2", "-2,147,483,648"],
    ["Bo Jangles", "bo-lieve", "movin'", "Fea. 2018", "I know.", "68", "381"],
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
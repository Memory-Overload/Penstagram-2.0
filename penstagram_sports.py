from secrets import choice

def pick_one_and_remove(x: list):
  return x.pop(x.index(choice(x)))

def generate_games():
  teams = ["Ogres", "Painbow Warriors", "Wendigos", "Banshees", "Gorgons", "Grenwitch Giants", "Fairies", "Emerald Entrails"]
  games = []
  while(teams):
    team_one: str = pick_one_and_remove(teams)
    team_two: str = pick_one_and_remove(teams)
    win_score = choice(range(1, 73))
    lose_score = choice(range(win_score))
    victory_message = [
      f"{team_one} win! Final score: {team_one} {win_score}, {team_two} {lose_score}.",
      f"FINAL: {team_one} walk away with the W over {team_two}, {win_score} - {lose_score}!",
      f"{team_one} call game against the {team_two}. {team_one} score {win_score}, while {team_two} only put up {lose_score}.",
      f"{team_one} take down the {team_two}, {win_score} to {lose_score}.",
    ]
    loss_message = [
      f"Final: {win_score} - {lose_score}",
      f"Let's not talk about what happened.",
      f"We fought until the very end. {win_score} - {lose_score}",
      f"That was brutal. Final score is {win_score} to {lose_score}",
    ]
    minutes = choice(range(0, 1440))
    hour = (minutes // 60) % 12
    if hour == 0: hour == 12
    games.append([[team_one.replace(" ", ""), f"{hour}:{(minute:= (('0' if len(str(minutes % 60)) == 1 else '') + str(minutes % 60)))} {(suffix := 'AM' if (minutes // 60) < 12 else 'PM')}", choice(victory_message)], minutes])
    games.append([[team_two.replace(" ", ""), f"{hour}:{minute} {suffix}", choice(loss_message)], minutes])
  
  games.sort(key=lambda game: game[1])
  return [game[0] for game in games]

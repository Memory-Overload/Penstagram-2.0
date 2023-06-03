import secrets

locations = [location.strip() for location in open("locations.txt")]
teams = [mascot.strip() for mascot in open("mascots.txt")]
game_times = [f"{i}:00 PM" for i in range(1, 8)]

current_user = "eda"

def final_score(team1: str, team2: str):
    winning_team = secrets.choice([team1, team2])
    score1 = secrets.randbelow(73) + 1
    score2 = secrets.randbelow(score1)
    difference = score1 - score2
    
    if winning_team == team1 and difference >= 28:
        return f"A slaughtering. {team1} destroy the {team2} by a score of {score1}-{score2}."
    
    if winning_team == team1 and 7 <= difference < 28:
        return f"That's time! {team1} beat the {team2}, {score1}-{score2}."
    
    if winning_team == team1 and difference < 7:
        return f"A nailbiter til the end, we eak out a {difference}-point win against the {team2}, {score1}-{score2}."
    
    if winning_team == team2 and difference < 7:
        return f"We nearly had 'em. {score1}-{score2}, {team2} win."
    
    if winning_team == team2 and 7 <= difference < 28:
        return f"A tough loss. {team2} win, {score1}-{score2}."
    
    if winning_team == team2 and difference > 28:
        return f"Let's not talk about what hapened. Final: {team2} {score1}, {team1} {score2}."
    return f"We end with a tie against the {team2}, {score1}-{score2}"

games_played = int(len(teams) / 2)
final_score_posts = [[((locations.pop(locations.index(secrets.choice(locations))) if (secrets.randbits(1) % 2) else "") + (team:= teams.pop(teams.index(secrets.choice(teams))))).replace(" ", ""), \
          final_score(team, teams.pop(teams.index(secrets.choice(teams)))), secrets.choice(game_times)] for _ in range(games_played)]

def sort_by_time(post):
    return post[2][0]

final_score_posts.sort(key=sort_by_time)
string = ""

for author, message, time in final_score_posts:
    post_to_add = f"""
  <p class="post"><span class="post_author"><b><a href="#{author}_profile_{current_user}" rel="nofollow">{author}</a></b> {time}<br /></span>
    {message}
  </p>"""
    string += post_to_add

print(string)
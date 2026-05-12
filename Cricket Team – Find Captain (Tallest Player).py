team = {
    "Player1": 170,
    "Player2": 175,
    "Player3": 180,
    "Player4": 178,
    "Player5": 172,
    "Player6": 176,
    "Player7": 174,
    "Player8": 179,
    "Player9": 173,
    "Player10": 177,
    "Player11": 181
}

captain = max(team, key=team.get)  
print("Captain of the Team:", captain)
print("Height:", team[captain])

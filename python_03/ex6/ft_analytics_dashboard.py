my_dic = {
    "players": {
        "alice": {
            "level": 12,
            "total_score": 2300,
            "sessions_played": 2,
            "favorite_mode": "ranked",
            "achievements": [
                "first_kill",
                "speed_runner",
                "treasure_hunter"
            ]
        },
        "bob": {
            "level": 7,
            "total_score": 1800,
            "sessions_played": 2,
            "favorite_mode": "casual",
            "achievements": [
                "first_kill",
                "level_10"
            ]
        },
        "charlie": {
            "level": 15,
            "total_score": 2150,
            "sessions_played": 2,
            "favorite_mode": "competitive",
            "achievements": [
                "boss_slayer",
                "speed_runner",
                "level_10"
            ]
        },
        "diana": {
            "level": 5,
            "total_score": 1200,
            "sessions_played": 2,
            "favorite_mode": "casual",
            "achievements": [
                "first_kill",
                "treasure_hunter"
            ]
        }
    },
    "sessions": [
        {"player": "alice", "score": 400, "mode": "ranked", "completed": True},
        {"player": "alice", "score": 300, "mode": "ranked", "completed": False},
        {"player": "bob", "score": 200, "mode": "casual", "completed": True},
        {"player": "bob", "score": 180, "mode": "casual", "completed": True},
        {"player": "charlie", "score": 500, "mode": "competitive", "completed": True},
        {"player": "charlie", "score": 450, "mode": "competitive", "completed": False},
        {"player": "diana", "score": 150, "mode": "casual", "completed": True},
        {"player": "diana", "score": 100, "mode": "casual", "completed": True}
    ],
    "game_modes": ["casual", "competitive", "ranked"]
}


print("=== Game Analytics Dashboard ===")

print("\n=== List Comprehension Examples ===")

high_scorers = [
    name
    for name in my_dic["players"]
    if my_dic["players"][name]["total_score"] > 2000
]

print("High scorers (>2000):", high_scorers)

scores_doubled = [
    my_dic["players"][name]["total_score"] * 2
    for name in my_dic["players"]
]

print("Scores doubled:", scores_doubled)

active_players = [
    session["player"]
    for session in my_dic["sessions"]
    if session["completed"]
]
print("Active players:", set(active_players))


print("\n=== Dict Comprehension Examples ===")
player_scores = {
    name: my_dic["players"][name]["total_score"]
    for name in my_dic["players"]
}
print("Player scores:", player_scores)

score_categories = {
    "high": sum(
        1
        for name in my_dic["players"]
        if my_dic["players"][name]["total_score"] > 5000
    ),
    "medium": sum(
        1
        for name in my_dic["players"]
        if 3000 <= my_dic["players"][name]["total_score"] <= 5000
    ),
    "low": sum(
        1
        for name in my_dic["players"]
        if my_dic["players"][name]["total_score"] < 3000
    )
}
print("Score categories:", score_categories)

achievement_counts = {
    name: len(my_dic["players"][name]["achievements"])
    for name in my_dic["players"]
}

print("Achievement counts:", achievement_counts)

print("\n=== Set Comprehension Examples ===")

unique_players = {
    session["player"]
    for session in my_dic["sessions"]
}
print("Unique players:", unique_players)

unique_achievements = {
    ach
    for player_name in my_dic["players"]
    for ach in my_dic["players"][player_name]["achievements"]
}
print("Unique achievements:", unique_achievements)

active_regions = {
    session["mode"]
    for session in my_dic["sessions"]
}
print("Active regions:", active_regions)

print("\n=== Combined Analysis ===")

total_player = sum(1 for player in my_dic["players"])

print("Total players:", total_player)
print("Total unique achievements:",len(unique_achievements))
print("Average score:",sum(player_scores.values()) / total_player)

top_score = 0
top_player = ""
for player_name in my_dic["players"]:
    score = my_dic["players"][player_name]["total_score"]
    if score > top_score:
        top_score = score
        top_player = player_name

print("Top performer:", f"{top_player} ({top_score} points, "
      f"{len(my_dic['players'][top_player]['achievements'])} achievements)")

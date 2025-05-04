football_players = {"Akash", "Yash", "Zafar"}
cricket_players = {"Yash", "Amit", "Ishaan"}

both = football_players & cricket_players
only_one = football_players ^ cricket_players
none = {"Akash", "Yash", "Amit", "Zafar", "Ishaan", "Shubham"} - (football_players | cricket_players)

print("\nSports Participation:")
print("Both Football & Cricket:", both)
print("Only one sport:", only_one)
print("None:", none)

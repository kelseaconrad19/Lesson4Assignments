import random

moods = ["happy", "sad", "angry", "embarrassed", "excited", "thoughtful", "proud"]
days = ["Monday", "Tuesday", "Wednesday", "Thursday", "Friday", "Saturday", "Sunday"]

for _ in range(1, 8):
    day_of_week = days[_ - 1]
    rand_mood = random.choice(moods)
    print(f"On {day_of_week}, you were feeling {rand_mood}.")


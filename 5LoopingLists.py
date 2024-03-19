# Task 1: The for Loop DJ Set
# Using the provided genres list, write a for loop that prints out each genre with a custom message. Extend this task by adding a counter that displays the number of the track before the genre.

# Our playlist of genres
genres = ['Jazz', 'Rock', 'Hip-hop', 'Classical']

for i in range(1, 5):
    genre = genres[i - 1]
    print(f"Track {i}: Enjoy this {genre} playlist.")

# # Task 2: The Remix Artist with while
# # Convert the for loop from Task 1 into a while loop. Ensure it performs the same function but also includes a condition to stop the loop if a certain genre is played for instance Hip-hop.

i = 0
while i < len(genres):
    print(f"Track {i + 1}: Enjoy this {genres[i]} playlist.")
    i = i + 1
    if genres[i] == "Classical":
        break

# Task 3: Light Show Technician Loop
# Using the range() function, loop through the genres list by index. For each genre, print out the track number and a message that the light show is ready. Modify the loop to skip a genre if it's not suitable for the light show, for instance Classical genre.

for i in range(0, len(genres)):
    if genres[i] == "Jazz" or genres[i] == "Classical":
        pass
    else:
        print(f"Track {i + 1}: The light show is ready.")


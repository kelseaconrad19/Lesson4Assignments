# Task 1: The Selective DJ
# Loop through a slice of the genres list from the previous question and print out the genres. Use slicing to create a sublist of genres from the second to the fourth track.
genres = ['Jazz', 'Rock', 'Hip-hop', 'Classical']
sublist = genres[0:2]

# Task 2: The One-Liner Band with List Comprehensions
# Use a list comprehension to create a new list that contains each genre with the word "Music" appended to it. Print this new list.
# newlist = [expression for item in iterable if condition == True]
music_list = [x + " Music" for x in genres]
print(music_list)

# Task 3: Numerical Beats with range
# Write a loop using range() to print out a countdown from 10 to 1, followed by the message "The beat drops now!".

for num in range(10, 0, -1):
    print(num)
print("The beat drops now!")

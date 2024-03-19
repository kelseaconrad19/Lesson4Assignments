# Task 1: Loop Condition Exploration
# Write a while loop with a condition that will never be true (an infinite loop). Inside the loop, print a statement. Then, use a break statement to exit the loop after 5 iterations.
infinity = 0
# Original code:
# while True:
#     print("Just keep printing. Just keep printing.")
#     infinity += 1
#     if infinity == 5:
#         break

# Task 2: Modify the infinite loop from Task 1 to include a condition that will eventually be true and remove the break statement. The loop should terminate naturally once the condition is met.
while infinity < 5:
    print("Just keep printing. Just keep printing.")
    infinity += 1

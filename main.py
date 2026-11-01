import game_data
import art
import random


# Compare the follower count
def comp(a_follower, b_follower):
    if a_follower > b_follower:
        return a_follower
    elif a_follower < b_follower:
        return b_follower
    else:
        return 0


# Start the score and select the first person
count = 0
print(art.logo)
A = random.choice(game_data.data)


# Keep playing until the user gives a wrong answer
while True:
    print(A["name"] + ", " + A["description"] + ", from " + A["country"])
    B = random.choice(game_data.data)
    if A["follower_count"] == B["follower_count"]:
        B = random.choice(game_data.data)
    print(art.vs)
    print(B["name"] + ", " + B["description"] + ", from " + B["country"])
    user_choice = input("Who has more followers? Type 'A' or 'B' ")

    # Check whether the user's choice is correct
    if user_choice == "A":
        if A["follower_count"] == comp(A["follower_count"], B["follower_count"]):
            count += 1
            print(f"Yor are right! your current score is {count}")
            A = B
        else:
            print(f"Sorry, that's wrong. Final score is {count}")
            break

    elif user_choice == "B":
        if B["follower_count"] == comp(A["follower_count"], B["follower_count"]):
            count += 1
            print(f"Yor are right! your current score is {count}")
            A = B
        else:
            print(f"Sorry, that's wrong. Final score is {count}")
            break

    else:
        print("invalid input")
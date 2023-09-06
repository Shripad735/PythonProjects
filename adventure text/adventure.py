import random

def main():
    name = input("Enter Your Name: ")
    print(f"{name}, you are stuck in a dense forest. Your task is to get out of the forest without getting caught or harmed.")
    
    while True:
        print("\nYou are walking through the forest and suddenly a wild animal appears in your path. Now you have two options:")
        print("1. Run")
        print("2. Climb the nearest tree")
        
        user_choice = input("Choose an option (1 or 2): ")

        if user_choice == '1':
            outcome = encounter_wild_animal()
            if outcome == "You Died!!":
                print(outcome)
                break
        elif user_choice == '2':
            print("You climb the nearest tree and wait for a while. The animal loses interest and leaves. You survived this encounter!")
        else:
            print("Incorrect Input. Please choose 1 or 2.")

    print("Game Over. Do you want to play again? (yes/no)")
    play_again = input()
    if play_again.lower() == "yes":
        main()
    else:
        print("Thanks for playing!")

def encounter_wild_animal():
    animal = random.choice(["wolf", "bear", "lion", "tiger", "snake"])
    print(f"You encounter a {animal}!")

    if random.randint(0, 1) == 0:
        return "You managed to run away from the wild animal!"
    else:
        return "You Died!!"

if __name__ == "__main__":
    main()

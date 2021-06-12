while(True):
    print("press q for quit : ")
    user = input("Enter your number : ")
    if user == "q":
        break
    try:
        user = int(user)
        if user < 6:
            print("plz enter greater number :crossed_swords: ")

    except Exception as e:
        print(f"Invalid input {e}")

print("Thanks for playing this game 😄")
 
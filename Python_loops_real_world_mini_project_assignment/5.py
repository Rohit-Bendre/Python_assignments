print("----------NUMBER GUESSING GAME----------")
original_number=37


attempts=5
used_attempts=0
guess_status=False
while attempts:
    user_num=int(input("Enter a number between : "))
    attempts-=1
    used_attempts+=1
    if user_num==original_number:
        guess_status=True
        print(f"Congratulations! You guessed the correct number {original_number}.")
        print(f"You guessed the number in {used_attempts} attempts.")
        break
    elif user_num<original_number:
        print("you entered a too low number ")
    elif user_num>original_number:
        print("you entered a too high number ")

print("-"*50)
if not guess_status:
    print("You have used all your attempts. Better luck next time!")
    print(f"The correct number was {original_number}.")
    print(f"Total attempts used: {used_attempts}")


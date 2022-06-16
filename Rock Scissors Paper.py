from tkinter import *
import random

# Variable
marks = {
    "Rock": {"Rock": 1, "Paper": 0, "Scissors": 2},
    "Paper": {"Rock": 2, "Paper": 1, "Scissors": 0},
    "Scissors": {"Rock": 0, "Paper": 2, "Scissors": 1}
}
computer_score = 0
player_score = 0
tie_times = 0


# Function
def result_handler(user_choice):
    global computer_score
    global player_score
    global tie_times

    result = ["Rock", "Scissors", "Paper"]
    random_number = random.randint(0, 2)
    computer_choice = result[random_number]
    outcome = marks[user_choice][computer_choice]

    Player_Choice_Label.config(fg="Red", text="Player's Choice = " + str(user_choice))
    Computer_Choice_Label.config(fg="Yellow", text="Computer's Choice = " + str(computer_choice))

    if outcome is 2:
        player_score = player_score + 1
        Player_Score_Label.config(text="Player's score = " + str(player_score))
        Result_Label.config(fg="Red", text="Player Wins")

    if outcome is 1:
        tie_times = tie_times + 1
        Tie_Times_Label.config(text="Tie times = " + str(tie_times))
        Result_Label.config(fg="White", text="It's a tie")

    if outcome is 0:
        computer_score = computer_score + 1
        Computer_Score_Label.config(text="Computer's score = " + str(computer_score))
        Result_Label.config(fg="Yellow", text="Computer Wins")

# Main screen
window = Tk()
window.title("Rock Scissors Paper")
window['bg'] = '#1A1F16'

# Labels
Label(window, text="Welcome to the game of Rock Scissors Paper", bg="#1A1F16", fg="#94ecbe", font=("HYRUNYUAN-75W", 18)).grid(row=0, sticky=N, pady=10, padx=150)
Label(window, text="Please make your choice", bg="#1A1F16", fg="#94ecbe", font=("HYRUNYUAN-75W", 14)).grid(row=1, sticky=N)

Player_Score_Label = Label(window, text="Player's score = 0", bg="#1A1F16", fg="#94ecbe", font=("HYRUNYUAN-75W", 14))
Player_Score_Label.grid(row=2, sticky=W, padx=10)

Computer_Score_Label = Label(window, text="Computer's score = 0", bg="#1A1F16", fg="#94ecbe", font=("HYRUNYUAN-75W", 14))
Computer_Score_Label.grid(row=2, sticky=E, padx=10)

Tie_Times_Label = Label(window, text="Tie times = 0", bg="#1A1F16", fg="#94ecbe", font=("HYRUNYUAN-75W", 14))
Tie_Times_Label.grid(row=2, sticky=N, padx=10)

Player_Choice_Label = Label(window, bg="#1A1F16", fg="#94ecbe", font=("HYRUNYUAN-75W", 14))
Player_Choice_Label.grid(row=3, sticky=W, padx=10)

Computer_Choice_Label = Label(window, bg="#1A1F16", fg="#94ecbe", font=("HYRUNYUAN-75W", 14))
Computer_Choice_Label.grid(row=3, sticky=E, padx=10)

Result_Label = Label(window, bg="#1A1F16", fg="#94ecbe", font=("HYRUNYUAN-75W", 18))
Result_Label.grid(row=4, sticky=N)

# Button
BtRock = Button(window, text="Rock", bg="#4A7856", fg="#1A1F16", width=15, font=("HYRUNYUAN-75W", 18), command=lambda: result_handler("Rock"))
BtRock.grid(row=5, sticky=W, pady=10, padx=10)

BtScissors = Button(window, text="Scissors", bg="#4A7856", fg="#1A1F16", width=15, font=("HYRUNYUAN-75W", 18), command=lambda: result_handler("Scissors"))
BtScissors.grid(row=5, sticky=S, pady=10, padx=10)

BtPaper = Button(window, text="Paper", bg="#4A7856", fg="#1A1F16", width=15, font=("HYRUNYUAN-75W", 18), command=lambda: result_handler("Paper"))
BtPaper.grid(row=5, sticky=E, pady=10, padx=10)

# Nicer look(Dummy Label)
Label(window, bg="#1A1F16", fg="#94ecbe").grid(row=6)

window.mainloop()
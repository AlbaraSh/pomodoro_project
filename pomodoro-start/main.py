from tkinter import *
from turtle import Screen
import math

# Constants
PINK = "#e2979c"
RED = "#e7305b"
GREEN = "#9bdeac"
YELLOW = "#f7f5dd"
FONT_NAME = "Courier"
FONT = (FONT_NAME, 35, "bold")
reps = 0
timer = None


# reset_timer method reset the timer and the reps and sets the label nad canvas back to their original text
def reset_timer():
    window.after_cancel(timer)
    canvas.itemconfig(timer_text, text="00:00")
    label.config(text='Timer')
    check_marks.config(text="")
    global reps
    reps = 0


# start_timer method converts the minutes to seconds and determines what phase is next once the clock hits 0
def start_timer():
    global reps
    reps += 1
    work_sec = WORK_MIN * 60
    short_break_sec = SHORT_BREAK_MIN * 60
    long_break_sec = LONG_BREAK_MIN * 60

    if reps % 8 == 0:
        count_down(long_break_sec)
        label.config(text="Long Break", fg=RED)
    elif reps % 2 == 0:
        count_down(short_break_sec)
        label.config(text="Short Break", fg=PINK)
    else:
        count_down(work_sec)
        label.config(text="Work Time", fg=GREEN)


# count_down method is the countdown mechanism that is used in start_timer(),
# this also prints a checkmark for each work rep that is completed
def count_down(count):
    global reps
    count_min = math.floor(count / 60)
    count_sec = math.floor(count % 60)
    if count_min < 10:
        count_min = '0' + str(count_min)
    if count_sec < 10:
        count_sec = '0' + str(count_sec)

    canvas.itemconfig(timer_text, text=f"{count_min}:{count_sec}")
    if count > 0:
        global timer
        timer = window.after(1000, count_down, count - 1)
    else:
        start_timer()
        marks = ""
        for n in range(math.floor(reps / 2)):
            marks += "✔"
        check_marks.config(text=marks)


# this section is for the UI setup
# setting up window
window = Tk()
window.title("Pomodoro")
window.config(padx=100, pady=50, bg=YELLOW)

# setting tomato image in canvas
canvas = Canvas(width=200, height=224, bg=YELLOW, highlightthickness=0)
photo = PhotoImage(file="tomato.png")
canvas.create_image(100, 110, image=photo)
timer_text = canvas.create_text(100, 130, text="00:00", fill="white", font=FONT)
canvas.grid(column=1, row=2)

# Timer Label
label = Label(text="Timer", bg=YELLOW, highlightthickness=0, font=FONT, fg=GREEN)
label.grid(column=1, row=1)

# start button
start_button = Button(text="start", highlightthickness=0, command=start_timer)
start_button.grid(column=0, row=3)

# reset button
reset_button = Button(text="reset", highlightthickness=0, command=reset_timer)
reset_button.grid(column=2, row=3)

# creating the green checkmark
check_marks = Label(fg=GREEN, bg=YELLOW)
check_marks.grid(column=1, row=3)

# using turtle module to have a pop-up appear and ask the user how long they want their work and break cycles
screen = Screen()
screen.bye()
WORK_MIN = float(
    screen.textinput(title='Timer Settings', prompt="How many minutes would you like your work cycle to be"))
SHORT_BREAK_MIN = float(screen.textinput(title='Timer Settings',
                                         prompt="How many minutes would you like your short break to be"))
LONG_BREAK_MIN = float(screen.textinput(title='Timer Settings',
                                        prompt="How many minutes would you like your long break to be"))


window.mainloop()

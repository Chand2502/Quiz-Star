import json
import tkinter
from tkinter import *
import random


with open('./data.json', encoding="utf8") as f:
    data = json.load(f)

questions = [v for v in data[0].values()]
answers_choice = [v for v in data[1].values()]

answers = [1, 1, 1, 1, 3, 1, 0, 1, 3, 3]

user_answer = []
indexes = []


def gen():
    global indexes
    while len(indexes) < 5:
        x = random.randint(0, 9)
        if x in indexes:
            continue
        else:
            indexes.append(x)


def showresult(score):
    lblQuestion.destroy()
    r1.destroy()
    r2.destroy()
    r3.destroy()
    r4.destroy()
    labelimage = Label(
        root,
        background="#ffffff",
        border=0,
    )
    labelimage.pack(pady=(50, 30))
    labelresulttext = Label(
        root,
        font=("Consolas", 20),
        background="#ffffff",
    )
    labelresulttext.pack()
    if score >= 20:
        img = PhotoImage(file="great.png")
        labelimage.configure(image=img)
        labelimage.image = img
        labelresulttext.configure(text="You Are Excellent !!")
    elif (score >= 10 and score < 20):
        img = PhotoImage(file="ok.png")
        labelimage.configure(image=img)
        labelimage.image = img
        labelresulttext.configure(text="You Can Be Better !!")
    else:
        img = PhotoImage(file="bad.png")
        labelimage.configure(image=img)
        labelimage.image = img
        labelresulttext.configure(text="You Should Work Hard !!")


def calc():
    global indexes, user_answer, answers
    x = 0
    score = 0
    for i in indexes:
        if user_answer[x] == answers[i]:
            score = score + 5
        x += 1
    print(score)
    showresult(score)


ques = 1


def selected():
    global radiovar, user_answer, lblQuestion, r1, r2, r3, r4
    global ques

    x = radiovar.get()
    user_answer.append(x)
    radiovar.set(-1)

    
    correct_answer_index = answers[indexes[ques - 1]]
    if x == correct_answer_index:
        
        if x == 0:
            r1.config(fg="green")
        elif x == 1:
            r2.config(fg="green")
        elif x == 2:
            r3.config(fg="green")
        elif x == 3:
            r4.config(fg="green")
    else:
        
        if x == 0:
            r1.config(fg="red")
        elif x == 1:
            r2.config(fg="red")
        elif x == 2:
            r3.config(fg="red")
        elif x == 3:
            r4.config(fg="red")

        
        if correct_answer_index == 0:
            r1.config(fg="green")
        elif correct_answer_index == 1:
            r2.config(fg="green")
        elif correct_answer_index == 2:
            r3.config(fg="green")
        elif correct_answer_index == 3:
            r4.config(fg="green")

   
    root.after(1000, refresh_question)

def refresh_question():
    global lblQuestion, r1, r2, r3, r4, ques, remaining_time

 
    r1.config(fg="black")
    r2.config(fg="black")
    r3.config(fg="black")
    r4.config(fg="black")

    if ques < 5:
        lblQuestion.config(text=questions[indexes[ques]])
        r1['text'] = answers_choice[indexes[ques]][0]
        r2['text'] = answers_choice[indexes[ques]][1]
        r3['text'] = answers_choice[indexes[ques]][2]
        r4['text'] = answers_choice[indexes[ques]][3]
        ques += 1
        remaining_time = 20
        update_timer_label()
    else:
        calc()
        hide_buttons()  



def save_answer():
    global user_answer, current_question_index, radiovar

 
    x = radiovar.get()
    user_answer[current_question_index] = x

def submit():
    global ques, current_question_index
    selected() 
    ques += 1
    if ques <= 5:
      
        current_question_index = ques - 1
        update_question()
    else:
        calc()
        hide_buttons() 



def update_question():
    global lblQuestion, r1, r2, r3, r4
    lblQuestion.config(text=questions[indexes[ques]])
    r1['text'] = answers_choice[indexes[ques]][0]
    r2['text'] = answers_choice[indexes[ques]][1]
    r3['text'] = answers_choice[indexes[ques]][2]
    r4['text'] = answers_choice[indexes[ques]][3]


def show_result():
    global lblQuestion, r1, r2, r3, r4, timer_lbl
    lblQuestion.destroy()
    r1.destroy()
    r2.destroy()
    r3.destroy()
    r4.destroy()
    timer_lbl.destroy()

    labelimage = Label(
        root,
        background="#ffffff",
        border=0,
    )
    labelimage.pack(pady=(50, 30))
    labelresulttext = Label(
        root,
        font=("Consolas", 20),
        background="#ffffff",
    )
    labelresulttext.pack()
    score = calculate_score()
    if score >= 20:
        img = PhotoImage(file="great.png")
        labelimage.configure(image=img)
        labelimage.image = img
        labelresulttext.configure(text="You Are Excellent !!")
    elif (score >= 10 and score < 20):
        img = PhotoImage(file="ok.png")
        labelimage.configure(image=img)
        labelimage.image = img
        labelresulttext.configure(text="You Can Be Better !!")
    else:
        img = PhotoImage(file="bad.png")
        labelimage.configure(image=img)
        labelimage.image = img
        labelresulttext.configure(text="You Should Work Hard !!")

 
    play_again_btn = Button(
        root,
        text="Play Again",
        font=("Consolas", 12),
        width=10,
        command=restart_quiz,
        background="#2196F3",
        fg="white",
    )
    play_again_btn.pack(pady=10)


def calculate_score():
    global indexes, user_answer, answers
    score = 0
    for i, index in enumerate(indexes):
        if user_answer[i] == answers[index]:
            score += 5
    return score


def restart_quiz():
    global ques, indexes, user_answer
    ques = 1
    indexes = []
    user_answer = []
    gen()
    update_question()


def show_buttons():
    save_btn.grid()
    submit_btn.grid()

def hide_buttons():
    save_btn.grid_remove()
    submit_btn.grid_remove()




remaining_time = 20
timer_running = False

def update_timer_label():
    global remaining_time, timer_lbl
    if remaining_time > 0:
        timer_lbl.config(text=f"Time Left: {remaining_time} seconds")
        remaining_time -= 1
        timer_lbl.after(1000, update_timer_label)  
    else:
        timer_lbl.config(text="Time's up!")
       
        submit()

def startquiz():
    global lblQuestion, r1, r2, r3, r4
    lblQuestion = Label(
        root,
        text=questions[indexes[0]],
        font=("cascadiacode", 16),
        width=500,
        justify="center",
        wraplength=400,
        background="#ffffff",
    )
    lblQuestion.pack(pady=(100, 30))

    

    
    show_buttons()  

    global radiovar
    radiovar = IntVar()
    radiovar.set(-1)

    r1 = Radiobutton(
        root,
        text=answers_choice[indexes[0]][0],
        font=("Times", 12),
        value=0,
        variable=radiovar,
        command=selected,
        background="#ffffff",
    )
    r1.pack(pady=5)

    r2 = Radiobutton(
        root,
        text=answers_choice[indexes[0]][1],
        font=("Times", 12),
        value=1,
        variable=radiovar,
        command=selected,
        background="#ffffff",
    )
    r2.pack(pady=5)

    r3 = Radiobutton(
        root,
        text=answers_choice[indexes[0]][2],
        font=("Times", 12),
        value=2,
        variable=radiovar,
        command=selected,
        background="#ffffff",
    )
    r3.pack(pady=5)

    r4 = Radiobutton(
        root,
        text=answers_choice[indexes[0]][3],
        font=("Times", 12),
        value=3,
        variable=radiovar,
        command=selected,
        background="#ffffff",
    )
    r4.pack(pady=5)

    global timer_lbl
    timer_lbl = Label(
        root,
        text="Time Left: 20 seconds",
        font=("Consolas", 14),
        background="#ffffff",
    )
    timer_lbl.pack()

    remaining_time = 20
    update_timer_label()  # Start the timer countdown



def startIspressed():
    global labelimage, labeltext, lblInstruction, lblRules, btnStart
    labelimage.destroy()
    labeltext.destroy()
    lblInstruction.destroy()
    lblRules.destroy()
    btnStart.destroy()
    gen()
    startquiz()
    show_buttons()


root = tkinter.Tk()
root.title("Quiz")
root.geometry("700x650")
root.config(background="#ffffff")
root.resizable(0, 0)

img1 = PhotoImage(file="Quiz.png")

labelimage = Label(
    root,
    image=img1,
    background="#ffffff",
)
labelimage.pack(pady=(40, 0))

labeltext = Label(
    root,
    text="Master",
    font=("Comic sans MS", 24, "bold"),
    background="#ffffff",
)
labeltext.pack(pady=(0, 50))

img2 = PhotoImage(file="design1.png")

btnStart = Button(
    root,
    image=img2,
    relief=FLAT,
    border=0,
    command=startIspressed,
)
btnStart.pack()


lblInstruction = Label(
    root,
    text="Read The Rules And\nClick Start Once You Are ready",
    background="#ffffff",
    font=("arial", 10),
    justify="center",
)
lblInstruction.pack(pady=(40, 80))

lblRules = Label(
    root,
    text="This quiz contains 10 questions\nYou will get 20 seconds to solve a question\nOnce you select a submit button that will be a final choice\nhence think before you select",
    width=100,
    font=("Bahnschrift", 12),
    background="#C99E73",
    foreground="#623A14",
)
lblRules.pack(pady=0,padx=0)


button_frame = Frame(root, background="#ffffff")
button_frame.pack(pady=10, side=BOTTOM)


save_btn = Button(
    button_frame,
    text="Save",
    font=("Consolas", 12),
    width=10,
    command=save_answer,
    background="#C99E73",
    fg="#623A14",
    state=DISABLED,  
)
submit_btn = Button(
    button_frame,
    text="Submit",
    font=("Consolas", 12),
    width=10,
    command=submit,
    background="#C99E73",
    fg="#623A14",
    state=DISABLED, 
)
save_btn.grid(row=4, column=0, padx=10, pady=50)
submit_btn.grid(row=4, column=1, padx=10, pady=50)
save_btn.grid_remove() 
submit_btn.grid_remove() 

root.mainloop()

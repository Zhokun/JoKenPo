from tkinter import *
from random import *
from tkinter import messagebox
from PIL import Image, ImageTk

app = Tk()
app.title('Jo Ken Po')
app.geometry(f'500x650+{app.winfo_screenwidth() - 1000}+{app.winfo_screenheight() - 800}')
app.resizable(False, False)
app.config(background='white')
app.columnconfigure(1)
app.iconphoto(True, ImageTk.PhotoImage(Image.open('Da.png')))


# ===== fucoes =====


def check_winner():
    if store_score[0] == 2 and (store_score[1] == 0 or store_score[1] == 1):
        if messagebox.askquestion('Continue?', 'Computer Won. Play again?') == 'yes':
            reset()
        else:
            app.destroy()
    elif store_score[1] == 2 and (store_score[0] == 0 or store_score[0] == 1):
        if messagebox.askquestion('Continue?', 'Congratulations, You Won! \n Play again?') == 'yes':
            reset()
        else:
            app.destroy()


def reset():
    store_score[0] = 0
    store_score[1] = 0
    scorecpu.set(store_score[0])
    scoreuser.set(store_score[1])
    l_result.config(image=None)
    computer.config(image=iqmark)


def c_rock():
    c_choice = choice(lst)
    u_choice = lst[0][1]

    if u_choice == c_choice[1]:  # Draw
        l_result.config(image=idraw)
        computer.config(image=c_choice[0])
    elif c_choice[1] == 'scisor':  # Win
        store_score[1] += 1
        scoreuser.set(store_score[1])
        l_result.config(image=ihappy)
        computer.config(image=c_choice[0])
    else:  # Lose
        l_result.config(image=isad)
        computer.config(image=c_choice[0])
        store_score[0] += 1
        scorecpu.set(store_score[0])

    check_winner()


def c_paper():
    c_choice = choice(lst)
    u_choice = lst[1][1]

    if u_choice == c_choice[1]:  # Draw
        l_result.config(image=idraw)
        computer.config(image=c_choice[0])
    elif c_choice[1] == 'rock':  # Win
        store_score[1] += 1
        scoreuser.set(store_score[1])
        l_result.config(image=ihappy)
        computer.config(image=c_choice[0])
    else:  # Lose
        l_result.config(image=isad)
        computer.config(image=c_choice[0])
        store_score[0] += 1
        scorecpu.set(store_score[0])

    check_winner()


def c_scisor():
    c_choice = choice(lst)
    u_choice = lst[2][1]

    if u_choice == c_choice[1]:  # Draw
        l_result.config(image=idraw)
        computer.config(image=c_choice[0])
    elif c_choice[1] == 'paper':  # Win
        store_score[1] += 1
        scoreuser.set(store_score[1])
        l_result.config(image=ihappy)
        computer.config(image=c_choice[0])
    else:  # Lose
        l_result.config(image=isad)
        computer.config(image=c_choice[0])
        store_score[0] += 1
        scorecpu.set(store_score[0])

    check_winner()


# ===== Images List =====
irock_c = PhotoImage(file='images/Rock.png')
ipaper_c = PhotoImage(file='images/Paper.png')
iscisor_c = PhotoImage(file='images/Scisor.png')
iqmark = PhotoImage(file='images/qmark3.png')
idraw = PhotoImage(file='images/Draw.png')
ihappy = PhotoImage(file='images/Happy.png')
isad = PhotoImage(file='images/Happy.png')

lst = [(irock_c, 'rock'), (ipaper_c, 'paper'), (iscisor_c, 'scisor')]
# ===== Images shown =====
irock = PhotoImage(file='images/Rock_u.png')
ipaper = PhotoImage(file='images/Paper_u.png')
iscisor = PhotoImage(file='images/Scisor_u.png')

# ===== Frame to the left =====
frame_computer = Frame(app, padx=15, pady=15)
frame_computer.pack(side=LEFT)
frame_computer.config(background='white')
# ===== Score variable =====
store_score = [0, 0]
scoreuser = StringVar()
scoreuser.set(store_score[1])
scorecpu = StringVar()
scorecpu.set(store_score[0])

# ===== Score Frame =====
score_frame = LabelFrame(frame_computer, text='', pady=10, padx=15)
score_frame.pack(side=TOP)
score_frame.config(background='white')
# ===== Score Label, reslut=====
text = Label(score_frame, text='Game ends at 10 points', font='Verdana, 13', justify='center', pady=10)
text.pack()
text.config(background='white')
l_score_cpu = Label(score_frame, text='Computer: ', font='Verdana, 12')
l_score_cpu.pack(side=LEFT)
l_score_cpu.config(background='white')
l_score_cpu_1 = Label(score_frame, textvariable=scorecpu, font='Verdana, 12')
l_score_cpu_1.pack(side=LEFT)
l_score_cpu_1.config(background='white')
#
l_score_user = Label(score_frame, text='Player:', font='Verdana, 12')
l_score_user.pack(side=LEFT)
l_score_user.config(background='white')
l_score_user_1 = Label(score_frame, text='0', textvariable=scoreuser, font='Verdana, 12')
l_score_user_1.pack(side=LEFT)
l_score_user_1.config(background='white')

# ===== Emoji result =====
l_result = Label(frame_computer, image=None)
l_result.pack(side=BOTTOM)
l_result.config(background='white')

# ===== Computer question mark =====
computer = Button(frame_computer, image=iqmark, borderwidth=0)
computer.pack()
computer.config(background='white')

# ===== Buttons Choice to the right =====
frame_user = Frame(app, padx=15)
frame_user.pack(side=RIGHT)
frame_user.config(background='white')
rock = Button(frame_user, image=irock, borderwidth=0, command=c_rock)
rock.pack()
rock.config(background='white')
paper = Button(frame_user, image=ipaper, borderwidth=0, command=c_paper)
paper.pack()
paper.config(background='white')
scisor = Button(frame_user, image=iscisor, borderwidth=0, command=c_scisor)
scisor.pack()
scisor.config(background='white')

app.mainloop()

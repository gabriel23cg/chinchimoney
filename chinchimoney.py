from tkinter import *
import random

def add_coin():
	if (user_coin.get()<3):
		user_coin.set(user_coin.get()+1)
	set_coin()
def subtract_coin():
	if (match.get()==1):	
		if (user_coin.get()>1):
			user_coin.set(user_coin.get()-1)
	else:
		if (user_coin.get()>0):
			user_coin.set(user_coin.get()-1)

	set_coin()
def set_coin():
	if(user_coin.get()==0):
		image_label.img = PhotoImage(file="user0.gif")
		image_label.config(image=image_label.img)
	elif(user_coin.get()==1):
		image_label.img = PhotoImage(file="user1.gif")
		image_label.config(image=image_label.img)
	elif(user_coin.get()==2):
		image_label.img = PhotoImage(file="user2.gif")
		image_label.config(image=image_label.img)
	elif(user_coin.get()==3):
		image_label.img = PhotoImage(file="user3.gif")
		image_label.config(image=image_label.img)
	image_label.pack()

def set_stage():
	if(stage.get()==0):
		button_down.config(state=NORMAL)
		button_up.config(state=NORMAL)
		button_ok.config(text="Aceptar")
		label_match.set("Partida {} \n {} - {}".format(match.get(),user_winnings.get(),computer_winnings.get()))
		label_stage.set("Selecciona la cantidad de monedas")
	elif(stage.get()==1 and match.get()%2==1):
		button_down.config(state=NORMAL)
		button_up.config(state=NORMAL)
		user_choice.set(user_coin.get())
		set_computer_choice()
		label_stage.set("Selecciona las monedas que cres que tiene Computer")
	elif(stage.get()==2 and match.get()%2==1):
		button_down.config(state=DISABLED)
		button_up.config(state=DISABLED)
		user_predict.set(user_coin.get()+user_choice.get())
		set_computer_predict()
		label_stage.set("Computer dice: En total hay {} monedas".format(computer_predict.get()))
	elif(stage.get()==1 and match.get()%2==0):
		button_down.config(state=DISABLED)
		button_up.config(state=DISABLED)
		user_choice.set(user_coin.get())
		set_computer_predict()
		label_stage.set("Computer dice: En total hay {} monedas".format(computer_predict.get()))
	elif(stage.get()==2 and match.get()%2==0):
		button_down.config(state=NORMAL)
		button_up.config(state=NORMAL)
		label_stage.set("Selecciona las monedas que cres que tiene Computer")
	elif(stage.get()==3):
		button_down.config(state=DISABLED)
		button_up.config(state=DISABLED)
		user_predict.set(user_coin.get()+user_choice.get())
		real_coin.set(user_choice.get()+computer_choice.get())
		showuser_coin()
		show_computer_coin()
		label_stage.set("Había {} monedas!".format(real_coin.get()))
	elif(stage.get()==4):
		button_down.config(state=DISABLED)
		button_up.config(state=DISABLED)
		set_winner()
		label_stage.set("{} ha ganado.".format(label_winner.get()))
		image_computer.img = PhotoImage(file="hc.gif")
		image_computer.config(image=image_computer.img)
		label_match.set("Partida {} \n {} - {}".format(match.get(),user_winnings.get(),computer_winnings.get()))
		game_over()
		match.set(match.get()+1)
		stage.set(-1)

def add_stage():
	stage.set(stage.get()+1)
	set_stage()
	button_up.pack()
	button_down.pack()

def set_computer_choice():
	if (match.get()==1):
		computer_choice.set(random.randrange(1,4))
	else:
		computer_choice.set(random.randrange(0,4))

def set_computer_predict():
	if (match.get()%2==1):
		if (user_predict.get()==0):
			computer_predict.set(computer_choice.get()+0)
		elif (user_predict.get()==1):
			computer_predict.set(computer_choice.get()+random.randrange(0,2))
		elif (user_predict.get()==2):
			computer_predict.set(computer_choice.get()+random.randrange(0,3))
		elif (user_predict.get()==3):
			computer_predict.set(computer_choice.get()+random.randrange(0,4))
		elif (user_predict.get()==4):
			computer_predict.set(computer_choice.get()+random.randrange(1,4))
		elif (user_predict.get()==5):
			computer_predict.set(computer_choice.get()+random.randrange(2,4))
		elif (user_predict.get()==6):
			computer_predict.set(computer_choice.get()+3)
	elif (match.get()%2==0):
		computer_predict.set(computer_choice.get()+random.randrange(0,4))

def set_winner():
	if (user_predict.get()==real_coin.get() and user_predict.get()!=computer_predict.get()):
		label_winner.set("Usuario")
		user_winnings.set(user_winnings.get()+1)
	elif (computer_predict.get()==real_coin.get() and user_predict.get()!=computer_predict.get()):
		label_winner.set("Computer")
		computer_winnings.set(computer_winnings.get()+1)
	else:
		label_winner.set("Nadie")

def show_computer_coin():
	if(computer_choice.get()==0):
		image_computer.img = PhotoImage(file="user0.gif")
		image_computer.config(image=image_computer.img)
	elif(computer_choice.get()==1):
		image_computer.img = PhotoImage(file="user1.gif")
		image_computer.config(image=image_computer.img)
	elif(computer_choice.get()==2):
		image_computer.img = PhotoImage(file="user2.gif")
		image_computer.config(image=image_computer.img)
	elif(computer_choice.get()==3):
		image_computer.img = PhotoImage(file="user3.gif")
		image_computer.config(image=image_computer.img)
	image_computer.pack()

def showuser_coin():
	if(user_choice.get()==0):
		image_label.img = PhotoImage(file="user0.gif")
		image_label.config(image=image_label.img)
		user_coin.set(0)
	elif(user_choice.get()==1):
		image_label.img = PhotoImage(file="user1.gif")
		image_label.config(image=image_label.img)
		user_coin.set(1)
	elif(user_choice.get()==2):
		image_label.img = PhotoImage(file="user2.gif")
		image_label.config(image=image_label.img)
		user_coin.set(2)
	elif(user_choice.get()==3):
		image_label.img = PhotoImage(file="user3.gif")
		image_label.config(image=image_label.img)
		user_coin.set(3)
	image_label.pack()

def game_over():
	if (user_winnings.get()==5 or computer_winnings.get()==5):
		button_ok.config(text="Nueva Partida")
		button_ok.pack()
		computer_winnings.set(0)
		user_winnings.set(0)
		match.set(0)


root = Tk()

user_coin = IntVar()
match = IntVar()
stage = IntVar()
user_choice = IntVar()
user_predict = IntVar()
computer_choice = IntVar()
computer_predict = IntVar()
real_coin = IntVar()
user_winnings = IntVar()
computer_winnings = IntVar()
label_stage = StringVar()
label_match = StringVar()
label_winner = StringVar()

label_stage.set("Selecciona la cantidad de monedas")
user_winnings.set(0)
computer_winnings.set(0)
stage.set(0) 
match.set(1)
user_coin.set(1)
label_match.set("Partida {} \n {} - {}".format(match.get(),user_winnings.get(),computer_winnings.get()))
root.title("Chinchimoney")
root.resizable(0,0)
root.iconbitmap('icon.ico')

title_image = Frame(root)
title_image.grid(row=0,column=0,columnspan=2)
title_image.config(width= 256, height=64)
title_image.config(bd=5)
score_board = Frame(root)
score_board.grid(row=1,column=0,columnspan=2)
score_board.config(width= 256, height=32)
score_board.config(bd=5)
display_text = Frame(root)
display_text.grid(row=2,column=0,columnspan=2)
display_text.config(width= 256, height=32)
display_text.config(bd=3)
user_up = Frame(root)
user_up.grid(row=3,column=0)
user_up.config(width= 128, height=32)
user_up.config(bd=5)
user_display = Frame(root)
user_display.grid(row=4,column=0)
user_display.config(width= 128, height=192)
computer_display = Frame(root)
computer_display.grid(row=4,column=1)
computer_display.config(width= 128, height=192)
user_down = Frame(root)
user_down.grid(row=5,column=0)
user_down.config(width= 128, height=32)
user_down.config(bd=5)
button_frame = Frame(root)
button_frame.grid(row=6,column=0,columnspan=2)
button_frame.config(width= 256, height=32)

button_up = Button(user_up,text="Más",command=add_coin)
button_down = Button(user_down,text="Menos",command=subtract_coin)
button_up.pack()
button_down.pack()
Label(button_frame).pack()
button_ok = Button(button_frame,text="Aceptar",command=add_stage)
button_ok.pack()
Label(button_frame).pack()
userImage = PhotoImage(file="user1.gif")
image_label = Label(user_display, image=userImage)
image_label.pack()
computer_image = PhotoImage(file="hc.gif")
image_computer = Label(computer_display, image=computer_image)
image_computer.pack()
header = PhotoImage(file="header.gif")
Label(title_image, image=header).pack()
Label(display_text, textvariable=label_stage).pack()
Label(score_board, textvariable=label_match).pack()
root.mainloop()

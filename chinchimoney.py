from tkinter import *
import random

def add_coin():
	if (coin_number.get()<3):
		coin_number.set(coin_number.get()+1)
	show_coin(image_label, coin_number.get(), "user")

def subtract_coin():
	if (match.get()==1):	
		if (coin_number.get()>1):
			coin_number.set(coin_number.get()-1)
	else:
		if (coin_number.get()>0):
			coin_number.set(coin_number.get()-1)

	show_coin(image_label, coin_number.get(), "user")

def show_coin(label, coin_number, display):
    image_name = "{}{}.gif".format(display,coin_number)
    label.img = PhotoImage(file=image_name)
    label.config(image=label.img)

def enable_selection():
	button_down.config(state=NORMAL)
	button_up.config(state=NORMAL)

def disable_selection():
	button_down.config(state=DISABLED)
	button_up.config(state=DISABLED)

def set_stage():
	if(stage.get()==0):
		enable_selection()
		button_ok.config(text="Aceptar")
		label_match.set("Partida {} \n {} - {}".format(match.get(),user_winnings.get(),computer_winnings.get()))
		label_stage.set("Selecciona la cantidad de monedas")
	elif(stage.get()==1 and match.get()%2==1):
		enable_selection()
		user_choice.set(coin_number.get())
		set_computer_choice()
		label_stage.set("Selecciona las monedas que cres que tiene Computer")
	elif(stage.get()==2 and match.get()%2==1):
		disable_selection()
		user_predict.set(coin_number.get()+user_choice.get())
		set_computer_predict()
		label_stage.set("Computer dice: En total hay {} monedas".format(computer_predict.get()))
	elif(stage.get()==1 and match.get()%2==0):
		disable_selection()
		user_choice.set(coin_number.get())
		set_computer_predict()
		label_stage.set("Computer dice: En total hay {} monedas".format(computer_predict.get()))
	elif(stage.get()==2 and match.get()%2==0):
		enable_selection()
		label_stage.set("Selecciona las monedas que cres que tiene Computer")
	elif(stage.get()==3):
		disable_selection()
		user_predict.set(coin_number.get()+user_choice.get())
		real_coin.set(user_choice.get()+computer_choice.get())
		show_user_choice()
		show_computer_coin()
		label_stage.set("Había {} monedas!".format(real_coin.get()))
	elif(stage.get()==4):
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

def set_computer_predict():		#Computer prediction is based on the information gived by the user,
								#eg. if user said 6 coins, the only posibility of that is if user had 3 coins
								#so computer will predict 3 plus the coins that computer has chosen.
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
	show_coin(image_computer, computer_choice.get(), "computer")

def show_user_choice():
	show_coin(image_label, user_choice.get(), "user")
	coin_number.set(user_choice.get())

def game_over():
	if (user_winnings.get()==5 or computer_winnings.get()==5):
		button_ok.config(text="Nueva Partida")
		button_ok.pack()
		computer_winnings.set(0)
		user_winnings.set(0)
		match.set(0)


root = Tk()
root.title("Chinchimoney")
root.resizable(0,0)	#window cant be resizable.
root.iconbitmap('icon.ico')

coin_number = IntVar()	#Number of current coins on the users display.
match = IntVar()
stage = IntVar()	#stages through the match.
user_choice = IntVar()	#number of coins selected by user.
user_predict = IntVar()	#number of total coins predicted by user.
computer_choice = IntVar() #number of coins selected by the computer.
computer_predict = IntVar()	#number of total coins predicted by the computer.
real_coin = IntVar()	#the real amount of coins, coins in user plus coins in the computer.
user_winnings = IntVar()	#winning counter.
computer_winnings = IntVar()	#winning counter also.
label_stage = StringVar()	#string that guides the user through all stages.
label_match = StringVar()	#string that shows the match and the scoreboard.
label_winner = StringVar()	#string that shows the winner.

label_stage.set("Selecciona la cantidad de monedas") #setting variables to the start of the game.
user_winnings.set(0)
computer_winnings.set(0)
stage.set(0) 
match.set(1)
coin_number.set(1)
label_match.set("Partida {} \n {} - {}".format(match.get(),user_winnings.get(),computer_winnings.get()))

#here starts the definition, by frames, of the GUI.
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
#here ends.

#Initialiting GUI objets.
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

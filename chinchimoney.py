from tkinter import *
def addCoin():
	if (userCoin.get()<3):
		userCoin.set(userCoin.get()+1)
	setCoin()
def subtractCoin():
	if (match.get()==1):	
		if (userCoin.get()>1):
			userCoin.set(userCoin.get()-1)
	else:
		if (userCoin.get()>0):
			userCoin.set(userCoin.get()-1)

	setCoin()
def setCoin():
	if(userCoin.get()==0):
		image_label.img = PhotoImage(file="user0.gif")
		image_label.config(image=image_label.img)
	elif(userCoin.get()==1):
		image_label.img = PhotoImage(file="user1.gif")
		image_label.config(image=image_label.img)
	elif(userCoin.get()==2):
		image_label.img = PhotoImage(file="user2.gif")
		image_label.config(image=image_label.img)
	elif(userCoin.get()==3):
		image_label.img = PhotoImage(file="user3.gif")
		image_label.config(image=image_label.img)
	image_label.pack()

def setStage():
	if(stage.get()==0):
		labelStage.set("Selecciona la cantidad de monedas")
	elif(stage.get()==1 and match.get()%2==1):
		labelStage.set("Selecciona las monedas que cres que tiene Computer")
	elif(stage.get()==2 and match.get()%2==1):
		labelStage.set("Computer dice: En total hay X monedas")
	elif(stage.get()==1 and match.get()%2==0):
		labelStage.set("Computer dice: En total hay X monedas")
	elif(stage.get()==2 and match.get()%2==0):
		labelStage.set("Selecciona las monedas que cres que tiene Computer")
	elif(stage.get()==3):
		labelStage.set("Había X monedas!")
	elif(stage.get()==4):
		labelStage.set("X ha ganado.")
		match.set(match.get()+1)
		stage.set(-1)

def addStage():
	stage.set(stage.get()+1)
	setStage()


root = Tk()
userCoin = IntVar()
computerCoin = IntVar()
match = IntVar()
stage = IntVar()
labelStage = StringVar()
labelStage.set("Selecciona la cantidad de monedas")
stage.set(0) 
match.set(1)
userCoin.set(1)
root.title("Chinchimoney")
root.resizable(0,0)
#root.iconbitmap('icon.ico') #icono
titleImage = Frame(root)
titleImage.grid(row=0,column=0,columnspan=2)
titleImage.config(width= 256, height=64)
titleImage.config(bd=5)
scoreBoard = Frame(root)
scoreBoard.grid(row=1,column=0,columnspan=2)
scoreBoard.config(width= 256, height=32)
scoreBoard.config(bd=3,relief="sunken")
displayText = Frame(root)
displayText.grid(row=2,column=0,columnspan=2)
displayText.config(width= 256, height=32)
displayText.config(bd=3)
userUP = Frame(root)
userUP.grid(row=3,column=0)
userUP.config(width= 128, height=32)
userUP.config(bd=5)
userDisplay = Frame(root)
userDisplay.grid(row=4,column=0)
userDisplay.config(width= 128, height=192)
#userDisplay.config(bd=3,relief="sunken")
computerDisplay = Frame(root)
computerDisplay.grid(row=4,column=1)
computerDisplay.config(width= 128, height=192)
#computerDisplay.config(bd=3,relief="sunken")
userDOWN = Frame(root)
userDOWN.grid(row=5,column=0)
userDOWN.config(width= 128, height=32)
userDOWN.config(bd=5)
buttonFrame = Frame(root)
buttonFrame.grid(row=6,column=0,columnspan=2)
buttonFrame.config(width= 256, height=32)
#buttonFrame.config(bd=3,relief="sunken")

Button(userUP,text="Más",command=addCoin).pack()
Button(userDOWN,text="Menos",command=subtractCoin).pack()
Label(buttonFrame).pack()
Button(buttonFrame,text="Aceptar",command=addStage).pack()
Label(buttonFrame).pack()
userImage = PhotoImage(file="user1.gif")
image_label = Label(userDisplay, image=userImage)
image_label.pack()
computerImage = PhotoImage(file="hc.gif")
Label(computerDisplay, image=computerImage).pack()
header = PhotoImage(file="header.gif")
Label(titleImage, image=header).pack()
Label(displayText, textvariable=labelStage).pack()
# fin
root.mainloop()




### notas: 10 9 9 10 10 6
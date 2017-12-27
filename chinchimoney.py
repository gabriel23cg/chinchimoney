from tkinter import *
def addCoin():
	if (userCoin.get()<=3):
		userCoin.set(userCoin.get()+1)
	setCoin()
def subtractCoin():
	if (userCoin.get()>=0):
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
	#Label(userDisplay, image=userImage).pack()
	image_label.pack()

root = Tk()
userCoin = IntVar()
userCoin.set(0)
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
displayText.config(bd=3,relief="sunken")
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
Button(buttonFrame,text="Aceptar",command="").pack()
Label(buttonFrame).pack()
userImage = PhotoImage(file="user0.gif")
image_label = Label(userDisplay, image=userImage)
image_label.pack()
computerImage = PhotoImage(file="computer3.gif")
Label(computerDisplay, image=computerImage).pack()
header = PhotoImage(file="header.gif")
Label(titleImage, image=header).pack()
# fin
root.mainloop()




### notas: 10 9 9 10 10 6
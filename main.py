from tkinter import *
import random

def new_game():
    global player

    player=random.choice(players)
    label.config(text=player +" turn")

    for row in range(3):
        for column in range(3):
            buttons[row][column].config(text="",bg="#F0F0F0")

def next_turn(row,column):
    global player

    if buttons[row][column]['text']=="" and winner() is False:

        if player==players[0]:
            buttons[row][column]['text']=player

            if winner() is False:
                player=players[1]
                label.config(text=players[1] + " turn")
            elif winner() is True:
                label.config(text=players[0] + " wins")
            elif winner() == "Tie":
                label.config(text="Tie")
        else:
            buttons[row][column]['text']=player

            if winner() is False:
                player=players[0]
                label.config(text=players[0] + " turn")
            elif winner() is True:
                label.config(text=players[1] + " wins")
            elif winner() == "Tie":
                label.config(text="Tie")
    

def winner():
     for row in range(3):
         if buttons[row][0]['text']==buttons[row][1]['text']==buttons[row][2]['text']!="":
             buttons[row][0].config(bg='green')
             buttons[row][1].config(bg='green')
             buttons[row][2].config(bg='green')
             return True
         
     for column in range(3):
         if buttons[0][column]['text']==buttons[1][column]['text']==buttons[2][column]['text']!= "":
            buttons[0][column].config(bg='green')
            buttons[1][column].config(bg='green')
            buttons[2][column].config(bg='green') 
            return True
     
     if buttons[0][0]['text']==buttons[1][1]['text']==buttons[2][2]['text'] != "":
         buttons[0][0].config(bg='green')
         buttons[1][1].config(bg='green')
         buttons[2][2].config(bg='green')
         return True
     
     elif buttons[0][2]['text']==buttons[1][1]['text']==buttons[2][0]['text'] != "":
         buttons[0][2].config(bg='green')
         buttons[1][1].config(bg='green')
         buttons[2][0].config(bg='green')
         return True
     
     elif empty_space()==False:
         for row in range(3):
             for column in range(3):
                 buttons[row][column].config(bg='yellow')
         return("Tie")
     else:
         return False
     
def empty_space():
    spaces=9
    for row in range(3):
        for column in range(3):
            if buttons[row][column]['text']!="":
                spaces-=1
             
    
    if spaces==0:
        return False
    else:
       return True



window=Tk()
window.title("Tic-Tac-Toe")
# window.geometry("500x500")
players=["x","o"]
player=random.choice(players)
buttons=[[0,0,0],
         [0,0,0],
         [0,0,0]]
label=Label(window,text=player  + " turn",font=("ink free","40"))
label.pack(side=TOP)
restart_button=Button(window,text="restart",font=("ink free","20"),command=new_game)
restart_button.pack(side=TOP)

frame=Frame(window)
frame.pack()

for row in range(3):
    for column in range(3):
        buttons[row][column]=Button(frame,text="",width=7,height=3,font=("free ink","30"),
                                    command=lambda row=row,column=column :next_turn(row,column))
        buttons[row][column].grid(row=row,column=column)


window.mainloop()
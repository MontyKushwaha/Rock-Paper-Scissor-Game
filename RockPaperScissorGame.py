#Rock,Paper,Scissor Game
import random
l=["Rock","Paper","Scissor"]
while True:
    Ccount=0
    Ucount=0
    UC=int(input('''Do You Want To Start The Game...
    1.Yes
    2.No
    \nEnter Choice: '''))
    if UC==1:
        for a in range(1,6):
            UserInput=int(input('''
             1.Rock
             2.Paper
             3.Scissor  
             \nEnter Choice: '''))
            if UserInput==1:
                uchoice="Rock"
            elif UserInput==2:
                uchoice="Paper"
            elif UserInput==3:
                uchoice="Scissor"
            else:
                print("Your Choice is Invalid")
                break
            Cchoice=random.choice(l)
            if Cchoice==uchoice:
                print("Computer Choice",Cchoice)
                print("User Choice",uchoice)
                print("Game Draw")
                Ucount=Ucount+1
                Ccount=Ccount+1
            elif (uchoice=="Rock" and Cchoice=="Scissor") or (uchoice=="Paper" and Cchoice=="Rock") or (uchoice=="Scissor" and Cchoice=="Paper"):
                print("Computer Choice",Cchoice)
                print("User Choice",uchoice)
                print("User Win")
                Ucount=Ucount+1
            else:
                print("Computer Choice",Cchoice)
                print("User Choice",uchoice)
                print("Computer Win")
                Ccount=Ccount+1   
        print("\n")
        print("The Game is Over")
        print("\n")
        print("User Count: ",Ucount)
        print("Computer Count: ",Ccount)         
        if Ucount>Ccount:
            print("User Won The Match")
        elif Ccount>Ucount:
            print("Computer Won The Match")
        else:
            print("No One Won")
        print("\n")
    else:
        break
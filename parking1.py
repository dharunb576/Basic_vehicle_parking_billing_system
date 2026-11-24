from datetime import datetime
import random

print("")
print("")

cn=input("Enter Vehicle No.: ")
print("")

print("1.FOR PARK IN")
print("2.FOR PARK OUT")
print("")
n=int(input("Enter Parking Option: "))
print("")

def parkin():
        # np=input("Enter No.: ")

        idt=datetime.now().time()
        print("Entering Time: ",idt.strftime("%H:%M:%S"))
        print("Vehicle ID: ",cn)
        print("")
        intim=idt.strftime("%H:%M:%S")
        return slotno()
        

def parkout():
        # op=input("Enter No.: ")
        odt=datetime.now().time()
        print("Exiting Time: ",odt.strftime("%H:%M:%S"))
        outtim=odt.strftime("%H:%M:%S")
        print("Vehicle ID: ",cn)
        print("")
        amt=[30,50,70,100]
        bill=random.choice(amt)
        print("Total Bill Amount:",bill)
        print("")
        print("  \\\\ Thank You ////")
        print("\\\\\ Visit Again ////")
        

def select(Op):
        match Op:
                case 1:
                        print("Vehicle is Entering")
                        print("                     ")
                        return parkin()
                case 2:
                        print("Vehicle is Exiting")
                        print("                     ")
                        return parkout()


def slotno():
        print("Slot Assigned")
        num = random.randint(1,50)
        print("Slot Number:",num)
        print("                     ")
        print("                     ")
        print("       ~~  Vehicle Registered  ~~          ")
        print("~~ Generating these information as Token ~~")
        print("     ~~~ Please Collect Your Token ~~~     ")
        
head=select(n)
print("")
print("")
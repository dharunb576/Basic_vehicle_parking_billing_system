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

# def parkin():
#         # np=input("Enter No.: ")

#         idt=datetime.now().time()
#         print("Entering Time: ",idt.strftime("%H:%M:%S"))
#         enttime=idt.strftime("%H:%M:%S")
#         print("Vehicle ID: ",cn)
#         print("")
#         intim=idt.strftime("%H:%M:%S")
#         return slotno()
#         return enttime



def parkin(cn):
    if vehicle_no in parking_lot:
        print("Vehicle already parked.")
    else:
        entry_time = datetime.datetime.now()
        parking_lot[vehicle_no] = entry_time
        print(f"Vehicle {vehicle_no} entered at {entry_time.strftime('%H:%M:%S')}.")
        

# def parkout():
#         # op=input("Enter No.: ")
#         odt=datetime.now().time()
#         print("Exiting Time: ",odt.strftime("%H:%M:%S"))
#         endtime=odt.strftime("%H:%M:%S")
#         print("Vehicle ID: ",cn)
#         print("")
#         amt=[30,50,70,100]
#         bill=random.choice(amt)
#         print("Total Bill Amount:",bill)
#         print("")
#         print("  \\\\ Thank You ////")
#         print("\\\\\ Visit Again ////")
#         return endtime


def parkout(cn):
    if vehicle_no not in parking_lot:
        print("Vehicle not found in parking lot.")
    else:
        exit_time = datetime.datetime.now()
        entry_time = parking_lot.pop(vehicle_no)  # Remove after exit
        duration = exit_time - entry_time
        hours_parked = duration.total_seconds() / 3600
        cost = round(hours_parked * COST_PER_HOUR, 2)
        print(f"Vehicle {vehicle_no} exited at {exit_time.strftime('%H:%M:%S')}.")
        print(f"Duration: {hours_parked:.2f} hours")
        print(f"Total cost: ₹{cost}")



# def allot():
#     slot=[]
#     n=n+1
#     for i in range(0,n):
#         i=i+1
#         val=cn[i]
#         slot.append(val)


def select(Op):
        match Op:
                case 1:
                        print("Vehicle is Entering")
                        print("")
                        return parkin()
                case 2:
                        print("Vehicle is Exiting")
                        print("")
                        return parkout()


def slotno():
        print("Slot Assigned")
        num = random.randint(1,50)
        print("Slot Number:",num)
        print("")
        print("")
        print("       ~~  Vehicle Registered  ~~          ")
        print("~~ Generating these information as Token ~~")
        print("     ~~~ Please Collect Your Token ~~~     ")
        
head=select(n)
print("")
print("")
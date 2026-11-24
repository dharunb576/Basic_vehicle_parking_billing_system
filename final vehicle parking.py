from datetime import datetime
import random
while True:
    # Initialize slot tracking
    total_slots = 50
    available_slots = list(range(1, total_slots + 1))
    assigned_slots = {}  # Stores: {vehicle_no: slot_number}

    print("")
    print("")

    cn = input("Enter Vehicle No.: ")
    print("")

    print("1.FOR PARK IN")
    print("2.FOR PARK OUT")
    print("")
    n = int(input("Enter Parking Option: "))
    print("")

    def parkin():
        if not available_slots:
            print("Sorry, Parking is Full!")
            return

        idt = datetime.now().time()
        print("Entering Time: ", idt.strftime("%H:%M:%S"))
        print("Vehicle ID: ", cn)
        print("")
        return slotno()

    def parkout():
        odt = datetime.now().time()
        print("Exiting Time: ", odt.strftime("%H:%M:%S"))
        outtim = odt.strftime("%H:%M:%S")
        print("Vehicle ID: ", cn)
        print("")

        slot = assigned_slots.get(cn)
        if slot:
            available_slots.append(slot)
            available_slots.sort()  # Optional: maintain slot order
            del assigned_slots[cn]
            print("Slot", slot, "is now free.")
        else:
            print("No slot was assigned to this vehicle.")

        amt = [30, 50, 70, 100]
        bill = random.choice(amt)
        print("Total Bill Amount:", bill)
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
            case _:
                print("Invalid Option")

    def slotno():
        slot = available_slots.pop(0)  # Assign first available slot
        assigned_slots[cn] = slot
        print("Slot Assigned")
        print("Slot Number:", slot)
        print("                     ")
        print("                     ")
        print("       ~~  Vehicle Registered  ~~          ")
        print("~~ Generating these information as Token ~~")
        print("     ~~~ Please Collect Your Token ~~~     ")

    head = select(n)



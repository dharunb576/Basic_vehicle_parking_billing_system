    
    
    
    
from datetime import datetime
import random
while True:
    print("\n\n")

    vehicle_db = {}  # Dictionary to store entry time of each vehicle

    cn = input("Enter Vehicle No.: ")
    print("")

    print("1. FOR PARK IN")
    print("2. FOR PARK OUT")
    print("")
    n = int(input("Enter Parking Option: "))
    print("")


    def parkin():
        idt = datetime.now()
        entry_time = idt
        vehicle_db[cn] = entry_time  # Store the entry time in dictionary

        print("Vehicle is Entering...\n")
        print("Entering Time: ", entry_time.strftime("%H:%M:%S"))
        print("Vehicle ID: ", cn)
        print("")

        slotno()
        print("       ~~  Vehicle Registered  ~~          ")
        print("~~ Generating these information as Token ~~")
        print("     ~~~ Please Collect Your Token ~~~     ")

        return entry_time


    def parkout():
        print("Vehicle is Exiting...\n")

        if cn not in vehicle_db:
            print("Error: Vehicle not found in the parking lot!")
            return

        exit_time = datetime.now()
        entry_time = vehicle_db.pop(cn)  # Remove from dictionary after exit
        duration = exit_time - entry_time
        minutes = duration.total_seconds() / 60

        print("Entering Time: ", entry_time.strftime("%H:%M:%S"))
        print("Exiting Time : ", exit_time.strftime("%H:%M:%S"))
        print("Total Time   : {:.2f} minutes".format(minutes))
        print("Vehicle ID   : ", cn)
        print("")

        rate_per_minute = 2  # ₹2 per minute
        bill = round(minutes * rate_per_minute)
        print("Total Bill Amount: ₹", bill)
        print("")
        print("  \\\\ Thank You ////")
        print("\\\\\ Visit Again ////")

        return exit_time


    def select(option):
        if option == 1:
            return parkin()
        elif option == 2:
            return parkout()
        else:
            print("Invalid Option")


    def slotno():
        print("Slot Assigned")
        num = random.randint(1, 50)
        print("Slot Number:", num)
        print("")


    # Run the selection
    select(n)

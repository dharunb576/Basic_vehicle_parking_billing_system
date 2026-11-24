from datetime import datetime
import time

# Configuration
total_slots = 10
available_slots = list(range(1, total_slots + 1))
parking_data = {}  # Format: {vehicle_no: {"slot": slot, "entry_time": time}}

# Billing
rate_per_minute = 0.25  # ₹0.25 per minute
cgst_rate = 0.09
sgst_rate = 0.09

def park_in():
    if not available_slots:
        print("No slots available.")
        return

    vehicle_no = input("Enter Vehicle Number: ").upper()
    if vehicle_no in parking_data:
        print("Vehicle is already parked.")
        return

    slot = available_slots.pop(0)
    entry_time = datetime.now()

    parking_data[vehicle_no] = {
        "slot": slot,
        "entry_time": entry_time
    }

    print(f"\nVehicle No: {vehicle_no}")
    print(f"Entry Time: {entry_time.strftime('%Y-%m-%d %H:%M:%S')}")
    print(f"Slot Assigned: {slot}")
    print("Vehicle parked successfully.\n")

def park_out():
    vehicle_no = input("Enter Vehicle Number: ").upper()
    if vehicle_no not in parking_data:
        print("Vehicle not found in parking lot.")
        return

    exit_time = datetime.now()
    entry_time = parking_data[vehicle_no]["entry_time"]
    slot = parking_data[vehicle_no]["slot"]

    # Calculate duration
    duration = exit_time - entry_time
    minutes = duration.total_seconds() / 60
    base_amount = minutes * rate_per_minute
    cgst = base_amount * cgst_rate
    sgst = base_amount * sgst_rate
    total_amount = base_amount + cgst + sgst

    # Remove vehicle from parking
    del parking_data[vehicle_no]
    available_slots.append(slot)
    available_slots.sort()

    # Time display
    hours, rem = divmod(duration.total_seconds(), 3600)
    mins = rem // 60

    print("\n=========== BILL RECEIPT ===========")
    print(f"Vehicle No      : {vehicle_no}")
    print(f"Slot Number     : {slot}")
    print(f"Entry Time      : {entry_time.strftime('%Y-%m-%d %H:%M:%S')}")
    print(f"Exit Time       : {exit_time.strftime('%Y-%m-%d %H:%M:%S')}")
    print(f"Duration        : {int(hours)} Hr {int(mins)} Min")
    print("------------------------------------")
    print(f"Base Amount     : ₹{base_amount:.2f}")
    print(f"CGST (9%)       : ₹{cgst:.2f}")
    print(f"SGST (9%)       : ₹{sgst:.2f}")
    print(f"Total Amount    : ₹{total_amount:.2f}")
    print("Thank You! Visit Again.")
    print("====================================\n")

def display_status():
    print("\n------ PARKING LOT STATUS ------")
    print(f"Total Slots   : {total_slots}")
    print(f"Available     : {len(available_slots)}")
    print(f"Occupied      : {total_slots - len(available_slots)}\n")
    print("Parked Vehicles:")
    for vehicle, info in parking_data.items():
        print(f"{vehicle} -> Slot {info['slot']} | In @ {info['entry_time'].strftime('%H:%M:%S')}")
    print("----------------------------------\n")

# Main menu
def menu():
    while True:
        print("====== VEHICLE PARKING SYSTEM ======")
        print("1. Park In")
        print("2. Park Out")
        print("3. View Parking Status")
        print("4. Exit")
        choice = input("Enter your choice: ")

        if choice == '1':
            park_in()
        elif choice == '2':
            park_out()
        elif choice == '3':
            display_status()
        elif choice == '4':
            print("Exiting... Thank you!")
            break
        else:
            print("Invalid choice. Try again.\n")

menu()
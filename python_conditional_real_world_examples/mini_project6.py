guest_name=input("Enter your name: ")
room_type=int(input("Enter room type: (1.Standard, 2.Deluxe, 3.Suite): "))
nights=int(input("Enter number of nights: "))
chosen_room=""
per_night_cost=0
discount=0
final_cost=0
if(guest_name.strip()!="" and room_type in [1,2,3] and nights>0):
    if(room_type==1):
        chosen_room="Standard"
        per_night_cost=2000
    elif(room_type==2):
        chosen_room="Deluxe"
        per_night_cost=350
    elif(room_type==3):
        chosen_room="Suite"
        per_night_cost=6000

    if(5<=nights<10):
        discount=((nights*per_night_cost)/100)*10
    if(nights>=10):
        discount=((nights*per_night_cost)/100)*20
    final_cost=(per_night_cost*nights)-discount
    print("Name of the guest = ",guest_name)
    print("Type of the room selected = ",room_type)
    print("Number of nights stayed = ",nights)
    print("Room cost per night = ",per_night_cost)
    print("Discount = ",discount)
    print("Final booking amount = ",final_cost)
    
else:
    if(guest_name.strip()==""):
        print("Invalid guest name")
    if(nights<=0):
        print("Invalid number of nights")
    if(room_type not in [1,2,3]):
        print("Invalid room type")

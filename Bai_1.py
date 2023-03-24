def calculate_taxi_fare(vehicle_type, num_kilometers, waiting_time):
    if vehicle_type == 4:
        opening_price = 11000
        within_30km_price = 15300
        beyond_30km_price = 12100
        opening_distance = 0.8
    elif vehicle_type == 7:
        opening_price = 12000
        within_30km_price = 16100
        beyond_30km_price = 13800
        opening_distance = 0.8
    else:
        return "Invalid vehicle type"

    if num_kilometers <= opening_distance:
        travel_money = opening_price
    elif num_kilometers <= 30:
        travel_money = opening_price + (num_kilometers - opening_distance) * within_30km_price
    else:
        travel_money = opening_price + 29 * within_30km_price + (num_kilometers - 30) * beyond_30km_price

    waiting_money = 0
    if waiting_time > 5:
        waiting_money = (waiting_time - 5) * 750

    total_fare = waiting_money + travel_money
    return f"Waiting money: {waiting_money} VND, Travel money: {travel_money} VND, Total fare: {total_fare} VND"


vehicle_type = int(input("Enter vehicle type (4 or 7 seats): "))
if vehicle_type not in [4, 7]:
    print("Invalid vehicle type")
else:
    num_kilometers = float(input("Enter number of kilometers: "))
    waiting_time = int(input("Enter waiting time (in minutes): "))


    result = calculate_taxi_fare(vehicle_type, num_kilometers, waiting_time)


    print(result)

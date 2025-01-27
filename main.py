from Battery import Battery

# initialise 3 batteries

B1_initial_charge = 8 #kwh
B2_initial_charge = 8 #kwh
B3_initial_charge = 8 #kwh

Batt1 = Battery(capacity = 10, depth_of_discharge=0, charge_rate = 5, discharge_rate = 5)
Batt2 = Battery( capacity = 10, depth_of_discharge=0, charge_rate = 5, discharge_rate = 5)
Batt3 = Battery( capacity = 10, depth_of_discharge=0, charge_rate = 5, discharge_rate = 5)


time_array = {
    'time_period': [1, 2 , 3, 4, 5],
    "customer_demand": [1, 2 , 3, 4, 5],
    "elec_price": [1, 2 , 3, 4, 5]
} #get these numbers from Rich



for t in time_array.time_period:
    Batt1.state_of_charge(charging_state = 'neutral', current_charge = 0)
    


class Battery:
    def __init__(self, capacity, depth_of_discharge=0, charge_rate =2, discharge_rate = 2):
        """
        Initialize a Battery object.
        """
        self.capacity = capacity  # Total capacity of the battery
        self.depth_of_discharge = depth_of_discharge  # Percentage of discharge (0-100)
        self.charge_rate = charge_rate
        self.discharge_rate = discharge_rate

    def state_of_charge(self, charging_state = 'neutral', current_charge = 0):
        time_unit = 1800 #time of each unit in seconds
        if charging_state == 'charging':
            energy_delta = time_unit * self.charge_rate
        elif charging_state == 'discharging':
            energy_delta = time_unit * self.discharge_rate
        else:
            energy_delta = 0
        
        new_SOC = current_charge - energy_delta
            
        return new_SOC

    def __str__(self):
        """
        String representation of the Battery object.

        :return: A string summarizing the battery's state
        """
        return (
            f"Battery State:\n"
            f"  Capacity: {self.capacity}\n"
            f"  Depth of Discharge: {self.depth_of_discharge}%\n"
            f"  Charging State: {'Charging' if self.charging_state else 'Not Charging'}\n"
            f"  State of Charge: {self.state_of_charge()}%"
        )
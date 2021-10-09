import stdev from statistics

#returns a list of standard deviations
#each standard deviation is calculated from 3 consecutive voltages in the voltage list
def voltage_stdev(voltage_list):
    if(len(voltage_list)%3 != 0):
        return None

    stdev_list = []
    temp_voltage_list = voltage_list.copy()
    while len(temp_voltage_list) != 0:
        voltage_set = []
        voltage_set.append(temp_voltage_list.pop(0))
        voltage_set.append(temp_voltage_list.pop(0))
        voltage_set.append(temp_voltage_list.pop(0))
        stdev_list.append(stdev(voltage_set))
        
    return stdev_list

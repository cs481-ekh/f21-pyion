from math import *

#Returns a list of Permeability ratios
def get_pr_list(voltage_list,temp,cr_list):
    if len(voltage_list) != len(cr_list):
        return None
    CONST_R = 8.3145
    CONST_F = 96485.3
    k_temp = temp + 273.15

    pr_list = []
    for i,cr in enumerate(cr_list):
        voltage = voltage_list[i] * pow(10,-6)
        numerator = exp((CONST_F*voltage)/(CONST_R*k_temp))-cr
        denominator = 1.0-cr*exp((CONST_F*voltage)/(CONST_R*k_temp))
        if(denominator == 0.0):
            pr = 1
        else:
            pr = numerator/denominator
        pr_list.append(pr)
    return pr_list
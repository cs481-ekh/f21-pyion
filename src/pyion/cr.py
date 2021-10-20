#Returns a list of concentration ratios
#c1 is the concentration of 
def get_ratios(c_init,vol_init,c_add,vol_add_list):
    ratio_list = []
    curr_vol = vol_init
    curr_c = c_init
    for v in vol_add_list:
        new_c = get_c_new(curr_c,curr_vol,c_add,v)
        curr_c = new_c
        curr_vol += v
        ratio_list.append(get_cr(c_init,new_c))
    return ratio_list

#Returns the new concentration after new solution is added
def get_c_new(c_init,vol_init,c_add,vol_add):
    moles_init = from_milli(c_init) * from_micro(vol_init)
    moles_add = from_milli(c_add) * from_micro(vol_add)
    new_moles = moles_init + moles_add
    new_vol = from_micro(vol_init) + from_micro(vol_add)
    return to_milli(float(new_moles)/new_vol)

#Returns the concentration ratio given two concentrations
def get_cr(c1,c2):
    return float(c2)/c1

#Convert a value from milli to base unit
def from_milli(milli_value):
    return milli_value * 1000.0

#Convert a value from base unit to milli
def to_milli(base_value):
    return float(base_value)/1000.0

#Convert a value from micro to base unit
def from_micro(micro_value):
    return micro_value * 1000000.0

#Convert a value from base unit to micro
def to_micro(base_value):
    return float(base_value)/1000000.0
#Returns a list of concentration ratios
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
    moles_init = c_init * vol_init
    moles_add = c_add * vol_add
    new_moles = moles_init + moles_add
    new_vol = vol_init + vol_add
    return float(new_moles)/new_vol

#Returns the concentration ratio given two concentrations
def get_cr(c1,c2):
    return float(c2)/c1

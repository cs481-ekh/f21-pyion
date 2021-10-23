#Returns a list of concentration ratios
def get_ratios(c_init=None,vol_init=None,c_add=None,vol_add_list=None):
    if c_init is None or vol_init is None or c_add is None or vol_add_list is None:
        raise Exception("get_ratios arguments must not be None")
    if len(vol_add_list) == 0:
        raise Exception("vol_add_list must contain one or more elements")
    if c_init < 0 or vol_init < 0 or c_add < 0:
        raise Exception("Concentrations and volumes must be positive")
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
def get_c_new(c_init=None,vol_init=None,c_add=None,vol_add=None):
    if c_init is None or vol_init is None or c_add is None or vol_add is None:
        raise Exception("get_ratios arguments must not be None")
    if c_init < 0 or vol_init < 0 or c_add < 0 or vol_add < 0:
        raise Exception("Concentrations and volumes must be positive")
    moles_init = c_init * vol_init
    moles_add = c_add * vol_add
    new_moles = moles_init + moles_add
    new_vol = vol_init + vol_add
    return float(new_moles)/new_vol

#Returns the concentration ratio given two concentrations
def get_cr(c1,c2):
    if c1 < 0 or c2 < 0:
        raise Exception("Concentrations must be positive")
    return float(c2)/c1

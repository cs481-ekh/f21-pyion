def get_ratios(c1,c_init,vol_init,c_add,vol_add_list):
    if len(c_add_list) != len(vol_add_list):
        return None
    ratio_list = []
    for v in vol_add_list:
        ratio_list.append(get_cr(c1,get_c_new(c_init,vol_init,c_add,v)))
    return ratio_list

def get_c_new(c_init,vol_init,c_add,vol_add):
    moles_init = c_init * vol_init
    moles_add = c_add * vol_add
    new_moles = moles_init + moles_add
    new_vol = vol_init + vol_add
    return float(new_moles)/new_vol

def get_cr(c1,c2):
    return float(c1)/c2
def ret_tp():
    el1 = 1
    el2 = 2
    el3 = 3
    return el1, el2, el3

def get_tp():
    el1, el2, el3 = ret_tp().remove(2)
    print(el2)

get_tp()
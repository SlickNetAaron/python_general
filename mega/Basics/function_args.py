def mean(*args):
    return sum(args) / len(args)

print(mean(1, 3, 4))

def mean2(**kwargs):
    return kwargs 
    # returns a dictionary of keys and values
    #return sum(kwargs) / len(kwargs) # This doesn't work... need to set it up for key/value

print(mean2(a = 1, b = 3, c = 4))
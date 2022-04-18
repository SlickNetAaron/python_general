import re
def multiply_two(x,y):
    if not isinstance(x, int):
        raise ValueError("Must be integer")
    if not isinstance(y, int):
        raise ValueError("Must be integer")
    return x * y

def name_reverse(name):
    m = re.search(r'(^[\w .-]*),([\w .-]*$)', name)
    if m is None:
        return name.strip()
    first_last = (m.group(2), m.group(1))
    return ' '.join(first_last).strip()
    



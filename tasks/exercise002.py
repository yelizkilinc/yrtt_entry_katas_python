# The clock shows 'h' hours, 'm' minutes and 's' seconds after midnight.
# Your task is to make the 'past' function return the time converted to milliseconds.
# More examples in the test cases below.

def past(h, m, s):
    return (s*1000)+(m*60*1000)+(h*60*60*1000)
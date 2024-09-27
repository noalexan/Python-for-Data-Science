import time

# Seconds since January 1, 1970: XX.XXX or X.XXe+XX in scientific notation
print("Seconds since January 1, 1970: \
{:,} or {:.2E} in scientific notation".format(time.time(), time.time()))

# e.g. Oct 21 2022
print(time.strftime("%b %d %Y"))

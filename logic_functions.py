
# Binary shift to the right. Input and output are in decimal representation.
def right_bin_shift(x, n):
    res = int(x) >> n
    return res

# Binary rotation to the right. Input and output are in decimal representation.
def right_bin_rot(x, n):
    res = (int(x) >> n) | (int(x) << 32-n)
    res = int(res % 4294967296)
    return int(res)

# Four different mixing functions are defined. The input and output are in decimal representation.
def mixing_fct_1(x):
    res = right_bin_rot(x, 2) ^ right_bin_rot(x, 13) ^ right_bin_rot(x, 22)
    return res


def mixing_fct_2(x):
    res = right_bin_rot(x, 6) ^ right_bin_rot(x, 11) ^ right_bin_rot(x, 25)
    return res


def mixing_fct_3(x):
    res = (right_bin_rot(x, 7) ^ right_bin_rot(x, 18)) ^ right_bin_shift(x, 3)
    return res


def mixing_fct_4(x):
    res = right_bin_rot(x, 17) ^ right_bin_rot(x, 19) ^ right_bin_shift(x, 10)
    return res

# Two additional logic functions that need three decimal entries, which binary representation is encoded on
# 32 bits
def ch_fct(x, y, z):
    res = (x & y) ^ (~x & z)
    return res


def maj_fct(x, y, z):
    res = (x & y) ^ (x & z) ^ (y & z)
    return res

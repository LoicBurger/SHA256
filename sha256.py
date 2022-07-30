import sys
import math
from logic_functions import *
from constant import *


def sha256(message, init_hash_table=standard_init_hash_table):
    # Message completion: first, transform the current message into a bit string of length l. Then compute k
    # such as k = 448-(l-1)(mod 512). M is then extended according to the following procedure. Add 1 to the
    # message, then k "0", and finally write l over 64 bits.

    bin_message = ''
    for i in range(len(message)):
        bin_char = bin(ord(message[i]))
        bin_char = bin_char.replace('0b', '')
        bin_char = (8-len(bin_char))*'0' + bin_char
        bin_message += bin_char

    l = len(bin_message)
    bin_l = bin(l)
    bin_l = bin_l.replace('0b', '')
    bin_l_64char = (64-len(bin_l))*'0' + bin_l
    k = (448-l-1) % 512

    bin_ext_message = ''
    bin_ext_message += bin_message
    bin_ext_message += '1'
    bin_ext_message += k*'0'
    bin_ext_message += bin_l_64char

    # Separation of the extended message into blocks of 512 bits, which are then separated in 16 blocks of 32
    # bits each.

    nbr_blocks = int(len(bin_ext_message)/512)
    ext_message_32bits_blocks = [
        [0 for i in range(16)] for j in range(nbr_blocks)]
    for i in range(nbr_blocks):
        curr_block = bin_ext_message[512*i:512*(i+1)]
        for j in range(16):
            curr_bin_str = curr_block[32*j:32*(j+1)]
            for k in range(32):
                ext_message_32bits_blocks[i][j] += int(
                    curr_bin_str[k]) * math.pow(2, 31-k)

    # Key table.

    key_table = standard_key_table[:]

    # Computing the shortened hash.

    hash_table = init_hash_table[:]
    variable_table = [0 for i in range(8)]

    for i in range(nbr_blocks):

        # Table containing the 64 words.
        word_table = [0 for i in range(64)]
        for j in range(16):
            word_table[j] = int(ext_message_32bits_blocks[i][j])
        for j in range(16, 64):
            word_table[j] = (mixing_fct_4(word_table[j-2]) + int(word_table[j-7]) +
                             mixing_fct_3(word_table[j-15]) + int(word_table[j-16])) % 4294967296

        # Initialisation of the variables values.
        for j in range(8):
            variable_table[j] = hash_table[j]

        # Variable update.
        for j in range(64):
            temp_var1 = (int(variable_table[7]) + mixing_fct_2(int(variable_table[4])) +
                         ch_fct(int(variable_table[4]), int(variable_table[5]), int(variable_table[6])) +
                         key_table[j] + int(word_table[j])) % 4294967296
            temp_var2 = (mixing_fct_1(int(variable_table[0])) +
                         maj_fct(int(variable_table[0]), int(variable_table[1]), int(variable_table[2]))) % 4294967296
            variable_table[7] = int(variable_table[6])
            variable_table[6] = int(variable_table[5])
            variable_table[5] = int(variable_table[4])
            variable_table[4] = (int(variable_table[3]) +
                                 temp_var1) % 4294967296
            variable_table[3] = int(variable_table[2])
            variable_table[2] = int(variable_table[1])
            variable_table[1] = int(variable_table[0])
            variable_table[0] = (temp_var1 + temp_var2) % 4294967296

        # Hash table update.

        for j in range(8):
            hash_table[j] = (
                hash_table[j] + int(variable_table[j])) % 4294967296
                

    # Concatenation of the different hashes to produce the final encrypted message.

    encrypted_message = ''
    for i in range(8):
        part_message = hex(hash_table[i])
        part_message = part_message.replace('0x', '')
        part_message = (8-len(part_message))*'0' + part_message
        encrypted_message += part_message

    return encrypted_message

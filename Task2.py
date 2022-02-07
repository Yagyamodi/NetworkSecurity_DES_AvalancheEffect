# Importing
import DESfiddle.utils as dfu
from statistics import median
import numpy as np
import matplotlib.pyplot as plt


def alterText(txt: str, ham_distance: int) -> str:
  """Alter the given txt at some hamming_dist number of positions. This is used to experimentally determine how the avalanche effect varies with hamming distance in DES. """
  length = len(txt)
  random_pos = sample(range(0,length),ham_distance)
  random_pos.sort() # To ensure the for loop below doesnot increase the length of txt
  altered_txt = ""
  i = 0
  for pos in random_pos:
    altered_txt += txt[i:pos]
    i = pos+1
    if(txt[pos] == '1'):
      altered_txt += '0'
    else:
      altered_txt += '1'
  
  altered_txt += txt[i:]
  return altered_txt

# Usage
permutation_arr = dfu.generate_PC_1(64)

from DESfiddle.utils import *

# Inputs in binary setting
plaintext = "0000011101001001000001111010111100101110001001011011101100101001"
key = "0110001101000000101101001010100110000000110110001110110011101011"

# Settings
total_rounds = 16
midlength = 32
ham_distance = 1

#output variables
task2_diff = np.zeros((16,1))


# Hamming the plaintext in binary mode
for i in range(0,10):
    plaintext_vector = [plaintext]
    second_plaintext_vector = [alterText(plaintext, ham_distance)]  # plaintext array with hamming distance i+1 with plaintext_vector
    key = [key]
    # generating round keys
    rkb,rkh = generate_round_keys(key, total_rounds, midlength)
    # running DES algorithm for 16 rounds
    original_ciphertext, original_round_ciphertexts = encrypt(plaintext_vector, rkb, total_rounds, midlength)
    _, round_ciphertexts = encrypt(second_plaintext_vector, rkb, total_rounds, midlength)
    # finding hamming distance between two ciphertexts
    ham_diff = calc_diff(original_round_ciphertexts, round_ciphertexts)
    task2_diff = np.column_stack((task2_diff, ham_diff))
    ham_distance += 1   # increasing hamming distance between P0 and next plaintext Pi


task2_diff = np.delete(task2_diff, 0, 1)
task2_diff = np.transpose(task2_diff)

fig = plt.figure(figsize =(12, 9))

# Creating axes instance
ax = fig.add_axes([0, 0, 1.5, 1])
ax.set_xlabel("Encryption Rounds")
ax.set_ylabel("Hamming distance in ciphertext")
ax.set_title("Task 2: For increasing hamming distance by 1 in plaintext, find out the hamming distance in ciphertext")

 
# Creating plot
bp = ax.boxplot(task2_diff)
 
# show plot
plt.show()

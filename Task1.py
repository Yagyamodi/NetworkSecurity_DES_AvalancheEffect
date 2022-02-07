# Importing
import DESfiddle.utils as dfu
from statistics import median
import matplotlib.pyplot as plt
import numpy as np


def alterText(txt: str, hamming_dist: int) -> str:
  """Alter the given txt at some hamming_dist number of positions. This is used to experimentally determine how the avalanche effect varies with hamming distance in DES. """
  length = len(txt)
  random_pos = sample(range(0,length),hamming_dist)
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
hamming_dist = 1

#output variables
task1_diff = np.zeros((16,1))


# Hamming the plaintext in binary mode
for i in range(0,10):
    original_pt_arr = [plaintext]
    pt_arr = [alterText(plaintext, hamming_dist)]
    key = [key]
    rkb,rkh = generate_round_keys(key, total_rounds, midlength)
    original_ciphertext, original_round_ciphertexts = encrypt(original_pt_arr, rkb, total_rounds, midlength)
    _, round_ciphertexts = encrypt(pt_arr, rkb, total_rounds, midlength)
    ham_diff = calc_diff(original_round_ciphertexts, round_ciphertexts)
    task1_diff = np.column_stack((task1_diff, ham_diff))

task1_diff = np.delete(task1_diff, 0, 1)
task1_diff = np.transpose(task1_diff)

fig = plt.figure(figsize =(12, 9))

# Creating axes instance
ax = fig.add_axes([0, 0, 1.5, 1])
ax.set_xlabel("Encryption Rounds")
ax.set_ylabel("Hamming distance in ciphertext")
ax.set_title("Task 1: For hamming distance of 1 in plain text, find out the hamming distance in the ciphertext.")
 
# Creating plot
bp = ax.boxplot(task1_diff)
 
# show plot
plt.show()
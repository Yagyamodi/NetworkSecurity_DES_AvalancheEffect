# -*- coding: utf-8 -*-
"""
Created on Mon Feb  7 12:26:01 2022

@author: 91876
"""
# Importing
import DESfiddle.utils as dfu

# Usage
permutation_arr = dfu.generate_PC_1(64)

from DESfiddle.utils import *

# Inputs in binary setting
plaintext = "0101010101010101010101010101010101010101010101010101010101010101"
key = "1111111111111111111111111111111100000000000000000000000000000000"

# Settings
nor = 16
halfwidth = 32
hamming_dist = 1

#output variables
task1_diff = []
task2_diff = []


# Hamming the plaintext in binary mode
for i in range(0,10):
    ref_pt_arr = preprocess_plaintext(plaintext, halfwidth)
    pt_arr = preprocess_plaintext(plaintext, halfwidth, hamming_dist)
    key = preprocess_key(key, halfwidth)
    rkb,rkh = generate_round_keys(key,nor, halfwidth)
    ref_ciphertext, ref_round_ciphertexts = encrypt(ref_pt_arr, rkb, nor, halfwidth)
    _, round_ciphertexts = encrypt(pt_arr, rkb, nor, halfwidth)
    diff = calc_diff(ref_round_ciphertexts, round_ciphertexts)
    task1_diff.append(diff[15])

'''
# Hamming the key in binary mode
for i in range(0,10):
    pt_arr = preprocess_plaintext(plaintext, halfwidth)
    ref_key = preprocess_key(key,halfwidth)
    key = preprocess_key(key, halfwidth, hamming_dist)
    ref_rkb, ref_rkh = generate_round_keys(ref_key, nor, halfwidth)
    rkb,_ = generate_round_keys(key, nor, halfwidth)
    ref_ciphertext, ref_round_ciphertexts = encrypt(pt_arr, ref_rkb, nor, halfwidth)
    _, round_ciphertexts = encrypt(pt_arr, rkb, nor, halfwidth)
    diff = calc_diff(ref_round_ciphertexts, round_ciphertexts)
    task2_diff.append(diff[15])
'''

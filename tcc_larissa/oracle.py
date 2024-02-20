#!/usr/bin/python3
# coding: latin-1

import re 
import sys

LINES = sys.stdin.readlines()
LEMMA = sys.argv[1]
L0, L1, L2, L3, L4, L5, L6, L7, L8 = [], [], [], [], [], [],[], [], []

if LEMMA=="Sim_swap_secret_answer":
    print("Aaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaa")
    for line in LINES:
        (num, val) = line.split(':')
        print(num, val)



    

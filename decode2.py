# -*- coding: utf-8 -*-
"""
Spyder Editor

This is a temporary script file.
"""


'''
text = "0000101111"
sembol = ["a", "b", "c", "d", "e", "f"]

sozluk = {}
i = 0
j = 0
k = 0
sayac = 0
temp = []
 
for i in range(len(text)):
    if(text[i] == "0"):
        temp.append(0)   
    else:
        sozluk[sembol[j]] = temp
        print sembol[j] + " : " + str(temp)
        j += 1
        x = temp.pop()
        while(x == 1):
            x = temp.pop()
        temp.append(1)
        

temp.pop()
temp.append(1) 
sozluk[sembol[j]] = temp
print sembol[j] + " : " + str(temp)       
'''


###############################################################
def huffman(p):
    '''Return a Huffman code for an ensemble with distribution p.'''
    assert(sum(p.values()) == 1.0) # Ensure probabilities sum to 1

    # Base case of only two symbols, assign 0 or 1 arbitrarily
    if(len(p) == 2):
        return dict(zip(p.keys(), ['1', '0']))

    # Create a new distribution by merging lowest prob. pair
    p_prime = p.copy()
    a1, a2 = lowest_prob_pair(p)
    p1, p2 = p_prime.pop(a1), p_prime.pop(a2)
    p_prime[a1 + a2] = p1 + p2

    # Recurse and construct code on new distribution
    c = huffman(p_prime)
    ca1a2 = c.pop(a1 + a2)
    c[a1], c[a2] = ca1a2 + '1', ca1a2 + '0'

    return c

def lowest_prob_pair(p):
    '''Return pair of symbols from distribution p with lowest probabilities.'''
    assert(len(p) >= 2) # Ensure there are at least 2 symbols in the dist.

    sorted_p = sorted(p.items(), key=lambda (i,pi): pi)
    return sorted_p[0][0], sorted_p[1][0]




sozluk = {}
input_text = "kkkkkkkaaaaaaaaaaaaaaaaaaaaaaaaazzeeeeeeeeeeeeeemmmmmmmmllll"
for i in range(len(input_text)):
    key = input_text[i]
    if key in sozluk:
        sozluk[key] += 1
    else:
        sozluk[key] = 1
    
print sozluk
print "here"
import collections
sozluk = collections.OrderedDict(sorted(sozluk.items(), reverse=True))
print sozluk

frequencies = {key:float(value)/sum(sozluk.values()) for (key,value) in sozluk.items()}
print frequencies
print(huffman(frequencies))



import string 

sembol = list(string.ascii_lowercase)
text = "0000101111"
temp = ""

sozluk = {}
i = 0
j = 0

for i in range(len(text)):
    if(text[i] == "1"):
        sozluk[sembol[j]] = temp
        j += 1
        x = temp[len(temp) - 1]
        temp = temp[:-1]
        while(x == "1"):
            x = temp[len(temp) - 1]
            temp = temp[:-1]
    temp += text[i]
        

temp = temp[:-1]
temp += text[i]
sozluk[sembol[j]] = temp
print sozluk

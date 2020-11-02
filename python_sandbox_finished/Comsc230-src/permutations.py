#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Thu Apr 16 16:27:09 2020

@author: tnewman
"""

def perm(l):
        # Compute the list of all permutations of l
    if len(l) <= 1:
                  return [l]
    
    r = []
    for i in range(len(l)):
             s = l[:i] + l[i+1:]
             
             p = perm(s)
             for x in p:
              r.append(l[i:i+1] + x)
    return r

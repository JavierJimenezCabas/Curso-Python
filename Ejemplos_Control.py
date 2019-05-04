# -*- coding: utf-8 -*-
"""
Created on Sat Apr 27 18:13:40 2019

@author: Javier
"""
import control
# from control.matlab import *

num = [[[1., 2.], [3., 4.]], [[5., 6.], [7., 8.]]]
den = [[[9., 8., 7.], [6., 5., 4.]], [[3., 2., 1.], [-1., -2., -3.]]]
sys1 = control.tf(num, den)

sys = control.ss("1. -2; 3. -4", "5.; 7", "6. 8", "9.")

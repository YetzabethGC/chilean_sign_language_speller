# -*- coding: utf-8 -*-
import bpy
import sys
sys.path.append("/home/vpoblete/chilean_sign_language_speller/avatar_pose_controls") #Control codes directory
import handctrl as hc
#import headctrl as hdc
#import spinectrl as sc


hc.hRH(3)   #Height of right hand, possible values:[0,1,2,3,4,5] from lowest to highest
hc.hLH(0)   #Height of left hand, same values as hRH
hc.dRH(0)   #Right hand's distance from body, possible values=[-1,0,1], from opposite, center and away.
hc.dLH(0)   #Left hand's distance from body. Same values as dRH
hc.rhF(0,0,0,0,0)   #extension of right hand fingers (thumb, index, heart, ring pinky), possible values=[0,...,5]
hc.lhF(0,0,0,0,0)   #extension of left hand fingers (thumb, index, heart, ring pinky), possible values=[0,...,5]
hc.detRF(0,0,0)

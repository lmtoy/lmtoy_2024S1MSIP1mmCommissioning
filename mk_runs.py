#! /usr/bin/env python
#

import os
import sys

from lmtoy import runs

project="2024S1MSIP1mmCommissioning"

#        obsnums per source (make it negative if not added to the final combination)
on = {}
#on['mars'] = [ 116442 ]

#  note lower case also available for some of these
on["3C273"] = \
 [ 115385, 115412, 115413, 115430, 115848, 115849, 115930, 115944, 115958, 115970, 115984, 115985, 115995, 116010, 116021, 116022,]

on["3C279"] = \
 [ 115330, 115378, 115384, 115562, 115924, 115939, 115953, 115966, 115979, 116004, 116018, 116069, 116073, 116100, 116114, 116127, 116139, 116184,]

on["CIT6"] = \
 [ 115394, 115539, 115540, 115787, 115826, 115827, 115828, 115829, 115830, 115837, 115846, 116212, 116214, 116215, 116229, 116241, 125247, 125249, 125251, 125260, 125269, 125324, 125326, 125336, 125348, 125350, 125540, 125542, 125544, 125546, 125561, 125570, 125610, 125612, 125620, 125622, 125623, 125624, 125634, 125636, 125715, 125717, 125729, 125739,
   129921, 129923, 129939, 129941, 129943, 129952, 132252, 132253, 132254, 132255, 132262, 132263, 132273, 132328, 132330, 132332, 132360, 132370, 132380, 132494, 132496, 132504, 132569, 132584, 132592, 133191, 133192, 133194, 133195, 133201, 133209,]   # during EHT

on["GL1922"] = \
 [ 115444, 115452, 115459, 115673, 115676, 115677, 115684, 115687, 115697, 115698, 115701, 115710, 115717, 115718, 115734, 132436, 132438, 132650, 132655, 132662, 132663, 132681, 132687, 133211, 133213, 133222, 133228,]


on["IRC+10216"] = \
 [ 110436, 110438, 110589, 110627, 111214, 111216, 111221, 111224, 111247, 111354, 111390, 115341, 115342, 115352, 115353, 115362, 115768, 115770,-115771, 115772, 115774, 115775, 115776,-115778,]

on["Ori-KL"] = \
 [ 110553, 110554, 115176, 115177, 115183, 115193, 115289, 115290, 115291, 115303, 115313, 115542, 115543, 116040, 116041, 116049, 116059, 125175, 125176, 125188, 125200, 125413, 125415,
   132772, 132782, 132791, 132811, 132830,]   # during EHT

on["R-Leo"] = \
 [ 110556, 110558, 110560, 110561, 110573, 110584, 110585, 111226, 111228, 111229, 111237, 111245, 111358, 111368, 111386, 115339, 115545, 115546, 115552, 115559, 115560, 115878, 115879, 115880, 115886, 115893, 116125, 116243, 116249, 116257, 116265, 116271, 116280, 116290, 116296, 116305, 116314, 116320, 116330, 116340, 116346, 116357, 116367, 116372, 116373, 116379, 116380,]

on["RT-Vir"] = \
 [ 110603, 110605, 110606, 110607, 110616, 110625, 111392, 111393, 111394, 115567, 115568, 115574, 115582, 115588, 115589, 115597, 115602, 115610, 115624, 115651, 115652, 115660, 115851, 115852, 115853, 115863, 115875, 115876, 115895, 115896, 115905, 115916, 116031, 116061, 116062, 125240,
   132962, 132967, 132968, 133235,]   # during EHT

on["RX-Boo"] = \
 [ 111473, 111474, 111481, 111491, 111500, 111501, 111508, 111516, 111522, 111530, 111538, 111552, 115120, 115122, 115123, 115129, 115140, 115150, 115157, 115419,]

on["W-Hya"] = \
 [ 111261, 111263, 111271, 111273, 111275, 111285, 111287, 111445, 111446, 111463, 114943, 114944, 114945, 114953, 114969, 115071, 115073, 115074, 115090, 115091, 115102, 115112, 115633, 115642, 115649, 116160, 116162, 116163, 116175, 116191, 116192, 116204, 116382, 116383, 116389, 125606, 125608,
   132250, 132422, 132424, 132425, 132506, 132519, 132521, 132523, 132596, 132597, 132598, 133087, 133096, 133101, 133102,]   # during EHT


#        common parameters per source on the first dryrun (run1a, run2a)
pars1 = {}
pars1['mars']   = ""
pars1["3C273"]     = "pix_list=0,1,2,3"                    # no line
pars1["3C279"]     = "pix_list=0,1,2,3"                    # no line
pars1["CIT6"]      = "pix_list=0,1,2,3 dv=50 dw=100 b_order=3"
pars1["GL1922"]    = "pix_list=0,1,2,3 dv=50 dw=100 b_order=3"

pars1["IRC+10216"] = "pix_list=0,1,2,3 dv=50 dw=100 b_order=3"
pars1["Ori-KL"]    = "pix_list=0,1,2,3"                    # many (&broad) lines
pars1["R-Leo"]     = "pix_list=0,1,2,3 dv=30 dw=60  b_order=3"
pars1["RT-Vir"]    = "pix_list=0,1,2,3 dv=30 dw=60  b_order=3"
pars1["RX-Boo"]    = "pix_list=0,1,2,3 dv=30 dw=60  b_order=3"
pars1["W-Hya"]     = "pix_list=0,1,2,3 dv=30 dw=60  b_order=3"

#        common parameters per source on subsequent runs (run1b, run2b)
pars2 = {}
pars2['mars']   = "srdp=1 admit=0"
pars2["3C273"]     = "pix_list=0,2 bank=0"
pars2["3C279"]     = "pix_list=0,2 bank=0"
pars2["CIT6"]      = "pix_list=0,2 bank=0"
pars2["GL1922"]    = "pix_list=0,2 bank=0"
pars2["IRC+10216"] = "pix_list=0,2 bank=0"
pars2["Ori-KL"]    = "pix_list=0,2 bank=0"
pars2["R-Leo"]     = "pix_list=0,2 bank=0"
pars2["RT-Vir"]    = "pix_list=0,2 bank=0"
pars2["RX-Boo"]    = "pix_list=0,2 bank=0"
pars2["W-Hya"]     = "pix_list=0,2 bank=0"

pars3 = {}
pars3["3C273"]     = "pix_list=1,3 bank=1"
pars3["3C279"]     = "pix_list=1,3 bank=1"
pars3["CIT6"]      = "pix_list=1,3 bank=1"
pars3["GL1922"]    = "pix_list=1,3 bank=1"
pars3["IRC+10216"] = "pix_list=1,3 bank=1"
pars3["Ori-KL"]    = "pix_list=1,3 bank=1"
pars3["R-Leo"]     = "pix_list=1,3 bank=1"
pars3["RT-Vir"]    = "pix_list=1,3 bank=1"
pars3["RX-Boo"]    = "pix_list=1,3 bank=1"
pars3["W-Hya"]     = "pix_list=1,3 bank=1"

if __name__ == '__main__':    
    runs.mk_runs(project, on, pars1, pars2, pars3, sys.argv)

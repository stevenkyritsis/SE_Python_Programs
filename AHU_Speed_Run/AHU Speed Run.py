####### AHU Speedrun Program v1.0 ########
###### Written by Steven Kyritsis ########
############### 3-18-2024 ################

################## README ##################
# Written to assist with quickly writing 
# multiple VAVs to a sVavCalc program.
# To use the program, you put your exported
# list of VAVs in a text file and write the
# path to the "input file". That generates
# the result in a "result.txt".
############################################
import re

filename_in = 'VAV_List.txt' # Input file
filename_out = 'result.txt'  # Output file

vavF = open(filename_in, 'r') # VAV List
newF = open(filename_out, 'w') # Output File

l = [] # List to store VAV names

# For loop adding the VAV names to the list
for line in vavF:
    # ex: VAV_N5_101
    reg_vav = re.findall("VAV_[A-Z][0-9]_[0-9]+",line)
    # ex: VAV_N1_E_318
    exhaust_vav = re.findall("VAV_[A-Z][0-9]_E_[0-9]*",line)
    # ex: VAV_E_S2_116B
    rExhaust_vav = re.findall("VAV_E_[A-Z][0-9]_[0-9]*",line)
    # ex: VAV_S1_101A
    a_vav = re.findall("VAV_[A-Z][0-9]_[0-9]*A",line)
    # ex: VAV_D2_S_113_R_208
    loop_vav = re.findall("VAV_[A-Z][0-9]_[A-Z]_[0-9]*_[A-Z]_[0-9]*",line)
    # ex: VAV_D2_S_112_EAV_W2_111ABC
    spec_loop_vav = re.findall("VAV_[A-Z][0-9]_[A-Z]_[0-9]*_[A-Z]*_[A-Z][0-9]_[0-9]*[A-Z]*",line)

    for vav in a_vav:
        if vav not in l:
            l.append(vav)
 
    for vav in exhaust_vav:
        if vav not in l:
            l.append(vav)
    
    for vav in rExhaust_vav:
        if vav not in l:
            l.append(vav)
    
    for vav in loop_vav:
        if vav not in l:
            l.append(vav)
    
    for vav in spec_loop_vav:
        if vav not in l:
            l.append(vav)
    
    for vav in reg_vav:
        if vav not in l:
            l.append(vav)

vavF.close() # Closing the VAV file

l.sort() # sorting the list of VAVs

# Adding the inputs
for line in l:
    newF.write(f'Numeric Input {line}_StPrRstReq_vi, {line}_RmTmp_vi, {line}_RhtVlvPos_vi\n')
newF.write('\n')

# Adding the outputs
for line in l:
    newF.write(f'Numeric Output {line}_StPrRstReq, {line}_RmTmp, {line}_RhtVlvPos\n')
newF.write('\n')

newF.write('CALC:\n')
# Adding the assignments
for line in l:
    newF.write(f'\t{line}_StPrRstReq = {line}_StPrRstReq_vi \n\t{line}_RmTmp = {line}_RmTmp_vi \n\t{line}_RhtVlvPos = {line}_RhtVlvPos_vi\n')

newF.write('\n')
newF.write('E:\n')
newF.write('\tif (TS > 15) then goto CALC')

newF.close() # Closing the output file
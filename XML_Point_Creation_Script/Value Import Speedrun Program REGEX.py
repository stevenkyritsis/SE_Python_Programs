### Value Import Speedrun Program v1.0 ###
###### Written by Steven Kyritsis ########
############### 3-18-2024 ################

################## README ##################
# Written to assist with quickly writing 
# multiple values to an XML file.
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

# Adding the inputs
for line in l:
    line = line.strip('\n')
    newF.write(f'\t<OI DESCR="Reheat Valve Position" NAME="{line}_RhtVlvPos" TYPE="server.point.AV"/>\n')
    newF.write(f'\t<OI DESCR="Room Temperature" NAME="{line}_RmTmp" TYPE="server.point.AV"/>\n')
    newF.write(f'\t<OI DESCR="Static Pressure Reset Request" NAME="{line}_StPrRstReq" TYPE="server.point.AV"/>\n')

newF.close() # Closing the output file

print(len(l)*3) # Prints the count of how many ponts we are importing
##### sVavCalc Speedrun Program v1.0 #####
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

filename_in = './VAV_List.txt' # Input file
filename_out = './result.txt'  # Output file

vavF = open(filename_in, 'r') # VAV List
newF = open(filename_out, 'w') # Output File

l = [] # List to store VAV names

# For loop adding the VAV names to the list
for vav in vavF:
    l.append(vav)

vavF.close() # Closing the VAV file

# Adding the inputs
for line in l:
    line = line.strip('\n')
    newF.write(f'Numeric Input {line}_StPrRstReq_vi, {line}_RmTmp_vi, {line}_RhtVlvPos_vi\n')
newF.write('\n')

# Adding the outputs
for line in l:
    line = line.strip('\n')
    newF.write(f'Numeric Output {line}_StPrRstReq, {line}_RmTmp, {line}_RhtVlvPos\n')
newF.write('\n')
newF.write('CALC:\n')
# Adding the assignments
for line in l:
    line = line.strip('\n')
    newF.write(f'\t{line}_StPrRstReq = {line}_StPrRstReq_vi \n\t{line}_RmTmp = {line}_RmTmp_vi \n\t{line}_RhtVlvPos = {line}_RhtVlvPos_vi\n')
newF.write('E:\n')
newF.write('\tif (TS > 15) then goto CALC')
newF.close() # Closing the output file
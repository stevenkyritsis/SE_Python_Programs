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

filename_in = 'VAV_List.txt' # Input file
filename_out = 'result.txt'  # Output file

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
    newF.write(f'<OI DESCR="Reheat Valve Position" NAME="{line}_RhtVlvPos" TYPE="server.point.AV"/>\n')
    newF.write(f'<OI DESCR="Room Temperature" NAME="{line}_RmTmp" TYPE="server.point.AV"/>\n')
    newF.write(f'<OI DESCR="Static Pressure Reset Request" NAME="{line}_StPrRstReq" TYPE="server.point.AV"/>\n')

newF.close() # Closing the output file
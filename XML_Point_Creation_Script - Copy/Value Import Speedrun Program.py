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

count = 1
# Adding the inputs
for line in l:
    line = line.strip('\n')
    newF.write(f'<PI Name="VAVRmTmp{count}">\n')
    newF.write(f'\t<Reference DeltaFilter="0" Object="../../MPV/{line}/Application/Values/RmTmp" Property="Value" Retransmit="0" TransferRate="10"/>\n')
    newF.write(f'</PI>\n')
    count += 1

newF.close() # Closing the output file
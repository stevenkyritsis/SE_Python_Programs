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

filename_in = 'C:\\Users\\sesa751843\\OneDrive - Schneider Electric\\Documents\\Python Programs\\Reset Request\\VAV_List.txt' # Input file
a_filename_out = 'C:\\Users\\sesa751843\\OneDrive - Schneider Electric\\Documents\\Python Programs\\Reset Request\\StPr_result_a.txt'  # Output file
b_filename_out = 'C:\\Users\\sesa751843\\OneDrive - Schneider Electric\\Documents\\Python Programs\\Reset Request\\StPr_result_b.txt'

vavF = open(filename_in, 'r') # VAV List
a_newF = open(a_filename_out, 'w') # Output File
b_newF = open(b_filename_out, 'w')

a_list = [] # List to store VAV names
b_list = []

# For loop adding the VAV names to the list
for line in vavF:
    # ex: VAV_N5_101
    a_vav = re.findall("VAV[-]*A[0-9]+[A-Z]*",line)
    # ex: VAV_N1_E_318
    b_vav = re.findall("VAVB[0-9]+[A-Z]*",line)

    bs_vav= re.findall("VAVB[0-9]+_[0-9]",line)

    for vav in a_vav:
        if vav not in a_list:
            a_list.append(vav)
 
    for vav in b_vav:
        if vav not in b_list:
            b_list.append(vav)

    for vav in bs_vav:
        if vav not in b_list:
            b_list.append(vav)

vavF.close() # Closing the VAV file

a_list.sort() # sorting the list of VAVs
b_list.sort()

count = 1
sCount = 1
a_newF.write(f'Sum{sCount} = Sum(')
for line in a_list:
    if count%10 == 0:
        sCount+=1
        a_newF.write(')\n')
        a_newF.write(f'Sum{sCount} = Sum(')
    a_newF.write(f'VAVStPrRstReq{count},')
    if count == len(a_list):
        a_newF.write(')')
    count+= 1

a_newF.write('\n\n')

count = 1
for line in a_list:
    a_newF.write(f'Numeric Input VAVStPrRstReq{count}\n')
    count+= 1
a_newF.write('\n')

count = 1
# Adding the inputs
for line in a_list:
    a_newF.write(f'<PI Name="VAVStPrRstReq{count}">\n')
    a_newF.write(f'\t<Reference DeltaFilter="0" Object="../../../MPV/{line}/Application/Values/StPrRstReq" Property="Priority16" Retransmit="0" TransferRate="10"/>\n')
    a_newF.write(f'</PI>\n')
    count+= 1
a_newF.write('\n')

a_newF.close() # Closing the output file

count = 1
sCount = 1
b_newF.write(f'Sum{sCount} = Sum(')
for line in b_list:
    if count%10 == 0:
        sCount+=1
        b_newF.write(')\n')
        b_newF.write(f'Sum{sCount} = Sum(')
    b_newF.write(f'VAVStPrRstReq{count},')
    if count == len(b_list):
        b_newF.write(')')
    count+= 1

b_newF.write('\n\n')

count = 1
for line in b_list:
    b_newF.write(f'Numeric Input VAVStPrRstReq{count}\n')
    count+= 1
b_newF.write('\n')

count = 1
# Adding the inputs
for line in b_list:
    b_newF.write(f'<PI Name="VAVStPrRstReq{count}">\n')
    b_newF.write(f'\t<Reference DeltaFilter="0" Object="../../../MPV/{line}/Application/Values/StPrRstReq" Property="Priority16" Retransmit="0" TransferRate="10"/>\n')
    b_newF.write(f'</PI>\n')
    count+= 1
b_newF.write('\n')

b_newF.close()
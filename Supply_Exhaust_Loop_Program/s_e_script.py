import re
filename_in = './VAV_List.txt' # Input file
filename_out = './result.txt'  # Output file

vavF = open(filename_in, 'r') # VAV List
newF = open(filename_out, 'w') # Output File

l = [] # List to store VAV names

# For loop adding the VAV names to the list
for vav in vavF:
                    # VAV_D2_S_113_R_208
    x = re.search("VAV_[A-Z][0-9]_[A-Z]_[0-9]*_[A-Z]_[0-9]*",vav)
                    # VAV_D2_S_112_EAV_W2_111ABC
    y = re.search("VAV_[A-Z][0-9]_[A-Z]_[0-9]*_[A-Z]*_[A-Z][0-9]_[0-9]*[A-Z]*",vav)
    if x is not None:
        l.append(x.group())
    if y is not None:
        l.append(y.group())
    

vavF.close() # Closing the VAV file

for line in l:
    newF.write(f'../../../Private IP Network/{line}/Application/Values/RhtVlvPos/Priority16\n')
    newF.write(f'../../../Private IP Network/{line}/Application/Values/RmTmp/Priority16\n')
    newF.write(f'../../../Private IP Network/{line}/Application/Values/StPrRstReq/Priority16\n')
    newF.write('\n')

newF.close() # Closing the output file
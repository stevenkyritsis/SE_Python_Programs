import re

new_vav = open("new.txt", 'r') # Input text of program we are looking to replace
result = open("new_list.txt", 'w')

l1 = []

for line in new_vav:
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
        if vav not in l1:
            l1.append(vav.strip('\n'))
 
    for vav in exhaust_vav:
        if vav not in l1:
            l1.append(vav.strip('\n'))
    
    for vav in rExhaust_vav:
        if vav not in l1:
            l1.append(vav.strip('\n'))
    
    for vav in loop_vav:
        if vav not in l1:
            l1.append(vav.strip('\n'))
    
    for vav in spec_loop_vav:
        if vav not in l1:
            l1.append(vav.strip('\n'))
    
    for vav in reg_vav:
        if vav not in l1:
            l1.append(vav.strip('\n'))

new_vav.close()

# List of VAVs from MPV Network
vavF = open("VAV_List.txt", 'r')

l2 = []

for vav in vavF:
    l2.append(vav.strip('\n'))

vavF.close()

# Splitting up the elements of the VAV
for i in range(len(l1)):
    l1[i] = l1[i].split('_')
for i in range(len(l2)):
    l2[i] = l2[i].split('_')

print(l1, '\n\n', l2)

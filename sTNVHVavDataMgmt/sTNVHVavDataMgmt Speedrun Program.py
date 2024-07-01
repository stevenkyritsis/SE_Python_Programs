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
import re

filename_in = './VAV_List.txt' # Input file
filename_out = './result.txt'  # Output file

vavF = open(filename_in, 'r') # VAV List
newF = open(filename_out, 'w') # Output File

l = [] # List to store VAV names

# For loop adding the VAV names to the list
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

# Making the comments at the top of the program
newF.write(f'{chr(0x27)}Data Management Program\n')
newF.write(f'{chr(0x27)}Last Edit Date: March 29, 2024\n\n')

newF.write(f'{chr(0x27)}Counts the number of requests from VAVs for Static Pressure Reset requests.\n')
newF.write(f'{chr(0x27)}Calculates Total Airflow and Temperature Max/Average/Min.\n\n')

# Adding program inputs
for line in l:
    line = line.strip('\n')
    newF.write(f'Numeric Input {line}_StPrRstReq, {line}_RmTmp, {line}_RhtVlvPos\n')
newF.write('Numeric Input vi_VavOpnRhtVlvPos, vi_VavOpnRhtVlvPct\n\n')

# Program outputs
newF.write('Numeric Output vo_VavSaStPrSptRstReq\n')
newF.write('Numeric Output vo_VavRmTmpHi, vo_VavRmTmpLo, vo_VavRmTmpAvg\n')
newF.write('Numeric Output vo_VavSaTmpSptRstReq\n')
newF.write('String Output Vav01Label, Vav02Label, Vav03Label, Vav04Label, Vav05Label\n\n')

newF.write('Numeric Req0Cnt, Req1Cnt, Req2Cnt, Req3Cnt, i, AvgSum, AvgDiv, TempHi, TempLo, RhtCnt\n')
newF.write(f'Numeric Arr1[{len(l)}], Arr2[{len(l)+1}]\n')
newF.write(f'String Arr3[{len(l)+1}]\n\n')

newF.write('STPRRESET:\n')
newF.write(f'{chr(0x27)}(*)Static Pressure Reset Requests\n')
newF.write(f'{chr(0x27)}(1)If the measured air flow is less than 50% of setpoint while setpoint is greater than zero and the damper position is greater than 95% for 1 minute, send 3 requests.\n')
newF.write(f'{chr(0x27)}(2)Else if the measured air flow is less than 70% of setpoint while setpoint is greater than zero and the damper position is greater than 95% for 1 minute, send 2 requests.\n')
newF.write(f'{chr(0x27)}(3)Else if the damper position is greater than 95%, send 1 request until the damper position is less than 85%.\n')
newF.write(f'{chr(0x27)}(4)Else if the damper position is less than 95%, send 0 requests.\n\n')
for i in range(len(l)):
    newF.write(f'\tArr1[{i+1}] = {l[i]}_StPrRstReq\n')

newF.write('\tSetArraySize(Arr2, GetArraySize(Arr3))\n')


for i in range(len(l)):
    newF.write(f'\tArr3[{i+1}] = "{l[i]}"\n')
newF.write(f'\tArr3[{len(l)+1}] = "---"\n')
newF.write('\tReq0Cnt = 0\n')
newF.write('\tReq1Cnt = 0\n')
newF.write('\tReq2Cnt = 0\n')
newF.write('\tReq3Cnt = 0\n')
newF.write('\n')

newF.write(f'\tFor i = 1 to {len(l)}\n')
newF.write(f'\t\tIf (Arr1[i] = 0) Then Req0Cnt = Req0Cnt + 1 Else Arr2[i] = {len(l)+1}\t{chr(0x27)}Else clear Arr2 with index i (Arr3[{len(l)+1}] = "---")\n')
newF.write(f'\t\tIf (Arr1[i] = 1) Then Req1Cnt = Req1Cnt + 1 Else Arr2[i] = {len(l)+1}\t{chr(0x27)}Else clear Arr2 with index i (Arr3[{len(l)+1}] = "---")\n')
newF.write(f'\t\tIf (Arr1[i] = 2) Then Req2Cnt = Req2Cnt + 1 Else Arr2[i] = {len(l)+1}\t{chr(0x27)}Else clear Arr2 with index i (Arr3[{len(l)+1}] = "---")\n')
newF.write(f'\t\tIf (Arr1[i] = 3) Then\n')
newF.write(f'\t\t\tReq3Cnt = Req3Cnt + 1\n')
newF.write(f'\t\t\tArr2[Req3Cnt] = i\n')
newF.write(f'\t\tElse\n')
newF.write(f'\t\t\tArr2[i] = {len(l)+1}\t{chr(0x27)}Else clear Arr2 with index i (Arr3[{len(l)+1}] = "---")\n')
newF.write(f'\t\tEndif\n')
newF.write('\tNext i\n\n')

newF.write('\tvo_VavSaStPrSptRstReq = MaxItem(Req0Cnt, Req1Cnt, Req2Cnt, Req3Cnt) - 1\n')
newF.write('\tVav01Label = Arr3[Arr2[1]]\n')
newF.write('\tVav02Label = Arr3[Arr2[2]]\n')
newF.write('\tVav03Label = Arr3[Arr2[3]]\n')
newF.write('\tVav04Label = Arr3[Arr2[4]]\n')
newF.write('\tVav05Label = Arr3[Arr2[5]]\n\n')

newF.write('\tgoto RMTMPCALC\n\n')

newF.write('RMTMPCALC:\n')
for i in range(len(l)):
    newF.write(f'\tArr1[{i+1}] = {l[i]}_RmTmp\n')
newF.write('\tAvgSum = 0\n')
newF.write('\tAvgDiv = 0\n')
newF.write('\tTempHi = -999\n')
newF.write('\tTempLo = 999\n\n')

newF.write(f'\tFor i = 1 to {len(l)}\n')
newF.write('\t\tIf (Arr1[i] <> 0) and (Arr1[i] > -20) and (Arr1[i] < 200) Then\n')
newF.write('\t\t\tAvgSum = AvgSum + Arr1[i]\n')
newF.write('\t\t\tAvgDiv = AvgDiv + 1\n')
newF.write('\t\t\tTempHi = maximum(TempHi, Arr1[i])\n')
newF.write('\t\t\tTempLo = minimum (TempLo, Arr1[i])\n')
newF.write('\t\tEndif\n')
newF.write('\tNext i\n\n')

newF.write('\tIf AvgDiv > 0 Then\n')
newF.write('\t\tvo_VavRmTmpAvg = AvgSum/AvgDiv\n')
newF.write('\tElse\n')
newF.write('\t\tvo_VavRmTmpAvg = 70\n')
newF.write('\tEndif\n\n')

newF.write('\tvo_VavRmTmpHi = TempHi\n')
newF.write('\tvo_VavRmTmpLo = TempLo\n\n')

newF.write('\tgoto SATMPRESET\n\n')

newF.write('SATMPRESET:\n')
for i in range(len(l)):
    newF.write(f'\tArr1[{i+1}] = {l[i]}_RhtVlvPos\n')
newF.write('\tRhtCnt = 0\n\n')

newF.write(f'\tFor i = 1 to {len(l)}\n')
newF.write(f'\t\tIf (Arr1[i] >= vi_VavOpnRhtVlvPos) Then RhtCnt = RhtCnt + 1\n')
newF.write('\tNext i\n\n')

newF.write('\tvo_VavSaTmpSptRstReq = (RhtCnt >= (GetArraySize(Arr1) * vi_VavOpnRhtVlvPct / 100))\n\n')

newF.write('\tgoto STPRRESET\n\n')

newF.write('E:\n')
newF.write('\tif (TS > 10) then goto STPRRESET')
newF.close() # Closing the output file
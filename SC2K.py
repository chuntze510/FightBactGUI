import os,sys,re,time,datetime,struct
#   >------Analyze SC2-D_8Die_share A files to Array

def SC2D8_Calc_Afile(ASC_filedata,path):
    SC2_AFile_New=[]
    lines = ASC_filedata.split('\n')
    for i in range(0, len(lines)):
        line=lines[i]

#   >>-----Set 8 Die data
        matchObj = re.search( r'^X(...),Y(...),A(....),B(..)', line, re.M|re.I)
        if matchObj:
            DieX=int(matchObj.group(1))
            DieY=int(matchObj.group(2))
            BinN=matchObj.group(4)
            bin1=int(hexget(BinN[0]))
            bin2=int(hexget(BinN[1]))
            #將bin轉成十進位記錄
            newbin=bin1*16+bin2
            SC2_AFile_New.append([DieX,DieY,1,newbin])


    return SC2_AFile_New



def hexget(bin):

    if bin=='A':
        return 10
    elif bin=='B':
        return 11
    elif bin=='C':
        return 12
    elif bin=='D':
        return 13
    elif bin=='E':
        return 14
    elif bin=='F':
        return 15
    else:
        return bin

import os,sys,re,time,datetime,struct
#   >------Analyze SC2-D_8Die_share A files to Array

def SC2D8_Calc_Afile(ASC_filedata,path):
    SC2_AFile_New=[]
    lines = ASC_filedata.split('\n')
    for i in range(0, len(lines)):
        line=lines[i]

#   >>-----Set 8 Die data
        matchObj = re.search( r'^X(...),Y(...),A(....),B(.*)', line, re.M|re.I)
        if matchObj:
            XXX=int(matchObj.group(1))
            YYY=int(matchObj.group(2))
            AAA=int(matchObj.group(3))
            BBB=matchObj.group(4)

            if AAA > 16:
                YYY += 11
                each_line = f"X{XXX:03d},Y{YYY:03d},A{AAA:04d},B{BBB}"

            match = re.match( r'^X(...),Y(...),A(.*)', each_line)
            if match:
                xxx = int(match.group(1))
                yyy = int(match.group(2))
                aaa = match.group(3)                   
                ddx = (xxx - 17) * 2 + 5
                ddy = (yyy - 16) * 4 + 5
                    
                # Create 8 lines with calculated coordinates
                lines = []
                lines.append(f"X{ddx+0:03d},Y{ddy+0:03d},A{aaa}")
                lines.append(f"X{ddx+1:03d},Y{ddy+0:03d},A{aaa}")
                lines.append(f"X{ddx+0:03d},Y{ddy+1:03d},A{aaa}")
                lines.append(f"X{ddx+1:03d},Y{ddy+1:03d},A{aaa}")
                lines.append(f"X{ddx+0:03d},Y{ddy+2:03d},A{aaa}")
                lines.append(f"X{ddx+1:03d},Y{ddy+2:03d},A{aaa}")
                lines.append(f"X{ddx+0:03d},Y{ddy+3:03d},A{aaa}")
                lines.append(f"X{ddx+1:03d},Y{ddy+3:03d},A{aaa}")




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

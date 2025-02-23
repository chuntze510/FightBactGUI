import os,sys,re,time,datetime,struct
from IPC3  import IPC3_Calc_Afile
from IPC5  import IPC5_Calc_Afile
from IPC5  import IPC5_Calc_RAfile
from IPC6  import IPC6_Calc_Afile
from SC6   import SC6_Calc_Afile
from IPC7  import IPC7_Calc_Afile
from IPC9  import IPC9_Calc_Afile
from SC2D8 import SC2D8_Calc_Afile
from COMM  import ReadWholeAFile
from COMM  import ReadWholeSTDF
from COMM  import OpenSTDF
from COMM  import CloseSTDF
from COMM  import BuildSTDF
from STDF  import STDF_CheckFormat
from STDF  import STDF_BuildNew
import glob
import zipfile

#--------------------How to execute script with parameters
#python a2stdf_Vx.py Afile OriSTDF OutputSTDF OutputAfle Option
#argv[1] --> original Afile 
#argv[2] --> original STDF
#        --> "NA" 
#argv[3] --> Output new STDF
#        --> "NA" 
#argv[4] --> Output new Afile
#        --> "NA" 
#argv[5] --> Option FLAG
#        --> SC6
#        --> IPC3
#        --> IPC5
#--------------------Change Lists
#Ver.1.0 Ector/Bruce 2024/03/19
#    1. Build script for SC6
#
#Ver.2.0 Ector/Bruce 2024/03/25
#    1. add IPC3
#
#Ver.3.0 Ector/Bruce 2024/05/21
#    1. Afile include Cap & Leak value for IPC3
#    2. add IPC5
#    3. add SC2-D
#Ver.4.0 Ector 2024/06/28
#    1. revised IP35/IPC5 assign bin rule
#    2. add IPC6/IPC7
#    3. unit8 for file read
# 
#
#--------------------Global variable 
New_AFile_Data=[]


#--------------------Main
if __name__ == "__main__":

    ASC_file_path ="pmtn026290v22_202502121057.asc"
    ASC_filedata  =ReadWholeAFile(ASC_file_path)
    AFile_All_lines = ASC_filedata.split('\n')
    AFile_line1=AFile_All_lines[1]
    AFile_Lot=""
    matchObj = re.search( r'^DEVICE=(.*),FABLOT=(.*),WAFER=(.*),NOTCH=(.*),GROSSDICE=(.*)', AFile_line1, re.M|re.I)
    if matchObj:
        AFile_Lot=matchObj.group(2)
   #print('%s'%(AFile_Lot))
#   >------Calc New Bin & Output new Afile/IPC analysis file

    New_AFile_Data=SC2D8_Calc_Afile(ASC_filedata,"nouse.asc")

#   >------Output new STDF
    if(1==1):
        STDF_file_path = "ANC2KD11_MTS168-01-G5_12Feb2025_1359.std"
        FileChSTDF=OpenSTDF(STDF_file_path)
        STDF_CheckFormat(FileChSTDF)
        NewSTPF=STDF_BuildNew(FileChSTDF,New_AFile_Data,AFile_Lot)
        BuildSTDF(NewSTPF,"nouse.std")
        CloseSTDF(FileChSTDF)








    #Note *1
    #FORMAT  [C TYPE]            [PYTHON TYPE]       [STANDARD SIZE]     
    #x       pad byte            no value        
    #c       char                string of length    1               
    #b       signed char         integer             1               
    #B       unsigned char       integer             1               
    #?       _Bool               bool                1               
    #h       short               integer             2               
    #H       unsigned short      integer             2               
    #i       int                 integer             4               
    #I       unsigned int        integer             4               
    #l       long                integer             4               
    #L       unsigned long       integer             4               
    #q       long long           integer             8               
    #Q       unsigned long       long integer        8               
    #f       float               float               4               
    #d       double              float               8               
    #s       char[]              string        
    #p       char[]              string        
    #P       void *              integer                             

    #Note *2
    #if(not ('A%s'% EachXYDB[2] in Site_Fail_Count)): --> check Key
    #Site_Fail_Count['A%04d'% 9999]=0                 --> init dictionary 
    #for key in dict:                                 --> list all keys
    #    print(key)
    #for key, value in dict.items():
    #    print(key, value)

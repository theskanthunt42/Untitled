# 国道139
#Probably for testing/showcasing denshadekill.py
# Btw, The JIS keyboard is so damn hard to use when u try to code with it
# Side note for myself: ehh, gotta grab and use my good old standard 103 
import wmi
import denshadekill
local_session = wmi.WMI()
#drive_count = 0
#print(type(local_session.Win32_LogicalDisk()))
#for i in local_session.Win32_LogicalDisk():
#
dummy = ""
#print(type(local_session.Win32_LogicalDisk()))
for i in local_session.Win32_LogicalDisk():
    #drive_count += 1
    dummy = dummy + str(i)
#print(dummy)



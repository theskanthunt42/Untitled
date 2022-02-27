# Straight down to your spine(After u crash into a "PROTEIN THINGNY" by E235 at 65km/h, imagine that high-speed and safe brought u by JR East and ATC/ATS)
# Be "straight" here for sure: This is for some external features that I just want to share around the repo and test it out
# Btw, remenber what this repo for?


def unwrap(incoming: str):
    dump = incoming
    # What a typical Win32 API(I guess, wmi.WMI().Win32_LogicalDisk()) output looks like:
    # instance of Win32_LogicalDisk
    # {
	# Access = 0;
	# Caption = "C:";
	# Compressed = FALSE;
	# CreationClassName = "Win32_LogicalDisk";
	# Description = "Local Fixed Disk";
	# DeviceID = "C:";
	# DriveType = 3;
	# FileSystem = "NTFS";
	# FreeSpace = "114514191981";
	# MaximumComponentLength = 255;
	# MediaType = 12;
	# Name = "C:";
	# Size = "1145141919810";
	# SupportsDiskQuotas = FALSE;
	# SupportsFileBasedCompression = TRUE;
	# SystemCreationClassName = "Win32_ComputerSystem";
	# SystemName = "NA-ME";
	# VolumeName = "";
	# VolumeSerialNumber = ""; #Your S/N
    # };
    # Messy.
    # So I am gonna process this in this file in my own way(String stuff) before I get a better option(Hope for help on this) 
    try:
        head = dump.index("{")
    except Exception:
        return IOError
    try:
        tail = dump.index("};")
    except Exception:
        return IOError
    dump = dump[head-1:tail-1]
    raw_val = dump.split(";")
    counter = 0
    backed_val = {}
    for i in raw_val:
        name = i.split("\ = \ ")[0]
        data = i.split("\ = \ ")[1]
        backed_val[name] = data
    return backed_val
    
        


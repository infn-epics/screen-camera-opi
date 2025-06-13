from org.csstudio.display.builder.runtime.script import PVUtil, ScriptUtil
import os

StopPrevAcq=True;

logger = ScriptUtil.getLogger()
pv = PVUtil.getString(pvs[0])
device_actual = widget.getEffectiveMacros().getValue("DEVICE")
#print("DEVICE: "+device_actual)
#print("ACTUAL DEVICE '%s'" % device_actual)
print("User selection: " + pv)
#logger.info("SELECTION: " + pv)

#if device_actual and pv:
if pv:
    vals = pv.split(" (")
    cam_name=vals[0]
    print("Camera: "+cam_name)
    #print("PV Name: " + str(pvs[0])) #+ " DEVICE: " + device_actual)
    #trick to update the subpanel
    widget.setPropertyValue("file", "")
    macros = widget.getPropertyValue("macros")
    #do not set the DEVICE, use the one passed through the button!
    #macros.add("DEVICE", device_actual)
    macros.add("CAM", cam_name)
    #macros.add("HW", vals[1])
    widget.setPropertyValue("file", "CompactCamera.bob")

    #append the camera name to a txt file
    home_dir = os.path.expanduser("~")
    file_path = os.path.join(home_dir, "cam_history.txt")
    # Read existing lines (if file exists)
    if os.path.exists(file_path):
        with open(file_path, "r") as file:
            lines = file.readlines()
    else:
        lines = []

    # Keep only last entry (so we have room for 1 old + 1 new = 2 entries)
    lines = lines[-1:]  # last one or empty if file was empty

    # Append new entry
    lines.append(device_actual+":"+cam_name+"\n")

    # Write back only last 2 entries
    with open(file_path, "w") as file:
        file.writelines(lines)

    # Now check: if there are exactly 2 lines, print/display first one
    if len(lines) == 2:
        old_cam = lines[0]
        if "NULL" in old_cam or StopPrevAcq==False:
            pass;
        else:
            #stop acquire
            old_cam=old_cam.replace("\n","")
            pv00=PVUtil.createPV(old_cam+":Acquire",100)
            pv00.setValue(0)
            print("Stopped acquisition of the previous camera: "+old_cam)
else:
	pass




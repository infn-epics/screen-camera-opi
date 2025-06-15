from org.csstudio.display.builder.runtime.script import PVUtil, ScriptUtil
#import os

StopPrevAcq=True;
logger = ScriptUtil.getLogger()
pv = PVUtil.getString(pvs[0])
print("User selection: " + pv)
#logger.info("SELECTION: " + pv)

#if device_actual and pv:
if pv:
    mydev = widget.getEffectiveMacros().getValue("DEVICE")
    old_cam = widget.getEffectiveMacros().getValue("CAM")

    combo = ScriptUtil.findWidgetByName(widget,"CamMenu")
    device_list=combo.getItems()

    for device in device_list:
        if old_cam in device and StopPrevAcq==True:
            #stop acquire
            pv00=PVUtil.createPV(mydev+":"+old_cam+":Acquire",100)
            pv00.setValue(0)
            print("Stopped acquisition of the previous camera: "+old_cam)
            break  # Stop after finding the first match
        else:
            #print(old_cam+" not found in "+device)
            pass;

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
else:
	pass




from org.csstudio.display.builder.runtime.script import PVUtil
from org.csstudio.display.builder.runtime.script import ScriptUtil

logger = ScriptUtil.getLogger()
pv = PVUtil.getString(pvs[0])
device_actual = widget.getEffectiveMacros().getValue("DEVICE")
print("DEVICE: "+device_actual)
#print("ACTUAL DEVICE '%s'" % device_actual)
print("User selection: " + pv)
#logger.info("SELECTION: " + pv)

#if device_actual and pv:
if pv:
    vals = pv.split(" (")
    print("Camera: "+vals[0])
    #newdev = device_actual + vals[0]
    print("PV Name: " + str(pvs[0])) #+ " DEVICE: " + device_actual)
    #trick to update the subpanel
    widget.setPropertyValue("file", "")
    macros = widget.getPropertyValue("macros")
    #do not set the DEVICE, use the one passed through the button!
    #macros.add("DEVICE", "SPARC:CAM")
    macros.add("CAM", vals[0])
    #macros.add("HW", vals[1])
    widget.setPropertyValue("file", "CompactCamera.bob")


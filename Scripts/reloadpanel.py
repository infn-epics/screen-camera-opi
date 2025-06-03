from org.csstudio.display.builder.runtime.script import PVUtil
from org.csstudio.display.builder.runtime.script import ScriptUtil

logger = ScriptUtil.getLogger()
pv = PVUtil.getString(pvs[0])
#device_actual = widget.getEffectiveMacros().getValue("DEVICE")
#print("ACTUAL DEVICE '%s'" % device_actual)
logger.info("SELECTION: " + pv)

#if device_actual and pv:
if pv:
    vals = pv.split()
    #newdev = device_actual + vals[0]
    logger.info("PV Name: " + str(pvs[0]) + " Val: " + vals[0]) #+ " DEVICE: " + device_actual)
    #trick to update the subpanel
    widget.setPropertyValue("file", "")
    macros = widget.getPropertyValue("macros")
    macros.add("DEVICE", "SPARC:CAM")
    macros.add("CAM", vals[0])
    #macros.add("HW", vals[1])
    widget.setPropertyValue("file", "CompactCamera.bob")

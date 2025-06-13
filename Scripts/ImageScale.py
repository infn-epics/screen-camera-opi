from org.csstudio.display.builder.runtime.script import PVUtil, ScriptUtil
# Access the widget (the parent of this script)
# widget = display.getWidget("CameraImage")  # Replace with your widget's name

#try:
#    min_value = PVUtil.getDouble(pvs[0])
#except:
#    min_value = 0
#    print("min_val not initialized")
#
#try:
#    max_value = PVUtil.getDouble(pvs[1])
#except:
#    max_value = 4095
#    print("max_val not initialized")

# Get PV values (replace with your PV names)
min_value = PVUtil.getDouble(pvs[0])
max_value = PVUtil.getDouble(pvs[1])

# Set colormap range
widget.setPropertyValue("minimum", min_value)
widget.setPropertyValue("maximum", max_value)

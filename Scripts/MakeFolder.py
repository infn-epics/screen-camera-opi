from org.csstudio.display.builder.runtime.script import PVUtil
from org.csstudio.display.builder.runtime.script import ScriptUtil
import os

logger = ScriptUtil.getLogger()
folder_path = PVUtil.getString(pvs[0])

make_dir = PVUtil.getDouble(pvs[1])

# Set visibility
if make_dir==1: 
	# Create the folder (including parent folders if they don't exist)
    os.makedirs(folder_path,True)
    logger.info("Created folder: " + folder_path)
else:
	pass

#update the LED, writing different temp folder for a while
pvs[2].write(folder_path+"x")
# Write back original (after small delay if necessary)
pvs[2].write(folder_path)

#at the end put back to 0
pvs[1].write(0);

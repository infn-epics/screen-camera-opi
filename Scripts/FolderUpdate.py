from java.util import Date
from java.text import SimpleDateFormat
from org.csstudio.display.builder.runtime.script import PVUtil
from org.csstudio.display.builder.runtime.script import ScriptUtil
import os

logger = ScriptUtil.getLogger()

# Get current date
date = Date()

# Format date string as YYYY_MM_DD
formatter = SimpleDateFormat("yyyy_MM_dd")
date_string = formatter.format(date)
update_dir = PVUtil.getDouble(pvs[1])

# Set visibility
if update_dir==1:
    logger.info("Today's date string: " + date_string);
    pvs[0].write("/nfs/data/"+date_string);
else:
	pass

#at the end put back to 0
pvs[1].write(0);

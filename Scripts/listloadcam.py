#By default, Phoebus uses Jython for scripting (accessible from the Script or Python panels).
#Jython is a Java-based Python interpreter, and it does not support C extensions—this includes libraries like PyYAML, which are implemented in C.
#You cannot directly import yaml in Phoebus’s Jython scripting environment because PyYAML relies on C extensions.
#To use the YAML functionality in Phoebus --> use Java’s SnakeYAML in Jython
from org.yaml.snakeyaml import Yaml
from java.io import FileReader, BufferedWriter, FileWriter
from java.util import ArrayList

from org.csstudio.display.builder.runtime.script import ScriptUtil,PVUtil
import os
display_model =  widget.getDisplayModel()
display_path = display_model.getUserData(display_model.USER_DATA_INPUT_FILE)
camdir=os.path.dirname(display_path)
#print(camdir)
maindir=os.path.abspath(os.path.join(camdir,'..', '..'))
#maindir=os.path.dirname(opidir)
yaml_file=maindir+"/deploy/values.yaml"
#yaml_file=maindir+"/epik8-sparc/deploy/values.yaml"
print("Loading file '%s'." % yaml_file)

# Load YAML file using SnakeYAML
yaml = Yaml()
data = yaml.load(FileReader(yaml_file))
#print("Top-level keys:", data.keySet())

# Get epicsConfiguration -> iocs list
epics_config = data.get("epicsConfiguration")
if epics_config is None:
    print("No 'epicsConfiguration' found.")
    exit()

iocs = epics_config.get("iocs")
if iocs is None:
    print("No 'iocs' section found.")
    exit()
#print("Number of IOCs found:", len(iocs))

# Find cameras under IOCs with iocprefix ":CAM" and devtype "camera"
#results = ArrayList()
device_list=[]
for ioc in iocs:
    ioc_name = ioc.get("name", "")
    iocprefix = ioc.get("iocprefix", "")
    devtype = ioc.get("devtype", "")
    #print("Checking IOC:", ioc_name, "iocprefix:", iocprefix, "devtype:", devtype)    
    if iocprefix and iocprefix.endswith(":CAM") and devtype == "camera":
        cameras = ioc.get("devices", [])
        if cameras:
            for cam in cameras:
                cam_name = cam.get("name", "")
                if cam_name:
                    #results.add((cam_name, ioc_name))
                    out_str=cam_name+" ("+ioc_name+")"
                    device_list.append(out_str)
                    print("Found: "+out_str)

# Sort results by camera name
#results.sort(key=lambda x: x[0])
device_list.sort()

####################################
#put the list in the cam menu box
combo = ScriptUtil.findWidgetByName(widget,"CamMenu")
combo.setItems(device_list)
if len(device_list): #remove the first item (pv initialization)
    ScriptUtil.getPrimaryPV(combo).write(device_list[0])
print("Cam menu updated!")


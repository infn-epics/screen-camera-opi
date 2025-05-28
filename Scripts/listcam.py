#By default, Phoebus uses Jython for scripting (accessible from the Script or Python panels).
#Jython is a Java-based Python interpreter, and it does not support C extensions—this includes libraries like PyYAML, which are implemented in C.
#You cannot directly import yaml in Phoebus’s Jython scripting environment because PyYAML relies on C extensions.
#To use the YAML functionality in Phoebus --> use Java’s SnakeYAML in Jython
from org.yaml.snakeyaml import Yaml
from java.io import FileReader, BufferedWriter, FileWriter
from java.util import ArrayList

# Load YAML file using SnakeYAML
yaml = Yaml()
data = yaml.load(FileReader("epik8-sparc/deploy/values.yaml"))
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

# Find cameras under IOCs with iocprefix "SPARC:CAM" and devtype "camera"
results = ArrayList()
for ioc in iocs:
    ioc_name = ioc.get("name", "")
    iocprefix = ioc.get("iocprefix", "")
    devtype = ioc.get("devtype", "")
    #print("Checking IOC:", ioc_name, "iocprefix:", iocprefix, "devtype:", devtype)    
    if iocprefix and iocprefix.startswith("SPARC:CAM") and devtype == "camera":
        cameras = ioc.get("cameras", [])
        if cameras:
            for cam in cameras:
                cam_name = cam.get("name", "")
                if cam_name:
                    results.add((cam_name, ioc_name))

# Sort results by camera name
results.sort(key=lambda x: x[0])

# Write to file
output_file = "epik8-sparc/opi/ini/sparc_cam.ini"
writer = BufferedWriter(FileWriter(output_file))
try:
    for pair in results:
        writer.write("%s\t%s\n" % (pair[0], pair[1]))
    writer.flush()
finally:
    writer.close()
print("Camera names with IOC names have been exported to '%s'." % output_file)


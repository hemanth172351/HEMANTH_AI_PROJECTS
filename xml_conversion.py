import sys

import lxml.etree as ET

# inFile = sys.argv[1]
inFile = "C:\\Users\\heman\\Downloads\\example.xml"
print(f"File Name is:{inFile}")
dom = ET.parse(inFile)
print(f"DOM object is:{dom}")
xslt = ET.parse('C:\\Users\\heman\\Downloads\\MAT_LIM.xsl')
print(f"XSLT is: {xslt}")
transform = ET.XSLT(xslt)
print(f"transform is:{transform}")
newdom = transform(dom)
print(f"New DOM is:{newdom}")
print(ET.tostring(newdom, pretty_print=True))
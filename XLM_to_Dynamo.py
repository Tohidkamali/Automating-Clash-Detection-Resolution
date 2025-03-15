import xml.etree.ElementTree as ET

file_path = IN[0]
tree = ET.parse(file_path)
root = tree.getroot()

clash_ids, element1_ids, element2_ids, clash_locations = [], [], [], []

for clash in root.findall(".//clashresult"):
    clash_id = clash.get("name")
    clash_ids.append(clash_id)

    clashpoint = clash.find("clashpoint/pos3f")
    x, y, z = float(clashpoint.get("x")), float(clashpoint.get("y")), float(clashpoint.get("z"))
    clash_locations.append([x, y, z])

    clashobjects = clash.findall("clashobjects/clashobject")
    element1_ids.append(clashobjects[0].find("objectattribute/value").text)
    element2_ids.append(clashobjects[1].find("objectattribute/value").text)

OUT = clash_ids, element1_ids, element2_ids, clash_locations

import json
import xml.etree.ElementTree as ET

with open('test/data_Source_3.json') as json_file:
    data = json.load(json_file, strict=False)


class Product1:
    def __init__(self, name, id, EANs):
        self.data = 'data_source_3'
        self.name = name
        self.id = id
        self.EAN = EANs


objects = []
for el in range(len(data)):
    objects.append(Product1(data[el]['name'], data[el]['Id'], data[el]['EANs'][0]))


class Product2:
    def __init__(self, name, EAN, id):
        self.data = 'data_source_1'
        self.name = name
        self.id = id
        self.EAN = EAN


object1 = []
tree = ET.parse("test/data_Soruce_1.xml")
for element in tree.findall("SHOPITEM"):
    name = element.find("NAME").text
    id = element.find("id").text
    try:
        EAN = element.find("EAN").text
    except:
        EAN = "none"
    object1.append(Product2(name, EAN, id))


class Product3:
    def __init__(self, name, EAN, id):
        self.data = 'data_source_2'
        self.name = name
        self.EAN = EAN
        self.id = id


object2 = []
tree = ET.parse("test/data_Source_2.xml").getroot()
for element in tree.findall("Product"):
    EAN = element.find("EAN").text
    id = element.find("id").text
    name = element.find("Description").text
    object2.append(Product3(name, EAN, id))

i = Product1
if i == Product2:
    print(name)

sort = []
for el1 in range(len(objects)):
    el11 = objects[el1].__dict__
    el111 = el11['EAN']
    for el2 in range(len(object1)):
        el22 = object1[el2].__dict__
        el222 = el22['EAN']
        if el111 == el222:
            for el3 in range(len(object2)):
                el33 = object2[el3].__dict__
                el333 = el33['EAN']
                # print(el111, el222, el333)
                if el111 == el222 and el111 == el333:
                    sort.append(el22)
                    sort.append(el33)
                    sort.append(el11)
                else:
                    pass
        else:
            pass

with open("data_file.json", "w") as write_file:
    json.dump(sort, write_file, indent=4)

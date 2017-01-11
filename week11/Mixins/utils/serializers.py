import json
import xml.etree.ElementTree as ET


class Jsonable:

    json_types = (int, str, bool, float, list, tuple, None, dict)

    def to_json(self, indent=4):
        data = {
                    'dict': {},
                    'class_name': self.__class__.__name__
               }

        for k, v in self.__dict__.items():
            if type(v) in self.json_types:
                data['dict'][k] = v

        return json.dumps(data, indent=indent)

    @classmethod
    def from_json(cls, json_string):
        data = json.loads(json_string)
        name = data.get('class_name', None)  # we don't throw key error if
        # not valid key
        if cls.__name__ != name:
            raise ValueError("Not a valid instance of {}!"
                             .format(cls.__name__))
        return cls(**data['dict'])


class Xmlable:

    def to_xml(self):
        class_name = ET.Element(self.__class__.__name__)
        ET.SubElement(class_name, 'name').text =\
            "{}".format(self.__dict__['name'])
        return ET.tostring(class_name).decode('utf8')

    @classmethod
    def from_xml(cls, xml_string):
        root = ET.fromstring(xml_string)

        if root.tag != cls.__name__:
            raise ValueError("Not a valid instance!")

        data = {}

        for child in root:
            data[child.tag] = child.text

        return cls(**data)

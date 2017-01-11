from serializers import Jsonable, Xmlable


class Panda(Jsonable, Xmlable):

    def __init__(self, name):
        self.name = name

    def __eq__(self, other):
        return self.name == other.name

    def __str__(self):
        return "{}".format(self.name)

    def __repr__(self):
        return self.__str__()


def main():
    p = Panda("Pesho")
    # print(p.to_json())
    # print(p.to_xml())

    # json_string = p.to_json()
    # p1 = Panda.from_json(json_string)
    # print(p1)
    xml_string = p.to_xml()
    p1 = Panda.from_xml(xml_string)
    # print(xml_string)
    print(p1)


if __name__ == '__main__':
    main()

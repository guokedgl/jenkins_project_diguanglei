import yaml


def read_setting(filename, key_name):
    with open("./data/" + filename + ".yaml","r",encoding="utf-8") as f:
        data = yaml.load(f)[key_name]
        list1 = []
        list1.extend(data.values())
        return list1

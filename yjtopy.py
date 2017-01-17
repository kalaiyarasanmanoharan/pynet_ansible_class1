import yaml
import json

with open ("json_file.json") as j:
    my_json_list = json.load(j)

print "After reading the Json file, here is the list output\n"
print my_json_list

with open ("ex_file1.yml") as y:
    my_yaml_list = yaml.load(y)

print "After reading the Yaml  file, here is the list output\n"
print my_yaml_list

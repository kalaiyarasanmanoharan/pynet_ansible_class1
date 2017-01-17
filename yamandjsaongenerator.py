import sys
import yaml
import json
my_list = [ 1,2,3,4,5,6,7,8,9,10,{"ip_addr":"10.0.0.1","model": "Nexus", "Usage": "Router", "Attrib": [1,2,3,4]}]
print 'Got the List, working on creating a yaml file'

with open("ex_file1.yml" , "w") as y:
    yaml.dump(my_list, y)

print 'yaml value dumped'

with open("json_file.json" , "w") as j:
    json.dump(my_list,j)


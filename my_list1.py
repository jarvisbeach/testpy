#!/usr/bin/python
import yaml

my_list1 = [ 10, 20, 30, 40, {'name': 'john', 'hometown': 'chicago', 'favorite_numbers':[3,23,33]}]  
print my_list1

with open("some_yaml_file.yml", "w") as f:
    f.write(yaml.dump(my_list1, default_flow_style=False))



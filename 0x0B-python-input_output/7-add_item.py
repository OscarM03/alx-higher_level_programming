#!/usr/bin/python3
import sys
import json
save_to_json_file = __import__('5-save_to_json_file').save_to_json_file
load_from_json_file = __import__('6-load_from_json_file').load_from_json_file
filename = "add_item.json"


args_list = []
for word in sys.argv[1:]:
    args_list.append(str(word))

save_to_json_file(args_list, filename)
j_file = load_from_json_file(filename)
print(j_file)



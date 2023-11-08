
#!/usr/bin/python3
def complex_delete(a_dictionary, value):
    if input_dict:
        keys_to_delete = []
        for key, val in input_dict.items():
            if val == target_value:
                keys_to_delete.append(key)
        if keys_to_delete:
            num_keys_to_delete = len(keys_to_delete)
            i = 0
            while num_keys_to_delete > 0:
                input_dict.pop(keys_to_delete[i])
                i += 1
                num_keys_to_delete -= 1
        return input_dict

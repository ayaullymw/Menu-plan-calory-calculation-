def add_record(data_dict, key, value):
    data_dict[key] = value

def delete_record(data_dict, key):
    if key in data_dict:
        del data_dict[key]

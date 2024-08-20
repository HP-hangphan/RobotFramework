def convert_to_dict(data):
    columns = list(data.keys())[0].split(',')
    values = data[list(data.keys())[0]].split(',')
    result_dict = dict(zip(columns, values))
    return result_dict
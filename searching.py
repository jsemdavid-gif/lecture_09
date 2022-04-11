import os
import json

# get current working directory path
cwd_path = os.getcwd()


def read_data(file_name, field):
    """
    Reads json file and returns sequential data.
    :param file_name: (str), name of json file
    :param field: (str), field of a dict to return
    :return: (list, string),
    """
    with open(file_name) as datafile:
        data = json.load(datafile)

    if field in data.keys():
        sequential_data = data[field]
        print(sequential_data)
        return sequential_data
    else:
        return None




def linear_search(sekvence,cislo):
    dict = {"positions":[],"count":[]}
    count = 0
    for index,num in enumerate(sekvence):

        if cislo == num:
            count = count+1
            dict["positions"].append(index)
    dict["count"].append(count)
    print(dict)
    return dict


def main():
    sequenc = read_data("sequential.json","unordered_numbers")
    linear_search(sequenc,9)
    pass


if __name__ == '__main__':
    main()
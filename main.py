
import json
import sys
import pprint

with open(sys.argv[1]) as json_data:
   data = json.load(json_data)


def flatten_json(data2flatten):
    flat_data = { }

    def do_flatten(y, name=''):

        # if nested key-value
        #pair is of type dict then recurse
        if type(y) is dict:
            for n in y:
                do_flatten(y[n], name + n + '.')

        #nested key value pair of type list
        elif type(y) is list:
            i = 0

            for n in y:
                do_flatten(n, name + str(i) + '.')
                i +=1
        else:
            flat_data[name[:-1]] = y

    do_flatten(data2flatten)
    return flat_data


flattened_data = flatten_json(data)
pprint.pprint(flattened_data, indent = 3, width= 20)
import json
from pprint import pprint

def prYellow(prt): print("\033[93m {}\033[00m" .format(prt))
def prBoldBlue(prt): print("\033[1;94m {}\033[00m" .format(prt))

def list_to_path(liste):
    path=""
    for l in liste:
        path = l + "/"
    return path

def get_model():
    with open('model.json') as data_file:    
            models = json.load(data_file)
            model = models[0]
            return model

def get_data():
    with open('data.json') as data_file:
            objects = json.load(data_file)
            return objects

def create_updated_data(data, child):
    updated = []

    for d in data:
     #   print("****D *****")
     #   pprint(d)
     #   print(child)
        if d.get(child) != None:
            updated.append(d[child])

    return updated

def data_has_key(key, data, path):
    for obj in data:

    #    print("Checking: " + key + " in " + str(obj) + "\n\n")

        if obj.get(key) == None:
            formattedPath = list_to_path(path) + key
            print("\033[93mLooked everywhere for \033[00m" + "\033[1;94m" + formattedPath + "\033[00m" +"\033[93m but couldn't find him anywhere :(\033[00m")
            optionals.append(formattedPath)
            break
   #     else:
  #          print("Found:" + key + " - Run!")

def has_key(dictionary, data, path):
    for k, v in dictionary.iteritems():

        data_has_key(k, data, path)
        if type(v) == dict:
 #           print "******************************************************************************************************************************DICT"
 #           print(v) # from attributes
 #           print(k) # from
            path.append(k)
            has_key(v, create_updated_data(data, k), path)
            path.remove(k)


model = get_model()
objects = get_data()
optionals = []
path = []

#pprint("***************************** Data Model ***********************")
#pprint(model)

has_key(model, objects, path)

print("\n")
prYellow("Here is the list of all missing kittens:")
print("")

for o in set(optionals):
    prBoldBlue("\t" + o)



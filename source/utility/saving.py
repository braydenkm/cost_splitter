import pickle
import os


def save_group(group):
  filename = './saves/' + group.name + '.pkl'
  save_object(group, filename)


def save_object(obj, filename):
  with open(filename, 'wb') as output:
    pickle.dump(obj, output, pickle.HIGHEST_PROTOCOL)



def load_all_groups():
  return load_all('./saves', '.pkl')


def load_object(filename):
  with open(filename, 'rb') as input:
    obj = pickle.load(input)
  return obj


def load_all(directory, extension):
  objects = {}
  for filename in os.listdir(directory):
    if filename.endswith(extension):
      obj = load_object(directory+ '/' + filename)
      objects[obj.name] = obj
  return objects
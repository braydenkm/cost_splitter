import pickle
import os

SAVE_LOCATION = './saves/'


# Returns a path to save file.
def make_path(filename):
  return SAVE_LOCATION + filename + '.pkl'


# Save a single group, this will overwrite an existing save.
def save_group(group):
  save_object(group, make_path(group.name))


# Save a single object to filename.
def save_object(obj, filename):
  with open(filename, 'wb') as output:
    pickle.dump(obj, output, pickle.HIGHEST_PROTOCOL)


# Returns a dictionary of all saved groups.
def load_all_groups():
  return load_all(SAVE_LOCATION, '.pkl')


# Loads a single object from filename.
def load_object(filename):
  with open(filename, 'rb') as input:
    obj = pickle.load(input)
  return obj


# Returns a dictionary of saved objects from directory
# if they end with extension.
def load_all(directory, extension):
  objects = {}
  if not os.path.exists(directory):
    os.makedirs(directory)
  for filename in os.listdir(directory):
    if filename.endswith(extension):
      obj = load_object(directory + filename)
      objects[obj.name] = obj
  return objects


# Delete a group from saves.
def delete_group(group):
  delete_object(make_path(group.name))


# Delete an object file from directory.
def delete_object(filepath):
  if os.path.exists(filepath):
    os.remove(filepath)
  else:
    print('ERR: File could not be found')

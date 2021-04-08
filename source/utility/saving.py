import pickle
import os


# Save a single group, this will overwrite an existing save.
def save_group(group):
  filename = './saves/' + group.name + '.pkl'
  save_object(group, filename)


# Save a single object to filename.
def save_object(obj, filename):
  with open(filename, 'wb') as output:
    pickle.dump(obj, output, pickle.HIGHEST_PROTOCOL)


# Returns a dictionary of all saved groups.
def load_all_groups():
  return load_all('./saves', '.pkl')


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
      obj = load_object(directory+ '/' + filename)
      objects[obj.name] = obj
  return objects


# Delete a group from saves.
def delete_group(group):
  directory = './saves'
  filename = group.name + '.pkl'
  delete_object(directory, filename)


# Delete an object file from directory.
def delete_object(directory, filename):
  file_path = directory + '/' + filename
  if os.path.exists(file_path):
    os.remove(file_path)
  else:
    print('ERR: File could not be found')

import sys
import os
sys.path.append(os.path.join(os.path.dirname(__file__), "class"))
sys.path.append(os.path.join(os.path.dirname(__file__), "utility"))

import Group
import saving as s


# List the group names.
def list_group_names(groups):
  string = ''
  for name in groups:
    string += '  ' + name + '\n'
  print(string)


# Prints group menu options.
def print_group_menu(group_name):
    print(
    "\n[" + group_name + "] - Group Menu\n" \
    " 1. Print Group\n" \
    " 2. Add Purchase\n" \
    " 3. List Transactions\n" \
    " 4. List Members\n" \
    " 5. Add Member\n" \
    " 6. Remove Member\n" \
    " q or exit. Quit\n" \
    " > ", end="")


# Loops through single group menu.
def group_menu(group):
  user_in = ''
  while user_in != 'exit' and user_in != 'q':
    print_group_menu(group.name)
    user_in = input()
    print('\n')

    # Print group.
    if user_in == '1':
      print('Group Information:')
      group.print_group()
      print('')
    
    # Add purchase.
    if user_in == '2':
      print('Which member paid for this purchase?: ', end='')
      paying_member = input()
      print('How much did the purchase cost?: ', end='')
      amount_paid = int(input())
      group.add_purchase(group.members[paying_member], amount_paid)
      s.save_group(group)

    # List transactions.
    if user_in == '3':
      if len(group.transactions) == 0:
        print('No past transactions')
        continue
      print('Past Transactions')
      for purchase in group.transactions:
        print('  ' + purchase.as_string())

    # List members.
    if user_in == '4':
      if len(group.members) == 0:
        print('No members in group')
        continue
      print('Group Members')
      for person in group.members:
        print('  ' + group.members[person].as_string())

    # Add new member.
    if user_in == '5':
      print('Enter name of member to add: ', end='')
      member_name = input()
      if member_name in group.members:
        print('"' + member_name+ '" already exists in list of members.')
        continue
      group.add_member(member_name)
      s.save_group(group)
    
    # Remove existing member.
    if user_in == '6':
      print('Enter name of member to remove: ', end='')
      member_name = input()
      if member_name not in group.members:
        print('"' + member_name+ '" cannot be found in list of members.')
        continue
      group.remove_member(member_name)
      s.save_group(group)


# Prints the main menu options.
def print_main_menu():
  print(
    "Main Menu\n" \
    " 1. Print Groups\n" \
    " 2. Select Group\n" \
    " 3. Add Group\n" \
    " 4. Remove Group\n" \
    " q or exit. Quit\n" \
    " > ", end="")


# Entrance to program.
# Loops through main menu.
def main():
  print('\n- Cost Splitter -')

  # Load save.
  groups = s.load_all_groups()
  if groups is None:
    groups = {}

  # Loop.
  user_in = ''
  while user_in != 'exit' and user_in != 'q':
    print_main_menu()
    user_in = input()
    print('')

    # Print groups.
    if user_in == '1':
      if len(groups) == 0:
        print('No stored groups')
        continue
      print('Stored Groups:')
      for group_name in groups:
        groups[group_name].print_group()
        print('')
    
    # Select group.
    if user_in == '2':
      print('Which group would you like to select?:')
      list_group_names(groups)
      group_name = input()
      if group_name not in groups:
        print('Group ' + group_name + ' does not exist\n')
        continue
      group_menu(groups[group_name])

    # Add new group.
    if user_in == '3':
      print('Enter name of group to add: ', end='')
      group_name = input()
      if group_name in groups:
        print('"' + group_name+ '" already exists in list of groups.')
        continue
      groups[group_name] = Group.Group(group_name)
      s.save_group(groups[group_name])
      # Select group automatically after creation.
      group_menu(groups[group_name])
    
    # Remove existing group.
    if user_in == '4':
      print('Enter name of group to remove:')
      list_group_names(groups)
      group_name = input()
      if group_name not in groups:
        print('"' + group_name+ '" cannot be found in list of groups.')
        continue
      deleted_group = groups.pop(group_name)
      s.delete_group(deleted_group)


if __name__ == '__main__':
  main()
import sys
sys.path.append("C:\\Users\\Brayden\\Documents\\Code\\cost_splitter\\source\\classes")

import Group


# Prints group menu options.
def print_group_menu(group_name):
    print(
    "\n[" \
    + group_name + "] Menu\n" \
    " 1. Print Group\n" \
    " 2. Add Purchase\n" \
    " 3. Add Member\n" \
    " 4. Remove Member\n" \
    " q or exit. Quit\n" \
    " > ", end="")


# Loops through single group menu.
def group_menu(group):
  user_in = ''
  while user_in != 'exit' and user_in != 'q':
    print_group_menu(group.name)
    user_in = input()

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

    # Add new member.
    if user_in == '3':
      print('Enter name of member to add: ', end='')
      member_name = input()
      if member_name in group.members:
        print('"' + member_name+ '" already exists in list of members.')
        continue
      group.add_member(member_name)
    
    # Remove existing member.
    if user_in == '4':
      print('Enter name of member to remove: ', end='')
      member_name = input()
      if member_name not in group.members:
        print('"' + member_name+ '" cannot be found in list of members.')
        continue
      group.remove_member(member_name)


# Prints the main menu options.
def print_main_menu():
  print(
    "\n" \
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
  print('- Cost Splitter -')
  groups = {}

  user_in = ''
  while user_in != 'exit' and user_in != 'q':
    print_main_menu()
    user_in = input()

    # Print groups.
    if user_in == '1':
      print('Stored Groups:')
      for group_name in groups:
        groups[group_name].print_group()
        print('')
    
    # Select group.
    if user_in == '2':
      print('Which group would you like to select?:')
      group_name = input()
      group_menu(groups[group_name])

    # Add new group.
    if user_in == '3':
      print('Enter name of group to add: ', end='')
      group_name = input()
      if group_name in groups:
        print('"' + group_name+ '" already exists in list of groups.')
        continue
      groups[group_name] = Group.Group(group_name)
      # Select group automatically after creation.
      group_menu(groups[group_name])
    
    # Remove existing group.
    if user_in == '4':
      print('Enter name of group to remove: ', end='')
      group_name = input()
      if group_name not in groups:
        print('"' + group_name+ '" cannot be found in list of groups.')
        continue
      groups.pop(group_name)

if __name__ == '__main__':
  main()
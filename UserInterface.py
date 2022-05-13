import Classes
import datetime as timer

def main_menu():
  main_menu_actions = {"first": "1","second": "2", "third": "3", "exit": "q"}
  main_menu_string = f"Welcome to Pool Table Manager\n\nPress {main_menu_actions['first']} to edit a table or view it's details\nPress {main_menu_actions['second']} to load saved tables\nPress {main_menu_actions['exit']} to exit the program\n"
  
  pool_tables = {}

  while len(pool_tables) <= 11:
        pool_tables[str(len(pool_tables) + 1)] = Classes.PoolTable(len(pool_tables) + 1)
  while True:

    if len(pool_tables) > 0:
      print_tables(pool_tables)
    menu_input = input(main_menu_string)
    if menu_input == main_menu_actions["first"]:
      table_view_menu(pool_tables)
    elif menu_input == main_menu_actions["second"]:
      print("What saved table history do you want to read?")
      year = input('Please enter the year\n Format of "YYYY"\n')
      month = input('Please enter the month\n Format of "MM"\n')
      day = input('Please enter the day\n Format of "DD"\n')
      full_file_name = f"{month}-{day}-{year}.json"
      Classes.file_manager(full_file_name, [], "r")
      input("press any key to continue...")

    elif menu_input.lower() == main_menu_actions["exit"]:
      break


def table_view_menu(tables):

  table_numbers_string = ""
  table_divider = "--------------------------"
  for table in tables:
    table_numbers_string += (str(table) + ",")
  menu_string = f"Which table do you want to view?\nValid table numbers are {table_numbers_string}\ntype q to exit view\n"
  while True:
    menu_inputs = input(menu_string)
    if menu_inputs.lower() == "q":
      break
    elif tables[menu_inputs] != None:

      is_editing = True
      while is_editing == True:
        print(table_divider)
        tables[menu_inputs].print_table_info()
        print(table_divider)
        table_edit_string = ""
        if tables[menu_inputs].is_occupied:
          table_edit_string  = "What do you want to do with this table?\n1: Close out the table\nq: stop viewing\n"
        else:
          table_edit_string = "What do you want to do with this table?\n1: Book the table\nq: stop viewing\n"
          
        table_edit_input = input(table_edit_string)
        if table_edit_input == "1":
          if tables[menu_inputs].is_occupied:
            end_time = timer.datetime.now()
            tables[menu_inputs].table_finishes(end_time, f"{end_time.month}-{end_time.day}-{end_time.year}.json")
          else:
            tables[menu_inputs].occupy_table(timer.datetime.now())
        elif table_edit_input.lower() == "q":
          is_editing = False

def print_tables(tables):
  table_header = "**********TABLES**********"
  table_closer = "**************************"
  table_divider = "--------------------------"

  print(table_header)
  for table in tables:
    print(table_divider)
    tables[table].print_table_info()
    print(table_divider)
  print(table_closer)
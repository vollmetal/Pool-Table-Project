import unittest
import Classes as ClassFile
import datetime as timer
import os as operating_system
import UserInterface

class TableTests(unittest.TestCase):

  def setUp(self):
    self.pool_tables = []
    self.pool_tables.append(ClassFile.PoolTable(1))
    
  #@unittest.skip("Not testing Tables")
  def test_table(self):
    print(self.pool_tables[0].readable_datetime(timer.datetime.now()))


    print(self.pool_tables[0].convert_time(36950))
    start_time = timer.datetime(1, 12, 30, 1, 0, 59)

    self.pool_tables[0].occupy_table(start_time)

    
    end_time = timer.datetime(1, 12, 30, 1, 50, 59)
    self.pool_tables[0].table_finishes(end_time, f"{end_time}.json")
    #self.pool_tables[0].print_table_info()
    ClassFile.file_manager(f"{end_time}.json", {}, "r")
    operating_system.remove(f"{end_time}.json")

  @unittest.skip("Not testing File Manager")
  def test_file_manager(self):
    ClassFile.file_manager("fubar.txt", ["hello", " world"])
    ClassFile.file_manager("fubar.txt", [], "r")
    operating_system.remove("./fubar.txt")

#unittest.main()
UserInterface.main_menu()
import unittest
import Classes as ClassFile
import datetime as timer
import os as operating_system

class TableTests(unittest.TestCase):

  def setUp(self):
    self.pool_tables = []
    self.pool_tables.append(ClassFile.PoolTable(1))

  def test_table(self):
    
    start_time = timer.datetime.now()
    #self.pool_tables[0].print_table_info()
    self.pool_tables[0].table_finishes(start_time, f"{start_time}")

    self.pool_tables[0].occupy_table(timer.datetime.now())
    x = 0
    while x < 500000:
      x += 1
    end_time = timer.datetime.now()
    end_time_date = end_time.date()
    end_time_date_string = f"{end_time_date.month}, {end_time_date.day}, {end_time_date.year}"
    self.pool_tables[0].table_finishes(end_time, f"{end_time_date_string}.txt")
    self.pool_tables[0].print_table_info()
    ClassFile.file_manager(f"{end_time_date_string}.txt", [], "r")
    operating_system.remove(f"{end_time_date_string}.txt")

  def test_file_manager(self):
    ClassFile.file_manager("fubar.txt", ["hello", " world"])
    ClassFile.file_manager("fubar.txt", [], "r")
    operating_system.remove("./fubar.txt")

unittest.main()
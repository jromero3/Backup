class Region():
    def __init__(self):
        self.name = ""

class Suppliers():
    def __init__(self):
        self.CompanyName = "MS"

class Connection():
    def __init__(self, connection_string):
        self.connect_string = connection_string

class ReadOperation():
    def __init__(self, sql):
        self.ops = sql

class Program_Main():
    def __init__(self):
        self.result = ""

    def crud_operation(self):
        # Need an object representing the table
        # I need the sql statement to run
        # I need the connection object to send query to the database
        result = ""

main_prog = Program_Main()
main_prog.run()

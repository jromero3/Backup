import pyodbc

class Customers():
    def __init__(self, Customer_ID, Company_Name, Contact_Name, Contact_Title, Address, City, Region, Postal_Code, Country, Phone,
                 Fax):
        self.CustomerID = Customer_ID
        self.CompanyName = Company_Name
        self.ContactName = Contact_Name
        self.ContactTitle = Contact_Title
        self.Address = Address
        self.City = City
        self.Region = Region
        self.PostalCode = Postal_Code
        self.Country = Country
        self.Phone = Phone
        self.Fax = Fax
        self.server = ""
        self.database_name = "NORTHWND"
        self.user_name = ""
        self.password = ""


        #docker_Northwind = pyodbc.connect('Driver={SQL Server Native Client 11.0};np:\\\\.\pipe\LOCALDB#844FDE7F\\tsql\query\\\\v11.0;integrated security = true')
        self.docker_Northwind = pyodbc.connect('Driver={SQL Server};'
                              'Server=(local);'
                              'Database=NORTHWND;'
                             'Trusted_Connection=yes;'
                              'Integrated Security=SSPI;')
        self.name_pipe = "np:\\.\pipe\LOCALDB#9C917E5E\tsql\query"
        self.cursor = self.docker_Northwind.cursor()


    def save_to_database(self):
        sql_insert = "INSERT INTO Customers (CompanyName, ContactName, ContactTitle, Address, City, Region, " \
                     "PostalCode, Country, Phone, Fax) VALUES ({}, {}, {}, {}, {}, {}, {}, {}, {}, {}, {});"\
            .format(self.CustomerID, self.CompanyName, self.ContactName, self.ContactTitle, self.Address, self.City,
                    self.Region, self.PostalCode, self.Country, self.Phone, self.Fax)
        # print(sql_insert)
        self.cursor.execute(sql_insert)
        self.cursor.commit()

customer1 = Customers("SPRTN", "SpartaGlobal", "James", "Sir", "Homeless", "London", "SE", "WD2", "UK", "077", "What?")
customer1.save_to_database()


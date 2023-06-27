import sqlite3
from datetime import datetime
import time
from objects import Employer,Employee,Client,Product,History,Log

def_us="admin"
def_pw="12345"

class DBmanager:
    def __init__(self) -> None:
        self.connection=sqlite3.connect("stockMarket.db")
        self.cursor=self.connection.cursor()
        self.create_tables()

    def logIn(self,username,password):
        self.cursor.execute(f"SELECT username,password FROM employer")
        employers=self.cursor.fetchall()
        for i in employers:
            if username==i[0] and password==i[1]:
                return True

        self.cursor.execute(f"SELECT username,password FROM employee")
        employees=self.cursor.fetchall()
        for i in employees:
            if username==i[0] and password==i[1]:
                return False
        return None
    
    def addProduct(self,product:Product):
        sql="INSERT INTO product (name,cost,price,quantity,category) VALUES(?,?,?,?,?)"
        values=(product.name,
                product.cost,
                product.price,
                product.quantity,
                product.category)
        self.cursor.execute(sql,values)
        try:
            self.connection.commit()
        except sqlite3.Error as e:
            print(e)

    def getProducts(self):
        self.cursor.execute("SELECT * FROM product")
        try:
            obj= self.cursor.fetchall()
            return Product.createProduct(obj)
        except sqlite3.Error as e:
            print(e)

    def getProductByName(self,name):
        self.cursor.execute("SELECT * FROM product WHERE name=?",(name,))
        try:
            obj= self.cursor.fetchone()
            return Product.createProduct(obj)
        except sqlite3.Error as e:
            print(e)

    def getProductsByName(self,name):
        name=f"%{name}%"
        self.cursor.execute("SELECT * FROM product WHERE name LIKE ?",(name,))
        try:
            obj= self.cursor.fetchall()
            return Product.createProduct(obj)
        except sqlite3.Error as e:
            print(e)

    def updatePrice(self,product:Product):
        sql="UPDATE product SET cost=?,price=? WHERE name=?"
        values=(product.cost,product.price,product.name)
        self.cursor.execute(sql,values)
        try:
            self.connection.commit()
        except sqlite3.Error as e:
            print(e)
  
    def editProduct(self,product:Product):
        sql="UPDATE product SET name=?,cost=?,price=?,quantity=?,category=? WHERE id=?"
        values=(product.name,product.cost,product.price,product.quantity,product.category,product.id)
        self.cursor.execute(sql,values)
        try:
            self.connection.commit()
        except sqlite3.Error as e:
            print(e)
     
    def addIntoHistory(self,history:History):
        sql="INSERT INTO history (name,cost,price,quantity,category,soldTo,soldDate,employee) VALUES(?,?,?,?,?,?,?,?)"
        values=(history.name,
                history.cost,
                history.price,
                history.quantity,
                history.category,
                history.soldTo,
                history.soldDate,
                history.employee)
        self.cursor.execute(sql,values)
        try:
            self.connection.commit()
        except sqlite3.Error as e:
            print(e)

    def getProductsInBox(self):
        self.cursor.execute("SELECT * FROM history")
        try:
            obj=self.cursor.fetchall()
            return History.createBox(obj)
        
        except sqlite3.Error as e:
            print(e)

    def getHistoryByDate(self,date):
        name=f"%{date}%"
        self.cursor.execute("SELECT soldDate,name,cost,price,quantity,soldTo,employee,ROUND(price-cost) FROM history WHERE soldDate LIKE ? ORDER BY soldDate DESC",(name,))
        try:
            obj= self.cursor.fetchall()
            return obj
        except sqlite3.Error as e:
            print(e)

    def getLatestProductsSold(self):
        self.cursor.execute("SELECT soldDate,name,cost,price,quantity,soldTo,employee,ROUND(price-cost) FROM history ORDER BY soldDate DESC")
        try:
            obj=self.cursor.fetchall()
            return obj
        
        except sqlite3.Error as e:
            print(e)

    def getMostProductsSold(self):
        self.cursor.execute("SELECT id,name,cost,price,SUM(quantity) as totalSold,category,soldTo,soldDate,employee FROM history GROUP BY name ORDER BY totalSold DESC")
        try:
            obj=self.cursor.fetchall()
            return History.createBox(obj)
        
        except sqlite3.Error as e:
            print(e)

    def getHistoryProducts(self):
        self.cursor.execute("SELECT id,name,cost,price,ROUND(SUM(price)-SUM(cost)) as netProfit,SUM(quantity) as totalSold,category,soldTo,soldDate,employee FROM history GROUP BY name ORDER BY netProfit DESC")
        try:
            obj=self.cursor.fetchall()
            return obj
        
        except sqlite3.Error as e:
            print(e)

    def decreaseQuantity(self,productName,productQuantity):
        sql="UPDATE product SET quantity = quantity - ? WHERE name=?"
        values=(productQuantity,productName)
        self.cursor.execute(sql,values)
        try:
            self.connection.commit()
        except sqlite3.Error as e:
            print(e)

    def addEmployee(self,employee:Employee):
        sql="INSERT INTO employee(name,phone,email,username,password) VALUES(?,?,?,?,?)"
        values=(employee.name,
                employee.phone,
                employee.email,
                employee.username,
                employee.password)
        self.cursor.execute(sql,values)
        try:
            self.connection.commit()
            print("Added employee")
        except sqlite3.Error as e:
            print(e)

    def getEmployees(self):
        self.cursor.execute("SELECT * FROM employee")
        try:
            obj= self.cursor.fetchall()
            return Employee.createEmployee(obj)
        except sqlite3.Error as e:
            print(e)

    def getEmployeeByName(self,name):
        self.cursor.execute("SELECT * FROM employee WHERE name= ?",(name,))
        try:
            obj= self.cursor.fetchone()
            return Employee.createEmployee(obj)
        except sqlite3.Error as e:
            print(e)

    def editEmployee(self,employee:Employee):
        sql="UPDATE employee SET name=?,phone=?,email=?,username=?,password=? WHERE id=?"
        values=(employee.name,employee.phone,employee.email,employee.username,employee.password,employee.id)
        self.cursor.execute(sql,values)
        try:
            self.connection.commit()
        except sqlite3.Error as e:
            print(e)

    def getEmployeesByName(self,name):
        name=f"%{name}%"
        self.cursor.execute("SELECT * FROM employee WHERE name LIKE ?",(name,))
        try:
            obj= self.cursor.fetchall()
            return Employee.createEmployee(obj)
        except sqlite3.Error as e:
            print(e)

    def getTopSellingEmployees(self):
        self.cursor.execute("SELECT SUM(cost),SUM(price) ,ROUND((SUM(price)-SUM(cost))) as netProfit,SUM(quantity),employee FROM history GROUP BY employee ORDER BY netProfit DESC")
        try:
            obj=self.cursor.fetchall()
            return obj
        
        except sqlite3.Error as e:
            print(e)
            
    def addEmployer(self,employer:Employer):
        sql="INSERT INTO employer(username,password) VALUES(?,?)"
        values=(employer.username,employer.password)
        self.cursor.execute(sql,values)
        try:
            self.connection.commit()
            print("Added employer")
        except sqlite3.Error as e:
            print(e)

    def getEmployers(self):
        self.cursor.execute("SELECT * FROM employer")
        try:
            obj= self.cursor.fetchall()
            return Employer.createEmployer(obj)
        except sqlite3.Error as e:
            print(e)

    def addClient(self,client:Client):
        sql="INSERT INTO client(name,phone,address) VALUES(?,?,?)"
        values=(client.name,client.phone,client.address)
        self.cursor.execute(sql,values)
        try:
            self.connection.commit()
            print("Added client")
        except sqlite3.Error as e:
            print(e)

    def editClient(self,client:Client):
        sql="UPDATE client SET name=?,phone=?,address=? WHERE id=?"
        values=(client.name,client.phone,client.address,client.id)
        self.cursor.execute(sql,values)
        try:
            self.connection.commit()
        except sqlite3.Error as e:
            print(e)

    def getClients(self):
        self.cursor.execute("SELECT * FROM client")
        try:
            obj= self.cursor.fetchall()
            return Client.createClient(obj)
        except sqlite3.Error as e:
            print(e)

    def getClientByName(self,name):
        self.cursor.execute("SELECT * FROM client WHERE name= ?",(name,))
        try:
            obj= self.cursor.fetchone()
            return Client.createClient(obj)
        except sqlite3.Error as e:
            print(e)

    def getClientsByName(self,name):
        name=f"%{name}%"
        self.cursor.execute("SELECT * FROM client WHERE name LIKE ?",(name,))
        try:
            obj= self.cursor.fetchall()
            return Client.createClient(obj)
        except sqlite3.Error as e:
            print(e)

    def getTopCustomers(self):
        self.cursor.execute("SELECT ROUND(SUM(price)-SUM(cost)) as netProfit ,SUM(quantity),soldTo FROM history GROUP BY soldTo ORDER BY netProfit DESC")
        try:
            obj=self.cursor.fetchall()
            return obj
        
        except sqlite3.Error as e:
            print(e)

    def addLog(self,name,date):
        self.cursor.execute("INSERT INTO logs(employee,lastDate) VALUES(?,?)",(name,date))
        try:
            self.connection.commit()
        except sqlite3.Error as e:
            print(e)

    def getLogs(self):
        self.cursor.execute("SELECT * FROM logs")
        try:
            obj= self.cursor.fetchall()
            return Log.createLog(obj)
        except sqlite3.Error as e:
            print(e)

    def latestLog(self):
        self.cursor.execute("SELECT * FROM logs ORDER BY lastDate DESC")
        try:
            obj= self.cursor.fetchall()
            return Log.createLog(obj)
        except sqlite3.Error as e:
            print(e)

    def create_tables(self):
        self.cursor.execute('CREATE TABLE IF NOT EXISTS "product" ("id" INTEGER NOT NULL UNIQUE,"name" TEXT NOT NULL UNIQUE,"cost" REAL NOT NULL,"price" REAL NOT NULL,"quantity" INTEGER NOT NULL,"category"	TEXT NOT NULL,PRIMARY KEY("id" AUTOINCREMENT))')

        self.cursor.execute('CREATE TABLE IF NOT EXISTS "client" ( "id" INTEGER NOT NULL UNIQUE, "name" TEXT NOT NULL UNIQUE, "phone" TEXT NOT NULL, "address" TEXT NOT NULL, PRIMARY KEY("id" AUTOINCREMENT) )')

        self.cursor.execute('CREATE TABLE IF NOT EXISTS "employer" ( "id" INTEGER NOT NULL UNIQUE, "username" TEXT NOT NULL UNIQUE, "password" TEXT NOT NULL, PRIMARY KEY("id" AUTOINCREMENT) )')

        self.cursor.execute('CREATE TABLE IF NOT EXISTS "employee" ( "id" INTEGER NOT NULL UNIQUE, "name" TEXT NOT NULL, "phone" TEXT NOT NULL, "email" TEXT NOT NULL, "username" TEXT NOT NULL UNIQUE, "password" TEXT NOT NULL, PRIMARY KEY("id" AUTOINCREMENT) )')
        
        self.cursor.execute('CREATE TABLE IF NOT EXISTS "history" ( "id" INTEGER NOT NULL UNIQUE, "name" TEXT NOT NULL, "cost" REAL NOT NULL, "price" REAL NOT NULL, "quantity" INTEGER NOT NULL, "category" TEXT NOT NULL, "soldTo" TEXT NOT NULL, "soldDate" TEXT NOT NULL, "employee" TEXT NOT NULL, PRIMARY KEY("id" AUTOINCREMENT) )')

        self.cursor.execute('CREATE TABLE IF NOT EXISTS "logs" ( "id" INTEGER NOT NULL, "employee" TEXT NOT NULL, "lastDate" TEXT NOT NULL, PRIMARY KEY("id" AUTOINCREMENT) )')
        result=self.getEmployers()
        if len(result) == 0:
            self.addEmployer(Employer(None,def_us,def_pw))

    def __del__(self):
        self.connection.close()
        print("Connection closed")

db=DBmanager()
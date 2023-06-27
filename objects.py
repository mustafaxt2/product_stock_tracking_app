class Employer:
    def __init__(self,id,username,password):
        if id is None:
            self.id = 0
        else:
            self.id=id
        self.username = username
        self.password = password
    
    @staticmethod
    def createEmployer(obj):
        employerList=[]
        if isinstance(obj,tuple):
            return Employer(obj[0],obj[1],obj[2])
        else:
            for i in obj:
                employerList.append(Employer(i[0],i[1],i[2]))
            return employerList

class Employee:
    def __init__(self,id,name,phone,email,username,password):
        if id is None:
            self.id = 0
        else:
            self.id=id
        self.name = name
        self.phone = phone
        self.email = email
        self.username = username
        self.password = password
    
    @staticmethod
    def createEmployee(obj):
        employeeList=[]
        if isinstance(obj,tuple):
            return Employee(obj[0],obj[1],obj[2],obj[3],obj[4],obj[5])
        else:
            for i in obj:
                employeeList.append(Employee(i[0],i[1],i[2],i[3],i[4],i[5]))
            return employeeList
        
class Client:
    def __init__(self,id,name,phone,address):
        if id is None:
            self.id = 0
        else:
            self.id=id
        self.name = name
        self.phone = phone
        self.address = address
    
    @staticmethod
    def createClient(obj):
        clientList=[]
        if isinstance(obj,tuple):
            return Client(obj[0],obj[1],obj[2],obj[3])
        else:
            for i in obj:
                clientList.append(Client(i[0],i[1],i[2],i[3]))
            return clientList
        
class Product:
    def __init__(self,id,name,cost,price,quantity,category):
        if id is None:
            self.id = 0
        else:
            self.id = id
        self.name = name
        self.cost = cost
        self.price = price
        self.quantity = quantity
        self.category = category
    
    @staticmethod
    def createProduct(obj):
        productList=[]
        if isinstance(obj,tuple):
            return Product(obj[0],obj[1],obj[2],obj[3],obj[4],obj[5])
        else:
            for i in obj:
                productList.append(Product(i[0],i[1],i[2],i[3],i[4],i[5]))
            return productList
        
class History:
    def __init__(self,id,name,cost,price,quantity,category,soldTo,soldDate,employee):
        if id is None:
            self.id=0
        else:
            self.id = id
        self.name = name
        self.cost = cost
        self.price = price
        self.quantity = quantity
        self.category = category
        self.soldTo = soldTo
        self.soldDate = soldDate
        self.employee = employee

    @staticmethod
    def createBox(obj):
        historyList=[]
        if isinstance(obj,tuple):
            return History(obj[0],obj[1],obj[2],obj[3],obj[4],obj[5],obj[6],obj[7],obj[8])
        else:
            for i in obj:
                historyList.append(History(i[0],i[1],i[2],i[3],i[4],i[5],i[6],i[7],i[8]))
            return historyList
        
class Log():
    def __init__(self,id,employee,lastDate):
        if id is None:
            self.id=0
        else:
            self.id = id
        self.employee=employee
        self.lastDate=lastDate

    @staticmethod
    def createLog(obj):
        logs=[]
        if isinstance(obj,tuple):
            return Log(obj[0],obj[1],obj[2])
        else:
            for i in obj:
                logs.append(Log(i[0],i[1],i[2]))
            return logs
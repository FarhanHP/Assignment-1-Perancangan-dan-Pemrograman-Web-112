import pymongo
import model
import view
import datetime

def sortModels(models, column, descending=False):
    #bubble sort
    if(type(models[0].getInfo()[column]) == int):
        for i in range(1, len(models)):
            isChanged = False
            for j in range(len(models)-i):
                if(not descending and models[j].getInfo()[column] > models[j+1].getInfo()[column]):
                    models[j], models[j+1] = models[j+1], models[j]
                    isChanged = True
                elif (descending and models[j].getInfo()[column] < models[j+1].getInfo()[column]) :
                    models[j], models[j+1] = models[j+1], models[j]
                    isChanged = True

            if(not isChanged):
                return

    elif(type(models[0].getInfo()[column])  == str):
        for i in range(1, len(models)):
            isChanged = False
            for j in range(len(models)-i):
                if(not descending and models[j].getInfo()[column].lower() > models[j+1].getInfo()[column].lower()):
                    models[j], models[j+1] = models[j+1], models[j]
                    isChanged = True
                elif (descending and models[j].getInfo()[column].lower() < models[j+1].getInfo()[column].lower()) :
                    models[j], models[j+1] = models[j+1], models[j]
                    isChanged = True

            if(not isChanged):
                return

    elif(type(models[0].getInfo()[column])  == list):
        if(type(models[0].getInfo()[column][0]) == str):
            for i in range(1, len(models)):
                isChanged = False
                for j in range(len(models)-i):
                    if(not descending and models[j].getInfo()[column][1].lower() > models[j+1].getInfo()[column][1].lower()):
                        models[j], models[j+1] = models[j+1], models[j]
                        isChanged = True
                    elif (descending and models[j].getInfo()[column][1].lower() < models[j+1].getInfo()[column][1].lower()) :
                        models[j], models[j+1] = models[j+1], models[j]
                        isChanged = True

                if(not isChanged):
                    return

        elif(type(models[0].getInfo()[column][0]) == int):
            for i in range(1, len(models)):
                isChanged = False
                for j in range(len(models)-i):
                    if(not descending and models[j].getInfo()[column][1] > models[j+1].getInfo()[column][1]):
                        models[j], models[j+1] = models[j+1], models[j]
                        isChanged = True
                    elif (descending and models[j].getInfo()[column][1] < models[j+1].getInfo()[column][1]) :
                        models[j], models[j+1] = models[j+1], models[j]
                        isChanged = True

                if(not isChanged):
                    return


class Guest:
    def __init__(self, root):
        self.view = view.Guest(root)
        self.col = pymongo.MongoClient()["olshop"]["user"]
        self.root = root

    def login(self, error):
        data = self.view.login(error)
        if(data["action"] == "register"):
            return {
                "action" : "register",
                "error" : {
                    "username" : "", 
                    "password" : "", 
                    "email" : "",
                    "fullname" : "",
                    "phone" : "",
                }
            }
            
        search = self.col.find_one({"username":data["data"]["username"], "password":data["data"]["password"]})

        if(search != None):
            result = {
                "action" : "login-confirmed",
                "data" : None
            }
            if search["role"] == "owner":
                result["data"] = Owner(search["_id"], search["username"], search["password"], search["email"], search["fullname"], 
                search["gender"], search["phone"], search["address"], datetime.datetime.today().strftime("%Y-%m-%d %H:%M:%S"), 
                search["join_date"], self.root)
                return result

            elif (search["role"] == "employee"):
                result["data"] = Employee(search["_id"], search["username"], search["password"], search["email"], search["fullname"], 
                search["gender"], search["phone"], search["address"], datetime.datetime.today().strftime("%Y-%m-%d %H:%M:%S"), 
                search["join_date"], self.root)
                return result

            result["data"] = Customer(search["_id"], search["username"], search["password"], search["email"], search["fullname"], 
            search["gender"], search["phone"], search["address"], datetime.datetime.today().strftime("%Y-%m-%d %H:%M:%S"), 
            search["join_date"], self.root)
            return result
        
        return {
            "error" : "Username or Password is Invalid",
            "action" : "login"
        }

    def register(self, error):
        data = self.view.register(error)
        error = {
            "username" : "", 
            "password" : "", 
            "email" : "",
            "fullname" : "",
            "phone" : "",
        }

        if(data["action"] == "login"):
            return {"action" : "login", "error" : ""}

        #check username
        if(self.col.find_one({"email":data["data"]["username"]}) != None):
            error["username"] = "*Username is Already Used"
            data["action"] = "register"
        elif(len(data["data"]["username"]) < 8 or len(data["data"]["username"]) > 20):
            error["username"] = "*Username Length Only 8-20 Characters"
            data["action"] = "register"

        #check password
        if(len(data["data"]["password"]) < 8 or len(data["data"]["password"]) > 20):
            error["password"] = "*Password Length Only 8-20 Characters"
            data["action"] = "register"

        #check email
        if(self.col.find_one({"email":data["data"]["email"]}) != None):
            error["email"] = "*Email is Already Used"
            data["action"] = "register"
        elif(len(data["data"]["email"]) == 0):
            error["email"] = "*Email Cannot be Empty"
            data["action"] = "register"

        #check fullname
        if(len(data["data"]["fullname"]) < 8 or len(data["data"]["fullname"]) > 30):
            error["fullname"] = "*Fullname Length Only 8-30 Characters"
            data["action"] = "register"

        #check phone
        try:
            int(data["data"]["phone"])
        except:
            error["phone"] = "*Phone Number is Invalid"
            data["action"] = "register"
        if(len(data["data"]["phone"]) == 0):
            error["phone"] = "*Phone Number Cannot be Empty"
            data["action"] = "register"
        elif(self.col.find_one({"phone" : data["data"]["phone"]}) != None):
            error["phone"] = "*Phone Number is Already Used"
            data["action"] = "register"

        if(data["action"] == "register"):
            return {"action" : "register", "error" : error}

        self.col.insert_one({
            "username" : data["data"]["username"],
            "password" : data["data"]["password"],
            "email" : data["data"]["email"],
            "fullname" : data["data"]["fullname"],
            "gender" : data["data"]["gender"],
            "phone" : data["data"]["phone"],
            "address" : data["data"]["address"],
            "role" : "customer",
            "last_login" : "",
            "join_date" : datetime.datetime.today().strftime("%Y-%m-%d %H:%M:%S")
        })
        return {"action" : "login", "error" : ""}

class User:
    def __init__(self, view, model, root):
        self.client = pymongo.MongoClient()["olshop"]
        self.view = view
        self.model = model
        self.root = root

    def showProducts(self, keyword):
        self.recentSearch = keyword
        queryResult = self.client["product"].find().sort("name", pymongo.ASCENDING)
        data = {
            "user" : self.model,
            "products" : list()
        }

        for i in queryResult :
            if keyword in i["name"].lower():
                data["products"].append(model.Product(i["_id"], i["name"], i["price"], i["pic"], i["qty"], i["sold"], i["input_date"]))

        return self.view.showProducts(data)
        
    def showProductDetail(self, product):
        data = {
            "user" : self.model,
            "product" : product,
            "respond" : None
        }
        return self.view.showProductDetail(data)

    def editInfo(self, error, success):
        result = self.view.editInfo(self.model, error, success)
        
        if(result["action"] == None):
            result["action"] = "edit-info"
            result["success"] = ""
            result["error"] = {"username" : "", "email" : "", "fullname" : "", "phone": ""}
            isChange = False
            isError = False
            if(result["username"] != self.model.getInfo()["username"]):
                result["error"]["username"] = self.model.setUsername(result["username"])
                if(result["error"]["username"] != ""):
                    isError = True
                isChange = True
            if (result["email"] != self.model.getInfo()["email"]):
                result["error"]["email"] = self.model.setEmail(result["email"])
                if(result["error"]["email"] != ""):
                    isError = True
                isChange = True
            if (result["fullname"] != self.model.getInfo()["fullname"]):
                result["error"]["fullname"]  = self.model.setFullname(result["fullname"])
                if(result["error"]["fullname"]  != ""):
                    isError = True
                isChange = True
            if (result["gender"] != self.model.getInfo()["gender"]):
                self.model.setGender(result["gender"])
                isChange = True
            if(result["phone"] != self.model.getInfo()["phone"]):
                result["error"]["phone"] = self.model.setPhone(result["phone"])
                if(result["error"]["phone"] != ""):
                    isError = True
                isChange = True
            if(result["address"] != self.model.getInfo()["address"]):
                self.model.setAddress(result["address"])
                isChange = True

            if(not isError and isChange):
                result["success"] = "Your Information is Sucessfully Changed"
            
        return result

    def changePassword(self, error, success):
        result = self.view.changePassword(self.model, error, success)
        if(result["action"] == None):
            result["action"] = "change-password"
            result["error"] = {
                "old-password" : "",
                "new-password" : "",
                "confirm-new-password" : "" 
            }
            result["success"] = ""

            isError = False
            if(result["old-password"] != self.model.getInfo()["password"]):
                result["error"]["old-password"] = "Wrong Password"
                isError = True
            if(result["new-password"] != result["confirm-new-password"]):
                result["error"]["confirm-new-password"] = "*Not Match"
                isError = True

            if (not isError) :
                result["error"]["new-password"] = self.model.setPassword(result["new-password"])
                if(result["error"]["new-password"] != ""):
                    isError = True

            if(not isError):
                result["success"] = "Your Password is Succesfully Changed"

        return result

class Seller(User):
    def __init__(self, view, model, root):
        super().__init__(view, model, root)
    
    def addProduct(self, error):
        data = {
            "user" : self.model,
            "error" : error
        }

        result = self.view.addProduct(data)
        if(result["action"] == None):
            isError = False
            col = self.client["product"]
            #check product name
            if(len(result["data"]["name"]) == 0):
                isError = True
                error["productName"] = "Product Name Can't be Empty"
            elif (col.find_one({"name" : result["data"]["name"]}) != None):
                isError = True
                error["productName"] = "Product Name Already Used"
            #check product price
            try:
                if(int(result["data"]["price"]) < 0 ):
                    isError = True
                    error["productPrice"] = "Invalid Value"
            except:
                isError = True
                error["productPrice"] = "Invalid Value"
            #check product quantity
            try:
                if(int(result["data"]["qty"]) < 0 ):
                    isError = True
                    error["productQty"] = "Invalid Value"
            except:
                isError = True
                error["productQty"] = "Invalid Value"

            if(isError):
                return self.addProduct(error)
            else:
                col.insert_one({
                    "name" : result["data"]["name"],
                    "price" : int(result["data"]["price"]),
                    "pic" : "img/default-product.png",
                    "qty" : int(result["data"]["qty"]),
                    "sold" : 0,
                    "input_date" : datetime.datetime.today().strftime("%Y-%m-%d %H:%M:%S")
                })

                currentProduct = self.client["product"].find_one({"name" : result["data"]["name"]})

                #record action
                self.client["input_product_history"].insert_one({
                    "user" : self.model.getInfo()["_id"],
                    "product" : currentProduct["_id"],
                    "product_name" : currentProduct["name"],
                    "input_date" : currentProduct["input_date"]
                })

                result["action"] = "product-detail"
                result["product"] = model.Product(currentProduct["_id"], result["data"]["name"], int(result["data"]["price"]), "img/default-product.png", 
                int(result["data"]["qty"]), currentProduct["sold"], currentProduct["input_date"])
                return result
        else:
            return result

    def editProduct(self, product, newValue):
        oldProductInfo = product.getInfo()

        product.setName(newValue["name"])
        product.setPrice(newValue["price"])
        product.setQty(newValue["qty"])

        newProductInfo = product.getInfo()

        if(oldProductInfo != newProductInfo):
            #save record
            self.client["product_edit_history"].insert_one({
                "user" : self.model.getInfo()["_id"],
                "product" : newProductInfo["_id"],
                "name" : [oldProductInfo["name"], newProductInfo["name"]],
                "price" : [oldProductInfo["price"], newProductInfo["price"]],
                "qty" : [oldProductInfo["qty"], newProductInfo["qty"]],
                "edit_date" : datetime.datetime.today().strftime("%Y-%m-%d %H:%M:%S")
            })

        return {
            "action" : "product-detail",
            "product" : product
        }

    def deleteProduct(self, product):
        product.delete()

        #save record
        self.client["product_delete_history"].insert_one({
            "user" : self.model.getInfo()["_id"],
            "product_name" : product.getInfo()["name"],
            "delete_date" : datetime.datetime.today().strftime("%Y-%m-%d %H:%M:%S")
        })

        return {"action" : "search-product", "keyword" : ""}

class Owner(Seller):
    def __init__(self, _id, username, password, email, fullname, gender, phone, address, lastLogin, joinDate, root):
        super().__init__(view.Owner(root), model.User(_id, username, password, email, fullname, gender, phone, address, "owner", lastLogin, 
        joinDate), root)

    def manageUsers(self, interact, targetUser):
        if(interact != None and targetUser != None):
            if(interact=="fire"):
                targetUser.setRole("customer")
            elif(interact=="assign"):
                targetUser.setRole("employee")

            #record the interact
            self.client["assign_fire_history"].insert_one({
                "user" : targetUser.getInfo()["_id"],
                "interact" : interact,
                "date" : datetime.datetime.today().strftime("%Y-%m-%d %H:%M:%S")
            })

        usersLst = list()

        for i in self.client["user"].find().sort("username", pymongo.ASCENDING):
            if(i["username"] != self.model.getInfo()["username"]):
                usersLst.append(model.User(i["_id"], i["username"], i["password"], i["email"], i["fullname"], i["gender"], i["phone"], i["address"],
                i["role"], i["last_login"], i["join_date"]))

        return self.view.manageUsers(self.model, usersLst)

    def showAssignFireHistory(self, col, descending):
        if(col == "date" or col == "interact"):
            if(descending):
                histories = self.client["assign_fire_history"].find().sort(col, pymongo.DESCENDING)
            else:
                histories = self.client["assign_fire_history"].find().sort(col, pymongo.ASCENDING)
        else:
            histories = self.client["assign_fire_history"].find().sort("date", pymongo.DESCENDING)
        
        historiesLst = list()
        for history in histories :
            historiesLst.append(model.AssignFireHistory(history["user"], history["interact"], history["date"]))

        if(col == "username"):
            sortModels(historiesLst, col, descending)

        return self.view.showAssignFireHistory(historiesLst, self.model, descending)

    def showTransactionHistory(self, col, descending):
        if(col != "username"):
            if(descending):
                histories = self.client["transaction"].find().sort(col, pymongo.DESCENDING)
            else:
                histories = self.client["transaction"].find().sort(col, pymongo.ASCENDING)
        else:
            histories = self.client["transaction"].find().sort("transaction_date", pymongo.DESCENDING)

        historiesLst = list()
        for history in histories :
            historiesLst.append(model.TransactionHistory(history["user"], history["product"], history["product_name"], history["qty"], 
            history["price"], history["total"], history["transaction_date"]))

        if(col=="username"):
            sortModels(historiesLst, col, descending)

        return self.view.showTransactionHistory(historiesLst, self.model, descending)

    def showProductDeleteHistory(self, col, descending):
        if(col != "username"):
            if(descending):
                histories = self.client["product_delete_history"].find().sort(col, pymongo.DESCENDING)
            else:
                histories = self.client["product_delete_history"].find().sort(col, pymongo.ASCENDING)
        else:
            histories = self.client["product_delete_history"].find().sort("delete_date", pymongo.DESCENDING)

        historiesLst = list()
        for history in histories :
            historiesLst.append(model.DeleteProductHistory(history["user"], history["product_name"], history["delete_date"]))

        if(col == "username"):
            sortModels(historiesLst, col, descending)

        return self.view.showProductDeleteHistory(historiesLst, self.model, descending)

    def showProductInputHistory(self, col, descending):
        if(col != "username"):
            if(descending):
                histories = self.client["input_product_history"].find().sort(col, pymongo.DESCENDING)
            else:
                histories = self.client["input_product_history"].find().sort(col, pymongo.ASCENDING)
        else:
            histories = self.client["input_product_history"].find().sort(col, pymongo.DESCENDING)
        
        historiesLst = list()
        for history in histories :
            historiesLst.append(model.InputProductHistory(history["user"], history["product"], history["product_name"], history["input_date"]))

        if(col == "username"):
            sortModels(historiesLst, col, descending)

        return self.view.showProductInputHistory(historiesLst, self.model, descending)

    def showProductEditHistory(self, col, descending):
        if(col=="edit-date" and not descending):
            histories = self.client["product_edit_history"].find().sort(col, pymongo.ASCENDING)
        else:
            histories = self.client["product_edit_history"].find().sort(col, pymongo.DESCENDING)

        historiesLst = list()
        for history in histories :
            historiesLst.append(model.EditProductHistory(history["user"], history["product"], history["name"], history["price"], history["qty"], 
            history["edit_date"]))

        if(col != "edit_date"):
            sortModels(historiesLst, col, descending)

        return self.view.showProductEditHistory(historiesLst, self.model, descending)

    def showUserDetail(self, user):
        return self.view.showUserDetail(self.model, user)

class Employee(Seller):
    def __init__(self, _id, username, password, email, fullname, gender, phone, address, lastLogin, joinDate, root):
        super().__init__(view.Employee(root), model.User(_id, username, password, email, fullname, gender, phone, address, "employee", 
        lastLogin, joinDate), root)

    def showProductDeleteHistory(self, col, descending):
        if(descending):
            histories = self.client["product_delete_history"].find({"user" : self.model.getInfo()["_id"]}).sort(col, pymongo.DESCENDING)
        else:
            histories = self.client["product_delete_history"].find({"user" : self.model.getInfo()["_id"]}).sort(col, pymongo.ASCENDING)

        historiesLst = list()
        for history in histories :
            historiesLst.append(model.DeleteProductHistory(history["user"], history["product_name"], history["delete_date"]))

        return self.view.showProductDeleteHistory(historiesLst, self.model, descending)

    def showProductInputHistory(self, col, descending):
        if(descending):
            histories = self.client["input_product_history"].find({"user" : self.model.getInfo()["_id"]}).sort(col, pymongo.DESCENDING)
        else:
            histories = self.client["input_product_history"].find({"user" : self.model.getInfo()["_id"]}).sort(col, pymongo.ASCENDING)

        historiesLst = list()
        for history in histories :
            historiesLst.append(model.InputProductHistory(history["user"], history["product"], history["product_name"], history["input_date"]))

        return self.view.showProductInputHistory(historiesLst, self.model, descending)

    def showProductEditHistory(self, col, descending):
        if(col=="edit-date" and not descending):
            histories = self.client["product_edit_history"].find({"user" : self.model.getInfo()["_id"]}).sort(col, pymongo.ASCENDING)
        else:
            histories = self.client["product_edit_history"].find({"user" : self.model.getInfo()["_id"]}).sort(col, pymongo.DESCENDING)

        historiesLst = list()
        for history in histories :
            historiesLst.append(model.EditProductHistory(history["user"], history["product"], history["name"], history["price"], history["qty"], 
            history["edit_date"]))

        if(col != "edit_date"):
            sortModels(historiesLst, col, descending)

        return self.view.showProductEditHistory(historiesLst, self.model, descending)

class Customer(User):
    def __init__(self, _id, username, password, email, fullname, gender, phone, address, lastLogin, joinDate, root):
        super().__init__(view.Customer(root), model.User(_id, username, password, email, fullname, gender, phone, address, "customer", 
        lastLogin, joinDate), root)

    def buy(self, product, ammount):
        data = {
            "user" : self.model,
            "product" : product,
            "respond" : None
        }
        try:
            if(int(ammount) < 0 or int(ammount) > product.getInfo()["qty"]):
                data["respond"] = "Invalid Value"
            else:
                product.setQty(product.getInfo()["qty"] - int(ammount))
                product.setSold(product.getInfo()["sold"] + int(ammount))
                data["respond"] = "Transaction Success"

                #record action
                self.client["transaction"].insert_one({
                    "user" : self.model.getInfo()["_id"],
                    "product" : product.getInfo()["_id"],
                    "product_name" : product.getInfo()["name"],
                    "qty" : int(ammount),
                    "price" : int(product.getInfo()["price"]),
                    "total" : int(ammount) * int(product.getInfo()["price"]),
                    "transaction_date" : datetime.datetime.today().strftime("%Y-%m-%d %H:%M:%S")
                })
        except:
            data["respond"] = "Invalid Value"

        return self.view.showProductDetail(data)

    def showTransactionHistory(self, col, descending):
        if(descending):
            histories = self.client["transaction"].find({"user" : self.model.getInfo()["_id"]}).sort(col, pymongo.DESCENDING)
        else:
            histories = self.client["transaction"].find({"user" : self.model.getInfo()["_id"]}).sort(col, pymongo.ASCENDING)

        historiesLst = list()
        for history in histories :
            historiesLst.append(model.TransactionHistory(history["user"], history["product"], history["product_name"], history["qty"], 
            history["price"], history["total"], history["transaction_date"]))

        return self.view.showTransactionHistory(historiesLst, self.model, descending)

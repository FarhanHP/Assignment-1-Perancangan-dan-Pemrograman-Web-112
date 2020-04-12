import pymongo

class History:
    def __init__(self, userId, date):
        self.userId = userId
        self.username = pymongo.MongoClient()["olshop"]["user"].find_one({"_id" : userId})["username"]
        self.date = date

class AssignFireHistory(History):
    def __init__(self, userId, interact, date):
        super().__init__(userId, date)
        self.interact = interact

    def getInfo(self):
        return {
            "userId" : self.userId,
            "username" : self.username,
            "interact" : self.interact,
            "date" : self.date
        }

class DeleteProductHistory(History):
    def __init__(self, userId, productName, date):
        super().__init__(userId, date)
        if(len(productName) > 20) : 
            productName = productName[:20]+"..."
        self.productName = productName

    def getInfo(self):
        return {
            "userId" : self.userId,
            "username" : self.username,
            "productName" : self.productName,
            "date" : self.date
        }

class EditProductHistory(History):
    def __init__(self, userId, productId, name, price, qty, date):
        super().__init__(userId, date)
        self.productId = productId
        if(len(name[0]) > 20):
            name[0] = name[0][:20]+"..."
        if(len(name[1]) > 20):
            name[1] = name[1][:20]+"..."
        self.name = name
        self.price = price
        self.qty = qty

    def getInfo(self):
        return {
            "userId" : self.username,
            "username" : self.username,
            "productId" : self.productId,
            "name" : self.name,
            "price" : self.price,
            "qty" : self.qty,
            "date" : self.date
        }

class InputProductHistory(History):
    def __init__(self, userId, productId, productName, date):
        super().__init__(userId, date)
        self.productId = productId
        if(len(productName) > 20) : 
            productName = productName[:20]+"..."
        self.productName = productName

    def getInfo(self):
        return {
            "userId" : self.userId,
            "username" : self.username,
            "productId" : self.productId,
            "productName" : self.productName,
            "date" : self.date
        }

class Product:
    '''
        _id: ObjectId
        name: string
        price: int
        pic: string
        qty: int
        sold: int
        inputDate: string
    '''
    def __init__(self, _id, name, price, pic, qty, sold, inputDate):
        self._id = _id
        self.name = name
        self.price = price
        self.pic = pic
        self.qty = qty
        self.sold = sold
        self.inputDate = inputDate
        self.col = pymongo.MongoClient()["olshop"]["product"]

    def getInfo(self):
        return {
            "_id": self._id, 
            "name": self.name, 
            "price":self.price, 
            "pic": self.pic, 
            "qty": self.qty,
            "sold" : self.sold,
            "inputDate" : self.inputDate
        }

    def setName(self, newName):
        if(len(newName) > 90):
            return "*Product Name Cannot be More Than 90 Characters Long"

        self.col.update_one({
            "_id":self._id
        }, {
            "$set" : {"name":newName}
        })
        self.name = newName
        return ""

    def setPrice(self, newPrice):
        try:
            newPrice = int(newPrice)
        except:
            return "*Invalid Value"

        if(newPrice < 0):
            newPrice = 0

        self.col.update_one({
            "_id":self._id
        }, {
            "$set" : {"price":newPrice}
        })
        self.price = newPrice
        return ""

    def setPic(self, newPic):
        self.col.update_one({
            "_id":self._id
        }, {
            "$set" : {"pic":newPic}
        })
        self.pic = newPic

    def setQty(self, newQty):
        try:
            newQty = int(newQty)
        except:
            return "*Invalid Value"

        if(newQty < 0):
            newQty = 0

        self.col.update_one({
            "_id":self._id
        }, {
            "$set" : {"qty":newQty}
        })
        self.qty = newQty
        return ""

    def setSold(self, newSold):
        self.col.update_one({
            "_id":self._id
        }, {
            "$set" : {"sold":newSold}
        })
        self.sold = newSold
        return ""

    def delete(self):
        self.col.delete_one({"_id" : self._id})

class TransactionHistory(History):
    def __init__(self, userId, productId, productName, qty, price, total, date):
        super().__init__(userId, date)
        self.productId = productId
        if(len(productName) > 20) : 
            productName = productName[:20]+"..."
        self.productName = productName
        self.qty = qty
        self.price = price
        self.total = total

    def getInfo(self):
        return {
            "userId" : self.userId,
            "username" : self.username,
            "productId" : self.productId,
            "productName" : self.productName,
            "qty" : self.qty,
            "price" : self.price,
            "total" : self.total,
            "date" : self.date
        }

class User:
    '''
        _id: ObjectId
        username: string
        password: string
        email: string
        fullname: string
        gender: string
        phone: string
        address: string
        role: string
        lastLogin: string
        joinDate: string
        col: MongoDB Collection
    '''
    def __init__(self, _id, username, password, email, fullname, gender, phone, address, role, lastLogin, joinDate):
        self._id = _id
        self.username = username
        self.password = password
        self.email = email
        self.fullname = fullname
        self.gender = gender
        self.phone = phone
        self.address = address
        self.role = role
        self.col = pymongo.MongoClient()["olshop"]["user"]
        self.lastLogin = lastLogin
        self.setLastLogin(lastLogin)
        self.joinDate = joinDate

    def getInfo(self):
        return {
            "_id" : self._id,
            "username": self.username, 
            "password" : self.password,
            "email": self.email, 
            "fullname" : self.fullname,
            "gender" : self.gender,
            "phone" : self.phone,
            "address" : self.address,
            "role": self.role,
            "last_login" : self.lastLogin,
            "join_date" : self.joinDate
        }
    
    def setUsername(self, newUsername):
        if(len(newUsername) < 8 or len(newUsername) > 20):
            return "*Username Must 8 to 20 Characters Long"
        if(len(list(self.col.find({"username" : newUsername}))) == 1):
            return "*Username is Already Used"
        
        self.col.update_one({
            "username" : self.username
        }, {
            "$set" : {
                "username" : newUsername
            }
        })

        self.username = newUsername
        return ""

    def setPassword(self, newPassword):
        if(len(newPassword) < 8):
            return "Password Must More Than 8 Characters Long"

        self.col.update_one({
            "username" : self.username
        }, {
            "$set" : {
                "password" : newPassword
            }
        })

        self.password = newPassword

        return ""

    def setEmail(self, newEmail):
        if(len(list(self.col.find({"email" : newEmail}))) == 1):
            return "*Email is Already Used"

        self.col.update_one({
            "username":self.username
        }, {
            "$set" : {
                "email" : newEmail
            }
        })
        self.email = newEmail
        return ""

    def setFullname(self, newFullname):
        if(len(newFullname) < 8 or len(newFullname) > 30):
            return "Fullname Length Only 8-30 Characters"
        
        self.col.update_one({
            "username":self.username
        }, {
            "$set" : {
                "fullname" : newFullname
            }
        })
        self.fullname = newFullname
        return ""

    def setGender(self, newGender):
        self.col.update_one({
            "username":self.username
        }, {
            "$set" : {
                "gender" : newGender
            }
        })
        self.gender = newGender
        return ""

    def setPhone(self, newPhone):
        try:
            int(newPhone)
        except:
            return "Phone Number is Invalid"
        if(len(newPhone) == 0):
            return "Phone Number Cannot be Empty"
        elif(self.col.find_one({"phone" : newPhone}) != None):
            return "Phone Number is Already Used"
        
        self.col.update_one({
            "username":self.username
        }, {
            "$set" : {
                "phone" : newPhone
            }
        })
        self.phone = newPhone
        return ""

    def setAddress(self, newAddress):
        self.col.update_one({
            "username":self.username
        }, {
            "$set" : {
                "address" : newAddress
            }
        })
        self.address = newAddress
        return ""

    def setRole(self, newRole):
        self.col.update_one({
            "username":self.username
        }, {
            "$set" : {
                "role" : newRole
            }
        })
        self.role = newRole

    def setLastLogin(self, newTime):
        self.col.update_one({
            "username":self.username
        }, {
            "$set" : {
                "last_login" : newTime
            }
        })
        self.lastLogin = newTime
        return ""
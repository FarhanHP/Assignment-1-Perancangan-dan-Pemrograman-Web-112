import tkinter as tk
from PIL import ImageTk, Image

def priceBeautify(price):
    price = str(price)
    output = ""
    for i in range(len(price)-1, -1, -1):
        if(i != len(price)-1 and (len(price)-1 - i) % 3 == 0):
            output = "."+output
        output = price[i] + output
    return output

class BackButton(tk.Button):
    def __init__(self, master, output, page, actionData={"action" : "search-product", "keyword" : ""}):
        super().__init__(master, cursor="hand2", text="\u2190 Back", font="courier 12 bold")
        self["background"] = master["background"]
        def backBtnClicked():
            for key in actionData.keys():
                output[key] = actionData[key]

            page.quit()
            page.destroy()
        self["command"] = backBtnClicked

class BlankSpace(tk.Frame):
    def __init__(self, master, width=0, height=0, background=None):
        super().__init__(master, width=width, height=height)
        if background == None :
            self["background"] = master["background"]
        else :
            self["background"] = background    

class ButtonPicture(tk.Button):
    def __init__(self, master, imgLoc, imgW, imgH, background):
        img = Image.open(imgLoc)
        img = img.resize((imgW, imgH), Image.ANTIALIAS)
        img = ImageTk.PhotoImage(img)
        super().__init__(master, image=img, background=background, cursor="hand2")
        self.image = img

class logOutButton(BackButton):
    def __init__(self, master, output, page):
        super().__init__(master, output, page, actionData={"action" : "login", "error" : ""})
        self["text"] = "Log Out"
        self["relief"] = "flat"
        self["padx"] = 5
        self["pady"] = 5
        self["fg"] = "red"
        self["anchor"] = "w"
        
class Picture(tk.Label):
    def __init__(self, master, imgLoc, imgW, imgH, background):
        img = Image.open(imgLoc)
        img = img.resize((imgW, imgH), Image.ANTIALIAS)
        img = ImageTk.PhotoImage(img)
        super().__init__(master, image=img, background=background)
        self.image = img

class Navbar(tk.Frame):
    def __init__(self, master, user, output, page):
        super().__init__(master, background="deep sky blue", padx=20, pady=5, relief="solid", borderwidth=1)
        navBar = tk.Frame(self, background=self["background"])

        #logo
        logo = tk.Label(navBar, text="Olshop", fg="white")
        logo["font"] = "courier 16 bold"
        logo["background"] = logo.master["background"]
        logo.pack(side="left")
        #logo end

        space = BlankSpace(navBar, width=30)
        space.pack(side="left")

        #searchbar
        searchEntryContainer = tk.Frame(navBar, padx=5, pady=5, background="white", relief="solid", borderwidth=1)

        search = tk.Entry(searchEntryContainer, bd=0, width=60, font="courier 12")
        search["background"] = search.master["background"]
        search.pack(side="left")

        searchBtn = tk.Button(searchEntryContainer, text="Search", background="lightskyblue1", fg="white", relief="solid", cursor="hand2", 
        borderwidth=1, font="courier 12 bold")

        def searchBtnClicked():
            output["action"] = "search-product"
            output["keyword"] = search.get()
            page.destroy()
            page.quit()

        searchBtn["command"] = searchBtnClicked
        searchBtn.pack(side="left")

        searchEntryContainer.pack(side="left")
        #searchbar end

        container = tk.Frame(navBar)
        container["background"] = container.master["background"]

        #add-product
        if(user.getInfo()["role"] != "customer"):
            def addProductBtnClicked():
                
                output["action"] = "add-product"
                output["error"] = {"productName" : "", "productPrice": "", "productQty" : ""}

                page.quit()
                page.destroy()

            addProductBtn = ButtonPicture(container, "img/add-product.png", 30, 30, "white")
            addProductBtn["command"] = addProductBtnClicked
            addProductBtn.pack(side="left")
        #add-product end

        space = BlankSpace(container, width = 10)
        space.pack(side="left", fill="y")

        #profil-button
        def profileBtnClicked():
            output["action"] = "edit-info"
            output["error"] = {"username" : "", "email" : "", "fullname" : "", "phone": ""}
            output["success"] = ""

            page.destroy()
            page.quit()

        profileBtn = tk.Button(container, text=user.getInfo()["username"], relief="solid", background="lightskyblue1", fg="white", cursor="hand2", 
        command=profileBtnClicked, padx=5, pady=5, borderwidth=1)
        profileBtn["font"] = "courier 14"
        profileBtn.pack(side="left", fill="y")
        #profil-button end

        container.pack(side="right")

        navBar.pack(fill="x")

class PageBtns():
    def __init__(self):
        self.children = list()

    def append(self, newChild):
        self.children.append(newChild)

    def getChildren(self):
        return self.children

class PageBtn(tk.Button):
    def __init__(self, master, text, state, parent, page, setting={"disabled" : {"relief" : "flat"}, "normal" : {"relief" : "raised"}}):
        if (state == "disabled"):
            super().__init__(master, text=text, state="disabled", font="courier 12 bold")
        else:
            super().__init__(master, text=text, font="courier 12 bold")
        self.parent = parent
        self.parent.append(self)
        self.page = page
        self.setting = setting
        self["command"] = self.clicked
        
        if(state == "disabled"):
            self.disable()
        else:
            self.enable()

    def disable(self):
        self["state"] = "disabled"
        self["cursor"] = ""

        for i in self.setting["disabled"].keys():
            self[i] = self.setting["disabled"][i]

        self.page.pack(expand=True, fill="both")

    def enable(self):
        self["state"] = "normal"
        self["cursor"] = "hand2"
        
        for i in self.setting["normal"].keys():
            self[i] = self.setting["normal"][i]

        self.page.pack_forget()

    def clicked(self):
        for i in self.parent.getChildren() :
            i.enable()
        self.disable()

class ProductCard(tk.Frame):
    def __init__(self, master, product, output, page):
        super().__init__(master, background="white", padx=5, pady=5, relief="solid", borderwidth=1)
        container = tk.Frame(self, background=self["background"])

        productImg = Picture(container, product.getInfo()["pic"], 150, 100, "white")
        productImg.pack(expand=True, fill="both")

        space = BlankSpace(container, height=5)
        space.pack(fill="x")

        productDesc = tk.Frame(container, background="white")

        productDescName = tk.Label(productDesc, text=product.getInfo()["name"], font="courier 10 bold", wraplength=250)
        productDescName["background"] = productDescName.master["background"]
        productDescName.pack(expand=True, fill="both")

        productDescPrice = tk.Label(productDesc, text="Rp"+priceBeautify(product.getInfo()["price"]), font="courier 14 bold", fg="blue")
        productDescPrice["background"] = productDescPrice.master["background"]
        productDescPrice.pack(expand=True, fill="both")

        detailBtn = tk.Button(productDesc, text="Detail", cursor="hand2", background="lightskyblue1", relief="flat", fg="white", font="courier 14 bold")
        def detailBtnClicked():
            output["action"] = "product-detail"
            output["product"] = product
            page.quit()
            page.destroy()

        detailBtn["command"] = detailBtnClicked
        detailBtn.pack(fill="x")

        productDesc.pack(fill="x")

        container.pack(expand=True, fill="both")

class ProfileBtns(BackButton):
    def __init__(self, master, text, output, page, actionData):
        super().__init__(master, output, page, actionData)
        self["text"] = text
        self["relief"] = "flat"
        self["padx"] = 5
        self["pady"] = 5
        self["anchor"] = "w"
    
    def disable(self):
        self["disabledforeground"] = "blue"
        self["background"] = "#f0f0f0"
        self["cursor"] = ""
        self["state"] = "disabled"

    def enable(self):
        self["fg"] = "black"
        self["background"] = self.master["background"]
        self["cursor"] = "hand2"
        self["state"] = "normal"

class UserCard(tk.Frame):
    def __init__(self, master, user, output, page):
        super().__init__(master, relief="solid", borderwidth=1, pady=5)

        infoUser = user.getInfo()

        body = tk.Frame(self, background=self["background"], padx=5, pady=5)
        username = tk.Label(body, background=body["background"], padx=5, pady=5, font="courier 12 bold", text=infoUser["username"], anchor="w")
        username.pack(fill="x")
        email = tk.Label(body, background=body["background"], padx=5, pady=5, font="courier 12", text=infoUser["email"], anchor="w")
        email.pack(fill="x")
        role = tk.Label(body, background=body["background"], padx=5, pady=5, font="courier 12", text=infoUser["role"], anchor="w")
        role.pack(fill="x")
        body.pack(side="left", expand=True, fill="both")

        verticalLine = BlankSpace(self, width=1, background="black")
        verticalLine.pack(side="left", fill="y")

        btnContainer = tk.Frame(self, background=self["background"], padx=20, width=20)
        assignBtn = tk.Button(btnContainer, fg="white", font="courier 12 bold", cursor="hand2")
        assignBtn.pack(expand=True)

        def detailBtnClicked():
            output["action"] = "user-detail"
            output["user"] = user

            page.quit()
            page.destroy()

        detailBtn = tk.Button(btnContainer, fg="white", font="courier 12 bold", cursor="hand2", background="lightskyblue1", text="Detail", command=detailBtnClicked)
        detailBtn.pack(expand=True)

        def fireEmployee():
            output["action"] = "manage-users"
            output["interact"] = "fire"
            output["target_user"] = user
            page.quit()
            page.destroy()

        def assignEmployee():
            output["action"] = "manage-users"
            output["interact"] = "assign"
            output["target_user"] = user
            page.quit()
            page.destroy()

        if(infoUser["role"] == "customer"):
            assignBtn["background"] = "green"
            assignBtn["text"] = "Assign"
            assignBtn["command"] = assignEmployee
            
        elif(infoUser["role"] == "employee"):
            assignBtn["background"] = "red"
            assignBtn["text"] = "Fire"
            assignBtn["command"] = fireEmployee

        btnContainer.pack(side="left", fill="y")
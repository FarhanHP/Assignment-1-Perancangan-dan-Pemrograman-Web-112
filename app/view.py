import tkinter as tk
import customGui
import math

class Guest:
    '''
        root:Tk
    '''
    def __init__(self, root):
        self.root = root

    def login(self, error):
        output = {
            "action" : "",
            "data" : dict()
        }

        #GUI
        outerContainer = tk.Frame(self.root, background="white")

        innerContainer = tk.Frame(outerContainer, background="white smoke", padx=20, pady=20, relief="solid", borderwidth=1)

        loginLabel = tk.Label(innerContainer, text="Olshop - Login", pady=10)
        loginLabel["background"] = loginLabel.master["background"]
        loginLabel["font"] = ("courier", 30)
        loginLabel.pack()

        usernameLabelContainer = tk.Frame(innerContainer)
        usernameLabelContainer["background"] = usernameLabelContainer.master["background"]
        usernameLabel = tk.Label(usernameLabelContainer, text="Username : ")
        usernameLabel["background"] = usernameLabel.master["background"]
        usernameLabel["font"] = ("courier", 16)
        usernameLabel.pack(side="left")
        usernameLabelContainer.pack(fill="x")

        usernameEntryContainer = tk.Frame(innerContainer, background="white", padx=10, pady=5, relief="solid", borderwidth=1)
        usernameEntry = tk.Entry(usernameEntryContainer, bd=0)
        usernameEntry["background"] = usernameEntry.master["background"]
        usernameEntry.pack(fill="x")
        usernameEntryContainer.pack(fill="x")

        space = customGui.BlankSpace(innerContainer, height=20)
        space.pack(fill="x")

        passwordLabelContainer = tk.Frame(innerContainer)
        passwordLabelContainer["background"] = passwordLabelContainer.master["background"]
        passwordLabel = tk.Label(passwordLabelContainer, text="Password : ")
        passwordLabel["background"] = passwordLabel.master["background"]
        passwordLabel["font"] = ("courier", 16)
        passwordLabel.pack(side="left")
        passwordLabelContainer.pack(fill="x")

        passwordEntryContainer = tk.Frame(innerContainer, background="white", padx=10, pady=5, relief="solid", borderwidth=1)
        passwordEntry = tk.Entry(passwordEntryContainer, bd=0, show="*")
        passwordEntry["background"] = passwordEntry.master["background"]
        passwordEntry.pack(fill="x")
        passwordEntryContainer.pack(fill="x")

        space = customGui.BlankSpace(innerContainer, height=5)
        space.pack(fill="x")

        errorLabel = tk.Label(innerContainer, text=error, fg="red")
        errorLabel["background"] = errorLabel.master["background"]
        errorLabel["font"] = ("courier", 12)
        errorLabel.pack()

        space = customGui.BlankSpace(innerContainer, height=5)
        space.pack(fill="x")

        loginBtn = tk.Button(innerContainer, background="lightskyblue1", text="Login", relief="flat", fg="white", cursor="hand2")
        
        def loginBtnClicked():
            output["data"]["username"] = usernameEntry.get()
            output["data"]["password"] = passwordEntry.get()
            output["action"] = ""
            outerContainer.destroy()
            outerContainer.quit()

        loginBtn["command"] = loginBtnClicked

        loginBtn.pack(fill="x")

        space = customGui.BlankSpace(innerContainer, height=10)
        space.pack(fill="x")

        registerBtn = tk.Button(innerContainer, background="lightskyblue1", text="Register", relief="flat", fg="white", cursor="hand2")
        
        def registerBtnClicked():
            output["data"]["username"] = ""
            output["data"]["password"] = ""
            output["action"] = "register"
            outerContainer.destroy()
            outerContainer.quit()

        registerBtn["command"] = registerBtnClicked
        
        registerBtn.pack(fill="x")

        innerContainer.pack(expand=True)

        outerContainer.pack(expand=True, fill="both")
        outerContainer.mainloop()
        #GUI END

        return output

    def register(self, errorMsg):
        output = {
            "data" : dict(),
            "action" : ""
        }

        #GUI
        outerContainer = tk.Frame(self.root, background="white")

        innerContainer = tk.Frame(outerContainer, background="white smoke", padx=20, pady=20, relief="solid", borderwidth=1)

        container = tk.Frame(innerContainer)
        container["background"] = container.master["background"]
        
        def backBtnClicked():
            output["action"] = "login"
            outerContainer.destroy()
            outerContainer.quit()

        backBtn = tk.Button(container, command=backBtnClicked, cursor="hand2", text="\u2190 Back", font="courier 12 bold")
        backBtn["background"] = backBtn.master["background"]
        backBtn.pack(side="left")
        
        container.pack(fill="x")

        registerLabel = tk.Label(innerContainer, text="Olshop - Register", pady=10)
        registerLabel["background"] = registerLabel.master["background"]
        registerLabel["font"] = ("courier", 16)
        registerLabel.pack()
        
        #username
        usernameLabelContainer = tk.Frame(innerContainer)
        usernameLabelContainer["background"] = usernameLabelContainer.master["background"]

        usernameLabel = tk.Label(usernameLabelContainer, text="Username : ")
        usernameLabel["background"] = usernameLabel.master["background"]
        usernameLabel["font"] = ("courier", 12)
        usernameLabel.pack(side="left")

        error = tk.Label(usernameLabelContainer, text=errorMsg["username"], fg="red")
        error["background"] = error.master["background"]
        error["font"] = ("courier", 12)
        error.pack(side="left")
        
        usernameLabelContainer.pack(fill="x")

        usernameEntryContainer = tk.Frame(innerContainer, background="white", padx=10, pady=5, relief="solid", borderwidth=1)
        usernameEntry = tk.Entry(usernameEntryContainer, bd=0)
        usernameEntry["background"] = usernameEntry.master["background"]
        usernameEntry.pack(fill="x")
        usernameEntryContainer.pack(fill="x")
        #username end

        #password
        passwordLabelContainer = tk.Frame(innerContainer)
        passwordLabelContainer["background"] = passwordLabelContainer.master["background"]

        passwordLabel = tk.Label(passwordLabelContainer, text="Password : ")
        passwordLabel["background"] = passwordLabel.master["background"]
        passwordLabel["font"] = ("courier", 12)
        passwordLabel.pack(side="left")

        error = tk.Label(passwordLabelContainer, text=errorMsg["password"], fg="red")
        error["background"] = error.master["background"]
        error["font"] = ("courier", 12)
        error.pack(side="left")

        passwordLabelContainer.pack(fill="x")

        passwordEntryContainer = tk.Frame(innerContainer, background="white", padx=10, pady=5, relief="solid", borderwidth=1)
        passwordEntry = tk.Entry(passwordEntryContainer, bd=0, show="*")
        passwordEntry["background"] = passwordEntry.master["background"]
        passwordEntry.pack(fill="x")
        passwordEntryContainer.pack(fill="x")
        #password end

        #email
        emailLabelContainer = tk.Frame(innerContainer)
        emailLabelContainer["background"] = emailLabelContainer.master["background"]

        emailLabel = tk.Label(emailLabelContainer, text="Email : ")
        emailLabel["background"] = emailLabel.master["background"]
        emailLabel["font"] = ("courier", 12)
        emailLabel.pack(side="left")

        error = tk.Label(emailLabelContainer, text=errorMsg["email"], fg="red")
        error["background"] = error.master["background"]
        error["font"] = ("courier", 12)
        error.pack(side="left")

        emailLabelContainer.pack(fill="x")

        emailEntryContainer = tk.Frame(innerContainer, background="white", padx=10, pady=5, relief="solid", borderwidth=1)
        emailEntry = tk.Entry(emailEntryContainer, bd=0)
        emailEntry["background"] = emailEntry.master["background"]
        emailEntry.pack(fill="x")
        emailEntryContainer.pack(fill="x")
        #email end

        #fullname
        fullnameLabelContainer = tk.Frame(innerContainer)
        fullnameLabelContainer["background"] = fullnameLabelContainer.master["background"]

        fullnameLabel = tk.Label(fullnameLabelContainer, text="Fullname : ")
        fullnameLabel["background"] = fullnameLabel.master["background"]
        fullnameLabel["font"] = ("courier", 12)
        fullnameLabel.pack(side="left")

        error = tk.Label(fullnameLabelContainer, text=errorMsg["fullname"], fg="red")
        error["background"] = error.master["background"]
        error["font"] = ("courier", 12)
        error.pack(side="left")

        fullnameLabelContainer.pack(fill="x")

        fullnameEntryContainer = tk.Frame(innerContainer, background="white", padx=10, pady=5, relief="solid", borderwidth=1)
        fullnameEntry = tk.Entry(fullnameEntryContainer, bd=0)
        fullnameEntry["background"] = fullnameEntry.master["background"]
        fullnameEntry.pack(fill="x")
        fullnameEntryContainer.pack(fill="x")
        #fullname end

        #gender
        genderValue = tk.StringVar()
        genderLabel = tk.Label(innerContainer, text="Gender : ", anchor="w", font="courier 12")
        genderLabel["background"] = genderLabel.master["background"]
        genderLabel.pack(fill="x")

        radioBtnContainer = tk.Frame(innerContainer)
        radioBtnContainer["background"] = radioBtnContainer.master["background"]

        male = tk.Radiobutton(radioBtnContainer, text="male", variable=genderValue, value="male", 
        background=radioBtnContainer["background"], cursor="hand2", font="courier 12")
        male.select()
        male.pack(side="left")

        space = customGui.BlankSpace(radioBtnContainer, width=5)
        space.pack(side="left")

        female = tk.Radiobutton(radioBtnContainer, text="female", variable=genderValue, value="female", 
        background=radioBtnContainer["background"], cursor="hand2", font="courier 12")
        female.pack(side="left")

        space = customGui.BlankSpace(radioBtnContainer, width=5)
        space.pack(side="left")

        other = tk.Radiobutton(radioBtnContainer, text="other", variable=genderValue, value="other", 
        background=radioBtnContainer["background"], cursor="hand2", font="courier 12")
        other.pack(side="left")

        radioBtnContainer.pack(fill="x")
        #gender end

        #phone
        phoneLabelContainer = tk.Frame(innerContainer)
        phoneLabelContainer["background"] = phoneLabelContainer.master["background"]

        phoneLabel = tk.Label(phoneLabelContainer, text="Phone Number : ")
        phoneLabel["background"] = phoneLabel.master["background"]
        phoneLabel["font"] = ("courier", 12)
        phoneLabel.pack(side="left")

        error = tk.Label(phoneLabelContainer, text=errorMsg["phone"], fg="red")
        error["background"] = error.master["background"]
        error["font"] = ("courier", 12)
        error.pack(side="left")

        phoneLabelContainer.pack(fill="x")

        phoneEntryContainer = tk.Frame(innerContainer, background="white", padx=10, pady=5, relief="solid", borderwidth=1)
        phoneEntry = tk.Entry(phoneEntryContainer, bd=0)
        phoneEntry["background"] = phoneEntry.master["background"]
        phoneEntry.pack(fill="x")
        phoneEntryContainer.pack(fill="x")
        #phone end

        #address
        addressLabelContainer = tk.Frame(innerContainer)
        addressLabelContainer["background"] = addressLabelContainer.master["background"]

        addressLabel = tk.Label(addressLabelContainer, text="Address : ")
        addressLabel["background"] = addressLabel.master["background"]
        addressLabel["font"] = ("courier", 12)
        addressLabel.pack(side="left")

        addressLabelContainer.pack(fill="x")

        addressEntryContainer = tk.Frame(innerContainer, background="white", padx=10, pady=5, relief="solid", borderwidth=1)
        addressEntry = tk.Entry(addressEntryContainer, bd=0)
        addressEntry["background"] = addressEntry.master["background"]
        addressEntry.pack(fill="x")
        addressEntryContainer.pack(fill="x")
        #address end

        space = customGui.BlankSpace(innerContainer, height=20)
        space.pack(fill="x")

        registerBtn = tk.Button(innerContainer, background="lightskyblue1", text="register", relief="flat", fg="white", cursor="hand2")
        
        def registerBtnClicked():
            output["data"]["username"] = usernameEntry.get()
            output["data"]["password"] = passwordEntry.get()
            output["data"]["email"] = emailEntry.get()
            output["data"]["fullname"] = fullnameEntry.get()
            output["data"]["gender"] = genderValue.get()
            output["data"]["phone"] = phoneEntry.get()
            output["data"]["address"] = addressEntry.get() 
            outerContainer.destroy()
            outerContainer.quit()

        registerBtn["command"] = registerBtnClicked

        registerBtn.pack(fill="x")

        space = customGui.BlankSpace(innerContainer, height=10)
        space.pack(fill="x")

        innerContainer.pack(expand=True)

        outerContainer.pack(expand=True, fill="both")
        outerContainer.mainloop()
        #GUI END

        return output

class User:
    def __init__(self, root):
        self.root = root
        self.availableProfileTabs = {
            "Edit Information" : {
                "action" : "edit-info", 
                "error" : {
                    "username" : "", "email" : "", "fullname" : "", "phone": ""
                }, 
                "success" : ""
            },
            "Change Password" : {
                "action" : "change-password",
                "error" : {
                    "old-password" : "", "new-password" : "", "confirm-new-password" : ""
                }, 
                "success" : ""
            }
        }

    def showProducts(self, data):
        output = {}

        #GUI
        body = tk.Frame(self.root)

        #navbar
        navBar = customGui.Navbar(body, data["user"], output, body)
        navBar.pack(fill="x")
        #navbar end

        productLength = len(data["products"])
        pageNumbers = int(math.ceil(productLength / 10))

        #products list
        container = tk.Frame(body, padx=20, pady=5, background="white smoke")
        container["background"] = container.master["background"]

        pages = list()
        for h in range(pageNumbers):
            page = tk.Frame(container)
            page["background"] = page.master["background"]
            for i in range(10):
                if ( i % 5 == 0 ) :
                    row = tk.Frame(page)
                    row["background"] = row.master["background"]
                elif (i % 5 == 4 or i == 7):
                    row.pack(expand=True, fill="both")

                colBorder = tk.Frame(row, padx=5, pady=5)
                colBorder["background"] = colBorder.master["background"]

                if(10*h+i < productLength):
                    currentProductInfo = data["products"][10*h+i]

                    col = customGui.ProductCard(colBorder, currentProductInfo, output, body)
                    col.pack(expand=True, fill="both")
                
                colBorder.pack(side="left", fill="both", expand=True)

            pages.append(page)

        container.pack(expand=True, fill="both")
        #product list end

        #product list pages
        container = tk.Frame(body, pady=5)
        filler = tk.Frame(container)
        filler["background"] = filler.master["background"]
        filler.pack(side="left", expand=True)
        pageBtns = customGui.PageBtns()
        for i in range(pageNumbers):
            if(i == 0):
                pageBtn = customGui.PageBtn(container, str(i+1), "disabled", pageBtns, pages[i])
            else :
                pageBtn = customGui.PageBtn(container, str(i+1), "normal", pageBtns, pages[i])

            pageBtn.pack(side="left")

        filler = tk.Frame(container)
        filler["background"] = filler.master["background"]
        filler.pack(side="left", expand=True)
        container.pack(fill="x")
        #product list pages end

        body.pack(expand=True, fill="both")
        body.mainloop()
        #GUI END

        return output

    def editInfo(self, user, error, success):
        output = {}

        #GUI
        page = tk.Frame(self.root)

        #navbar
        navBar = customGui.Navbar(page, user, output, page)
        navBar.pack(fill="x")
        #navbar end

        #back-button
        backBtn = tk.Frame(page, padx=20, pady=5)
        btn = customGui.BackButton(backBtn, output, page)
        btn.pack(side="left")
        backBtn.pack(fill="x")
        #back-button end

        #main-page
        mainPageContainer = tk.Frame(page, padx=20, pady=5)
        mainPage = tk.Frame(mainPageContainer, background="white", relief="solid", borderwidth=1)

        #profile-btns
        lst = tk.Frame(mainPage)
        lst["background"] = lst.master["background"]

        for i in self.availableProfileTabs.keys():
            temp = customGui.ProfileBtns(lst, i, output, page, self.availableProfileTabs[i])
            temp.pack(fill="x")
            if i == "Edit Information" :
                temp.disable()

        logout = customGui.logOutButton(lst, output, page)
        logout.pack(fill="x")

        lst.pack(side="left", fill="y")
        #profile-btns end

        line = customGui.BlankSpace(mainPage, width=1, background="black")
        line.pack(side="left", fill="y")

        #edit-information page
        editInfoPage = tk.Frame(mainPage, padx=20, pady=20)
        editInfoPage["background"] = editInfoPage.master["background"]

        #change-username
        container = tk.Frame(editInfoPage)
        container["background"] = container.master["background"]
        labelChangeUsername = tk.Label(container, font="courier 12", text="Username : ", pady=10)
        labelChangeUsername["background"] = labelChangeUsername.master["background"]
        labelChangeUsername.pack(side="left")

        labelChangeUsernameError = tk.Label(container, font="courier 12", pady=10, fg="red", text=error["username"])
        labelChangeUsernameError["background"] = labelChangeUsernameError.master["background"]
        labelChangeUsernameError.pack(side="left")
        container.pack(fill="x")

        container = tk.Frame(editInfoPage, background="white", padx=5, pady=5, relief="solid", borderwidth=1)
        changeUsernameEntry = tk.Entry(container, font="courier 12", background="white", bd=0)
        changeUsernameEntry.insert(0, user.getInfo()["username"])
        changeUsernameEntry.pack(fill="both", expand=True)
        container.pack(fill="x")
        #change-username end

        #change-email
        container = tk.Frame(editInfoPage)
        container["background"] = container.master["background"]
        labelChangeEmail = tk.Label(container, font="courier 12", text="Email : ", pady=10)
        labelChangeEmail["background"] = labelChangeEmail.master["background"]
        labelChangeEmail.pack(side="left")

        labelChangeEmailError = tk.Label(container, font="courier 12", pady=10, fg="red", text=error["email"])
        labelChangeEmailError["background"] = labelChangeEmailError.master["background"]
        labelChangeEmailError.pack(side="left")
        container.pack(fill="x")

        container = tk.Frame(editInfoPage, background="white", pady=5, padx=5, relief="solid", borderwidth=1)
        changeEmailEntry = tk.Entry(container, font="courier 12", background="white", bd=0)
        changeEmailEntry.insert(0, user.getInfo()["email"])
        changeEmailEntry.pack(fill="both", expand=True)
        container.pack(fill="x")
        #change-email end

        #change-fullname
        container = tk.Frame(editInfoPage)
        container["background"] = container.master["background"]
        labelChangeFullname = tk.Label(container, font="courier 12", text="Fullname : ", pady=10)
        labelChangeFullname["background"] = labelChangeFullname.master["background"]
        labelChangeFullname.pack(side="left")

        labelChangeFullnameError = tk.Label(container, font="courier 12", pady=10, fg="red", text=error["fullname"])
        labelChangeFullnameError["background"] = labelChangeFullnameError.master["background"]
        labelChangeFullnameError.pack(side="left")
        container.pack(fill="x")

        container = tk.Frame(editInfoPage, background="white", pady=5, padx=5, relief="solid", borderwidth=1)
        changeFullnameEntry = tk.Entry(container, font="courier 12", background="white", bd=0)
        changeFullnameEntry.insert(0, user.getInfo()["fullname"])
        changeFullnameEntry.pack(fill="both", expand=True)
        container.pack(fill="x")
        #change-fullname end

        #change-gender
        genderValue = tk.StringVar()
        genderLabel = tk.Label(editInfoPage, text="Gender : ", anchor="w", font="courier 12")
        genderLabel["background"] = genderLabel.master["background"]
        genderLabel.pack(fill="x")

        radioBtnContainer = tk.Frame(editInfoPage)
        radioBtnContainer["background"] = radioBtnContainer.master["background"]

        male = tk.Radiobutton(radioBtnContainer, text="male", variable=genderValue, value="male", 
        background=radioBtnContainer["background"], cursor="hand2", font="courier 12")
        male.pack(side="left")

        space = customGui.BlankSpace(radioBtnContainer, width=5)
        space.pack(side="left")

        female = tk.Radiobutton(radioBtnContainer, text="female", variable=genderValue, value="female", 
        background=radioBtnContainer["background"], cursor="hand2", font="courier 12")
        female.pack(side="left")

        space = customGui.BlankSpace(radioBtnContainer, width=5)
        space.pack(side="left")

        other = tk.Radiobutton(radioBtnContainer, text="other", variable=genderValue, value="other", 
        background=radioBtnContainer["background"], cursor="hand2", font="courier 12")
        other.pack(side="left")

        radioBtnContainer.pack(fill="x")

        if(user.getInfo()["gender"] == "male"):
            male.select()
        elif(user.getInfo()["gender"] == "female"):
            female.select()
        else:
            other.select()
        #change-gender end

        #change-phone
        container = tk.Frame(editInfoPage)
        container["background"] = container.master["background"]
        labelChangePhone = tk.Label(container, font="courier 12", text="Phone : ", pady=10)
        labelChangePhone["background"] = labelChangePhone.master["background"]
        labelChangePhone.pack(side="left")

        labelChangePhoneError = tk.Label(container, font="courier 12", pady=10, fg="red", text=error["phone"])
        labelChangePhoneError["background"] = labelChangePhoneError.master["background"]
        labelChangePhoneError.pack(side="left")
        container.pack(fill="x")

        container = tk.Frame(editInfoPage, background="white", pady=5, padx=5, relief="solid", borderwidth=1)
        changePhoneEntry = tk.Entry(container, font="courier 12", background="white", bd=0)
        changePhoneEntry.insert(0, user.getInfo()["phone"])
        changePhoneEntry.pack(fill="both", expand=True)
        container.pack(fill="x")
        #change-phone end

        #change-address
        container = tk.Frame(editInfoPage)
        container["background"] = container.master["background"]
        labelChangeAddress = tk.Label(container, font="courier 12", text="Address : ", pady=10)
        labelChangeAddress["background"] = labelChangeAddress.master["background"]
        labelChangeAddress.pack(side="left")
        container.pack(fill="x")

        container = tk.Frame(editInfoPage, background="white", pady=5, padx=5, relief="solid", borderwidth=1)
        changeAddressEntry = tk.Entry(container, font="courier 12", background="white", bd=0)
        changeAddressEntry.insert(0, user.getInfo()["address"])
        changeAddressEntry.pack(fill="both", expand=True)
        container.pack(fill="x")
        #change-address end

        #save-change
        buttonContainer = tk.Frame(editInfoPage)
        buttonContainer["background"] = buttonContainer.master["background"]
        saveInfoSuccess = tk.Label(buttonContainer, fg="green", anchor="w", font="courier 12", text=success)
        saveInfoSuccess["background"] = saveInfoSuccess.master["background"]
        saveInfoSuccess.pack(fill="x")

        space = customGui.BlankSpace(buttonContainer, height=10)
        space.pack(fill="x")

        def saveInfoClicked():
            output["action"] = None
            output["username"] = changeUsernameEntry.get()
            output["email"] = changeEmailEntry.get()
            output["fullname"] = changeFullnameEntry.get()
            output["gender"] = genderValue.get()
            output["phone"] = changePhoneEntry.get()
            output["address"] = changeAddressEntry.get()
            
            page.quit()
            page.destroy()

        saveInfo = tk.Button(buttonContainer, font="courier 12 bold", background="lightskyblue1", fg="white", text="Save Edit", cursor="hand2", command=saveInfoClicked)
        saveInfo.pack(fill="x")
        buttonContainer.pack(fill="x", side="bottom")
        #save-change end

        editInfoPage.pack(expand=True, fill="both")
        #edit-information page end

        mainPage.pack(expand=True, fill="both")
        mainPageContainer.pack(expand=True, fill="both")

        page.pack(expand=True, fill="both")
        page.mainloop()
        #GUI END

        return output

    def changePassword(self, user, error, success):
        output = {}

        #GUI
        page = tk.Frame(self.root)

        #navbar
        navBar = customGui.Navbar(page, user, output, page)
        navBar.pack(fill="x")
        #navbar end

        #back-button
        backBtn = tk.Frame(page, padx=20, pady=5)
        btn = customGui.BackButton(backBtn, output, page)
        btn.pack(side="left")
        backBtn.pack(fill="x")
        #back-button end

        #main-page
        mainPageContainer = tk.Frame(page, padx=20, pady=5)
        mainPage = tk.Frame(mainPageContainer, background="white", relief="solid", borderwidth=1)

        #profile-btns
        lst = tk.Frame(mainPage)
        lst["background"] = lst.master["background"]

        for i in self.availableProfileTabs.keys():
            temp = customGui.ProfileBtns(lst, i, output, page, self.availableProfileTabs[i])
            temp.pack(fill="x")
            if i == "Change Password" :
                temp.disable()

        logout = customGui.logOutButton(lst, output, page)
        logout.pack(fill="x")

        lst.pack(side="left", fill="y")
        #profile-btns end

        line = customGui.BlankSpace(mainPage, width=1, background="black")
        line.pack(side="left", fill="y")

        #change-password page
        changePasswordPage = tk.Frame(mainPage, padx=20, pady=20)
        changePasswordPage["background"] = changePasswordPage.master["background"]
        
        #old-password
        container = tk.Frame(changePasswordPage)
        container["background"] = container.master["background"]
        labelOldPassword = tk.Label(container, text="Old Password : ", pady=10, font="courier 12")
        labelOldPassword["background"] = labelOldPassword.master["background"]
        labelOldPassword.pack(side="left")

        labelOldPasswordError = tk.Label(container, fg="red", pady=10, font="courier 12", text=error["old-password"])
        labelOldPasswordError["background"] = labelOldPasswordError.master["background"]
        labelOldPasswordError.pack(side="left")
        container.pack(fill="x")

        container = tk.Frame(changePasswordPage, relief="solid", borderwidth=1, pady=5, padx=5, background="white")
        oldPasswordEntry = tk.Entry(container, bd=0, font="courier 12", show="*")
        oldPasswordEntry["background"] = oldPasswordEntry.master["background"]
        oldPasswordEntry.pack(fill="both", expand=True)
        container.pack(fill="x")
        #old-password end

        #new-password
        container = tk.Frame(changePasswordPage)
        container["background"] = container.master["background"]
        labelNewPassword = tk.Label(container, text="New Password : ", pady=10, font="courier 12")
        labelNewPassword["background"] = labelNewPassword.master["background"]
        labelNewPassword.pack(side="left")

        labelNewPasswordError = tk.Label(container, fg="red", pady=10, font="courier 12", text=error["new-password"])
        labelNewPasswordError["background"] = labelNewPasswordError.master["background"]
        labelNewPasswordError.pack(side="left")
        container.pack(fill="x")

        container = tk.Frame(changePasswordPage, relief="solid", borderwidth=1, pady=5, padx=5, background="white")
        newPasswordEntry = tk.Entry(container, bd=0, font="courier 12", show="*")
        newPasswordEntry["background"] = newPasswordEntry.master["background"]
        newPasswordEntry.pack(fill="both", expand=True)
        container.pack(fill="x")
        #new-password end

        #confirm-new-password
        container = tk.Frame(changePasswordPage)
        container["background"] = container.master["background"]
        labelConfirmNewPassword = tk.Label(container, text="Confirm New Password : ", pady=10, font="courier 12")
        labelConfirmNewPassword["background"] = labelConfirmNewPassword.master["background"]
        labelConfirmNewPassword.pack(side="left")

        labelConfirmNewPasswordError = tk.Label(container, fg="red", pady=10, font="courier 12", text=error["confirm-new-password"])
        labelConfirmNewPasswordError["background"] = labelConfirmNewPasswordError.master["background"]
        labelConfirmNewPasswordError.pack(side="left")
        container.pack(fill="x")

        container = tk.Frame(changePasswordPage, relief="solid", borderwidth=1, pady=5, padx=5, background="white")
        confirmNewPasswordEntry = tk.Entry(container, bd=0, font="courier 12", show="*")
        confirmNewPasswordEntry["background"] = confirmNewPasswordEntry.master["background"]
        confirmNewPasswordEntry.pack(fill="both", expand=True)
        container.pack(fill="x")
        #confirm-new-password end

        #save change
        buttonContainer = tk.Frame(changePasswordPage)
        buttonContainer["background"] = buttonContainer.master["background"]
        changePasswordSuccess = tk.Label(buttonContainer, fg="green", anchor="w", font="courier 12", text=success)
        changePasswordSuccess["background"] = changePasswordSuccess.master["background"]
        changePasswordSuccess.pack(fill="x")

        space = customGui.BlankSpace(buttonContainer, height=10)
        space.pack(fill="x")

        def saveChangePasswordClicked():
            output["action"] = None
            output["old-password"] = oldPasswordEntry.get()
            output["new-password"] = newPasswordEntry.get()
            output["confirm-new-password"] = confirmNewPasswordEntry.get()

            page.quit()
            page.destroy()

        saveChangePassword = tk.Button(buttonContainer, font="courier 12 bold", background="lightskyblue1", fg="white", text="Save Edit", cursor="hand2", command=saveChangePasswordClicked)
        saveChangePassword.pack(fill="x")
        buttonContainer.pack(fill="x", side="bottom")
        #save-change end

        changePasswordPage.pack(expand=True, fill="both")
        #change-password page end 

        mainPage.pack(expand=True, fill="both")
        mainPageContainer.pack(expand=True, fill="both")

        page.pack(expand=True, fill="both")
        page.mainloop()
        #GUI END

        return output

class Seller(User):
    def __init__(self, root):
        super().__init__(root)
        self.availableProfileTabs["Delete Product History"] = {"action" : "delete-product-history", "col" : "delete_date", "descending" : True}
        self.availableProfileTabs["Edit Product History"] = {"action" : "edit-product-history", "col" : "edit_date", "descending" : True}
        self.availableProfileTabs["Input Product History"] = {"action" : "input-product-history", "col" : "input_date", "descending" : True}

    def showProductDetail(self, data):
        output = {
            "action" : None,
            "data" : None
        }

        #GUI
        body = tk.Frame(self.root)

        #navbar
        navBar = customGui.Navbar(body, data["user"], output, body)
        navBar.pack(fill="x")
        #navbar end

        #back-button
        backBtn = tk.Frame(body, padx=20, pady=5)

        btn = customGui.BackButton(backBtn, output, body)

        btn.pack(side="left")

        backBtn.pack(fill="x")
        #back-button end

        #product-detail
        container = tk.Frame(body, padx=20, pady=5)
        
        innerContainer = tk.Frame(container, background="white", borderwidth=1, relief="solid", pady=20)

        productImg = customGui.Picture(innerContainer, data["product"].getInfo()["pic"], 500, 500, "white")
        productImg.pack(side="left", fill="both", expand=True)

        line = customGui.BlankSpace(innerContainer, width=1, background="black")
        line.pack(side="left", fill="y")

        productDesc = tk.Frame(innerContainer)
        productDesc["background"] = productDesc.master["background"]

        productName = tk.Frame(productDesc)
        productName["background"] = productName.master["background"]

        name = tk.Label(productName, text=data["product"].getInfo()["name"], fg="blue", font="courier 20 bold", wraplength=500)
        name["background"] = name.master["background"]
        name.pack(fill="both", expand=True)

        nameEdit = tk.Entry(productName, fg="blue", font="courier 20 bold", background="white")
        nameEdit.insert(0, data["product"].getInfo()["name"])

        productName.pack(fill="x")

        space = customGui.BlankSpace(productDesc, height=20)
        space.pack(fill="x")

        productPrice = tk.Frame(productDesc, padx=10, pady=10)
        productPrice["background"] = productPrice.master["background"]

        caption = tk.Label(productPrice, text="Price : ", font="courier 16")
        caption["background"] = caption.master["background"]
        caption.pack(side="left")

        price = tk.Label(productPrice, text="Rp"+customGui.priceBeautify(data["product"].getInfo()["price"]), font="courier 16")
        price["background"] = price.master["background"]
        price.pack(side="left")

        priceEdit = tk.Entry(productPrice, font="courier 16", background="white")
        priceEdit.insert(0, data["product"].getInfo()["price"])

        productPrice.pack(fill="x")

        productQty = tk.Frame(productDesc, padx=10, pady=10)
        productQty["background"] = productQty.master["background"]

        caption = tk.Label(productQty, text="Quantity : ", font="courier 16")
        caption["background"] = caption.master["background"]
        caption.pack(side="left")

        qty = tk.Label(productQty, text=data["product"].getInfo()["qty"], font="courier 16")
        qty["background"] = qty.master["background"]
        qty.pack(side="left")

        qtyEdit = tk.Entry(productQty, font="courier 16", background="white")
        qtyEdit.insert(0, data["product"].getInfo()["qty"])

        productQty.pack(fill="x")

        productSold = tk.Frame(productDesc, padx=10, pady=10)
        productSold["background"] = productSold.master["background"]

        caption = tk.Label(productSold, text="Sold : ", font="courier 16")
        caption["background"] = caption.master["background"]
        caption.pack(side="left")

        sold = tk.Label(productSold, text=data["product"].getInfo()["sold"], font="courier 16")
        sold["background"] = sold.master["background"]
        sold.pack(side="left")

        productSold.pack(fill="x")

        space = customGui.BlankSpace(productDesc)
        space.pack(fill="both", expand=True)

        btnContainer = tk.Frame(productDesc, padx=20, pady=20)
        btnContainer["background"] = btnContainer.master["background"]

        editBtn = tk.Button(btnContainer, background="lightskyblue1", text="Edit Product", fg="white", font="courier 16 bold", padx=5, pady=5, cursor="hand2")
        editBtn.pack(side="left", expand=True)

        deleteBtn = tk.Button(btnContainer, background="red", text="Delete Product", fg="white", font="courier 16 bold", padx=5, pady=5, cursor="hand2")
        deleteBtn.pack(side="left", expand=True)

        btnContainer.pack(fill="x")

        productDesc.pack(side="left", expand=True, fill="both")

        innerContainer.pack(expand=True, fill="both")

        container.pack(expand=True, fill="both")
        #product-detail end

        def saveEdit():
            output["product"] = data["product"]
            productInfo = data["product"].getInfo()
            if(productInfo["name"] != nameEdit.get() or productInfo["price"] != priceEdit.get() or productInfo["qty"] != qtyEdit.get()):
                output["action"] = "edit-product"
                output["newValue"] = {
                    "name" : nameEdit.get(),
                    "price" : priceEdit.get(),
                    "qty" : qtyEdit.get()
                }
            else :
                output["action"] = "product-detail"

            body.quit()
            body.destroy()

        def deleteProduct():
            output["action"] = "delete-product"
            output["product"] = data["product"]
            body.quit()
            body.destroy()

        def showEditMode():
            editBtn["text"] = "Save Edit"
            editBtn["command"] = saveEdit

            deleteBtn["text"] = "Cancel Edit"
            deleteBtn["background"] = "lightskyblue1"
            deleteBtn["command"] = quitEditMode
            
            name.pack_forget()
            price.pack_forget()
            qty.pack_forget()

            nameEdit.pack(fill="x")
            priceEdit.pack(side="left", fill="x", expand=True)
            qtyEdit.pack(side="left", fill="x", expand=True)

        def quitEditMode():
            editBtn["text"] = "Edit Product"
            editBtn["command"] = showEditMode

            deleteBtn["text"] = "Delete Product"
            deleteBtn["background"] = "red"
            deleteBtn["command"] = deleteProduct

            nameEdit.pack_forget()
            priceEdit.pack_forget()
            qtyEdit.pack_forget()

            name.pack(fill="x")
            price.pack(side="left")
            qty.pack(side="left")

        editBtn["command"] = showEditMode
        deleteBtn["command"] = deleteProduct


        body.pack(expand=True, fill="both")
        body.mainloop()
        #GUI END

        return output

    def addProduct(self, data):
        output = {
            "action" : None,
            "data" : None
        }

        body = tk.Frame(self.root)

        #navbar
        navBar = customGui.Navbar(body, data["user"], output, body)
        navBar.pack(fill="x")
        #navbar end

        #back-button
        backBtn = tk.Frame(body, padx=20, pady=5)

        btn = customGui.BackButton(backBtn, output, body)

        btn.pack(side="left")

        backBtn.pack(fill="x")
        #back-button end

        #main
        container = tk.Frame(body, padx=20, pady=5)

        innerContainer = tk.Frame(container, relief="solid", borderwidth=1, background="white", padx=20, pady=20)
        title = tk.Label(innerContainer, text="Add A Product", font="courier 20 bold")
        title["background"] = title.master["background"]
        title.pack(fill="x")

        space = customGui.BlankSpace(innerContainer, height=10)
        space.pack(fill="x")

        productNameLabelContainer = tk.Frame(innerContainer, pady=5)
        productNameLabelContainer["background"] = productNameLabelContainer.master["background"]
        productNameLabel = tk.Label(productNameLabelContainer, font="courier 16", text="Product Name : ", anchor="w")
        productNameLabel["background"] = productNameLabel.master["background"]
        productNameLabel.pack(side="left")

        productNameError = tk.Label(productNameLabelContainer, font="courier 16", fg="red", text=data["error"]["productName"])
        productNameError["background"] = productNameError.master["background"]
        productNameError.pack(side="left")
        productNameLabelContainer.pack(fill="x")

        productNameEntryContainer = tk.Frame(innerContainer, padx=5, pady=5, relief="solid", borderwidth=1)
        productNameEntryContainer["background"] = productNameEntryContainer.master["background"]
        productNameEntry = tk.Entry(productNameEntryContainer, font="courier 16", bd=0)
        productNameEntry["background"] = productNameEntry.master["background"]
        productNameEntry.pack(fill="both", expand=True)
        productNameEntryContainer.pack(fill="x")

        productPriceLabelContainer = tk.Frame(innerContainer, pady=5)
        productPriceLabelContainer["background"] = productPriceLabelContainer.master["background"]
        productPriceLabel = tk.Label(productPriceLabelContainer, font="courier 16", text="Product Price : ", anchor="w")
        productPriceLabel["background"] = productPriceLabel.master["background"]
        productPriceLabel.pack(side="left")

        productPriceError = tk.Label(productPriceLabelContainer, font="courier 16", fg="red", text=data["error"]["productPrice"])
        productPriceError["background"] = productPriceError.master["background"]
        productPriceError.pack(side="left")
        productPriceLabelContainer.pack(fill="x")

        productPriceEntryContainer = tk.Frame(innerContainer, padx=5, pady=5, relief="solid", borderwidth=1)
        productPriceEntryContainer["background"] = productPriceEntryContainer.master["background"]
        productPriceEntry = tk.Entry(productPriceEntryContainer, font="courier 16", bd=0)
        productPriceEntry["background"] = productPriceEntry.master["background"]
        productPriceEntry.insert(0, "0")
        productPriceEntry.pack(fill="both", expand=True)
        productPriceEntryContainer.pack(fill="x")

        productQtyLabelContainer = tk.Frame(innerContainer, pady=5)
        productQtyLabelContainer["background"] = productQtyLabelContainer.master["background"]
        productQtyLabel = tk.Label(productQtyLabelContainer, font="courier 16", text="Product Quantity : ", anchor="w")
        productQtyLabel["background"] = productQtyLabel.master["background"]
        productQtyLabel.pack(side="left")

        productQtyError = tk.Label(productQtyLabelContainer, font="courier 16", fg="red", text=data["error"]["productQty"])
        productQtyError["background"] = productQtyError.master["background"]
        productQtyError.pack(side="left")
        productQtyLabelContainer.pack(fill="x")

        productQtyEntryContainer = tk.Frame(innerContainer, padx=5, pady=5, relief="solid", borderwidth=1)
        productQtyEntryContainer["background"] = productQtyEntryContainer.master["background"]
        productQtyEntry = tk.Entry(productQtyEntryContainer, font="courier 16", bd=0)
        productQtyEntry["background"] = productQtyEntry.master["background"]
        productQtyEntry.insert(0, "0")
        productQtyEntry.pack(fill="both", expand=True)
        productQtyEntryContainer.pack(fill="x")

        space = customGui.BlankSpace(innerContainer, height=10)
        space.pack(fill="x")

        def submitClicked():
            output["data"] = {
                "name" : productNameEntry.get(),
                "price": productPriceEntry.get(),
                "qty" : productQtyEntry.get()
            }
            body.quit()
            body.destroy()

        submit = tk.Button(innerContainer, relief="solid", borderwidth=1, text="Submit", background="lightskyblue1", font="courier 16 bold", 
        fg="white", cursor="hand2", command=submitClicked)
        submit.pack(fill="x")

        innerContainer.pack()

        container.pack(fill="both", expand=True)
        #main end

        body.pack(fill="both", expand=True)
        body.mainloop()

        return output

class Owner(Seller):
    def __init__(self, root):
        super().__init__(root)
        self.availableProfileTabs["Manage Users"] = {"action" : "manage-users", "interact" : None, "target_user" : None}
        self.availableProfileTabs["Assign/Fire History"] = {"action" : "assign-fire-history", "col" : "date", "descending" : True}
        self.availableProfileTabs["Transaction History"] = {"action" : "transaction-history", "col" : "transaction_date", "descending" : True}

    def manageUsers(self, user, usersLst):
        output = {}

        #GUI
        page = tk.Frame(self.root)

        #navbar
        navBar = customGui.Navbar(page, user, output, page)
        navBar.pack(fill="x")
        #navbar end

        #back-button
        backBtn = tk.Frame(page, padx=20, pady=5)
        btn = customGui.BackButton(backBtn, output, page)
        btn.pack(side="left")
        backBtn.pack(fill="x")
        #back-button end

        #main-page
        mainPageContainer = tk.Frame(page, padx=20, pady=5)
        mainPage = tk.Frame(mainPageContainer, background="white", relief="solid", borderwidth=1)

        #profile-btns
        lst = tk.Frame(mainPage)
        lst["background"] = lst.master["background"]

        for i in self.availableProfileTabs.keys():
            temp = customGui.ProfileBtns(lst, i, output, page, self.availableProfileTabs[i])
            temp.pack(fill="x")
            if i == "Manage Users" :
                temp.disable()

        logout = customGui.logOutButton(lst, output, page)
        logout.pack(fill="x")

        lst.pack(side="left", fill="y")
        #profile-btns end

        line = customGui.BlankSpace(mainPage, width=1, background="black")
        line.pack(side="left", fill="y")

        #manage-users page
        pageNumbers = math.ceil(len(usersLst) / 4)
        pageBtns = customGui.PageBtns()
        pages = list()
        manageUsersPage = tk.Frame(mainPage, padx=20, pady=20)
        manageUsersPage["background"] = manageUsersPage.master["background"]
        
        pageContainer = tk.Frame(manageUsersPage)
        pageContainer["background"] = pageContainer.master["background"]

        for i in range(pageNumbers):
            pageTemp = tk.Frame(pageContainer)
            pageTemp["background"] = pageTemp.master["background"]
            for j in range(4):
                if (4*i + j < len(usersLst)):
                    userCard = customGui.UserCard(pageTemp, usersLst[4*i+j], output, page)
                    userCard.pack(fill="x")
            pages.append(pageTemp)

        pageContainer.pack(fill="both", expand=True)

        pageBtnsContainer = tk.Frame(manageUsersPage, pady=5)
        pageBtnsContainer["background"] = pageBtnsContainer.master["background"]

        space = customGui.BlankSpace(pageBtnsContainer)
        space.pack(fill="both", expand=True, side="left")

        for i in range(pageNumbers):
            if i == 0:
                customGui.PageBtn(pageBtnsContainer, str(i+1), "disabled", pageBtns, pages[i]).pack(side="left")
            else :
                customGui.PageBtn(pageBtnsContainer, str(i+1), "normal", pageBtns, pages[i]).pack(side="left")

        space = customGui.BlankSpace(pageBtnsContainer)
        space.pack(fill="both", expand=True, side="left")

        pageBtnsContainer.pack(fill="x")
        manageUsersPage.pack(fill="both", expand=True)
        #manage-users page end

        mainPage.pack(expand=True, fill="both")
        mainPageContainer.pack(expand=True, fill="both")

        page.pack(expand=True, fill="both")
        page.mainloop()
        #GUI END

        return output

    def showAssignFireHistory(self, historiesLst, user, descending):
        output = {}

        #GUI
        page = tk.Frame(self.root)

        #navbar
        navBar = customGui.Navbar(page, user, output, page)
        navBar.pack(fill="x")
        #navbar end

        #back-button
        backBtn = tk.Frame(page, padx=20, pady=5)
        btn = customGui.BackButton(backBtn, output, page)
        btn.pack(side="left")
        backBtn.pack(fill="x")
        #back-button end

        #main-page
        mainPageContainer = tk.Frame(page, padx=20, pady=5)
        mainPage = tk.Frame(mainPageContainer, background="white", relief="solid", borderwidth=1)

        #profile-btns
        lst = tk.Frame(mainPage)
        lst["background"] = lst.master["background"]

        for i in self.availableProfileTabs.keys():
            temp = customGui.ProfileBtns(lst, i, output, page, self.availableProfileTabs[i])
            temp.pack(fill="x")
            if i == "Assign/Fire History" :
                temp.disable()

        logout = customGui.logOutButton(lst, output, page)
        logout.pack(fill="x")

        lst.pack(side="left", fill="y")
        #profile-btns end

        line = customGui.BlankSpace(mainPage, width=1, background="black")
        line.pack(side="left", fill="y")
        
        #table
        pageNumbers = math.ceil(len(historiesLst)/22)
        pageBtns = customGui.PageBtns()
        pages = list()

        body = tk.Frame(mainPage)
        body["background"] = body.master["background"]

        def col2TitleClicked():
            output["action"] = "assign-fire-history"
            output["col"] = "username"
            output["descending"] = not descending

            page.quit()
            page.destroy()

        def col3TitleClicked():
            output["action"] = "assign-fire-history"
            output["col"] = "interact"
            output["descending"] = not descending

            page.quit()
            page.destroy()

        def col4TitleClicked():
            output["action"] = "assign-fire-history"
            output["col"] = "date"
            output["descending"] = not descending

            page.quit()
            page.destroy()

        tableContainer = tk.Frame(body)
        tableContainer["background"] = tableContainer.master["background"]

        for i in range(pageNumbers):
            table = tk.Frame(tableContainer)
            table["background"] = table.master["background"]

            col1 = tk.Frame(table, relief="solid", borderwidth=1, background="lightskyblue1")
            
            col1Title = tk.Label(col1, text="No.", font="courier 12 bold", relief="flat", padx=5, pady=5, 
            background="lightskyblue1", fg="white")
            col1Title.pack(fill="x")

            line = customGui.BlankSpace(col1, height=1, background="black")
            line.pack(fill="x")

            col1.pack(side="left", fill="y")

            col2 = tk.Frame(table, relief="solid", borderwidth=1)
            col2["background"] = col2.master["background"]

            col2Title = tk.Button(col2, text="User", font="courier 12 bold", cursor="hand2", relief="flat", command=col2TitleClicked, 
            background="lightskyblue1", fg="white")
            col2Title.pack(fill="x")

            line = customGui.BlankSpace(col2, height=1, background="black")
            line.pack(fill="x")

            col2.pack(side="left", fill="both", expand=True)

            col3 = tk.Frame(table, relief="solid", borderwidth=1)
            col3["background"] = col3.master["background"]

            col3Title = tk.Button(col3, text="Interact", font="courier 12 bold", cursor="hand2", relief="flat", command=col3TitleClicked,
            background="lightskyblue1", fg="white")
            col3Title.pack(fill="x")

            line = customGui.BlankSpace(col3, height=1, background="black")
            line.pack(fill="x")

            col3.pack(side="left", fill="both", expand=True)

            col4 = tk.Frame(table, relief="solid", borderwidth=1)
            col4["background"] = col4.master["background"]

            col4Title = tk.Button(col4, text="Datetime", font="courier 12 bold", cursor="hand2", relief="flat", command=col4TitleClicked, 
            background="lightskyblue1", fg="white")
            col4Title.pack(fill="x")

            line = customGui.BlankSpace(col4, height=1, background="black")
            line.pack(fill="x")

            col4.pack(side="left", fill="both", expand=True)

            for j in range(22):
                if(22*i+j < len(historiesLst)):
                    info = historiesLst[22*i+j].getInfo()
                    tk.Label(col1, text=str(22*i+j+1)+".", font="courier 12", fg="white", background="lightskyblue1").pack(fill="x")
                    tk.Label(col2, text=info["username"], font="courier 12", background="white").pack(fill="x")
                    if(info["interact"] == "fire"):
                        tk.Label(col3, text=info["interact"], font="courier 12", background="white", fg="red").pack(fill="x")
                    else:
                        tk.Label(col3, text=info["interact"], font="courier 12", background="white", fg="green").pack(fill="x")
                    tk.Label(col4, text=info["date"], font="courier 12", background="white").pack(fill="x")

            table.pack(fill="both", expand=True)
            pages.append(table)

        tableContainer.pack(fill="both", expand=True)

        pagination = tk.Frame(body, pady=5)
        pagination["background"] = pagination.master["background"]

        space = customGui.BlankSpace(pagination)
        space.pack(fill="both", expand=True, side="left")

        for i in range(pageNumbers):
            if i == 0 :
                customGui.PageBtn(pagination, str(i+1), "disabled", pageBtns, pages[i]).pack(side="left")
            else:
                customGui.PageBtn(pagination, str(i+1), "normal", pageBtns, pages[i]).pack(side="left")

        space = customGui.BlankSpace(pagination)
        space.pack(fill="both", expand=True, side="left")

        pagination.pack(fill="x")

        body.pack(side="left", fill="both", expand=True)
        #table end

        mainPage.pack(expand=True, fill="both")
        mainPageContainer.pack(expand=True, fill="both")

        page.pack(expand=True, fill="both")
        page.mainloop()
        #GUI END

        return output

    def showTransactionHistory(self, historiesLst, user, descending):
        output = {}

        #GUI
        page = tk.Frame(self.root)

        #navbar
        navBar = customGui.Navbar(page, user, output, page)
        navBar.pack(fill="x")
        #navbar end

        #back-button
        backBtn = tk.Frame(page, padx=20, pady=5)
        btn = customGui.BackButton(backBtn, output, page)
        btn.pack(side="left")
        backBtn.pack(fill="x")
        #back-button end

        #main-page
        mainPageContainer = tk.Frame(page, padx=20, pady=5)
        mainPage = tk.Frame(mainPageContainer, background="white", relief="solid", borderwidth=1)

        #profile-btns
        lst = tk.Frame(mainPage)
        lst["background"] = lst.master["background"]

        for i in self.availableProfileTabs.keys():
            temp = customGui.ProfileBtns(lst, i, output, page, self.availableProfileTabs[i])
            temp.pack(fill="x")
            if i == "Transaction History" :
                temp.disable()

        logout = customGui.logOutButton(lst, output, page)
        logout.pack(fill="x")

        lst.pack(side="left", fill="y")
        #profile-btns end

        line = customGui.BlankSpace(mainPage, width=1, background="black")
        line.pack(side="left", fill="y")
        
        #table
        pageNumbers = math.ceil(len(historiesLst)/22)
        pageBtns = customGui.PageBtns()
        pages = list()

        body = tk.Frame(mainPage)
        body["background"] = body.master["background"]

        def col2TitleClicked():
            output["action"] = "transaction-history"
            output["col"] = "username"
            output["descending"] = not descending

            page.quit()
            page.destroy()

        def col3TitleClicked():
            output["action"] = "transaction-history"
            output["col"] = "product_name"
            output["descending"] = not descending

            page.quit()
            page.destroy()

        def col4TitleClicked():
            output["action"] = "transaction-history"
            output["col"] = "qty"
            output["descending"] = not descending

            page.quit()
            page.destroy()

        def col5TitleClicked():
            output["action"] = "transaction-history"
            output["col"] = "price"
            output["descending"] = not descending

            page.quit()
            page.destroy()

        def col6TitleClicked():
            output["action"] = "transaction-history"
            output["col"] = "total"
            output["descending"] = not descending

            page.quit()
            page.destroy()

        def col7TitleClicked():
            output["action"] = "transaction-history"
            output["col"] = "transaction_date"
            output["descending"] = not descending

            page.quit()
            page.destroy()

        tableContainer = tk.Frame(body)
        tableContainer["background"] = tableContainer.master["background"]

        for i in range(pageNumbers):
            table = tk.Frame(tableContainer)
            table["background"] = table.master["background"]

            col1 = tk.Frame(table, relief="solid", borderwidth=1, background="lightskyblue1")
            
            col1Title = tk.Label(col1, text="No.", font="courier 12 bold", relief="flat", padx=5, pady=5, 
            background="lightskyblue1", fg="white")
            col1Title.pack(fill="x")

            line = customGui.BlankSpace(col1, height=1, background="black")
            line.pack(fill="x")

            col1.pack(side="left", fill="y")

            col2 = tk.Frame(table, relief="solid", borderwidth=1)
            col2["background"] = col2.master["background"]

            col2Title = tk.Button(col2, text="User", font="courier 12 bold", cursor="hand2", relief="flat", command=col2TitleClicked, 
            background="lightskyblue1", fg="white")
            col2Title.pack(fill="x")

            line = customGui.BlankSpace(col2, height=1, background="black")
            line.pack(fill="x")

            col2.pack(side="left", fill="both", expand=True)

            col3 = tk.Frame(table, relief="solid", borderwidth=1)
            col3["background"] = col3.master["background"]

            col3Title = tk.Button(col3, text="Product", font="courier 12 bold", cursor="hand2", relief="flat", command=col3TitleClicked,
            background="lightskyblue1", fg="white")
            col3Title.pack(fill="x")

            line = customGui.BlankSpace(col3, height=1, background="black")
            line.pack(fill="x")

            col3.pack(side="left", fill="both", expand=True)

            col4 = tk.Frame(table, relief="solid", borderwidth=1)
            col4["background"] = col4.master["background"]

            col4Title = tk.Button(col4, text="Qty", font="courier 12 bold", cursor="hand2", relief="flat", command=col4TitleClicked, 
            background="lightskyblue1", fg="white")
            col4Title.pack(fill="x")

            line = customGui.BlankSpace(col4, height=1, background="black")
            line.pack(fill="x")

            col4.pack(side="left", fill="both", expand=True)

            col5 = tk.Frame(table, relief="solid", borderwidth=1)
            col5["background"] = col5.master["background"]

            col5Title = tk.Button(col5, text="Price", font="courier 12 bold", cursor="hand2", relief="flat", command=col5TitleClicked, 
            background="lightskyblue1", fg="white")
            col5Title.pack(fill="x")

            line = customGui.BlankSpace(col5, height=1, background="black")
            line.pack(fill="x")

            col5.pack(side="left", fill="both", expand=True)

            col6 = tk.Frame(table, relief="solid", borderwidth=1)
            col6["background"] = col6.master["background"]

            col6Title = tk.Button(col6, text="Total", font="courier 12 bold", cursor="hand2", relief="flat", command=col6TitleClicked, 
            background="lightskyblue1", fg="white")
            col6Title.pack(fill="x")

            line = customGui.BlankSpace(col6, height=1, background="black")
            line.pack(fill="x")

            col6.pack(side="left", fill="both", expand=True)

            col7 = tk.Frame(table, relief="solid", borderwidth=1)
            col7["background"] = col7.master["background"]

            col7Title = tk.Button(col7, text="Datetime", font="courier 12 bold", cursor="hand2", relief="flat", command=col7TitleClicked, 
            background="lightskyblue1", fg="white")
            col7Title.pack(fill="x")

            line = customGui.BlankSpace(col7, height=1, background="black")
            line.pack(fill="x")

            col7.pack(side="left", fill="both", expand=True)

            for j in range(22):
                if(22*i+j < len(historiesLst)):
                    info = historiesLst[22*i+j].getInfo()
                    tk.Label(col1, text=str(22*i+j+1)+".", font="courier 12", fg="white", background="lightskyblue1").pack(fill="x")
                    tk.Label(col2, text=info["username"], font="courier 12", background="white").pack(fill="x")
                    tk.Label(col3, text=info["productName"], font="courier 12", background="white").pack(fill="x")
                    tk.Label(col4, text=info["qty"], font="courier 12", background="white").pack(fill="x")
                    tk.Label(col5, text=info["price"], font="courier 12", background="white").pack(fill="x")
                    tk.Label(col6, text=info["total"], font="courier 12", background="white").pack(fill="x")
                    tk.Label(col7, text=info["date"], font="courier 12", background="white").pack(fill="x")

            table.pack(fill="both", expand=True)
            pages.append(table)

        tableContainer.pack(fill="both", expand=True)

        pagination = tk.Frame(body, pady=5)
        pagination["background"] = pagination.master["background"]

        space = customGui.BlankSpace(pagination)
        space.pack(fill="both", expand=True, side="left")

        for i in range(pageNumbers):
            if i == 0 :
                customGui.PageBtn(pagination, str(i+1), "disabled", pageBtns, pages[i]).pack(side="left")
            else:
                customGui.PageBtn(pagination, str(i+1), "normal", pageBtns, pages[i]).pack(side="left")

        space = customGui.BlankSpace(pagination)
        space.pack(fill="both", expand=True, side="left")

        pagination.pack(fill="x")

        body.pack(side="left", fill="both", expand=True)
        #table end

        mainPage.pack(expand=True, fill="both")
        mainPageContainer.pack(expand=True, fill="both")

        page.pack(expand=True, fill="both")
        page.mainloop()
        #GUI END

        return output

    def showProductDeleteHistory(self, historiesLst, user, descending):
        output = {}

        #GUI
        page = tk.Frame(self.root)

        #navbar
        navBar = customGui.Navbar(page, user, output, page)
        navBar.pack(fill="x")
        #navbar end

        #back-button
        backBtn = tk.Frame(page, padx=20, pady=5)
        btn = customGui.BackButton(backBtn, output, page)
        btn.pack(side="left")
        backBtn.pack(fill="x")
        #back-button end

        #main-page
        mainPageContainer = tk.Frame(page, padx=20, pady=5)
        mainPage = tk.Frame(mainPageContainer, background="white", relief="solid", borderwidth=1)

        #profile-btns
        lst = tk.Frame(mainPage)
        lst["background"] = lst.master["background"]

        for i in self.availableProfileTabs.keys():
            temp = customGui.ProfileBtns(lst, i, output, page, self.availableProfileTabs[i])
            temp.pack(fill="x")
            if i == "Delete Product History" :
                temp.disable()

        logout = customGui.logOutButton(lst, output, page)
        logout.pack(fill="x")

        lst.pack(side="left", fill="y")
        #profile-btns end

        line = customGui.BlankSpace(mainPage, width=1, background="black")
        line.pack(side="left", fill="y")
        
        #table
        pageNumbers = math.ceil(len(historiesLst)/22)
        pageBtns = customGui.PageBtns()
        pages = list()

        body = tk.Frame(mainPage)
        body["background"] = body.master["background"]

        def col2TitleClicked():
            output["action"] = "delete-product-history"
            output["col"] = "username"
            output["descending"] = not descending

            page.quit()
            page.destroy()

        def col3TitleClicked():
            output["action"] = "delete-product-history"
            output["col"] = "product_name"
            output["descending"] = not descending

            page.quit()
            page.destroy()

        def col4TitleClicked():
            output["action"] = "delete-product-history"
            output["col"] = "delete_date"
            output["descending"] = not descending

            page.quit()
            page.destroy()

        tableContainer = tk.Frame(body)
        tableContainer["background"] = tableContainer.master["background"]

        for i in range(pageNumbers):
            table = tk.Frame(tableContainer)
            table["background"] = table.master["background"]

            col1 = tk.Frame(table, relief="solid", borderwidth=1, background="lightskyblue1")
            
            col1Title = tk.Label(col1, text="No.", font="courier 12 bold", relief="flat", padx=5, pady=5, 
            background="lightskyblue1", fg="white")
            col1Title.pack(fill="x")

            line = customGui.BlankSpace(col1, height=1, background="black")
            line.pack(fill="x")

            col1.pack(side="left", fill="y")

            col2 = tk.Frame(table, relief="solid", borderwidth=1)
            col2["background"] = col2.master["background"]

            col2Title = tk.Button(col2, text="User", font="courier 12 bold", cursor="hand2", relief="flat", command=col2TitleClicked, 
            background="lightskyblue1", fg="white")
            col2Title.pack(fill="x")

            line = customGui.BlankSpace(col2, height=1, background="black")
            line.pack(fill="x")

            col2.pack(side="left", fill="both", expand=True)

            col3 = tk.Frame(table, relief="solid", borderwidth=1)
            col3["background"] = col3.master["background"]

            col3Title = tk.Button(col3, text="Product", font="courier 12 bold", cursor="hand2", relief="flat", command=col3TitleClicked,
            background="lightskyblue1", fg="white")
            col3Title.pack(fill="x")

            line = customGui.BlankSpace(col3, height=1, background="black")
            line.pack(fill="x")

            col3.pack(side="left", fill="both", expand=True)

            col4 = tk.Frame(table, relief="solid", borderwidth=1)
            col4["background"] = col4.master["background"]

            col4Title = tk.Button(col4, text="Datetime", font="courier 12 bold", cursor="hand2", relief="flat", command=col4TitleClicked, 
            background="lightskyblue1", fg="white")
            col4Title.pack(fill="x")

            line = customGui.BlankSpace(col4, height=1, background="black")
            line.pack(fill="x")

            col4.pack(side="left", fill="both", expand=True)

            for j in range(22):
                if(22*i+j < len(historiesLst)):
                    info = historiesLst[22*i+j].getInfo()
                    tk.Label(col1, text=str(22*i+j+1)+".", font="courier 12", fg="white", background="lightskyblue1").pack(fill="x")
                    tk.Label(col2, text=info["username"], font="courier 12", background="white").pack(fill="x")
                    tk.Label(col3, text=info["productName"], font="courier 12", background="white").pack(fill="x")
                    tk.Label(col4, text=info["date"], font="courier 12", background="white").pack(fill="x")

            table.pack(fill="both", expand=True)
            pages.append(table)

        tableContainer.pack(fill="both", expand=True)

        pagination = tk.Frame(body, pady=5)
        pagination["background"] = pagination.master["background"]

        space = customGui.BlankSpace(pagination)
        space.pack(fill="both", expand=True, side="left")

        for i in range(pageNumbers):
            if i == 0 :
                customGui.PageBtn(pagination, str(i+1), "disabled", pageBtns, pages[i]).pack(side="left")
            else:
                customGui.PageBtn(pagination, str(i+1), "normal", pageBtns, pages[i]).pack(side="left")

        space = customGui.BlankSpace(pagination)
        space.pack(fill="both", expand=True, side="left")

        pagination.pack(fill="x")

        body.pack(side="left", fill="both", expand=True)
        #table end

        mainPage.pack(expand=True, fill="both")
        mainPageContainer.pack(expand=True, fill="both")

        page.pack(expand=True, fill="both")
        page.mainloop()
        #GUI END

        return output

    def showProductInputHistory(self, historiesLst, user, descending):
        output = {}

        #GUI
        page = tk.Frame(self.root)

        #navbar
        navBar = customGui.Navbar(page, user, output, page)
        navBar.pack(fill="x")
        #navbar end

        #back-button
        backBtn = tk.Frame(page, padx=20, pady=5)
        btn = customGui.BackButton(backBtn, output, page)
        btn.pack(side="left")
        backBtn.pack(fill="x")
        #back-button end

        #main-page
        mainPageContainer = tk.Frame(page, padx=20, pady=5)
        mainPage = tk.Frame(mainPageContainer, background="white", relief="solid", borderwidth=1)

        #profile-btns
        lst = tk.Frame(mainPage)
        lst["background"] = lst.master["background"]

        for i in self.availableProfileTabs.keys():
            temp = customGui.ProfileBtns(lst, i, output, page, self.availableProfileTabs[i])
            temp.pack(fill="x")
            if i == "Input Product History" :
                temp.disable()

        logout = customGui.logOutButton(lst, output, page)
        logout.pack(fill="x")

        lst.pack(side="left", fill="y")
        #profile-btns end

        line = customGui.BlankSpace(mainPage, width=1, background="black")
        line.pack(side="left", fill="y")
        
        #table
        pageNumbers = math.ceil(len(historiesLst)/22)
        pageBtns = customGui.PageBtns()
        pages = list()

        body = tk.Frame(mainPage)
        body["background"] = body.master["background"]

        def col2TitleClicked():
            output["action"] = "input-product-history"
            output["col"] = "username"
            output["descending"] = not descending

            page.quit()
            page.destroy()

        def col3TitleClicked():
            output["action"] = "input-product-history"
            output["col"] = "product_name"
            output["descending"] = not descending

            page.quit()
            page.destroy()

        def col4TitleClicked():
            output["action"] = "input-product-history"
            output["col"] = "input_date"
            output["descending"] = not descending

            page.quit()
            page.destroy()

        tableContainer = tk.Frame(body)
        tableContainer["background"] = tableContainer.master["background"]

        for i in range(pageNumbers):
            table = tk.Frame(tableContainer)
            table["background"] = table.master["background"]

            col1 = tk.Frame(table, relief="solid", borderwidth=1, background="lightskyblue1")
            
            col1Title = tk.Label(col1, text="No.", font="courier 12 bold", relief="flat", padx=5, pady=5, 
            background="lightskyblue1", fg="white")
            col1Title.pack(fill="x")

            line = customGui.BlankSpace(col1, height=1, background="black")
            line.pack(fill="x")

            col1.pack(side="left", fill="y")

            col2 = tk.Frame(table, relief="solid", borderwidth=1)
            col2["background"] = col2.master["background"]

            col2Title = tk.Button(col2, text="User", font="courier 12 bold", cursor="hand2", relief="flat", command=col2TitleClicked, 
            background="lightskyblue1", fg="white")
            col2Title.pack(fill="x")

            line = customGui.BlankSpace(col2, height=1, background="black")
            line.pack(fill="x")

            col2.pack(side="left", fill="both", expand=True)

            col3 = tk.Frame(table, relief="solid", borderwidth=1)
            col3["background"] = col3.master["background"]

            col3Title = tk.Button(col3, text="Product", font="courier 12 bold", cursor="hand2", relief="flat", command=col3TitleClicked,
            background="lightskyblue1", fg="white")
            col3Title.pack(fill="x")

            line = customGui.BlankSpace(col3, height=1, background="black")
            line.pack(fill="x")

            col3.pack(side="left", fill="both", expand=True)

            col4 = tk.Frame(table, relief="solid", borderwidth=1)
            col4["background"] = col4.master["background"]

            col4Title = tk.Button(col4, text="Datetime", font="courier 12 bold", cursor="hand2", relief="flat", command=col4TitleClicked, 
            background="lightskyblue1", fg="white")
            col4Title.pack(fill="x")

            line = customGui.BlankSpace(col4, height=1, background="black")
            line.pack(fill="x")

            col4.pack(side="left", fill="both", expand=True)

            for j in range(22):
                if(22*i+j < len(historiesLst)):
                    info = historiesLst[22*i+j].getInfo()
                    tk.Label(col1, text=str(22*i+j+1)+".", font="courier 12", fg="white", background="lightskyblue1").pack(fill="x")
                    tk.Label(col2, text=info["username"], font="courier 12", background="white").pack(fill="x")
                    tk.Label(col3, text=info["productName"], font="courier 12", background="white").pack(fill="x")
                    tk.Label(col4, text=info["date"], font="courier 12", background="white").pack(fill="x")

            table.pack(fill="both", expand=True)
            pages.append(table)

        tableContainer.pack(fill="both", expand=True)

        pagination = tk.Frame(body, pady=5)
        pagination["background"] = pagination.master["background"]

        space = customGui.BlankSpace(pagination)
        space.pack(fill="both", expand=True, side="left")

        for i in range(pageNumbers):
            if i == 0 :
                customGui.PageBtn(pagination, str(i+1), "disabled", pageBtns, pages[i]).pack(side="left")
            else:
                customGui.PageBtn(pagination, str(i+1), "normal", pageBtns, pages[i]).pack(side="left")

        space = customGui.BlankSpace(pagination)
        space.pack(fill="both", expand=True, side="left")

        pagination.pack(fill="x")

        body.pack(side="left", fill="both", expand=True)
        #table end

        mainPage.pack(expand=True, fill="both")
        mainPageContainer.pack(expand=True, fill="both")

        page.pack(expand=True, fill="both")
        page.mainloop()
        #GUI END

        return output

    def showProductEditHistory(self, historiesLst, user, descending):
        output = {}

        #GUI
        page = tk.Frame(self.root)

        #navbar
        navBar = customGui.Navbar(page, user, output, page)
        navBar.pack(fill="x")
        #navbar end

        #back-button
        backBtn = tk.Frame(page, padx=20, pady=5)
        btn = customGui.BackButton(backBtn, output, page)
        btn.pack(side="left")
        backBtn.pack(fill="x")
        #back-button end

        #main-page
        mainPageContainer = tk.Frame(page, padx=20, pady=5)
        mainPage = tk.Frame(mainPageContainer, background="white", relief="solid", borderwidth=1)

        #profile-btns
        lst = tk.Frame(mainPage)
        lst["background"] = lst.master["background"]

        for i in self.availableProfileTabs.keys():
            temp = customGui.ProfileBtns(lst, i, output, page, self.availableProfileTabs[i])
            temp.pack(fill="x")
            if i == "Edit Product History" :
                temp.disable()

        logout = customGui.logOutButton(lst, output, page)
        logout.pack(fill="x")

        lst.pack(side="left", fill="y")
        #profile-btns end

        line = customGui.BlankSpace(mainPage, width=1, background="black")
        line.pack(side="left", fill="y")
        
        #table
        pageNumbers = math.ceil(len(historiesLst)/22)
        pageBtns = customGui.PageBtns()
        pages = list()

        body = tk.Frame(mainPage)
        body["background"] = body.master["background"]

        def col2TitleClicked():
            output["action"] = "edit-product-history"
            output["col"] = "username"
            output["descending"] = not descending

            page.quit()
            page.destroy()

        def col3TitleClicked():
            output["action"] = "edit-product-history"
            output["col"] = "name"
            output["descending"] = not descending

            page.quit()
            page.destroy()

        def col4TitleClicked():
            output["action"] = "edit-product-history"
            output["col"] = "price"
            output["descending"] = not descending

            page.quit()
            page.destroy()

        def col5TitleClicked():
            output["action"] = "edit-product-history"
            output["col"] = "qty"
            output["descending"] = not descending

            page.quit()
            page.destroy()

        def col6TitleClicked():
            output["action"] = "edit-product-history"
            output["col"] = "edit_date"
            output["descending"] = not descending

            page.quit()
            page.destroy()

        tableContainer = tk.Frame(body)
        tableContainer["background"] = tableContainer.master["background"]

        for i in range(pageNumbers):
            table = tk.Frame(tableContainer)
            table["background"] = table.master["background"]

            col1 = tk.Frame(table, relief="solid", borderwidth=1, background="lightskyblue1")
            
            col1Title = tk.Label(col1, text="No.", font="courier 12 bold", relief="flat", padx=5, pady=5, 
            background="lightskyblue1", fg="white")
            col1Title.pack(fill="x")

            line = customGui.BlankSpace(col1, height=1, background="black")
            line.pack(fill="x")

            col1.pack(side="left", fill="y")

            col2 = tk.Frame(table, relief="solid", borderwidth=1)
            col2["background"] = col2.master["background"]

            col2Title = tk.Button(col2, text="User", font="courier 12 bold", cursor="hand2", relief="flat", command=col2TitleClicked, 
            background="lightskyblue1", fg="white")
            col2Title.pack(fill="x")

            line = customGui.BlankSpace(col2, height=1, background="black")
            line.pack(fill="x")

            col2.pack(side="left", fill="both", expand=True)

            col3 = tk.Frame(table, relief="solid", borderwidth=1)
            col3["background"] = col3.master["background"]

            col3Title = tk.Button(col3, text="Product Name", font="courier 12 bold", cursor="hand2", relief="flat", command=col3TitleClicked,
            background="lightskyblue1", fg="white")
            col3Title.pack(fill="x")

            line = customGui.BlankSpace(col3, height=1, background="black")
            line.pack(fill="x")

            col3.pack(side="left", fill="both", expand=True)

            col4 = tk.Frame(table, relief="solid", borderwidth=1)
            col4["background"] = col4.master["background"]

            col4Title = tk.Button(col4, text="Price", font="courier 12 bold", cursor="hand2", relief="flat", command=col4TitleClicked, 
            background="lightskyblue1", fg="white")
            col4Title.pack(fill="x")

            line = customGui.BlankSpace(col4, height=1, background="black")
            line.pack(fill="x")

            col4.pack(side="left", fill="both", expand=True)

            col5 = tk.Frame(table, relief="solid", borderwidth=1)
            col5["background"] = col5.master["background"]

            col5Title = tk.Button(col5, text="Qty", font="courier 12 bold", cursor="hand2", relief="flat", command=col5TitleClicked, 
            background="lightskyblue1", fg="white")
            col5Title.pack(fill="x")

            line = customGui.BlankSpace(col5, height=1, background="black")
            line.pack(fill="x")

            col5.pack(side="left", fill="both", expand=True)

            col6 = tk.Frame(table, relief="solid", borderwidth=1)
            col6["background"] = col6.master["background"]

            col6Title = tk.Button(col6, text="Datetime", font="courier 12 bold", cursor="hand2", relief="flat", command=col6TitleClicked, 
            background="lightskyblue1", fg="white")
            col6Title.pack(fill="x")

            line = customGui.BlankSpace(col6, height=1, background="black")
            line.pack(fill="x")

            col6.pack(side="left", fill="both", expand=True)

            for j in range(22):
                if(22*i+j < len(historiesLst)):
                    info = historiesLst[22*i+j].getInfo()
                    tk.Label(col1, text=str(22*i+j+1)+".", font="courier 12", fg="white", background="lightskyblue1").pack(fill="x")
                    tk.Label(col2, text=info["username"], font="courier 12", background="white").pack(fill="x")
                    
                    if(info["name"][0] != info["name"][1]):
                        tk.Label(col3, text=info["name"][1], font="courier 12", background="white", fg="blue").pack(fill="x")
                    else:
                        tk.Label(col3, text=info["name"][1], font="courier 12", background="white").pack(fill="x")

                    if(info["price"][0] < info["price"][1]):
                        tk.Label(col4, text="\u2191"+str(info["price"][1]), font="courier 12", background="white", fg="green").pack(fill="x")
                    elif(info["price"][0] > info["price"][1]):
                        tk.Label(col4, text="\u2193"+str(info["price"][1]), font="courier 12", background="white", fg="red").pack(fill="x")
                    else:
                        tk.Label(col4, text=str(info["price"][1]), font="courier 12", background="white").pack(fill="x")

                    if(info["qty"][0] < info["qty"][1]):
                        tk.Label(col5, text="\u2191"+str(info["qty"][1]), font="courier 12", background="white", fg="green").pack(fill="x")
                    elif(info["qty"][0] > info["qty"][1]):
                        tk.Label(col5, text="\u2193"+str(info["qty"][1]), font="courier 12", background="white", fg="red").pack(fill="x")
                    else:
                        tk.Label(col5, text=str(info["qty"][1]), font="courier 12", background="white").pack(fill="x")

                    tk.Label(col6, text=info["date"], font="courier 12", background="white").pack(fill="x")

                    

            table.pack(fill="both", expand=True)
            pages.append(table)

        tableContainer.pack(fill="both", expand=True)

        pagination = tk.Frame(body, pady=5)
        pagination["background"] = pagination.master["background"]

        space = customGui.BlankSpace(pagination)
        space.pack(fill="both", expand=True, side="left")

        for i in range(pageNumbers):
            if i == 0 :
                customGui.PageBtn(pagination, str(i+1), "disabled", pageBtns, pages[i]).pack(side="left")
            else:
                customGui.PageBtn(pagination, str(i+1), "normal", pageBtns, pages[i]).pack(side="left")

        space = customGui.BlankSpace(pagination)
        space.pack(fill="both", expand=True, side="left")

        pagination.pack(fill="x")

        body.pack(side="left", fill="both", expand=True)
        #table end

        mainPage.pack(expand=True, fill="both")
        mainPageContainer.pack(expand=True, fill="both")

        page.pack(expand=True, fill="both")
        page.mainloop()
        #GUI END

        return output

    def showUserDetail(self, user, targetUser):
        output = {
            "action" : None,
            "data" : None
        }

        info = targetUser.getInfo()

        body = tk.Frame(self.root)

        #navbar
        navBar = customGui.Navbar(body, user, output, body)
        navBar.pack(fill="x")
        #navbar end

        #back-button
        backBtn = tk.Frame(body, padx=20, pady=5)

        btn = customGui.BackButton(backBtn, output, body, {"action" : "manage-users", "interact" : None, "target_user" : None})

        btn.pack(side="left")

        backBtn.pack(fill="x")
        #back-button end

        #main
        container = tk.Frame(body, padx=20, pady=5)

        innerContainer = tk.Frame(container, relief="solid", borderwidth=1, background="white", padx=20, pady=20)

        username = tk.Label(innerContainer, text=info["username"], font="courier 20 bold", fg="blue")
        username["background"] = username.master["background"]
        username.pack(fill="x")

        space = customGui.BlankSpace(innerContainer, height=10)
        space.pack(fill="x")

        col1 = tk.Frame(innerContainer)
        col1["background"] = col1.master["background"]

        fullname = tk.Label(col1, text="Fullname", font="courier 16 bold", anchor="w")
        fullname["background"] = fullname.master["background"]
        fullname.pack(fill="x")

        email = tk.Label(col1, text="Email", font="courier 16 bold", anchor="w")
        email["background"] = email.master["background"]
        email.pack(fill="x")

        gender = tk.Label(col1, text="Gender", font="courier 16 bold", anchor="w")
        gender["background"] = gender.master["background"]
        gender.pack(fill="x")

        phone = tk.Label(col1, text="Phone", font="courier 16 bold", anchor="w")
        phone["background"] = phone.master["background"]
        phone.pack(fill="x")

        address = tk.Label(col1, text="Address", font="courier 16 bold", anchor="w")
        address["background"] = address.master["background"]
        address.pack(fill="x")

        role = tk.Label(col1, text="Role", font="courier 16 bold", anchor="w")
        role["background"] = role.master["background"]
        role.pack(fill="x")

        lastLogin = tk.Label(col1, text="Last Login", font="courier 16 bold", anchor="w")
        lastLogin["background"] = lastLogin.master["background"]
        lastLogin.pack(fill="x")

        joinDate = tk.Label(col1, text="Joined", font="courier 16 bold", anchor="w")
        joinDate["background"] = joinDate.master["background"]
        joinDate.pack(fill="x")

        col1.pack(side="left")

        col2 = tk.Frame(innerContainer)
        col2["background"] = col2.master["background"]

        fullname = tk.Label(col2, text=" : "+info["fullname"], font="courier 16", anchor="w")
        fullname["background"] = fullname.master["background"]
        fullname.pack(fill="x")

        email = tk.Label(col2, text=" : "+info["email"], font="courier 16", anchor="w")
        email["background"] = email.master["background"]
        email.pack(fill="x")

        gender = tk.Label(col2, text=" : "+info["gender"], font="courier 16", anchor="w")
        gender["background"] = gender.master["background"]
        gender.pack(fill="x")

        phone = tk.Label(col2, text=" : "+info["phone"], font="courier 16", anchor="w")
        phone["background"] = phone.master["background"]
        phone.pack(fill="x")

        address = tk.Label(col2, text=" : "+info["address"], font="courier 16", anchor="w")
        address["background"] = address.master["background"]
        address.pack(fill="x")

        role = tk.Label(col2, text=" : "+info["role"], font="courier 16 bold", anchor="w")
        role["background"] = role.master["background"]
        role.pack(fill="x")

        lastLogin = tk.Label(col2, text=" : "+info["last_login"], font="courier 16", anchor="w")
        lastLogin["background"] = lastLogin.master["background"]
        lastLogin.pack(fill="x")

        joinDate = tk.Label(col2, text=" : "+info["join_date"], font="courier 16", anchor="w")
        joinDate["background"] = joinDate.master["background"]
        joinDate.pack(fill="x")

        col2.pack(side="left")

        innerContainer.pack()

        container.pack(fill="both", expand=True)
        #main end

        body.pack(fill="both", expand=True)
        body.mainloop()

        return output


class Employee(Seller):
    def __init__(self, root):
        super().__init__(root)

    def showProductDeleteHistory(self, historiesLst, user, descending):
        output = {}

        #GUI
        page = tk.Frame(self.root)

        #navbar
        navBar = customGui.Navbar(page, user, output, page)
        navBar.pack(fill="x")
        #navbar end

        #back-button
        backBtn = tk.Frame(page, padx=20, pady=5)
        btn = customGui.BackButton(backBtn, output, page)
        btn.pack(side="left")
        backBtn.pack(fill="x")
        #back-button end

        #main-page
        mainPageContainer = tk.Frame(page, padx=20, pady=5)
        mainPage = tk.Frame(mainPageContainer, background="white", relief="solid", borderwidth=1)

        #profile-btns
        lst = tk.Frame(mainPage)
        lst["background"] = lst.master["background"]

        for i in self.availableProfileTabs.keys():
            temp = customGui.ProfileBtns(lst, i, output, page, self.availableProfileTabs[i])
            temp.pack(fill="x")
            if i == "Delete Product History" :
                temp.disable()

        logout = customGui.logOutButton(lst, output, page)
        logout.pack(fill="x")

        lst.pack(side="left", fill="y")
        #profile-btns end

        line = customGui.BlankSpace(mainPage, width=1, background="black")
        line.pack(side="left", fill="y")
        
        #table
        pageNumbers = math.ceil(len(historiesLst)/22)
        pageBtns = customGui.PageBtns()
        pages = list()

        body = tk.Frame(mainPage)
        body["background"] = body.master["background"]

        def col3TitleClicked():
            output["action"] = "delete-product-history"
            output["col"] = "product_name"
            output["descending"] = not descending

            page.quit()
            page.destroy()

        def col4TitleClicked():
            output["action"] = "delete-product-history"
            output["col"] = "delete_date"
            output["descending"] = not descending

            page.quit()
            page.destroy()

        tableContainer = tk.Frame(body)
        tableContainer["background"] = tableContainer.master["background"]

        for i in range(pageNumbers):
            table = tk.Frame(tableContainer)
            table["background"] = table.master["background"]

            col1 = tk.Frame(table, relief="solid", borderwidth=1, background="lightskyblue1")
            
            col1Title = tk.Label(col1, text="No.", font="courier 12 bold", relief="flat", padx=5, pady=5, 
            background="lightskyblue1", fg="white")
            col1Title.pack(fill="x")

            line = customGui.BlankSpace(col1, height=1, background="black")
            line.pack(fill="x")

            col1.pack(side="left", fill="y")

            col3 = tk.Frame(table, relief="solid", borderwidth=1)
            col3["background"] = col3.master["background"]

            col3Title = tk.Button(col3, text="Product", font="courier 12 bold", cursor="hand2", relief="flat", command=col3TitleClicked,
            background="lightskyblue1", fg="white")
            col3Title.pack(fill="x")

            line = customGui.BlankSpace(col3, height=1, background="black")
            line.pack(fill="x")

            col3.pack(side="left", fill="both", expand=True)

            col4 = tk.Frame(table, relief="solid", borderwidth=1)
            col4["background"] = col4.master["background"]

            col4Title = tk.Button(col4, text="Datetime", font="courier 12 bold", cursor="hand2", relief="flat", command=col4TitleClicked, 
            background="lightskyblue1", fg="white")
            col4Title.pack(fill="x")

            line = customGui.BlankSpace(col4, height=1, background="black")
            line.pack(fill="x")

            col4.pack(side="left", fill="both", expand=True)

            for j in range(22):
                if(22*i+j < len(historiesLst)):
                    info = historiesLst[22*i+j].getInfo()
                    tk.Label(col1, text=str(22*i+j+1)+".", font="courier 12", fg="white", background="lightskyblue1").pack(fill="x")
                    tk.Label(col3, text=info["productName"], font="courier 12", background="white").pack(fill="x")
                    tk.Label(col4, text=info["date"], font="courier 12", background="white").pack(fill="x")

            table.pack(fill="both", expand=True)
            pages.append(table)

        tableContainer.pack(fill="both", expand=True)

        pagination = tk.Frame(body, pady=5)
        pagination["background"] = pagination.master["background"]

        space = customGui.BlankSpace(pagination)
        space.pack(fill="both", expand=True, side="left")

        for i in range(pageNumbers):
            if i == 0 :
                customGui.PageBtn(pagination, str(i+1), "disabled", pageBtns, pages[i]).pack(side="left")
            else:
                customGui.PageBtn(pagination, str(i+1), "normal", pageBtns, pages[i]).pack(side="left")

        space = customGui.BlankSpace(pagination)
        space.pack(fill="both", expand=True, side="left")

        pagination.pack(fill="x")

        body.pack(side="left", fill="both", expand=True)
        #table end

        mainPage.pack(expand=True, fill="both")
        mainPageContainer.pack(expand=True, fill="both")

        page.pack(expand=True, fill="both")
        page.mainloop()
        #GUI END

        return output

    def showProductInputHistory(self, historiesLst, user, descending):
        output = {}

        #GUI
        page = tk.Frame(self.root)

        #navbar
        navBar = customGui.Navbar(page, user, output, page)
        navBar.pack(fill="x")
        #navbar end

        #back-button
        backBtn = tk.Frame(page, padx=20, pady=5)
        btn = customGui.BackButton(backBtn, output, page)
        btn.pack(side="left")
        backBtn.pack(fill="x")
        #back-button end

        #main-page
        mainPageContainer = tk.Frame(page, padx=20, pady=5)
        mainPage = tk.Frame(mainPageContainer, background="white", relief="solid", borderwidth=1)

        #profile-btns
        lst = tk.Frame(mainPage)
        lst["background"] = lst.master["background"]

        for i in self.availableProfileTabs.keys():
            temp = customGui.ProfileBtns(lst, i, output, page, self.availableProfileTabs[i])
            temp.pack(fill="x")
            if i == "Input Product History" :
                temp.disable()

        logout = customGui.logOutButton(lst, output, page)
        logout.pack(fill="x")

        lst.pack(side="left", fill="y")
        #profile-btns end

        line = customGui.BlankSpace(mainPage, width=1, background="black")
        line.pack(side="left", fill="y")
        
        #table
        pageNumbers = math.ceil(len(historiesLst)/22)
        pageBtns = customGui.PageBtns()
        pages = list()

        body = tk.Frame(mainPage)
        body["background"] = body.master["background"]

        def col3TitleClicked():
            output["action"] = "input-product-history"
            output["col"] = "product_name"
            output["descending"] = not descending

            page.quit()
            page.destroy()

        def col4TitleClicked():
            output["action"] = "input-product-history"
            output["col"] = "input_date"
            output["descending"] = not descending

            page.quit()
            page.destroy()

        tableContainer = tk.Frame(body)
        tableContainer["background"] = tableContainer.master["background"]

        for i in range(pageNumbers):
            table = tk.Frame(tableContainer)
            table["background"] = table.master["background"]

            col1 = tk.Frame(table, relief="solid", borderwidth=1, background="lightskyblue1")
            
            col1Title = tk.Label(col1, text="No.", font="courier 12 bold", relief="flat", padx=5, pady=5, 
            background="lightskyblue1", fg="white")
            col1Title.pack(fill="x")

            line = customGui.BlankSpace(col1, height=1, background="black")
            line.pack(fill="x")

            col1.pack(side="left", fill="y")

            col3 = tk.Frame(table, relief="solid", borderwidth=1)
            col3["background"] = col3.master["background"]

            col3Title = tk.Button(col3, text="Product", font="courier 12 bold", cursor="hand2", relief="flat", command=col3TitleClicked,
            background="lightskyblue1", fg="white")
            col3Title.pack(fill="x")

            line = customGui.BlankSpace(col3, height=1, background="black")
            line.pack(fill="x")

            col3.pack(side="left", fill="both", expand=True)

            col4 = tk.Frame(table, relief="solid", borderwidth=1)
            col4["background"] = col4.master["background"]

            col4Title = tk.Button(col4, text="Datetime", font="courier 12 bold", cursor="hand2", relief="flat", command=col4TitleClicked, 
            background="lightskyblue1", fg="white")
            col4Title.pack(fill="x")

            line = customGui.BlankSpace(col4, height=1, background="black")
            line.pack(fill="x")

            col4.pack(side="left", fill="both", expand=True)

            for j in range(22):
                if(22*i+j < len(historiesLst)):
                    info = historiesLst[22*i+j].getInfo()
                    tk.Label(col1, text=str(22*i+j+1)+".", font="courier 12", fg="white", background="lightskyblue1").pack(fill="x")
                    tk.Label(col3, text=info["productName"], font="courier 12", background="white").pack(fill="x")
                    tk.Label(col4, text=info["date"], font="courier 12", background="white").pack(fill="x")

            table.pack(fill="both", expand=True)
            pages.append(table)

        tableContainer.pack(fill="both", expand=True)

        pagination = tk.Frame(body, pady=5)
        pagination["background"] = pagination.master["background"]

        space = customGui.BlankSpace(pagination)
        space.pack(fill="both", expand=True, side="left")

        for i in range(pageNumbers):
            if i == 0 :
                customGui.PageBtn(pagination, str(i+1), "disabled", pageBtns, pages[i]).pack(side="left")
            else:
                customGui.PageBtn(pagination, str(i+1), "normal", pageBtns, pages[i]).pack(side="left")

        space = customGui.BlankSpace(pagination)
        space.pack(fill="both", expand=True, side="left")

        pagination.pack(fill="x")

        body.pack(side="left", fill="both", expand=True)
        #table end

        mainPage.pack(expand=True, fill="both")
        mainPageContainer.pack(expand=True, fill="both")

        page.pack(expand=True, fill="both")
        page.mainloop()
        #GUI END

        return output

    def showProductEditHistory(self, historiesLst, user, descending):
        output = {}

        #GUI
        page = tk.Frame(self.root)

        #navbar
        navBar = customGui.Navbar(page, user, output, page)
        navBar.pack(fill="x")
        #navbar end

        #back-button
        backBtn = tk.Frame(page, padx=20, pady=5)
        btn = customGui.BackButton(backBtn, output, page)
        btn.pack(side="left")
        backBtn.pack(fill="x")
        #back-button end

        #main-page
        mainPageContainer = tk.Frame(page, padx=20, pady=5)
        mainPage = tk.Frame(mainPageContainer, background="white", relief="solid", borderwidth=1)

        #profile-btns
        lst = tk.Frame(mainPage)
        lst["background"] = lst.master["background"]

        for i in self.availableProfileTabs.keys():
            temp = customGui.ProfileBtns(lst, i, output, page, self.availableProfileTabs[i])
            temp.pack(fill="x")
            if i == "Edit Product History" :
                temp.disable()

        logout = customGui.logOutButton(lst, output, page)
        logout.pack(fill="x")

        lst.pack(side="left", fill="y")
        #profile-btns end

        line = customGui.BlankSpace(mainPage, width=1, background="black")
        line.pack(side="left", fill="y")
        
        #table
        pageNumbers = math.ceil(len(historiesLst)/22)
        pageBtns = customGui.PageBtns()
        pages = list()

        body = tk.Frame(mainPage)
        body["background"] = body.master["background"]

        def col3TitleClicked():
            output["action"] = "edit-product-history"
            output["col"] = "name"
            output["descending"] = not descending

            page.quit()
            page.destroy()

        def col4TitleClicked():
            output["action"] = "edit-product-history"
            output["col"] = "price"
            output["descending"] = not descending

            page.quit()
            page.destroy()

        def col5TitleClicked():
            output["action"] = "edit-product-history"
            output["col"] = "qty"
            output["descending"] = not descending

            page.quit()
            page.destroy()

        def col6TitleClicked():
            output["action"] = "edit-product-history"
            output["col"] = "edit_date"
            output["descending"] = not descending

            page.quit()
            page.destroy()


        tableContainer = tk.Frame(body)
        tableContainer["background"] = tableContainer.master["background"]

        for i in range(pageNumbers):
            table = tk.Frame(tableContainer)
            table["background"] = table.master["background"]

            col1 = tk.Frame(table, relief="solid", borderwidth=1, background="lightskyblue1")
            
            col1Title = tk.Label(col1, text="No.", font="courier 12 bold", relief="flat", padx=5, pady=5, 
            background="lightskyblue1", fg="white")
            col1Title.pack(fill="x")

            line = customGui.BlankSpace(col1, height=1, background="black")
            line.pack(fill="x")

            col1.pack(side="left", fill="y")

            col3 = tk.Frame(table, relief="solid", borderwidth=1)
            col3["background"] = col3.master["background"]

            col3Title = tk.Button(col3, text="Product Name", font="courier 12 bold", cursor="hand2", relief="flat", command=col3TitleClicked,
            background="lightskyblue1", fg="white")
            col3Title.pack(fill="x")

            line = customGui.BlankSpace(col3, height=1, background="black")
            line.pack(fill="x")

            col3.pack(side="left", fill="both", expand=True)

            col4 = tk.Frame(table, relief="solid", borderwidth=1)
            col4["background"] = col4.master["background"]

            col4Title = tk.Button(col4, text="Price", font="courier 12 bold", cursor="hand2", relief="flat", command=col4TitleClicked, 
            background="lightskyblue1", fg="white")
            col4Title.pack(fill="x")

            line = customGui.BlankSpace(col4, height=1, background="black")
            line.pack(fill="x")

            col4.pack(side="left", fill="both", expand=True)

            col5 = tk.Frame(table, relief="solid", borderwidth=1)
            col5["background"] = col5.master["background"]

            col5Title = tk.Button(col5, text="Qty", font="courier 12 bold", cursor="hand2", relief="flat", command=col5TitleClicked, 
            background="lightskyblue1", fg="white")
            col5Title.pack(fill="x")

            line = customGui.BlankSpace(col5, height=1, background="black")
            line.pack(fill="x")

            col5.pack(side="left", fill="both", expand=True)

            col6 = tk.Frame(table, relief="solid", borderwidth=1)
            col6["background"] = col6.master["background"]

            col6Title = tk.Button(col6, text="Datetime", font="courier 12 bold", cursor="hand2", relief="flat", command=col6TitleClicked, 
            background="lightskyblue1", fg="white")
            col6Title.pack(fill="x")

            line = customGui.BlankSpace(col6, height=1, background="black")
            line.pack(fill="x")

            col6.pack(side="left", fill="both", expand=True)

            for j in range(22):
                if(22*i+j < len(historiesLst)):
                    info = historiesLst[22*i+j].getInfo()
                    tk.Label(col1, text=str(22*i+j+1)+".", font="courier 12", fg="white", background="lightskyblue1").pack(fill="x")
                    
                    if(info["name"][0] != info["name"][1]):
                        tk.Label(col3, text=info["name"][1], font="courier 12", background="white", fg="blue").pack(fill="x")
                    else:
                        tk.Label(col3, text=info["name"][1], font="courier 12", background="white").pack(fill="x")

                    if(info["price"][0] < info["price"][1]):
                        tk.Label(col4, text="\u2191"+str(info["price"][1]), font="courier 12", background="white", fg="green").pack(fill="x")
                    elif(info["price"][0] > info["price"][1]):
                        tk.Label(col4, text="\u2193"+str(info["price"][1]), font="courier 12", background="white", fg="red").pack(fill="x")
                    else:
                        tk.Label(col4, text=str(info["price"][1]), font="courier 12", background="white").pack(fill="x")

                    if(info["qty"][0] < info["qty"][1]):
                        tk.Label(col5, text="\u2191"+str(info["qty"][1]), font="courier 12", background="white", fg="green").pack(fill="x")
                    elif(info["qty"][0] > info["qty"][1]):
                        tk.Label(col5, text="\u2193"+str(info["qty"][1]), font="courier 12", background="white", fg="red").pack(fill="x")
                    else:
                        tk.Label(col5, text=str(info["qty"][1]), font="courier 12", background="white").pack(fill="x")

                    tk.Label(col6, text=info["date"], font="courier 12", background="white").pack(fill="x")

                    

            table.pack(fill="both", expand=True)
            pages.append(table)

        tableContainer.pack(fill="both", expand=True)

        pagination = tk.Frame(body, pady=5)
        pagination["background"] = pagination.master["background"]

        space = customGui.BlankSpace(pagination)
        space.pack(fill="both", expand=True, side="left")

        for i in range(pageNumbers):
            if i == 0 :
                customGui.PageBtn(pagination, str(i+1), "disabled", pageBtns, pages[i]).pack(side="left")
            else:
                customGui.PageBtn(pagination, str(i+1), "normal", pageBtns, pages[i]).pack(side="left")

        space = customGui.BlankSpace(pagination)
        space.pack(fill="both", expand=True, side="left")

        pagination.pack(fill="x")

        body.pack(side="left", fill="both", expand=True)
        #table end

        mainPage.pack(expand=True, fill="both")
        mainPageContainer.pack(expand=True, fill="both")

        page.pack(expand=True, fill="both")
        page.mainloop()
        #GUI END

        return output

class Customer(User):
    def __init__(self, root):
        super().__init__(root)
        self.availableProfileTabs["Transaction History"] = {"action" : "transaction-history", "col" : "transaction_date", "descending" : True}

    def showProductDetail(self, data):
        output = {}

        #GUI
        body = tk.Frame(self.root)

        #navbar
        navBar = customGui.Navbar(body, data["user"], output, body)
        navBar.pack(fill="x")
        #navbar end

        #back-button
        backBtn = tk.Frame(body, padx=20, pady=5)

        btn = customGui.BackButton(backBtn, output, body)

        btn.pack(side="left")

        backBtn.pack(fill="x")
        #back-button end

        #product-detail
        container = tk.Frame(body, padx=20, pady=5)
        
        innerContainer = tk.Frame(container, background="white", borderwidth=1, relief="solid")

        productImg = customGui.Picture(innerContainer, data["product"].getInfo()["pic"], 500, 500, "white")
        productImg.pack(side="left", fill="both", expand=True)

        line = customGui.BlankSpace(innerContainer, width=1, background="black")
        line.pack(side="left", fill="y")

        productDesc = tk.Frame(innerContainer)
        productDesc["background"] = productDesc.master["background"]

        productName = tk.Frame(productDesc)
        productName["background"] = productName.master["background"]

        name = tk.Label(productName, text=data["product"].getInfo()["name"], fg="blue", font="courier 20 bold", wraplength=500)
        name["background"] = name.master["background"]
        name.pack(fill="both", expand=True)

        productName.pack(fill="x")

        space = customGui.BlankSpace(productDesc, height=20)
        space.pack(fill="x")

        productPrice = tk.Frame(productDesc, padx=10, pady=10)
        productPrice["background"] = productPrice.master["background"]

        caption = tk.Label(productPrice, text="Price : ", font="courier 16")
        caption["background"] = caption.master["background"]
        caption.pack(side="left")

        price = tk.Label(productPrice, text="Rp"+customGui.priceBeautify(data["product"].getInfo()["price"]), font="courier 16")
        price["background"] = price.master["background"]
        price.pack(side="left")

        productPrice.pack(fill="x")

        productQty = tk.Frame(productDesc, padx=10, pady=10)
        productQty["background"] = productQty.master["background"]

        caption = tk.Label(productQty, text="Quantity : ", font="courier 16")
        caption["background"] = caption.master["background"]
        caption.pack(side="left")

        qty = tk.Label(productQty, text=data["product"].getInfo()["qty"], font="courier 16")
        qty["background"] = qty.master["background"]
        qty.pack(side="left")

        productQty.pack(fill="x")

        productSold = tk.Frame(productDesc, padx=10, pady=10)
        productSold["background"] = productSold.master["background"]

        caption = tk.Label(productSold, text="Sold : ", font="courier 16")
        caption["background"] = caption.master["background"]
        caption.pack(side="left")

        sold = tk.Label(productSold, text=data["product"].getInfo()["sold"], font="courier 16")
        sold["background"] = sold.master["background"]
        sold.pack(side="left")

        productSold.pack(fill="x")

        space = customGui.BlankSpace(productDesc)
        space.pack(fill="both", expand=True)

        btnContainer = tk.Frame(productDesc, padx=20, pady=20)
        btnContainer["background"] = btnContainer.master["background"]
        
        respond = tk.Label(btnContainer, text=data["respond"], anchor="w", font="courier 16")
        respond["background"] = respond.master["background"]
        if(data["respond"] == "Transaction Success"):
            respond["fg"] = "green"
        else :
            respond["fg"] = "red"
        respond.pack(fill="x")
        
        space = customGui.BlankSpace(btnContainer, height=5)
        space.pack(fill="x")

        transactionContainer = tk.Frame(btnContainer)
        transactionContainer["background"] = transactionContainer.master["background"]

        line1 = tk.Frame(transactionContainer)
        line1["background"] = line1.master["background"]
        label = tk.Label(line1, text="Buy Qty : ", font="courier 16")
        label["background"] = label.master["background"]
        label.pack(side="left")

        ammountContainer = tk.Frame(line1, background="white", pady=5, padx=5, relief="solid", borderwidth=1)
        ammount = tk.Entry(ammountContainer, font="courier 16", bd=0)
        ammount.insert(0, "0")
        ammount.pack(fill="both", expand=True)
        ammountContainer.pack(side="left", fill="both", expand=True)
        line1.pack(fill="x")

        space = customGui.BlankSpace(transactionContainer, height=5)
        space.pack(fill="x")
        
        buyBtn = tk.Button(transactionContainer, text="Buy", font="courier 16 bold", fg="white", background="lightskyblue1", cursor="hand2")
        def buyBtnClicked():
            output["action"] = "buy"
            output["product"] = data["product"]
            output["ammount"] = ammount.get()
 

            body.quit()
            body.destroy()

        buyBtn["command"] = buyBtnClicked
        buyBtn.pack(fill="x")

        transactionContainer.pack(fill="both", expand=True)

        btnContainer.pack(fill="x")

        productDesc.pack(side="left", expand=True, fill="both")

        innerContainer.pack(expand=True, fill="both")

        container.pack(expand=True, fill="both")
        #product-detail end

        body.pack(expand=True, fill="both")
        body.mainloop()
        #GUI END

        return output

    def showTransactionHistory(self, historiesLst, user, descending):
        output = {}

        #GUI
        page = tk.Frame(self.root)

        #navbar
        navBar = customGui.Navbar(page, user, output, page)
        navBar.pack(fill="x")
        #navbar end

        #back-button
        backBtn = tk.Frame(page, padx=20, pady=5)
        btn = customGui.BackButton(backBtn, output, page)
        btn.pack(side="left")
        backBtn.pack(fill="x")
        #back-button end

        #main-page
        mainPageContainer = tk.Frame(page, padx=20, pady=5)
        mainPage = tk.Frame(mainPageContainer, background="white", relief="solid", borderwidth=1)

        #profile-btns
        lst = tk.Frame(mainPage)
        lst["background"] = lst.master["background"]

        for i in self.availableProfileTabs.keys():
            temp = customGui.ProfileBtns(lst, i, output, page, self.availableProfileTabs[i])
            temp.pack(fill="x")
            if i == "Transaction History" :
                temp.disable()

        logout = customGui.logOutButton(lst, output, page)
        logout.pack(fill="x")

        lst.pack(side="left", fill="y")
        #profile-btns end

        line = customGui.BlankSpace(mainPage, width=1, background="black")
        line.pack(side="left", fill="y")
        
        #table
        pageNumbers = math.ceil(len(historiesLst)/22)
        pageBtns = customGui.PageBtns()
        pages = list()

        body = tk.Frame(mainPage)
        body["background"] = body.master["background"]

        def col3TitleClicked():
            output["action"] = "transaction-history"
            output["col"] = "product_name"
            output["descending"] = not descending

            page.quit()
            page.destroy()

        def col4TitleClicked():
            output["action"] = "transaction-history"
            output["col"] = "qty"
            output["descending"] = not descending

            page.quit()
            page.destroy()

        def col5TitleClicked():
            output["action"] = "transaction-history"
            output["col"] = "price"
            output["descending"] = not descending

            page.quit()
            page.destroy()

        def col6TitleClicked():
            output["action"] = "transaction-history"
            output["col"] = "total"
            output["descending"] = not descending

            page.quit()
            page.destroy()

        def col7TitleClicked():
            output["action"] = "transaction-history"
            output["col"] = "transaction_date"
            output["descending"] = not descending

            page.quit()
            page.destroy()


        tableContainer = tk.Frame(body)
        tableContainer["background"] = tableContainer.master["background"]

        for i in range(pageNumbers):
            table = tk.Frame(tableContainer)
            table["background"] = table.master["background"]

            col1 = tk.Frame(table, relief="solid", borderwidth=1, background="lightskyblue1")
            
            col1Title = tk.Label(col1, text="No.", font="courier 12 bold", relief="flat", padx=5, pady=5, 
            background="lightskyblue1", fg="white")
            col1Title.pack(fill="x")

            line = customGui.BlankSpace(col1, height=1, background="black")
            line.pack(fill="x")

            col1.pack(side="left", fill="y")

            col3 = tk.Frame(table, relief="solid", borderwidth=1)
            col3["background"] = col3.master["background"]

            col3Title = tk.Button(col3, text="Product", font="courier 12 bold", cursor="hand2", relief="flat", command=col3TitleClicked,
            background="lightskyblue1", fg="white")
            col3Title.pack(fill="x")

            line = customGui.BlankSpace(col3, height=1, background="black")
            line.pack(fill="x")

            col3.pack(side="left", fill="both", expand=True)

            col4 = tk.Frame(table, relief="solid", borderwidth=1)
            col4["background"] = col4.master["background"]

            col4Title = tk.Button(col4, text="Qty", font="courier 12 bold", cursor="hand2", relief="flat", command=col4TitleClicked, 
            background="lightskyblue1", fg="white")
            col4Title.pack(fill="x")

            line = customGui.BlankSpace(col4, height=1, background="black")
            line.pack(fill="x")

            col4.pack(side="left", fill="both", expand=True)

            col5 = tk.Frame(table, relief="solid", borderwidth=1)
            col5["background"] = col5.master["background"]

            col5Title = tk.Button(col5, text="Price", font="courier 12 bold", cursor="hand2", relief="flat", command=col5TitleClicked, 
            background="lightskyblue1", fg="white")
            col5Title.pack(fill="x")

            line = customGui.BlankSpace(col5, height=1, background="black")
            line.pack(fill="x")

            col5.pack(side="left", fill="both", expand=True)

            col6 = tk.Frame(table, relief="solid", borderwidth=1)
            col6["background"] = col6.master["background"]

            col6Title = tk.Button(col6, text="Total", font="courier 12 bold", cursor="hand2", relief="flat", command=col6TitleClicked, 
            background="lightskyblue1", fg="white")
            col6Title.pack(fill="x")

            line = customGui.BlankSpace(col6, height=1, background="black")
            line.pack(fill="x")

            col6.pack(side="left", fill="both", expand=True)

            col7 = tk.Frame(table, relief="solid", borderwidth=1)
            col7["background"] = col7.master["background"]

            col7Title = tk.Button(col7, text="Datetime", font="courier 12 bold", cursor="hand2", relief="flat", command=col7TitleClicked, 
            background="lightskyblue1", fg="white")
            col7Title.pack(fill="x")

            line = customGui.BlankSpace(col7, height=1, background="black")
            line.pack(fill="x")

            col7.pack(side="left", fill="both", expand=True)

            for j in range(22):
                if(22*i+j < len(historiesLst)):
                    info = historiesLst[22*i+j].getInfo()
                    tk.Label(col1, text=str(22*i+j+1)+".", font="courier 12", fg="white", background="lightskyblue1").pack(fill="x")
                    tk.Label(col3, text=info["productName"], font="courier 12", background="white").pack(fill="x")
                    tk.Label(col4, text=info["qty"], font="courier 12", background="white").pack(fill="x")
                    tk.Label(col5, text=info["price"], font="courier 12", background="white").pack(fill="x")
                    tk.Label(col6, text=info["total"], font="courier 12", background="white").pack(fill="x")
                    tk.Label(col7, text=info["date"], font="courier 12", background="white").pack(fill="x")

            table.pack(fill="both", expand=True)
            pages.append(table)

        tableContainer.pack(fill="both", expand=True)

        pagination = tk.Frame(body, pady=5)
        pagination["background"] = pagination.master["background"]

        space = customGui.BlankSpace(pagination)
        space.pack(fill="both", expand=True, side="left")

        for i in range(pageNumbers):
            if i == 0 :
                customGui.PageBtn(pagination, str(i+1), "disabled", pageBtns, pages[i]).pack(side="left")
            else:
                customGui.PageBtn(pagination, str(i+1), "normal", pageBtns, pages[i]).pack(side="left")

        space = customGui.BlankSpace(pagination)
        space.pack(fill="both", expand=True, side="left")

        pagination.pack(fill="x")

        body.pack(side="left", fill="both", expand=True)
        #table end

        mainPage.pack(expand=True, fill="both")
        mainPageContainer.pack(expand=True, fill="both")

        page.pack(expand=True, fill="both")
        page.mainloop()
        #GUI END

        return output

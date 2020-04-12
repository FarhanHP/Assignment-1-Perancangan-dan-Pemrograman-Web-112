import tkinter as tk
import controller

if __name__ == "__main__":
    root = tk.Tk()
    root.title("Olshop")

    w = root.winfo_screenwidth()
    h = root.winfo_screenheight()
    root.geometry(str(w)+"x"+str(h))

    guest = controller.Guest(root)
    user = None
    result = guest.login("")

    while True :
        #guest
        if(result["action"] == "register"):
            result = guest.register(result["error"])
        elif(result["action"] == "login"):
            result = guest.login(result["error"])

        #user
        elif(result["action"] == "login-confirmed"):
            user = result["data"]
            result = {"action" : "search-product", "keyword" : ""}
        elif(result["action"] == "search-product"):
            result = user.showProducts(result["keyword"])
        elif(result["action"] == "product-detail"):
            result = user.showProductDetail(result["product"])
        elif(result["action"] == "buy"):
            result = user.buy(result["product"], result["ammount"])
        elif(result["action"] == "edit-info"):
            result = user.editInfo(result["error"], result["success"])
        elif(result["action"] == "change-password"):
            result = user.changePassword(result["error"], result["success"])
        elif(result["action"] == "add-product"):
            result = user.addProduct(result["error"])
        elif(result["action"] == "manage-users"):
            result = user.manageUsers(result["interact"], result["target_user"])
        elif(result["action"] == "delete-product"):
            result = user.deleteProduct(result["product"])
        elif(result["action"] == "edit-product"):
            result = user.editProduct(result["product"], result["newValue"])
        elif(result["action"] == "assign-fire-history"):
            result = user.showAssignFireHistory(result["col"], result["descending"])
        elif(result["action"] == "transaction-history"):
            result = user.showTransactionHistory(result["col"], result["descending"])
        elif(result["action"] == "delete-product-history"):
            result = user.showProductDeleteHistory(result["col"], result["descending"])
        elif(result["action"] == "input-product-history"):
            result = user.showProductInputHistory(result["col"], result["descending"])
        elif(result["action"] == "edit-product-history"):
            result = user.showProductEditHistory(result["col"], result["descending"])
        elif(result["action"] == "user-detail"):
            result = user.showUserDetail(result["user"])

        else:
            print(result["action"])
            root.quit()
            root.destroy()
            break

    root.mainloop()

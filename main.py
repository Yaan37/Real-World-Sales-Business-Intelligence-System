





from datetime import date,datetime
import csv
import os 


class Backbone:

    def __init__(self):
        self.sales_file_name = "sales.csv"
        self.customer_file_name = "customers.csv"
        self.order_ID = None
        self.date = None
        self.customer_name = None
        self.customer_ID = None
        self.product_name = None
        self.category = None
        self.quantity = None
        self.unit_price = None
        self.discount = None
        self.city = None
        self.payment_method = None




    def load_file(self , filename):     

        if os.path.exists(filename):
            with open(filename , "r" , newline = "") as file:
                listing =  list(csv.reader(file))
                if len(listing) == 1:
                    return []
                else:
                    return listing
        else:
            return []
         
            
    def save_sales(self ,data):

        flag = os.path.exists(self.sales_file_name)
        with open(self.sales_file_name , "a" , newline="") as file:
            writer = csv.writer(file)

            if not flag:
                listing = self.load_file(self.sales_file_name)
                if len(listing) < 1:
                    writer.writerow(["Order_ID","Date","Customer_ID","Product","Category","Quantity","Unit_Price","Discount","City","Payment_Method"])

            writer.writerow(data)


    def save_customer_record(self, record):
        flag = os.path.exists(self.customer_file_name)
        with open(self.customer_file_name , "a" , newline="") as file:
            writer = csv.writer(file)

            if not flag:
                listing = self.load_file(self.customer_file_name)
                if len(listing) < 1:
                    writer.writerow("Customer_ID,Name")

            else:
                
                writer.writerow(record)
    

    def Add_sale(self):


        # ------------------------------------------------- 
        # WHOLE SET UP FOR CUSTOMER ID AND NAME 
        # ------------------------------------------------- 

        new_user_flag  = False
        file = self.load_file(self.customer_file_name)
        while True:      
            user_exist = input("Does Customer already exist(Y/N): ").capitalize()

            if user_exist != "Y" and user_exist != "N":
                print("Option can only be 'Y' or 'N'.")
                continue
            break
    
        if user_exist == "Y":
            if file != []:
                while True:
                    exist_flag = False 
                    name = input("Enter the customer's name: ").replace(" ","").lower()

                    for line in file:
                        customer_ID = line[0]
                        customer_name = line[1]

                        if name == customer_name.replace(" ","").lower():
                            self.customer_ID = customer_ID
                            self.customer_name = customer_name
                            exist_flag = True

                    if exist_flag:
                        break
                    else:
                        print("User-Name doesn't exist")        
            else:
                print("Customer record is empty. Please enter customer details:")


        elif user_exist == "N":
            file_empty_flag = False 
            file_customer = self.load_file(self.customer_file_name)

            if file_customer == []:
                file_empty_flag = True
                

            while True:
                found_flag = False
                name = input("Enter the customer's name: ").replace(" ","").lower()

                if file_empty_flag:
                    break

                for line in file_customer[1:]:
                    customer_ID = line[0]
                    customer_name = line[1]

                    if name == customer_name.replace(" ","").lower():
                        print(f"This username already exist and its customer id is {customer_ID}")
                        found_flag = True
                        break              

                if not found_flag:
                    break
                    
            self.customer_name = name
            length = len(file_customer)
            refined_id_number = file_customer[length - 1 ][0]
            final_id_number = int(refined_id_number.removeprefix("CUS"))

            self.customer_ID = f"CUS{final_id_number + 1:03}"
            new_user_flag  = True
            print(f"{self.customer_name} your customer id is: {self.customer_ID}")

            # self.customer_name = name
            # length = int(len(file_customer) - 1)
            # self.customer_ID = f"CUS{file_customer[length][0] + 1:03}"
            # new_user_flag  = True
            # print(f"{self.customer_name} your customer id is: {self.customer_ID}")
            





        # ---------------------------------------------
        # FOR ORDER-ID  
        # ---------------------------------------------

        # STORING USER ID IN THE FINAL VAULT
        file1 = self.load_file(self.sales_file_name)

        if file1 == []:
            final_order_id = "ORD001"
        else:    
            last_order_id = file1[-1][0]
            cal_order_id = int(last_order_id.removeprefix("ORD")) 
            final_order_id = f"ORD{cal_order_id + 1:03d}"

        # FINAL ORDER VALUE SET 
        self.order_ID = final_order_id



        

        # ---------------------------------------------
        # FOR DATE  
        # ---------------------------------------------

        # ASKING TIME FROM USER 
        while True:
            user_date = input("Enter Date (YYYY-MM-DD): ")
            try:
                final_date = datetime.strptime(user_date, "%Y-%m-%d").date()
                # CHECKING IF DATE IS CURRENT OR FUTURE 
                if final_date > date.today():
                    print("Invalid Date: Date cannot be in the future.")
                    continue
                print("Valid Date")
                break
            except ValueError:
                print("Invalid Date")
        # FINAL TIME VALUE SET 
        self.date = final_date.strftime("%Y-%m-%d")





        # ---------------------------------------------
        # FOR CUSTOMER-ID
        # ---------------------------------------------
        file3 = self.load_file(self.customer_file_name)          

        if file3 != []:
            while True:
                id_flag = False
                id = input("Enter your customer id: ").replace(" ","").upper()

                if  new_user_flag: 
                    if id == self.customer_ID:
                        id_flag = True
                        break
                else:
                    for line in file3:
                        customer_id = line[0]
                        if id == customer_id.replace(" ","").upper():
                            id_flag = True
                            break         

                    if id_flag:
                        break
                    else:
                        print("Enter correct customer id")
                        continue
        else:
            print("Customer record is empty. Please enter customer details:")
                




        
        # ---------------------------------------------
        # FOR PRODUCT
        # ---------------------------------------------
        while True:          
            pro_name = input("Enter the name of your product: ").strip()

            if not pro_name.strip():
                print("Error: Product name cannot be blank.")
                continue
            break
        self.product_name = pro_name


        

        # ---------------------------------------------
        # FOR CATEGORY
        # ---------------------------------------------
        while True:
            try:        
                    
                Cat_types = ["Electronics","Clothing","Footwear","Food","Furniture"]
                print("Category:")
                for i in range(len(Cat_types)):
                    print(f"{i+1}. {Cat_types[i]}")

                cat_opt = int(input("Choose any one category from these option(1-5): "))
                if cat_opt >= 1 and cat_opt <= 5:
                    cat = Cat_types[cat_opt - 1]
                    self.category = cat
                    break
                else:
                    print("Choose correct option")
                    continue

            except ValueError as ve:
                print(f"Error occured: {ve}") 






        # ---------------------------------------------
        # FOR QUANTITY
        # ---------------------------------------------
        while True:
            try:
                quan = int(input("Enter product quantity: "))
                if quan <= 0:
                    print("Value must be greater than zero.")
                    continue
                break
            except ValueError as ve:
                print(f"Error: {ve}")
        self.quantity = quan






        # ---------------------------------------------
        # FOR QUANTITY
        # ---------------------------------------------
        while True:
            try:             
                unit_pri = float(input("Enter the price of the unit: "))
                if unit_pri <= 0:
                    print("Unit price must be greater than zero")
                    continue
                break
            except ValueError as ve:
                print(f"Error:  Unit price must be any number greater than zero.")
        self.unit_price = unit_pri





        # ---------------------------------------------
        # FOR Discount
        # ---------------------------------------------
        while True:
            try:
                disc = int(input("Enter the discount percentage: "))
                if disc > 100 or disc < 0:
                    print("Unit price must be greater than zero")
                    continue

                break
            except ValueError as ve:
                print("Error: Discount must be a number between 0 and 100.")
        self.discount = disc



           

            

        # ---------------------------------------------
        # FOR City            
        # ---------------------------------------------
        while True:
                
            city_name = input("Enter the name of your City: ").strip()

            if not city_name:
                print("Error: City name cannot be blank.")
                continue
            break
        self.city_name = city_name



        # ---------------------------------------------
        # FOR Payment Method
        # ---------------------------------------------
        while True:
            try:                          
                pay_types = ["Cash","Credit Card","Debit Card","Bank Transfer","Easypaisa","JazzCash"]
                print("Payment Method:")

                for i in range(len(pay_types)):
                    print(f"{i+1}. {pay_types[i]}")

                pay_opt = int(input("Choose any one category from these option(1-6): "))
                if pay_opt >= 1 and pay_opt <= 6:
                    pay = pay_types[pay_opt - 1]
                    self.payment_method = pay
                    break
                else:
                    print("Choose correct option")
                    continue
            except ValueError as ve:
                print(f"Error occured: {ve}") 




        # # ---------------------------------------------
        # # SAVING SALES
        # # ---------------------------------------------
        data = [
         self.order_ID,
         self.date,
         self.customer_ID,
         self.product_name,
         self.category,
         self.quantity,
         self.unit_price,
         self.discount,
         self.city_name,
         self.payment_method]
        self.save_sales(data)
        


        # # ---------------------------------------------
        # # SAVING CUSTOMER RECORD
        # # ---------------------------------------------
        if new_user_flag:
            record = [self.customer_ID , self.customer_name]
            self.save_customer_record(record)

        print("Sale added successfully!")                       


    def View_sales(self):

        data = self.load_file(self.sales_file_name)

        if data == []:
            print("No sales records found.")
            return 

        for i in data[1:]:
            print(f"Order ID: {i[0]} ")
            print(f"Date: {i[1]}") 
            print(f"Customer ID: {i[2]}")  
            print(f"Product: {i[3]}") 
            print(f"Category: {i[4]}") 
            print(f"Quantity: {i[5]}")
            print(f"Unit Price: {i[6]}")
            print(f"Discount: {i[7]}")
            print(f"City: {i[8]}") 
            print(f"Payment Method: {i[9]}")
            print("\n-----------------------------------\n")


    def Search_sales(self):

        ord_id = input("Enter the Order ID you want to find: ")

        data = self.load_file(self.sales_file_name)

        if data == []:
            print("Order ID not found")
            return

        for i in data:

            if ord_id == i[0]:
                print("\n-----------------------------------")
                print(f"Order ID: {i[0]} ")
                print(f"Date: {i[1]}") 
                print(f"Customer ID: {i[2]}")  
                print(f"Product: {i[3]}") 
                print(f"Category: {i[4]}") 
                print(f"Quantity: {i[5]}")
                print(f"Unit Price: {i[6]}")
                print(f"Discount: {i[7]}")
                print(f"City: {i[8]}") 
                print(f"Payment Method: {i[9]}")
                print("\n-----------------------------------\n")
                return 

        print("Order ID not found")
      

    def delete_sales(self):
        ord_id = input("Enter the Order ID you want to delete: ")
        
        data = self.load_file(self.sales_file_name)
        new_data = []

        id_found_flag = False
        if data == []:
            print("Order ID not found")
            return

        for i in data:

            if ord_id == i[0]:
                id_found_flag = True
            else:
                new_data.append(i)


        if not id_found_flag:
            print("Order ID not found")

        else:
            with open(self.sales_file_name , "w" , newline="") as file:
                writer = csv.writer(file)
                writer.writerows(new_data)

            print("Sale deleted successfully.")
        

    def Main(self):


        while True:
            try:
                print("========================================")
                print("SALES MANAGEMENT SYSTEM")
                print("========================================\n")
                print("1. Add Sale")
                print("2. View Sales")
                print("3. Search Sale")
                print("4. Delete Sale")
                print("5. Exit\n")

                option = int(input("Please select an option (1-5): "))

                if option > 5 or option < 1:
                    print("Error: Option can be between 1 to 5.")
            
                if option == 1:
                    self.Add_sale()

                elif option == 2:
                    self.View_sales()
                   
                elif option == 3:
                    self.Search_sales()

                elif option == 4:
                    self.delete_sales()

                elif option == 5:
                    break
                 

            except Exception as e:
                # print("Error: Option should be in number between 1 to 5.")
                print(e)

        




if __name__ == "__main__":

    bk = Backbone()
    # bk.Add_sale()
    bk.Main()



# 1. Add Sale
# 2. View Sales
# 3. Search Sale
# 4. Delete Sale
# 5. Exit


# TESTING FILE DELETING AND THAN CHECKING CODE FOR FINAL TOUCH UP 



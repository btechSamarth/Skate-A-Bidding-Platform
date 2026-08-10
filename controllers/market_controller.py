from database.db_functions import list_product1
from database.db_functions import view_my_products1
from database.db_functions import view_all_products1
from database.db_functions import update_my_product1
from database.db_functions import get_product_Ids1
import traceback
from helpers.string_input_checker import string_checker
from helpers.int_input_checker import neg_int_checker , int_1_2_checker

def list_product(user):
    user_id = user.Id
    categories = ["electronics" , "clothes" , "accesories" , "footwears" , "transport"]
    name = ""

    print("                                                                              Welcome to SKATE Market Place")
    while(True):
        name = input("Please Enter Name of Your Product\n---->")
        flag = string_checker(name)
        if not flag:
            continue
        break
    quantity = 0
    while(True):
        quantity = input("Please Enter Avaialable Quantity\n---->")
        flag = neg_int_checker(quantity)
        if not flag:
            continue
        quantity = int(quantity)
        break
    price = 0
    while(True):
        price = input("Please Enter Marked Price\n---->")
        flag = neg_int_checker(price)
        if not flag:
            continue
        price = int(price)
        break
    prod_cat = ""
    while(True):
        try:
            print("                                                                              Please Provide Suitable Category (Index)")
            count = 1
            for cat in categories:
                print(                                                                              f"{count}) {cat}")
                count += 1
            user_input = int(input("Enter Your Choice\n---->"))-1
            prod_cat = categories[user_input]
        except (IndexError , Exception):
            traceback.print_exc()
            print("                                                                              Please Enter Correct Index")
        else:
            break

    list_product1(user_id , name , price , quantity , prod_cat)
    print("                                                                              Your Product is Live Now!!")

def view_my_products(user):
    offset = 0
    count = 1
    while(True):
        products = view_my_products1(user.Id , offset)
        count = 1
        if(len(products) == 0):
            print("                                                                              No More Products")
            break
        print("                                                                              Showing Results (5)")
        
        for row in products:
            print(f"                                                                              ------------------Product {count}----------------")
            print(f"                                                                              Product Id: {row.Id}\n                                                                              Name: {row.Name}\n                                                                              Price: {row.Price}\n                                                                              Quantity: {row.Quantity}\n                                                                              Category: {row.Category}")
            print("\n\n")
            count += 1
        user_input = -1
        while(True):
            user_input = input("Press 1 To Show More And 2 For Exit\n---->")
            flag = int_1_2_checker(user_input)
            if not flag:
                continue
            user_input = int(user_input)
            break
        if(user_input == 2):
            return
        offset += 5

    

def view_all_products(user):
    view_all_products1(user.Id)

def update_my_product(user):
    s_id = user.Id
    product_ids = get_product_Ids1(s_id)
    if(product_ids == None):
        return
    product_id = -1
    while(True):
        product_id = input("Please Enter Id of The Product To Update\n---->")
        if(int(product_id) not in product_ids):
            print("                                                                              Please Enter a Valid Product Id")
            print("\n")
        else:
            break
    quantity = 0
    while(True):
        quantity = input("How Much Quantity Is Avaialable Now?\n---->")
        flag = neg_int_checker(quantity)
        if not flag:
            continue
        quantity = int(quantity)
        break
    update_my_product1(s_id , product_id , quantity)


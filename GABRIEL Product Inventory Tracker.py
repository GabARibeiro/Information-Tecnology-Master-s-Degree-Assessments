#Inventory Management System

#Author: Gabriel A Ribeiro
#Created in Sep/24

#Step 1: Create a list of dictionaries with Chat GPT's provided Dataset:
products = [
    {'Code': 101, 'Name': 'Silver Sparkling Ring', 'Category': 'Rings', 'Price': 99.00, 'Stock Quantity': 15, 'Average Fortnightly Sales': 10},
    {'Code': 102, 'Name': 'Rose Gold Heart Ring', 'Category': 'Rings', 'Price': 129.00, 'Stock Quantity': 8, 'Average Fortnightly Sales': 12},
    {'Code': 103, 'Name': 'Gold Infinity Ring', 'Category': 'Rings', 'Price': 249.00, 'Stock Quantity': 5, 'Average Fortnightly Sales': 7},
    {'Code': 104, 'Name': 'Pearl Stud Earrings', 'Category': 'Earrings', 'Price': 79.00, 'Stock Quantity': 20, 'Average Fortnightly Sales': 15},
    {'Code': 105, 'Name': 'Crystal Drop Earrings', 'Category': 'Earrings', 'Price': 99.00, 'Stock Quantity': 12, 'Average Fortnightly Sales': 18},
    {'Code': 106, 'Name': 'Gold Hoop Earrings', 'Category': 'Earrings', 'Price': 159.00, 'Stock Quantity': 7, 'Average Fortnightly Sales': 6},
    {'Code': 107, 'Name': 'Silver Chain Necklace', 'Category': 'Necklaces', 'Price': 149.00, 'Stock Quantity': 9, 'Average Fortnightly Sales': 10},
    {'Code': 108, 'Name': 'Rose Gold Pendant Necklace', 'Category': 'Necklaces', 'Price': 199.00, 'Stock Quantity': 6, 'Average Fortnightly Sales': 7},
    {'Code': 109, 'Name': 'Gold Locket Necklace', 'Category': 'Necklaces', 'Price': 299.00, 'Stock Quantity': 4, 'Average Fortnightly Sales': 6},
    {'Code': 110, 'Name': 'Silver Charm Bracelet', 'Category': 'Bracelets', 'Price': 139.00, 'Stock Quantity': 14, 'Average Fortnightly Sales': 11},
    {'Code': 111, 'Name': 'Gold Bangle Bracelet', 'Category': 'Bracelets', 'Price': 199.00, 'Stock Quantity': 5, 'Average Fortnightly Sales': 9},
    {'Code': 112, 'Name': 'Rose Gold Link Bracelet', 'Category': 'Bracelets', 'Price': 179.00, 'Stock Quantity': 8, 'Average Fortnightly Sales': 5},
    {'Code': 113, 'Name': 'Silver Heart Charm', 'Category': 'Charms', 'Price': 59.00, 'Stock Quantity': 25, 'Average Fortnightly Sales': 20},
    {'Code': 114, 'Name': 'Rose Gold Star Charm', 'Category': 'Charms', 'Price': 69.00, 'Stock Quantity': 18, 'Average Fortnightly Sales': 22},
    {'Code': 115, 'Name': 'Gold Cross Charm', 'Category': 'Charms', 'Price': 99.00, 'Stock Quantity': 10, 'Average Fortnightly Sales': 15},
    {'Code': 116, 'Name': 'Silver Love Charm', 'Category': 'Charms', 'Price': 49.00, 'Stock Quantity': 30, 'Average Fortnightly Sales': 28},
    {'Code': 117, 'Name': 'Silver Zodiac Ring', 'Category': 'Rings', 'Price': 89.00, 'Stock Quantity': 13, 'Average Fortnightly Sales': 9},
    {'Code': 118, 'Name': 'Gold Diamond Ring', 'Category': 'Rings', 'Price': 399.00, 'Stock Quantity': 4, 'Average Fortnightly Sales': 5},
    {'Code': 119, 'Name': 'Crystal Teardrop Earrings', 'Category': 'Earrings', 'Price': 129.00, 'Stock Quantity': 10, 'Average Fortnightly Sales': 14},
    {'Code': 120, 'Name': 'Gold Tennis Bracelet', 'Category': 'Bracelets', 'Price': 299.00, 'Stock Quantity': 6, 'Average Fortnightly Sales': 8}
]

#Step 2: Create function to validate user input
def cleanEntry(text):
    
    #List containing space and most of the possible special characters
    special_characters = ['¨',' ','\n, ','!', '@', '#', '$', '%', '^', '&', '*', '(', ')', '-', '_', '=', '+','[', ']', '{', '}', '|', '/', '\\', ':', ';', '"', "'", '<', '>', ',','.','?','~', '`']
    
    #Request user input, convert it to lowercase and save it as inside_var1
    inside_var=input('\n'+text).lower() 
    
    #Check each digit of the user's input and remove the special characters
    for digit in inside_var:
        if digit in special_characters:
            inside_var=inside_var.replace(digit,'')
        else:
            pass            
    #Return inside_var
    return inside_var

#Step 3: Print a "Welcome" message 
print('Hello! Welcome to the Inventory Management System!'+'\n'+'This program will help you manage your store stock!')

#Step 4: Create a loop to allow the user to go back to the main menu after using any function
iteration_0 = 1
while iteration_0 == 1:
    
    # Step 5: Print the main menu
    print('What would you like to do?'+'\n')
    print('1 Search for products by category')
    print('2 Check stock levels')
    print('3 Calculate the total value of inventory')
    print('4 Order Assist')
    
    #Step 6: Create a loop that allows the user to type again the desired option in the main menu in case of a mistype
    iteration_1 = 1
    while iteration_1 == 1:
        
        #Step 7: Request the user to type the desired option in the main menu
        decision = cleanEntry('Enter option (Please type a number between 1-4): ')
             
        #Step 8: This function allows the user to search for products by category
        if decision == '1' or decision == 'one':
            
            #Step 9: Print to the user the categories available 
            print('\n'+'Which category would you like to check?')
            print("(Please type: 'Rings', 'Earrings', 'Necklaces', 'Bracelets' or 'Charms')")
            
            #Step 10: Create a loop to allow the user to type again the desired category in case of mistype
            iteration_2 = 1
            while iteration_2 == 1:
                
                #Step 11: Request the user to type the desired category
                category = cleanEntry('Enter category: ')

                #Step 12: Ajust customer input
                if category == 'ring' or category == 'earring' or category == 'necklace' or  category == 'bracelet' or category == 'charm':
                    category = category+'s'
                else:
                    pass

                #Step 13: Generate a new list containing the products included in the desired category
                filtered_products = [f for f in products if f['Category'].lower() == category]
                
                #Step 14: Line to executed in case there is at least a product in the desired category
                if filtered_products != []:
                    
                    #Step 15:  Print to user the items of the desired category
                    print('\n'+'These are the items in the category '+category.capitalize()+':'+'\n') 
                    
                    for f in filtered_products:
                        print('Item Code:',f['Code'],'\t','Name:',f['Name'],'\t','Price: AUD',f['Price'])
                    
                    #Step 16: It breaks the loop for user's input for the desired category
                    iteration_2 = 0
                
                #Step 17: Line to executed in case there is not a product in the desired category                 
                else:
                    
                    #Step 18: Print a message to acknowledge the user
                    print('\n'+'No products were found in the category '+category+'.'+'\n'+"Please, type: 'Rings', 'Earrings', 'Necklaces', 'Bracelets' or 'Charms'")
            
            #Step 19: It breaks the loop that allows the user to type again the desired option in the main menu in case of a mistype
            iteration_1 = 0     
        
        #Step 20: This function allows the user to check the stock levels 
        elif  decision == '2' or decision == 'two':
            
            #Step 21: Create a loop to allow the user to type again the item code in case of mistype
            iteration_3 = 1
            while iteration_3 == 1:
        
                #Step 22: Request the user to type the item code
                item_code = cleanEntry('Type Item Code: ')
                
                #Step 23: Generate a new list containing the item related to the provided item code if there is any                           
                filtered_products = [f for f in products if str(f['Code'])==item_code]
                
                #Step 24: Line to be executed in case there is a product related to the provided item code
                if filtered_products != []:
                    
                    #Step 25: Print to the user the item
                    print('\n'+'This is the item requested:','\n')
                    for f in filtered_products:
                        print('Item Code:',f['Code'],'\t','Name:',f['Name'],'\t','Stock Quantity',f['Stock Quantity'])
                        
                        #Step 26: It breaks the loop for user's input for item code
                        iteration_3 = 0
                
                #Step 27: Line to executed in case there is not a product in the desired category         
                else:
                    
                    #Step 28: Print a message to acknowledge the user
                    print('\n'+'Product not found.')
            
            #Step 29: It breaks the loop that allows the user to type again the desired option in the main menu in case of a mistype         
            iteration_1 = 0   
            
                
        #Step 30: This function allows the user to calculate the total value of inventory
        elif decision == '3' or decision == 'three':

            #Step 31: It creates an empty list called 'category_stock_value'
            category_stock_value = {}
            
            #Step 32: This function will execute the indented lines for each category in products
            for f in products:
                
                #Step 33: It creates a variable called category containing the selected category name
                category = f['Category']
                
                #Step 34: It creates a variable called stock_value which is the result of the price multiplied by the stock quantity
                stock_value = f['Price']*f['Stock Quantity']
                
                #Step 35: It checks if there is the selected category in the 'category_stock_value' and if yes, it adds her value to the respective stock value
                if category in category_stock_value:
                    category_stock_value[category] += stock_value
                
                #Step 36: If the selected category is not in the 'category_stock_value', it create the category and define its inicial value as the product’s stock value.   
                else:
                    category_stock_value[category] = stock_value
            
            
            #Step 37: It announces the exhibition of the stock value for each category and the total
            print('\n'+'Total stock value by category:'+'\n')
            
            #Step 38: It prints to the user the stock value of each category 
            for category in category_stock_value:
                print(category + ": AUD " + str(category_stock_value[category]))
            
            #Step 39: Create a variable called 'total_stock_value' and define it as the sum of the individual category stock values
            total_stock_value=0
            for category in category_stock_value:
                total_stock_value += category_stock_value[category]
            
            #Step 40: It prints to the user the total stock value    
            print('\n'+'Total Stock: AUD '+str(total_stock_value))
            
            #Step 41: It breaks the loop that allows the user to type again the desired option in the main menu in case of a mistype
            iteration_1 = 0   
            
        
        #Step 42: This function presents to the user a suggestion of the items to be ordered
        elif decision == '4' or decision == 'four':   
            
            #Step 43: Generate a new list containing the products where the stock quantity is lower than the average fortnightly sales
            suggested_order = [f for f in products if f['Stock Quantity'] < f['Average Fortnightly Sales']]
            
            
            #Step 44: Line to executed in case there is at least a product in the list
            if suggested_order != []:
                print('\n'+'This is the suggested order:'+'\n')
                
                #Step 45: Create a variable called 'suggested_amount' that equals the average fortnightly sales less the stock quantity
                for f in suggested_order :
                    suggested_amount = f['Average Fortnightly Sales'] - f['Stock Quantity']
                    f['Suggested Amount'] = suggested_amount
                    
                    #Step 46: Print the items which need to be ordered and the necessary amount
                    print('Item Code:',f['Code'],'\t','Name:',f['Name'],'\t','Average Fortnightly Sales:',f['Average Fortnightly Sales'],'\t','Stock Quantity:','\t',f['Stock Quantity'],'\t','Suggested Amount:','\t',f['Suggested Amount'])
            
            #Step 47: Line to be executed in case there is no product that needs to be ordered.
            elif suggested_order == []:
                
                #Step 48: Print a message to acknowledge the user
                print('\n'+'Stock levels are optimal. New orders are not necessary.')
            
            #Step 49: It breaks the loop that allows the user to type again the desired option in the main menu in case of a mistype    
            iteration_1 = 0   
        
        #Step 50: Line to be executed if the user types an invalid input in the main menu
        else:
            
            #Step 51: Print a message to acknowledge the user
            print('\n'+'You have entered an incorrect value. Please enter a number from 1 to 4.')
        

    #Step 52: Ask the user if they want to keep the loop after finishing the last interaction
    print('\n'+"Would you like to go back to the main menu?")
    
    #Step 53: Create a loop to allow the user to type again the desired option in case of mistype
    iteration_4 = 1
    while iteration_4 == 1:
        
        #Step 54: Obtain the user's input (decision to keep the loop)
        decision = cleanEntry('\n'+"Type 'Yes' or 'No':"+'\t')
        
        #Step 55: Line to be executed if the decision is "Yes"
        if "yes" in decision:
            print('\n')
            
            #Step 56: It breaks the loop that allows the user to type again the desired option in case of a mistype
            iteration_4 = 0
        
        #Step 57: Line to be executed if the decision is "No"
        elif "no" in decision:
            
            #Step 58: Print the "Thank you" message
            print('\n' + "Thank you for using the Inventory Management System!")
            
            #Step 59: It breaks the loop that allows the user to type again the desired option in case of a mistype
            iteration_4 = 0
            
            #Step 60: It breaks the loop that allows the user to be redirected to the main menu
            iteration_0 = 0
        
        #Step 61: Line to be executed if the user types an invalid input
        else:
            
            #Step 62: Print a message to acknowledge the user
            print('\n'+"Invalid option, please type 'Yes' or 'No'")


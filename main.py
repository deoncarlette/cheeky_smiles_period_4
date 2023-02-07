def party_invoice():
    
    price_dict = {
        "H": 50,
        "S": 40,
        "Y": 35,
        "p": 10,
        "b": 2,
        "s": .5,
        "C": 15,
        "c": .25,
    }

    word_dict = {
        "H": "Bouncy House",
        "S": "Slip & Slide",
        "Y": "Yard Sign",
        "p": "Pizza",
        "b": "Burger",
        "s": "Soda",
        "C": "Cake",
        "c": "Cupcake",
    }
    
    base_price = 100
    
    # input each addon as a string with the quantity and type
    # seperate each addon with a comma
    addons = input("What are the party addons? ")
    # print(addons)
    
    # use the "split" method to convert the addons to a list
    addons_list = addons.split(",")
    # print(addons_list)
    
    invoice_statement = "\n\nThank you for choosing Cheeky Smiles for your party needs! Here is your itemized invoice:\n\n"
    
    for addon in addons_list:
        
        item = addon[-1]
        count = int(addon[:-1])
        item_price = price_dict.get(item) * count
        item_name = word_dict.get(item)
        # print("item: ", item, "count: ", count)
        
        base_price = base_price + item_price
        # print(base_price)

        itemized = f"{item_name}, {count}, ${'{:.2f}'.format(item_price)}"
        print(itemized)


    print(invoice_statement)



    
    
    
    
    
    
    
    
    
    
    
    
if __name__ == "__main__":
    party_invoice()

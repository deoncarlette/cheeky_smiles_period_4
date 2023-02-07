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
        # print("item: ", item, "count: ", count)
        
        base_price = base_price + item_price
        # print(base_price)

        itemized = f"{item}, {count}, ${'{:.2f}'.format(item_price)}"
        print(itemized)


    print(invoice_statement)



    
    
    
    
    
    
    
    
    
    
    
    
if __name__ == "__main__":
    party_invoice()

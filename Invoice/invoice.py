"""
Program: invoice.py
Author: Jessie Horvath
Modified: 04/02/2022

The purpose of this program is to create a class with required and optional
inputs, update a dictionary of items to purchase and return the itemized
receipt, or invoice, of those products and their total and tax.
"""
class Invoice:
    def __init__(self, invoice_id, cid, address, lname, fname, phone, item_with_price = {}):
        name_char = set("ABCDEFGHIJKLMNOPQRSTUVWXYZabcdefghijklmnopqrstuvwxyz")
        phone_char = set("1234567890-()")
        cid_char = set("1234567890")
        iid_char = set("1234567890")
        addy_char = set("1234567890abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ, ")
        if not (name_char.issuperset(lname) and name_char.issuperset(fname)):
            raise ValueError
        if not phone_char.issuperset(phone):
            raise ValueError
        if not cid_char.issuperset(str(cid)):
            raise ValueError
        if not iid_char.issuperset(str(invoice_id)):
            raise ValueError
        if not addy_char.issuperset(address):
            raise ValueError
        self.invoice_id = invoice_id
        self.cid = cid
        self.lname = lname
        self.fname = fname
        self.phone = phone
        self.address = address
        self.item_dict = item_with_price
# Add iid and cid and item with price to these methods
    def __str__(self):
        return self.cid + ": " + self.lname + ", " + self.fname + " Phone: " + self.phone + " Address: " + self.address

    def __repr__(self):
        return "Customer({}, {}, {}, {}, {})".format(self.cid, self.lname, self.fname, self.phone, self.address)

    def change_lname(self, new_name):
        self.lname = new_name
    
    def change_fname(self, new_name):
        self.fname = new_name
    
    def change_phone(self, new_phone):
        self.phone = new_phone
    
    def change_address(self, new_add):
        self.address = new_add
    
    def display(self):
        return self.customer_id + ": " + self.lname + ", " + self.fname + " Phone: "  + self.phone + " Address: " + self.address

    def add_item(self, dict):
        self.item_dict.update(dict)
    
    def create_invoice(self):
        for key, value in self.item_dict.items():
            print(key, ".....$", value)
        subtotal = sum(self.item_dict.values())
        tax = subtotal * 0.06
        total = subtotal + tax
        print(f"Tax......${tax:.2f}")
        print(f"Total......${total:.2f}")
        return None

# Driver code
invoice = Invoice(1, 123, '1313 Disneyland Dr, Anaheim, CA 92802' ,'Mouse', 'Minnie', '555-867-5309')
invoice.add_item({'iPad': 799.99})
invoice.add_item({'Surface': 999.99})
invoice.create_invoice()

"""
Output:
iPad.....$799.99
Surface.....$999.99
Tax......... $108.00
Total.......$1907.98
"""
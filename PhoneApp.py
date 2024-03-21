# Making a phone app
class PhoneApp:
    def __init__(self):
        #Initialisation is over
        # We've to display the contact
        def display_contact(self):
            for name, number in self.contacts.items:
                print ("f{name}: {number}")
        # We have to add a contact
        def add_contact(self, name,number):
            if name in self.contacts:
                print ("The name is there.")
            else:
                self.contacts[name]= number
                print("The number has been added!")
        #We have to delete a contact
        def delete_contact(self,name):
            if name in self.contacts:
                del self.contacts[name]
                print("The number is deleted.")   
            else:
                print("The number does not exist.")    
        # We have to check a contact
        def check_contact(self,name):
            if name in self.contacts:
                print ("f {name}: {number}") 
            else:
                print("The number is not there.")    
            # Working code
                app= PhoneApp()
                while True:
                    print ("\nOptions!")
                    print ("1) Add contacts")
                    print ("2) Delete Contacts")
                    print  ("3) Display Contact")
                    print ("4) Check Contact")
                    print ("5) Exit")

                if n== "1":
                    a= input("Enter a name")
                    b= input("Enter a number")
                    app.add_contact(a,b)
                elif n== "2":
                    a= input("Enter a name.")
                    app.delete_contact(a)
                elif n== "3":
                    app.display_contact(a)
                elif n== "4":
                    a= input("Enter a number.")
                    app.check_contact(a)
                elif n== "5":
                    print("That's it!")   
                    return
                else:
                    print("Invalid input, try again.")     



                
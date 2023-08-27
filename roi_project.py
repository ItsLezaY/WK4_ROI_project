class User:
    
    def __init__(self, username, password):
        self.username = username
        self.password = password
        self.properties = []

        
    def add_property(self, property_name, total_invested):
        property = Property(property_name, total_invested)
        self.properties.append(property)

        
    def get_property_by_name(self, property_name):
        for prop in self.properties:
            if prop.name.lower() == property_name.lower():
                return prop
        return None

    
    def display_properties(self):
        print(f"Properties for User: {self.username}")
        for property in self.properties:
            print(f"- {property.name}")

            

class Property:
    def __init__(self, name, total_invested):
        self.name = name
        self.expenses = {}
        self.incomes = {}
        self.cash_flow = None
        self.total_invested = total_invested
        self.roi = None

        
    def calculate_cash_flow(self):
        total_income = sum(self.incomes.values())
        total_expense = sum(self.expenses.values())
        self.cash_flow = total_income - total_expense

        
    def calculate_roi(self):
        if self.cash_flow is not None and self.total_invested > 0:
            annual_cash_flow = self.cash_flow * 12
            self.roi = (annual_cash_flow / self.total_invested) * 100

            
    def display_property_info(self):
        print(f"Property Name: {self.name}")
        print("Incomes:")
        for income_type, amount in self.incomes.items():
            print(f"{income_type}: ${amount}")
        print("Expenses:")
        for expense_type, amount in self.expenses.items():
            print(f"{expense_type}: ${amount}")
        if self.cash_flow is not None:
            print(f"Monthly Cash Flow: ${self.cash_flow:.2f}")
        else:
            print("Monthly Cash Flow not calculated.")
        print(f"Total Invested: ${self.total_invested:.2f}")
        if self.roi is not None:
            print(f"ROI: {self.roi:.2f}%")
        else:
            print("ROI not calculated yet.")

            
    def add_income(self, income_type, amount):
        self.incomes[income_type] = amount
        self.calculate_cash_flow()
        self.calculate_roi()

        
    def add_expense(self, expense_type, amount):
        self.expenses[expense_type] = amount
        self.calculate_cash_flow()
        self.calculate_roi()


        
users = []


users.append(User("user1", "password1"))
users.append(User("user2", "password2"))


current_user = None



def main():
    global current_user

    
    while True:
        print("\nOptions:")
        if current_user is None:
            print("1. Sign In")
            print("2. Create New User")
            print("3. Exit")
        else:
            print("1. Sign Out")
            print("2. Add Property and Total Money Invested")
            print("3. View Property")
            print("4. Add Monthly Expenses")
            print("5. Add Monthly Income")
            print("6. Calculate ROI for Property")
            print("7. Delete Property")
            print("8. Exit")

        choice = input("Select an option: ").strip()
        

        if current_user is None:
            if choice == "1":
                username = input("Enter your username: ")
                password = input("Enter your password: ")

                for user in users:
                    if user.username == username and user.password == password:
                        current_user = user
                        print(f"Welcome, {current_user.username}!")
                        break
                else:
                    print("Invalid username/password. Please try again.")
                    
                    
            elif choice == "2":
                username = input("Create username: ")
                password = input("Create password: ")
                new_user = User(username, password)
                users.append(new_user)
                current_user = new_user
                print(f"User '{username}' created.")
            elif choice == "3":
                break
            else:
                print("Please select a valid option.")
                
                
        else:
            if choice == "1":
                current_user = None
                print("Signed out.")
                
                
            elif choice == "2":
                property_name = input("Enter property name: ")
                total_invested = float(input("Enter total money invested: "))
                current_user.add_property(property_name, total_invested)
                print(f"Property '{property_name}' added.")
                
            elif choice == "3":
                property_name = input("Enter property name: ")
                property = current_user.get_property_by_name(property_name)
                if property:
                    property.display_property_info()
                else:
                    print(f"Property '{property_name}' not found.")
                    
                    
            elif choice == "4":
                property_name = input("Enter property name: ")
                property = current_user.get_property_by_name(property_name)
                if property:
                    expense_type = input("Enter expense type: ")
                    expense_amount = float(input("Enter monthly expense amount: "))
                    property.add_expense(expense_type, expense_amount)
                    print(f"Monthly Expense added to '{property_name}'.")
                else:
                    print(f"Property '{property_name}' not found.")
                    
                    
            elif choice == "5":
                property_name = input("Enter property name: ")
                property = current_user.get_property_by_name(property_name)
                if property:
                    income_type = input("Enter income type: ")
                    income_amount = float(input("Enter monthly income amount: "))
                    property.add_income(income_type, income_amount)
                    print(f"Monthly Income added to '{property_name}'.")
                else:
                    print(f"Property '{property_name}' not found.")
                    
                    
            elif choice == "6":
                property_name = input("Enter property name: ")
                property = current_user.get_property_by_name(property_name)
                if property:
                    property.calculate_roi()
                    property.display_property_info()
                else:
                    print(f"Property '{property_name}' not found.")
                    
                    
            elif choice == "7":
                property_name = input("Enter property name to delete: ")
                property = current_user.get_property_by_name(property_name)
                if property:
                    current_user.properties.remove(property)
                    print(f"Property '{property_name}' deleted.")
                else:
                    print(f"Property '{property_name}' not found.")
            elif choice == "8":
                break
            else:
                print("Please select a valid option.")

if __name__ == "__main__":
    main()
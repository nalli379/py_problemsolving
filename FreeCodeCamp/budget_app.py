
class Category():
    def __init__(self, category):
        self.name = str(category)
        self.category = category
        self.ledger = list()
        self.balance = 0
    
    def deposit(self, amount, description=''):
        #adds money to balance
        #method append a dictionary object to ledge list with amount and description as keys
        self.amount = float(amount)
        self.balance += float(amount)
        self.description = description
        self.ledger.append({"amount": self.amount, "description": self.description})

        
    def withdraw(self, w_amount, w_description=''):
        #amount passed in should be stored in the ledger as a negative number.
        #This method should return True if the withdrawal took place, and False otherwise.
        self.w_amount = float(w_amount)
        self.w_description = w_description
        if self.check_funds(w_amount):
            self.ledger.append({"amount": -self.w_amount, "description": self.w_description})
            self.balance -= self.w_amount
            return True
        else:
            return False

    def get_balance(self):
        #returns the current balance of the budget category based on the deposits and withdrawals that have occurred.        
        return self.balance
    
    
    def transfer(self, t_amount, t_category):
        #transfer of funds from one category to another category - if funds not available returns false otherwise true
        if self.check_funds(t_amount):
            self.withdraw(t_amount, f"Transfer to {t_category.name}")            
            t_category.deposit(t_amount, f"Transfer from {self.name}")
            return True
        else:
            return False
    
    
    def check_funds(self, amount):
        #checks if the balance is greater than the amount, it returns False if the amount is greater otherwise True. 
        if self.balance > amount:
            return True
        else:
            return False
    
    def total_withdraws(self):
        #total withdraws for given category
        total = 0
        for item in self.ledger:
            if item["amount"] < 0:
                total += item["amount"]
        return total
    
    def __repr__(self):
        return f'Object: {self.category}'
    
    def __str__(self):
        #receipt showing transactions on a ledger for given category
        stat1 = f"{self.name:*^30}"
        stat2 = ''
        for item in self.ledger:
            stat2 = stat2 + '\n' + f"{item['description'][0:23]:<23}{item['amount']:>7.2f}"
        stat3 = f"Total:\t{self.balance:.2f}"
        
        return stat1 + '\n' + stat2 + '\n' + stat3
  

def total_withdraws_all_categories(categories):
    #calculate total withdraws for list of categories using class method total withdraws
    subtotals_dict = {}
    total = 0
    
    for category in categories:
        subtotal = category.total_withdraws()
        subtotals_dict[category.name] = subtotal
        total += subtotal
    
    return total, subtotals_dict
    
def calculate_percent(subtotals, total):
    #calculate percentage to nearest 10
    percentages = {}
    for item, subtotal in subtotals.items():
        percent = round((subtotal/total)*100, -1)
        percentages[item] = percent
    
    return percentages

def draw_x_axis(percent_dict, categories, chart):
    #function writing left hand axis of chart
    x = 100
    for num in range(11):
        x_row = f"{x}".rjust(3) +"| "
        #taking percent values to either indicate percent spent or not
        for name, percent in percent_dict.items():
            
            if percent >= (x):
                x_row += "o  "
            else:
                x_row += "   "
        chart += x_row + "\n"
        x -= 10
        
    #setting out x axis length based on categories length    
    x_axis = "    -"
    for i in range(len(categories)):
        x_axis += ("---")
    chart += x_axis + "\n"
    
    #set longest name length using category names for y axis
    name_length = 0
    for category in categories:
        if len(category.name) > name_length:
            name_length = len(category.name)
    
    return chart, name_length

def draw_y_axis(percent_dict, categories, chart, name_length):
    #draw y axis category names letter by letter leaving space 
    y = 0
    while y <= name_length:
        y_row = "     "
        for key, value in percent_dict.items():
            category_name = key
            try:
                y_row += category_name[y] + "  "
            except:
                y_row += "   "
        
        #at end of y axis create new row to print second row of letters across
        if y <= name_length -1:
            chart += y_row + "\n"
        else:
            chart += y_row.strip("")
        
        y += 1
    
    return chart

  
def create_spend_chart(categories):
    #function to execute sub tasks for creating a spend chart
    chart = "Percentage spent by category\n"
    total, subtotals = total_withdraws_all_categories(categories)
    percent_dict = calculate_percent(subtotals, total)
    
    chart_x, name_length = draw_x_axis(percent_dict, categories, chart)
    
    chart_x_y = draw_y_axis(percent_dict, categories, chart_x, name_length)
    
    return chart_x_y

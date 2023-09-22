class Category:
    def __init__(self, category):
        self.category = category
        self.ledger = []

    def deposit(self, amount, description=""):
        self.ledger.append({"amount": amount, "description": description})

    def withdraw(self, amount, description=""):
        if self.check_funds(amount):
            self.ledger.append({"amount": -amount, "description": description})
            return True
        return False

    def get_balance(self):
        return sum(item["amount"] for item in self.ledger)

    def transfer(self, amount, budget_category):
        if self.check_funds(amount):
            self.withdraw(amount, f"Transfer to {budget_category.category}")
            budget_category.deposit(amount, f"Transfer from {self.category}")
            return True
        return False

    def check_funds(self, amount):
        return amount <= self.get_balance()

    def get_total_withdraw(self):
        return sum(
            transaction["amount"]
            for transaction in self.ledger
            if transaction["amount"] < 0
        )

    def get_total_deposit(self):
        return sum(
            transaction["amount"]
            for transaction in self.ledger
            if transaction["amount"] > 0
        )

    def __str__(self):
        title = f"{self.category:*^30}\n"
        items = ""
        total = 0
        for item in self.ledger:
            description = item["description"][:23]
            amount = "{:.2f}".format(item["amount"])
            line_spacing = 23 - len(description) + 7 - len(amount)
            itemline = description + (" " * line_spacing) + amount + "\n"
            total = total + item["amount"]
            items += itemline
        return title + items + "Total: {:.2f}".format(total)


# create function that will take a list
def create_spend_chart(categories):
    chart = "Percentage spent by category\n"
    num_of_category = len(categories)

    total_spent = sum(category.get_total_withdraw() for category in categories)
    percentages_spending = [
        {
            "category": category.category,
            "spent percentage": (category.get_total_withdraw() / total_spent) * 100,
        }
        for category in categories
    ]
    print(percentages_spending)

    for i in range(100, -10, -10):
        chart = chart + str(i).rjust(3) + "| "
        j = 0
        for category in percentages_spending:
            bar = " " if category["spent percentage"] < i else "o"
            chart = chart + bar
            if j < num_of_category:
                chart += "  "
                j += 1
        chart = chart + "\n"

    chart += "    " + "-" * (1 + 3 * num_of_category)

    # get the category with the highest character count
    # max_char_count

    max_char_count = 0

    for category in categories:
        category_char_count = len(category.category)
        if category_char_count > max_char_count:
            max_char_count = category_char_count

    chart += "\n"

    k = 1
    for i in range(max_char_count):
        chart = f"{chart}     "
        j = 0
        for category in categories:
            char_print = category.category[i] if i < len(category.category) else " "
            chart += char_print
            if j < num_of_category:
                chart += "  "
                j += 1
        if k < max_char_count:
            chart = chart + "\n"
            k += 1

    return chart

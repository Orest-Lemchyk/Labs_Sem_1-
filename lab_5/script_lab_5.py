class Smartphone:
    def __init__(self, model = "no model", price = 0, memory = 0, battery_capacity = 0, phone_numbers=None):
        self.model = model
        self.price = price
        self.memory = memory
        self.battery_capacity = battery_capacity
        self.phone_numbers = phone_numbers if phone_numbers else []

    def get_model(self):
        return self._model

    def __repr__(self):
        return f"Model: {self.model}, Price: {self.price}, Memory: {self.memory}GB, Battery: {self.battery_capacity}mAh"


    def __del__(self):
        print(f"Phone {self.model} is deleted")

class Phonestore:
    def __init__(self):
        self.smartphones = []


    def add_smartphone(self, smartphone):
        self.smartphones.append(smartphone)


    def find_best_phone(self, budget):
        affordable_phones = [phone for phone in self.smartphones if phone.price <= budget]
        if affordable_phones:
            best_phone = sorted(affordable_phones, key=lambda x: (x.memory, x.battery_capacity), reverse=True)[0]
            return best_phone
        else:
            return "No phones available within your budget."


    def list_phones_sorted_by_price(self):
        return sorted(self.smartphones, key=lambda x: x.price)


def main():

    phone1 = Smartphone("iPhone 16", 999, 128, 2815)
    phone2 = Smartphone("Samsung Galaxy S23", 799, 256, 4000)
    phone3 = Smartphone("Xiaomi Mi 13", 699, 128, 4600)
    phone4 = Smartphone("OnePlus 11", 729, 256, 4500)

    store = Phonestore()
    store.add_smartphone(phone1)
    store.add_smartphone(phone2)
    store.add_smartphone(phone3)
    store.add_smartphone(phone4)

    while True:
        user_input = input("Enter a price or 'exit' : ").strip().lower()
        match user_input:
            case _ if user_input.isdigit():
                budget = int(user_input)
                best_phone = store.find_best_phone(budget)
                print(f"Best phone within budget: {best_phone}")
                sorted_phones = store.list_phones_sorted_by_price()
                print("Phones sorted by price:")
                for phone in sorted_phones:
                    print(phone)
            case "exit":
                break

main()

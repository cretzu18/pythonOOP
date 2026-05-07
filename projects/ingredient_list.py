import webbrowser

class Ingredient:
    def __init__(self, name : str, amount : int):
        self.name = name
        self.amount = amount

    def get_info(self):
        wiki_link = "https://en.wikipedia.org/wiki/" + self.name.capitalize()
        webbrowser.open(wiki_link, new=0)

    def __add__(self, other):
        new_amount = self.amount + other.amount
        return Ingredient(self.name, new_amount)
    
    def __str__(self):
        return f"{self.name}, amount: {self.amount}"
    
    def cook(self, amount):
        self.amount -= amount
        self.amount = max(0, self.amount)
        return self.amount

    
def print_main_menu():
    print("1. See ingredients list")
    print("2. Add ingredient to list")
    print("3. Remove ingredient to list")
    print("0. Exit")


if __name__ == "__main__":
    ingredient_list = list()

    while True:
        print_main_menu()
        try:
            option = int(input("Enter your option: "))
        except:
            print("Option must be a valid number\n")
            continue

        if option == 1:
            print("\n\n")
            for i, ingredient in enumerate(ingredient_list):
                print(f"{i + 1}. {ingredient}")
            print("\n\n")
            while True:
                option = int(input("Enter a ingredient number to see info or 0 to exit: "))
                if option == 0:
                    break
                try:
                    option -= 1
                    ingredient_list[option].get_info()
                except:
                    print("Invalid option!\n")
                
            
        elif option == 2:
            try:
                name = input("Enter ingredient name:")
                amount = int(input("Enter ingredient amount: "))

                names = [i.name.lower() for i in ingredient_list]
                if name.lower() in names:
                    idx = names.index(name)
                    ingredient_list[idx] += Ingredient(name, amount)
                else:
                    ingredient_list.append(Ingredient(name, amount))
                print("Ingredient added!\n\n")
            except:
                print("Invalid input!\n\n")
                continue

        elif option == 3:
            for i, ingredient in enumerate(ingredient_list):
                print(f"{i+1}. {ingredient}")

            try:
                delete = int(input("Select number of the ingredient you want to delete: "))
                ingredient_list.pop(delete - 1)
                print("Ingredient deleted\n\n")
            except:
                print("Invalid option to delete!\n\n")
                continue

        elif option == 0:
            break

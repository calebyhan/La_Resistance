import os
import re


class Game:
    def __init__(self):
        self.francs = 1000
        self.reichsmark = 10
        self.danger = 0
        self.distance = 0
        self.inventory = ["Handheld Radio", "First-aid kit", "Survival kit", "Rations"]

    @staticmethod
    def _info():
        os.system('cls' if os.name == 'nt' else 'clear')
        print("La Resistance is an Oregon Trail themed game based in 1944 designed to be difficult and may require strategy to beat the game.")
        print("You are a SOE agent tasked with delivering a crucial letter to an agent situated in Berlin. This must be done covertly since the Germans have learned of this plan.")
        print("\nThe goal of this game is to reach the final destination, Berlin, from Dover. There is a mandatory stop at Paris for resources and information.")
        print("You are to deliver secret intel crucial to defeating the Third Reich to a fellow spy in Berlin. If you get caught, there is no going back. Germany does not treat enemy spies kindly.")
        print("\nFor more detailed information and mechanics, please read the README.")

        input()

    def _menu(self):
        while True:
            os.system('cls' if os.name == 'nt' else 'clear')
            print("\t[0] Edit inventory")
            print("\t[1] View stats")
            print("\t[2] View shop")

            menu = input("\nChoose an option, or press enter to start: ").strip()

            if menu == "":
                break
            elif int(menu) in [0, 1, 2]:
                if int(menu) == 0:
                    self._remove_item()
                elif int(menu) == 1:
                    self._stats()
                elif int(menu) == 2 and self.distance < 1000:
                    self._france_shop()
                elif int(menu) == 2 and self.distance >= 1000:
                    self._german_shop()
            else:
                print("Invalid input.")

    def _setup(self):
        self._info()
        self._menu()

        os.system('cls' if os.name == 'nt' else 'clear')
        while True:
            self.difficulty = input("Select a difficulty: [0] Easy, [1] Medium, [2] Hard, [3] Insane: ").strip()
            if int(self.difficulty) in [0, 1, 2, 3]:
                break
            print("Invalid input.\n")

    def _main(self):
        while self.distance <= 1500:
            pass

    def _game_over(self, died):
        self.difficulty = 1
        if died:
            pass
        else:
            pass

    def _remove_item(self):
        while True:
            os.system('cls' if os.name == 'nt' else 'clear')
            print("Inventory:")
            for i, item in enumerate(self.inventory):
                print(f"\t[{str(i)}]: {item}")

            item_remove = input("\nChoose an item to remove, press enter to quit: ").strip()

            if item_remove == "":
                break
            elif int(item_remove) in list(range(0, len(self.inventory))):
                self.inventory.pop(int(item_remove))
                print("\nUpdated inventory: " + ", ".join(self.inventory))
                break
            else:
                print("Invalid input.")

    def _france_shop(self):
        while True:
            os.system('cls' if os.name == 'nt' else 'clear')
            print("France shop")
            print("\t[0] Train Ticket: 500 francs")
            print("\t[1] Revolver: 750 francs")
            print("\t[2] 6 bullets: 50 francs")
            print("\t[3] Extra camping supplies: 250 francs")

            fshop = input("\nEnter the number of the item you want to buy. Press enter to quit: ")

            if fshop == "":
                break
            elif int(fshop) in [0, 1, 2, 3]:
                if int(fshop) == 0 and self.francs >= 500:
                    self.francs -= 500
                    self.inventory.append("Train ticket")
                elif int(fshop) == 1 and self.francs >= 750:
                    self.francs -= 750
                    self.inventory.append("Revolver")
                elif int(fshop) == 2 and self.francs >= 50:
                    self.francs -= 50
                    found = False
                    for item in self.inventory:
                        if re.search("\d Bullets", item) is None:
                            item = str(int(item[0]) + 6) + " Bullets"
                            found = True
                    if not found:
                        self.inventory.append("6 Bullets")
                elif int(fshop) == 3 and self.francs >= 250:
                    self.francs -= 250
                    self.inventory.append("Extra camping supplies")
                    self.inventory.append("")
            else:
                print("Invalid input.")

    def _german_shop(self):
        while True:
            os.system('cls' if os.name == 'nt' else 'clear')
            print("German shop")
            print("\t[0] Train Ticket: 7 reichsmark")
            print("\t[1] 6 bullets: 0.5 reichsmark")
            print("\t[2] Radio antenna: 3 reichsmark")
            print("\t[3] Fake passport: 7 reichsmark")
            print("\t[4] Disguise kit: 1 reichsmark")

            gshop = input("\nEnter the number of the item you want to buy. Press enter to quit: ")

            if gshop == "":
                break
            elif int(gshop) in [0, 1, 2, 3, 4]:
                if int(gshop) == 0 and self.reichsmark >= 70:
                    self.reichsmark -= 7
                    self.inventory.append("Train ticket")
                elif int(gshop) == 1 and self.reichsmark >= 0.5:
                    self.reichsmark -= 0.5
                    self.inventory.append("6 Bullets")
                elif int(gshop) == 2 and self.reichsmark >= 3:
                    self.reichsmark -= 3
                    self.inventory.append("Radio antenna")
                elif int(gshop) == 3 and self.reichsmark >= 7:
                    self.reichsmark -= 7
                    self.inventory.append("Extra camping supplies")
                elif int(gshop) == 4 and self.reichsmark >= 1:
                    self.reichsmark -= 1
                    self.inventory.append("Disguise kit")
            else:
                print("Invalid input.")

    def _stats(self):
        print("STATS\n")
        print(f"Distance: {str(self.distance)}")
        print(f"Inventory: {', '.join(self.inventory)}")
        print(f"Danger: {str(self.danger)}")
        print(f"Francs: {str(self.francs)}, Reichsmark: {str(self.reichsmark)}")

    def play(self):
        self._setup()
        self._main()
        self._game_over()

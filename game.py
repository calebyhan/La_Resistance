import os


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
            print("[0] Edit inventory")
            print("[1] View stats")

            menu = input("\nChoose an option, press enter to start: ").strip()

            if menu == "":
                break
            elif int(menu) in [0, 1]:
                if int(menu) == 0:
                    self._remove_item()
            else:
                print("Invalid input.")

    def _setup(self):
        self._info()
        self._menu()

        while True:
            os.system('cls' if os.name == 'nt' else 'clear')
            self.difficulty = input("Select a difficulty: [0] Easy, [1] Medium, [2] Hard, [3] Insane: ").strip()
            if int(self.difficulty) in [0, 1, 2, 3]:
                break
            print("Invalid input.")

        self._main()

    def _main(self):
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

    def play(self):
        self._setup()

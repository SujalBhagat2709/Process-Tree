from process_engine import ProcessEngine


class ProcessTreeApp:

    def __init__(self):

        self.engine = ProcessEngine()

    def menu(self):

        while True:

            print("\n")

            print("=" * 35)

            print("        PROCESS TREE")

            print("=" * 35)

            print("1. Create Root Process")

            print("2. Add Child Process")

            print("3. Show Process Tree")

            print("4. Kill Process")

            print("5. Exit")

            choice = input("\nEnter Choice: ")

            if choice == "1":

                self.engine.create_root()

            elif choice == "2":

                self.engine.add_child()

            elif choice == "3":

                self.engine.show_tree()

            elif choice == "4":

                self.engine.kill_process()

            elif choice == "5":

                print("\nExiting Process Tree...")

                break

            else:

                print("\nInvalid Choice. Try Again.")


if __name__ == "__main__":

    app = ProcessTreeApp()

    app.menu()
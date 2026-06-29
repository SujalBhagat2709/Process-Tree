import json
import os


class ProcessEngine:

    def __init__(self):

        self.file_name = "process_tree.json"

        self.processes = {}

        self.load()

    def load(self):

        if os.path.exists(self.file_name):

            try:

                with open(

                    self.file_name,

                    "r",

                    encoding="utf-8"

                ) as file:

                    self.processes = json.load(file)

            except:

                self.processes = {}

    def save(self):

        with open(

            self.file_name,

            "w",

            encoding="utf-8"

        ) as file:

            json.dump(

                self.processes,

                file,

                indent=4

            )

    def create_root(self):

        print("\nCreate Root Process\n")

        name = input(

            "Process Name: "

        ).strip()

        if name == "":

            print("\nInvalid Name")

            return

        if name in self.processes:

            print("\nProcess Already Exists")

            return

        self.processes[name] = {

            "parent": None,

            "children": []

        }

        self.save()

        print("\nRoot Process Created.")

    def add_child(self):

        if not self.processes:

            print("\nNo Root Process Found.")

            return

        print("\nAvailable Processes\n")

        for process in self.processes:

            print("-", process)

        parent = input(

            "\nParent Process: "

        ).strip()

        if parent not in self.processes:

            print("\nParent Not Found")

            return

        child = input(

            "Child Process: "

        ).strip()

        if child == "":

            print("\nInvalid Name")

            return

        if child in self.processes:

            print("\nProcess Already Exists")

            return

        self.processes[child] = {

            "parent": parent,

            "children": []

        }

        self.processes[parent][

            "children"

        ].append(child)

        self.save()

        print("\nChild Process Added.")

    def show_tree(self):

        if not self.processes:

            print("\nNo Processes Found.")

            return

        print("\n========== PROCESS TREE ==========\n")

        for process in self.processes:

            if self.processes[process]["parent"] is None:

                self.print_tree(

                    process,

                    0

                )

    def print_tree(

        self,

        process,

        level

    ):

        print(

            "    " * level +

            "|-- " +

            process

        )

        for child in self.processes[

            process

        ][

            "children"

        ]:

            self.print_tree(

                child,

                level + 1

            )

    def kill_process(self):

        if not self.processes:

            print("\nNo Processes Found.")

            return

        process = input(

            "\nProcess To Kill: "

        ).strip()

        if process not in self.processes:

            print("\nProcess Not Found.")

            return

        parent = self.processes[

            process

        ][

            "parent"

        ]

        if parent is not None:

            if process in self.processes[

                parent

            ][

                "children"

            ]:

                self.processes[

                    parent

                ][

                    "children"

                ].remove(process)

        self.delete_recursive(

            process

        )

        self.save()

        print("\nProcess Terminated.")

    def delete_recursive(

        self,

        process

    ):

        for child in list(

            self.processes[

                process

            ][

                "children"

            ]

        ):

            self.delete_recursive(

                child

            )

        del self.processes[

            process

        ]
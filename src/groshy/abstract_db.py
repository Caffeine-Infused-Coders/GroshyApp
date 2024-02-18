import json
from pathlib import Path
from abc import ABC, abstractmethod


class AbstractDB(ABC):
    
    cwd = Path.cwd()
    db_root = Path.joinpath(cwd, ".dbs")
    
    def __init__(self, db_name: str, db_type: str, new: bool=False):
        self.name = db_name
        self.type = db_type
        self.dir = Path.joinpath(AbstractDB.db_root, self.type)
        self.path = Path.joinpath(self.dir, f"{self.name}.json")
        self._data = {}

        if new:
            if not AbstractDB.db_root.exists():
                Path.mkdir(AbstractDB.db_root)
                Path.mkdir(self.dir)
            elif AbstractDB.db_root.exists() and not self.dir.exists():
                Path.mkdir(self.dir)

            if self.build_db():  # Build new database
                print(f"{self.name} ready for use")
            else:
                print(f"{self.name} could not be built")
                self.db_remove()               
        else:
            res = self.db_read()

            if not res:
                print(f"Could not access {self.name}.\n\nPlease reboot the program")
                exit()

    def build_db(self) -> bool:

        msg = {}  # Message to print in new database file
        success = False  # Default return value for this method

        try:
            with open(self.path, "x") as db:  # Create database json file and dump message
                json.dump(msg, db, indent=4)
                
            print(f"{self.name} created successfully")
            success = True  # Signal creation of db
        except FileExistsError:
            print(f"A {self.type} named {self.name} already exists in location {self.dir}...")

            ans_flg = False
            attempts = 3
            while not ans_flg and attempts > 0:
                resp = input("Would you like to choose a different name? (y/n): ")

                match resp:
                    case "yes" | "y":
                        ans_flg = True
                        self.name = input("Enter new name: ")
                        self.path = Path.joinpath(self.dir, f"{self.name}.json")
                        success = self.build_db()
                    case "no" | "n":
                        ans_flg = True
                        print(f"{self.type} creation aborted")
                    case _:
                        print("Unexpected input, please try again.")
                        attempts -= 1
                        continue

        return success


    def db_add(self, msg: list[dict]):

        success = False

        for mess in msg:
            self._data.update(mess)  # Process the msg list by appending to self.data

        try:
            with open(self.path, "w") as db:
                json.dump(self._data, db)
                db.write("\n")
            success = True
        except FileNotFoundError:
            print(f"No database file found. Double check this location: {self.path}")
            pass

        return success


    def db_read(self) -> bool:
        success = False
        try:
            with open(self.path, "r") as db:
                self._data = json.load(db)
        except FileNotFoundError:
            print(f"No database file found. Double check this location: {self.path}")  # TODO: make this a logging statement  # noqa: E501
            pass

        return success


    def db_remove(self):
        """ Delete db from db repository. """
        success = False
        print(f"Removing {self.name} from {self.dir}")
        Path.unlink(self.path)
        if not self.path.exists():
            success = True
            print(f"{self.name} removed...")

        return success
    

    @classmethod
    @abstractmethod
    def fetch_dbs(cls) -> list[str]:
        pass



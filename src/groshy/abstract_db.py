"""Defines the Abstract DB Class which acts as parent class to Groshy's DB objects
(i.e. Pantry, Cookbook)."""

import json
from pathlib import Path
from abc import ABC, abstractmethod


class AbstractDB(ABC):

    cwd = Path(__file__).parent
    db_root = Path.joinpath(cwd, ".dbs")

    def __init__(self, db_name: str, db_type: str):
        """Abstract Base Class for app DB types. This handles atomic data manipulation
        functions such as reading and writing to files

        Args:
            :param db_name str Name of db to be created or opened
            :param db_type str Type specifier of db
        """

        self.name = db_name.replace(" ", "_")
        self.db_type = db_type
        self.dir = Path.joinpath(AbstractDB.db_root, self.db_type)
        self.path = Path.joinpath(self.dir, f"{self.name}.json")
        self._data = []  # Representation of data in the database

        try:
            res = self.db_read()

            if not res:
                print(
                    f"Could not access {AbstractDB.get_display_name(self.name)} (as {self.name})."
                    "\n\nPlease reboot the program"
                )
                exit()  # TODO: Implement DB_ACCESS_ERROR Exception

        except FileNotFoundError:
            if not AbstractDB.db_root.exists():
                Path.mkdir(AbstractDB.db_root)
                Path.mkdir(self.dir)
            elif AbstractDB.db_root.exists() and not self.dir.exists():
                Path.mkdir(self.dir)

            if self.build_db():  # Build new database
                print(f"{db_name} ready for use (as {self.name})")
            else:
                print(f"{db_name} could not be built (as {self.name})")
                self.db_remove()
                exit()  # TODO: Implement DB_BUILD_ERROR Exception

    def build_db(self) -> bool:
        """Creates new DB file and dumps and initial empty json list object into
        the file so that future reads do not throw an exception. Returns build status"""

        msg = []  # Message to print in new database file
        success = False  # Default return value for this method

        try:
            with open(
                self.path, "x"
            ) as db:  # Create database json file and dump message
                json.dump(msg, db, indent=4)

            print(f"{self.name} created successfully")
            success = True  # Signal creation of db

        except FileExistsError:
            print(
                f"A {self.db_type} named {self.name} already exists in location "
                f"{self.dir}..."
            )

            ans_flg = False
            attempts = 3
            while not ans_flg and attempts > 0:
                resp = input("Would you like to choose a different name? (y/n): ")

                match resp:
                    case "yes" | "y":
                        ans_flg = True
                        self.name = input("Enter new name: ")
                        self.path = Path.joinpath(
                            self.dir, f"{self.name.replace(' ', '_')}.json"
                        )
                        success = self.build_db()
                    case "no" | "n":
                        ans_flg = True
                        print(f"{self.db_type} creation aborted")
                    case _:
                        print("Unexpected input, please try again.")
                        attempts -= 1
                        continue

        return success

    def db_add(self, msg: list[dict]):
        """Add an entry, or multiple, to the db instance. Both runtime and saved to disk"""
        success = False

        self._data += msg  # Update runtime representation of db data

        try:
            with open(
                self.path, "w"
            ) as db:  # Open with 'w' permissions as all the data is re-dumped to db
                json.dump(self._data, db, indent=4, default=str)
                db.write("\n")  # Add new line to end of db file
                success = True
        except FileNotFoundError:
            print(f"No database file found. Double check this location: {self.path}")

        return success

    def db_read(self) -> bool:
        """Read information on disk into runtime"""
        success = False
        try:
            with open(self.path, "r") as db:
                self._data = json.load(db)
            success = True
        except FileNotFoundError:
            print(
                f"No database file found. Double check this location: {self.path}"
            )  # TODO: make this a logging statement  # noqa: E501
            pass

        return success

    def db_remove(self):
        """Delete db from db repository."""
        success = False
        print(f"Removing {self.name} from {self.dir}")
        Path.unlink(self.path)
        if not self.path.exists():
            success = True
            print(f"{self.name} removed...")

        return success

    @staticmethod
    def get_display_name(db: str):
        """Returns the db name with the underscores replaced by spaces"""
        return db.replace("_", " ")

    @staticmethod
    def get_db_name(display_name: str):
        """Returns the db name as saved in the system"""
        return display_name.replace(" ", "_")

    @classmethod
    @abstractmethod
    def fetch_dbs(cls) -> list[str]:
        pass

import os
from pathlib import Path

cwd = Path(__file__).parent
kivy_home = Path(cwd, ".internal")
os.environ["KIVY_HOME"] = str(kivy_home)

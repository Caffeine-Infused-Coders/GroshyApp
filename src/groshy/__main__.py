import logging
import logging.config
import tomllib
from pathlib import Path
from datetime import date

from kivy.app import App
from kivy.logger import Logger
from kivy.lang.builder import Builder

from groshy import gui


def setup_logging(fp: Path):
    """Creates logging config through logging.config.dictConfig from log_conf.toml
    file.

    Args:
        :param fp (Path) Path object describing absolute path to log_conf.toml
    """

    record_archive = Path(fp.parent, ".logs")
    record_name = f"{date.today()}_Groshy.log"

    with open(fp, "rb") as f:
        config = tomllib.load(f)

    if not record_archive.is_dir():
        record_archive.mkdir()
    elif not Path(record_archive, record_name).exists():
        config["handlers"]["default"]["mode"] = "w"

    config["handlers"]["default"]["filename"] = Path(record_archive, record_name)
    logging.config.dictConfig(config)


class GroshyApp(App):
    def __init__(self):
        super().__init__()
        self.screen_manager = gui.Controller()

    def build(self):

        sm = self.screen_manager

        sm.add_widget(gui.SplashScreen(name="splash"))
        # sm.add_widget(BookShelfScreen(name='bookshelf_screen'))
        Logger.info("Starting the ScreenManager")

        return sm


temp_dir = Path(__file__).parent
gui_dir = Path(temp_dir, "gui")

# setup_logging(Path(temp_dir, 'log_conf.toml'))

Logger.debug("Logger Created!")

## Load Utility Gui Files
Builder.load_file(str(Path(gui_dir, "utils.kv")))

## Load Screen Gui Files
Builder.load_file(str(Path(gui_dir, "splash_screen.kv")))
Builder.load_file(str(Path(gui_dir, "bookshelf_screen.kv")))
Builder.load_file(str(Path(gui_dir, "cookbook_toc_screen.kv")))

## Load Form Gui Files
Builder.load_file(str(Path(gui_dir, "cookbook_form.kv")))
Builder.load_file(str(Path(gui_dir, "recipe_form.kv")))
Builder.load_file(str(Path(gui_dir, "recipe_form_utils.kv")))

Logger.info("All KV files successfully loaded, starting GroshyApp")

GroshyApp().run()

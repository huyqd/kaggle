import zipfile
from time import sleep
import configparser
import os
from pathlib import Path
from datetime import datetime

root_path = Path(__file__).parent


def setup_api_locally():
    parser = configparser.ConfigParser()
    parser.read(root_path / 'KAGGLE_CONFIG.ini')
    os.environ["KAGGLE_USERNAME"] = parser["KAGGLE_API"]["KAGGLE_USERNAME"]
    os.environ["KAGGLE_KEY"] = parser["KAGGLE_API"]["KAGGLE_KEY"]


def load(competition):
    folder = root_path / "data/{}".format(competition)
    if not folder.is_dir():
        folder.mkdir()
    os.system("kaggle competitions download -c {} -p {}".format(competition, str(folder)))

    # Upzip download
    fname = folder / f"{competition}.zip"
    while not fname.exists():
        print("Waiting for file to be downloaded...")
        sleep(5)

    print("Extracting file...")
    with zipfile.ZipFile(fname, 'r') as zip_ref:
        zip_ref.extractall(folder)

    print("Removing zip file...")
    os.remove(fname)

    print("Finished!")

    return



setup_api_locally()
load('google-quest-challenge')

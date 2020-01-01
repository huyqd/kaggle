import os
import configparser


def setup_api_locally():
    parser = configparser.ConfigParser()
    parser.read('KAGGLE_CONFIG.ini')
    os.environ["KAGGLE_USERNAME"] = parser["KAGGLE_API"]["KAGGLE_USERNAME"]
    os.environ["KAGGLE_KEY"] = parser["KAGGLE_API"]["KAGGLE_KEY"]


def load(competition):
    folder = os.getcwd()+"/data/{}".format(competition)
    if not os.path.isdir(folder):
        os.mkdir(folder)
    os.system("kaggle competitions download {} -p {} --force".format(competition, folder))


setup_api_locally()
load('google-quest-challenge')

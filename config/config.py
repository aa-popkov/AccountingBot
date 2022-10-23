import configparser
from pathlib import Path


config = configparser.ConfigParser()
path_to_config = str(Path(__file__).resolve().parent / 'config.ini')
config.read(path_to_config)

TG_API_KEY = config.get('telegram', 'api_key')
TG_ADMIN_ID = config.get('telegram', 'admin_id')



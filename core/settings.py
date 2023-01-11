import os
from pathlib import Path
from typing import List

from dotenv import load_dotenv


load_dotenv()

# Dir...
ROOT_DIR = os.path.dirname(Path(__file__).parents[0])


# WebDriver...
WEB_DRIVER_WAIT_TIMEOUT: int = int(os.getenv('WEB_DRIVER_WAIT_TIMEOUT', default=15))

# Browser...
INCLUDE_BROWSERS: List[str] = os.getenv('INCLUDE_BROWSERS', default='chrome').split(', ')

CHROME_VERSION: str = os.getenv('CHROME_VERSION', default='latest')
FIREFOX_VERSION: str = os.getenv('FIREFOX_VERSION', default='latest')


# URL...
BASE_URL: str = os.getenv('BASE_URL', default='http://uitestingplayground.com')

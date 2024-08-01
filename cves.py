import requests
from bs4 import BeautifulSoup
from telegram import Bot
import schedule
import time
import logging
from datetime import datetime
import os
import json


logging.basicConfig(filename='newest-cves.log',
                    level=logging.INFO,
                    format='%(asctime)s - %(levelname)s - %(message)s')

TELEGRAM_TOKEN = ''
CHAT_ID = ''



def fetch_cves_tenable():



def main():
    print('main')

if __name__ == "__main__":
    main()

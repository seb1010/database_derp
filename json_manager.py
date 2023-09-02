import os
from tinydb import TinyDB, Query

load_dotenv()

class AddPoint:


    def __init__(self):
        self.filename = "local_boi.json"
        self.db = TinyDB(filename)
        

    def add_item(item: dict)

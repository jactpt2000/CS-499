#Programmer: Jorge Argueta
#Date: 3/31/2024
#Version: 1.0



# HashTable Project with AVL Tree Collision Resolution
# This Python script demonstrates the use of hash tables for efficient data storage and retrieval.
# It includes functionality to dynamically resize the hash table to maintain performance
# and uses AVL Trees for collision resolution, showcasing an advanced approach to handling hash collisions.
# The project is an enhancement from an original C++ implementation, aiming to leverage Python's dynamic features
# and built-in data structures, like dictionaries, to simulate hash table behavior.

import csv
from bintrees import AVLTree

class Bid:
    """Represents a single bid in the auction system."""
    def __init__(self, bidId="", title="", fund="", amount=0.0):
        # Initialize a new bid with optional attributes: ID, title, funding source, and bid amount.
        self.bidId = bidId
        self.title = title
        self.fund = fund
        self.amount = amount

class HashTable:
    """Implements a hash table using AVL Trees for collision resolution."""
    def __init__(self, initial_size=101):
        # Initialize the hash table with a prime initial size for better distribution.
        # AVL Trees are used for each bucket to handle collisions efficiently.
        self.table = [None] * initial_size
        self.item_count = 0
        self.load_factor_threshold = 0.75  # Determines when to resize the hash table to maintain performance.

    def hash(self, key):
        # Simple hash function: modulo operation on the key with the table size.
        return key % len(self.table)

    def resize_if_needed(self):
        # Check if the current load factor exceeds the threshold and resize the table if necessary.
        load_factor = self.item_count / len(self.table)
        if load_factor > self.load_factor_threshold:
            self.resize()

    def resize(self):
        # Double the size of the hash table and rehash all existing entries.
        old_table = self.table
        new_size = len(self.table) * 2
        self.table = [None] * new_size
        self.item_count = 0
        for bucket in old_table:
            if bucket is not None:
                for bidId, bid in bucket.items():
                    self.insert(bid)

    def insert(self, bid):
        # Insert a bid into the hash table. If a collision occurs, it is handled by the AVL Tree.
        key = self.hash(int(bid.bidId))
        if self.table[key] is None:
            self.table[key] = AVLTree()
        self.table[key].insert(bid.bidId, bid)
        self.item_count += 1
        self.resize_if_needed()

    def search(self, bidId):
        # Search for a bid by ID. Returns the bid if found, None otherwise.
        key = self.hash(int(bidId))
        if self.table[key] is not None and bidId in self.table[key]:
            return self.table[key].get(bidId)
        return None

    def remove(self, bidId):
        # Remove a bid from the hash table by ID.
        key = self.hash(int(bidId))
        if self.table[key] is not None and bidId in self.table[key]:
            del self.table[key][bidId]
            self.item_count -= 1

    def print_all(self):
        # Print all bids stored in the hash table.
        for bucket in self.table:
            if bucket is not None:
                for bidId, bid in bucket.items():
                    print(f"|{bid.bidId}|{bid.title}|{bid.amount}|{bid.fund}")

def str_to_double(str_val):
    # Convert a string value to a float. Used for converting bid amounts from strings to numbers.
    try:
        return float(str_val.replace('$', '').replace(',', ''))
    except ValueError as ve:
        print(f"Value conversion error: {ve}")
        return 0.0

def load_bids(csv_path, hash_table):
    # Load bids from a CSV file and insert them into the hash table.
    try:
        print(f"Loading CSV file {csv_path}")
        with open(csv_path, 'r', newline='', encoding='utf-8-sig') as file:
            csv_dict_reader = csv.DictReader(file)
            for row in csv_dict_reader:
                bidId = row['ArticleID'].strip()
                title = row['ArticleTitle'].strip()
                fund = row['Fund'].strip()
                amount = str_to_double(row['WinningBid '].strip())
                bid = Bid(bidId=bidId, title=title, fund=fund, amount=amount)
                hash_table.insert(bid)
    except Exception as e:
        print(f"Failed to load CSV file: {e}")

def main():
    # Entry point for the script. Loads bids from the CSV and prints them.
    print("Script started")
    csv_path = "eBid_Monthly_Sales_Dec_2016.csv"
    bid_table = HashTable()

    load_bids(csv_path, bid_table)
    bid_table.print_all()
       
    input("Press Enter to exit")

if __name__ == "__main__":
    main()

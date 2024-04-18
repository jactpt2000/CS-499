//============================================================================
// Name        : HashTable.cpp
// Author      : Jorge Argueta
// Date		   : March 31, 2024
// Version     : 1.0
//============================================================================

// Include necessary libraries for functionality such as I/O, string manipulation, and file parsing.
#include <algorithm>
#include <climits>
#include <iostream>
#include <string> 
#include <time.h>
#include <vector>
#include <list>
#include "CSVparser.hpp"

using namespace std;

// Define a constant for the default size of the hash table.
const unsigned int DEFAULT_SIZE = 179;

// Utility function forward declaration.
double strToDouble(string str, char ch);

// Struct to hold bid information, including an ID, title, fund, and amount.
struct Bid {
    string bidId; // Unique identifier
    string title;
    string fund;
    double amount;
    Bid() : amount(0.0) {}
};

// Hash Table class definition for managing bids.
class HashTable {
private:
    // Define the primary storage structure for bids - a vector of bid lists (chaining).
    vector<list<Bid>> bids;

    // Private method to calculate hash values.
    unsigned int hash(int key);

public:
    HashTable(); // Constructor
    virtual ~HashTable(); // Destructor
    void Insert(Bid bid); // Insert a bid into the table.
    void PrintAll(); // Print all bids in the table.
    void Remove(string bidId); // Remove a bid by ID.
    Bid Search(string bidId); // Search for a bid by ID.
};

HashTable::HashTable() {
    bids.resize(17939); // Initialize the vector with a specified size. Choice of size affects performance and collision rate.
}

HashTable::~HashTable() {
    bids.clear(); // Clears the vector, freeing memory.
}

unsigned int HashTable::hash(int key) {
    int hashVal = 25; // Simple hash function. This should be improved for a better distribution.
    return key % hashVal;
}

void HashTable::Insert(Bid bid) {
    int id = stoi(bid.bidId); // Convert bid ID to integer for hashing.
    int key = hash(id);
    bids[key].push_back(bid); // Insert bid into the appropriate list based on the hash key.
}

void HashTable::PrintAll() {
    for (int i = 0; i < bids.size(); ++i) {
        for (auto& j : bids[i])
            cout << "Key" << i << ":|" << j.bidId << "|" << j.title << "|" << j.amount << "|" << j.fund << endl;
    }
}

void HashTable::Remove(string bidId) {
    int id = stoi(bidId);
    int key = hash(id);
    auto& list = bids[key];
    list.remove_if([bidId](const Bid& b) { return b.bidId == bidId; }); // Use remove_if with a lambda to remove the bid.
}

Bid HashTable::Search(string bidId) {
    Bid bid;
    int id = stoi(bidId);
    int key = hash(id);
    for (auto& b : bids[key]) {
        if (b.bidId == bidId) return b;
    }
    return bid; // Returns an empty Bid struct if not found.
}

// Utility functions and main program logic follow...

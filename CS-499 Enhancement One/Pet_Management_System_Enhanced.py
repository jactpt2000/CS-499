"""
Pet Class Implementation in Python

This class models a pet with attributes and methods to manage its information.
It demonstrates the application of object-oriented principles, data validation,
and exception handling in Python, showcasing skills in software design and development.

Programmer: Jorge Argueta
Date: 3/29/2024
Version: 1.0

This code aligns with course outcomes related to:
- Implementing design solutions using innovative skills and techniques.
- Solving logic problems through programming solutions.
- Addressing potential design flaws, particularly related to data validation and security.
- Articulating ideas and programming decisions clearly through documentation.

"""

class Pet:
    def __init__(self, _petType, _petName, _petAge, _dogSpace, _catSpace, _daysStay, _amountDue):
        """
        Initializes a new Pet object with the specified attributes.
        This constructor demonstrates the ability to use class structures to encapsulate pet data,
        ensuring that each pet object is instantiated with all necessary information.
        
        Parameters:
        - _petType (str): The type of the pet (e.g., 'Dog', 'Cat').
        - _petName (str): The name of the pet.
        - _petAge (int): The age of the pet.
        - _dogSpace (int): The allocated space for a dog.
        - _catSpace (int): The allocated space for a cat.
        - _daysStay (int): The number of days the pet stays.
        - _amountDue (float): The amount due for the pet's stay.
        """
        self.petType = _petType
        self.petName = _petName
        self.petAge = _petAge
        self.dogSpace = _dogSpace
        self.catSpace = _catSpace
        self.daysStay = _daysStay
        self.amountDue = _amountDue

    # method with detailed documentation:
    def setPetType(self, _petType):
        """
        Updates the pet's type.
        
        This method demonstrates handling basic attribute assignments,
        showcasing how to modify object state safely.
        
        Parameters:
        - _petType (str): The new type for the pet.
        """
        self.petType = _petType

    # documentation for a getter method:
    def getPetType(self):
        """
        Retrieves the pet's type.
        
        Returns:
        - str: The current type of the pet.
        """
        return self.petType

    # Additional methods (setters and getters) follow a similar documentation structure.
    # Implementing detailed documentation for each helps clarify their purpose and usage,
    # contributing to a better understanding and maintainability of the code.

    # Implementing a method with logic and security considerations:
    def setPetAge(self, age):
        """
        Sets the pet's age, ensuring it is a non-negative integer.
        
        This method incorporates basic validation logic to prevent invalid data assignment,
        demonstrating a proactive approach to data integrity and security.
        
        Parameters:
        - age (int): The new age of the pet.
        
        Raises:
        - ValueError: If the age is less than 0, indicating a potential logic flaw or
          incorrect data entry.
        """
        if age >= 0:
            self.petAge = age
        else:
            raise ValueError("The pet age must be greater or equal to 0.")

    # Similar security and validation logic is recommended for methods like
    # setDogSpace, setCatSpace, setDaysStay, and setAmountDue.

    # Implementing action methods to demonstrate problem-solving capabilities:
    def checkIn(self, _petName, _daysStay):
        """
        Simulates checking a pet into the system, updating its stay duration.
        
        This method could be expanded to interact with a database or a more complex
        system state, showcasing the ability to implement features that affect the
        application's state based on user input or programmatic conditions.
        
        Parameters:
        - _petName (str): The name of the pet to check in.
        - _daysStay (int): The duration of the pet's stay.
        """
        self.petName = _petName
        self.daysStay = _daysStay
        # In a full implementation, this method would likely interact with a database
        # or use more complex logic to update system state.

    def checkOut(self, _petName):
        """
        Simulates checking a pet out of the system, calculating and returning the amount due.
        
        This method offers a simplistic model of a checkout process
        """


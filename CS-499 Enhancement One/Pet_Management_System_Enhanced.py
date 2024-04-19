# Pet Management System
# Programmer: Jorge Argueta
# Professor: Goggins
# Class: CS 499
# Date: April 10, 2024
#
# This program is designed to manage pet stays at a pet care facility. It allows the user
# to input pet details, determine the duration of stay, apply variable pricing based on pet
# type and season, and offer discounts and charges for long stays and special care needs.
# Additionally, it can apply coupon codes for discounts at checkout.

class Pet:
    """
    Class to manage details and charges for a pet's stay at a pet care facility.

    Attributes:
        pet_type (str): Type of the pet (e.g., 'dog', 'cat').
        pet_name (str): Name of the pet.
        pet_age (int): Age of the pet.
        special_care (bool): Indicates if special care is needed (default False).
        days_stay (int): Duration of the pet's stay in days.
        amount_due (float): Total charges due for the stay.
    """
    def __init__(self, pet_type, pet_name, pet_age, special_care=False):
        """
        Initializes a new Pet instance with given attributes.
        
        Args:
            pet_type (str): The type of the pet.
            pet_name (str): The pet's name.
            pet_age (int): The pet's age.
            special_care (bool): If the pet requires special care (default is False).
        """
        self.pet_type = pet_type
        self.pet_name = pet_name
        self.pet_age = pet_age
        self.special_care = special_care
        self.days_stay = 0
        self.amount_due = 0
    
    def inputStayDetails(self):
        """
        Prompts user to enter the number of days the pet will stay and if special care is needed.
        Uses exception handling to ensure valid input.
        """
        try:
            self.days_stay = int(input("Enter the number of days the pet will stay: "))
            self.special_care = input("Does this pet require special care (yes/no)? ").lower() == 'yes'
            self.applyPeakRates()
        except ValueError:
            print("Invalid input. Please enter a valid number of days.")
            return False
        return True

    def applyPeakRates(self):
        """
        Determines if the current date falls into peak rates months (June, July, August).
        Sets the attribute is_peak_time based on the current month.
        """
        import datetime
        today = datetime.date.today()
        peak_months = (6, 7, 8)  # Summer months considered as peak
        self.is_peak_time = today.month in peak_months

    def calculateBaseRate(self):
        """
        Calculates base rate depending on the pet type and whether it's peak time.
        Different rates are applied for dogs, cats, and other pets.
        """
        if self.pet_type.lower() == 'dog':
            return 25 if self.is_peak_time else 20
        elif self.pet_type.lower() == 'cat':
            return 20 if self.is_peak_time else 15
        else:
            return 15 if self.is_peak_time else 10

    def applyDiscounts(self):
        """
        Applies a discount for stays longer than 10 days.
        Returns a discount factor.
        """
        return 0.9 if self.days_stay > 10 else 1  # 10% discount

    def applySpecialCareCharge(self):
        """
        Adds a daily charge for special care needs.
        Returns the additional charge per day.
        """
        return 5 if self.special_care else 0  # $5 per day for special care

    def applyCoupon(self, coupon_code):
        """
        Applies a discount based on the provided coupon code.
        Supports multiple coupon codes with predefined discount values.
        
        Args:
            coupon_code (str): The coupon code entered by the user.

        Returns:
            float: The dollar value of the coupon discount.
        """
        coupons = {'SAVE10': 10, 'WELCOME5': 5}  # Example coupon codes with their discount values
        return coupons.get(coupon_code, 0)

    def checkOut(self, coupon_code=""):
        """
        Calculates and prints the final amount due at checkout, applying all charges and discounts.
        Incorporates base rates, special care charges, long stay discounts, and coupon discounts.

        Args:
            coupon_code (str): Optional coupon code for additional discounts.
        """
        base_rate = self.calculateBaseRate()
        discount_factor = self.applyDiscounts()
        special_care_charge = self.applySpecialCareCharge()
        coupon_discount = self.applyCoupon(coupon_code)

        self.amount_due = ((base_rate + special_care_charge) * self.days_stay) * discount_factor
        self.amount_due -= coupon_discount  # Apply coupon discount last as a flat rate
        
        print(f"{self.pet_name} will be charged ${self.amount_due:.2f} for {self.days_stay} days stay. Special care: {'Yes' if self.special_care else 'No'}")

# Main program interaction
if __name__ == "__main__":
    print("Welcome to the Pet Management System")
    pet_type = input("Enter the type of the pet (Dog/Cat): ")
    pet_name = input("Enter the name of the pet: ")
    pet_age = int(input("Enter the age of the pet: "))
    pet_special_care = input("Does this pet require special care (yes/no)? ").lower() == 'yes'
    
    my_pet = Pet(pet_type, pet_name, pet_age, pet_special_care)
    if my_pet.inputStayDetails():
        coupon_code = input("Enter a coupon code if you have one: ")
        my_pet.checkOut(coupon_code)

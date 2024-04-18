/**
 * Pet Class
 * This class models a pet, providing functionality to set and get pet details, 
 * check a pet in and out, and manage pet space.
 * 
 * Programmer: Jorge Argueta
 * Date: 3/29/2024
 * Version: 1.0
 * 
 */

public class Pet {
    private String petType;
    private String petName;
    private int petAge;
    private int dogSpace;
    private int catSpace;
    private int daysStay;
    private double amountDue;
    
    // Constructor
    public Pet(String _petType, String _petName, int _petAge, int _dogSpace, int _catSpace, int _daysStay, double _amountDue) {
        this.petType = _petType;
        this.petName = _petName;
        this.petAge = _petAge;
        this.dogSpace = _dogSpace;
        this.catSpace = _catSpace;
        this.daysStay = _daysStay;
        this.amountDue = _amountDue;
    }
    
    // Sets the pet type
    public void setPetType(String _petType) {
        this.petType = _petType;
    }
    
    // Returns the pet type
    public String getPetType() {
        return this.petType;
    }
    
    // Sets the pet name
    public void setPetName(String _petName) {
        this.petName = _petName;
    }
    
    // Returns the pet name
    public String getPetName() {
        return this.petName;
    }
    
    // Sets the pet's age, ensuring it is non-negative
    public void setPetAge(int age) {
        if(age >= 0) {
            this.petAge = age;
        } else {
            throw new ArithmeticException("The pet age must be greater or equal to 0.");
        }
    }
    
    // Returns the pet's age
    public int getPetAge() {
        return this.petAge;
    }
    
    // Sets the space available for dogs
    protected void setDogSpace(int _dogSpace) {
        if(_dogSpace >= 0) {
            this.dogSpace = _dogSpace;
        } else {
            throw new ArithmeticException("The dog space must be greater or equal to 0.");
        }
    }
    
    // Returns the space available for dogs
    protected int getDogSpace() {
        return this.dogSpace;
    }
    
    // Sets the space available for cats
    protected void setCatSpace(int _catSpace) {
        if(_catSpace >= 0) {
            this.catSpace = _catSpace;
        } else {
            throw new ArithmeticException("The cat space must be greater or equal to 0.");
        }
    }
    
    // Returns the space available for cats
    protected int getCatSpace() {
        return this.catSpace;
    }
    
    // Sets the number of days a pet stays
    public void setDaysStay(int _daysStay) {
        if(_daysStay >= 0) {
            this.daysStay = _daysStay;
        } else {
            throw new ArithmeticException("The days stay must be greater or equal to 0.");
        }
    }
    
    // Returns the number of days a pet stays
    public int getDaysStay() {
        return this.daysStay;
    }
    
    // Sets the amount due for the pet's stay
    public void setAmountDue(double _amountDue) {
        if(_amountDue >= 0) {
            this.amountDue = _amountDue;
        } else {
            throw new ArithmeticException("The amount due must be greater or equal to 0.");
        }
    }
    
    // Returns the amount due for the pet's stay
    public double getAmountDue() {
        return this.amountDue;
    }
    
    // Placeholder for checkIn method
    public void checkIn(String _petName, int _daysStay) {
        // Code to check a pet into the system
    }
    
    // Placeholder for checkOut method
    public double checkOut(String _petName) {
        // Code to check a pet out of the system and calculate the amount due
        return 0.0;
    }
    
    // Placeholder for getPet method
    public Pet getPet(String _petName

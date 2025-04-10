"""
Finance-related models for financial and health calculations.
Contains classes for Stock, Loan, and BMI calculations.
"""


class Stock:
    """Stock representing a financial market security."""
    
    def __init__(self, symbol, name):
        """
        Initialize a new Stock.
        
        Args:
            symbol (str): Stock ticker symbol
            name (str): Company name
        """
        self._symbol = symbol
        self._name = name
        self._previousClosingPrice = 0.0
        self._currentPrice = 0.0
    
    def getSymbol(self):
        """Get stock symbol."""
        return self._symbol
    
    def getName(self):
        """Get company name."""
        return self._name
    
    def setPreviousClosingPrice(self, price):
        """Set previous closing price."""
        self._previousClosingPrice = price
    
    def setCurrentPrice(self, price):
        """Set current price."""
        self._currentPrice = price
    
    def getChangePercent(self):
        """
        Calculate percent change in stock price.
        
        Returns:
            str: Formatted percentage change with % symbol
        """
        change = ((self._currentPrice - self._previousClosingPrice) / 
                 self._previousClosingPrice) * 100
        return f"{round(change, 3)} %"
    
    def __str__(self):
        """String representation of a Stock."""
        return (f"Stock: {self._name} ({self._symbol}) - "
                f"Current: {self._currentPrice}, "
                f"Previous: {self._previousClosingPrice}")


class Loan:
    """Loan with interest rate and payment calculations."""
    
    def __init__(self, annualInterestRate=2.5, numberOfYears=1, 
                 loanAmount=1000, borrower=""):
        """
        Initialize a new Loan.
        
        Args:
            annualInterestRate (float): Annual interest rate in percent
            numberOfYears (int): Duration of loan in years
            loanAmount (float): Principal amount of the loan
            borrower (str): Name of the borrower
        """
        self._annualInterestRate = annualInterestRate
        self._numberOfYears = numberOfYears
        self._loanAmount = loanAmount
        self._borrower = borrower
    
    def getAnnualInterestRate(self):
        """Get annual interest rate."""
        return self._annualInterestRate
    
    def getNumberOfYears(self):
        """Get loan duration in years."""
        return self._numberOfYears
    
    def getLoanAmount(self):
        """Get loan principal amount."""
        return self._loanAmount
    
    def getBorrower(self):
        """Get borrower name."""
        return self._borrower
    
    def getMonthlyPayment(self):
        """
        Calculate monthly payment.
        
        Returns:
            float: Monthly payment amount
        """
        principal_portion = self._loanAmount / self._numberOfYears
        interest_portion = (self._annualInterestRate * self._loanAmount) / 100
        return (principal_portion + interest_portion) / 12
    
    def getTotalPayment(self):
        """
        Calculate total payment over the life of the loan.
        
        Returns:
            float: Total payment amount
        """
        interest_total = self._numberOfYears * ((self._annualInterestRate * self._loanAmount) / 100)
        return self._loanAmount + interest_total
    
    def __str__(self):
        """String representation of a Loan."""
        return (f"Loan: Amount=${self._loanAmount}, "
                f"Interest={self._annualInterestRate}%, "
                f"Duration={self._numberOfYears} years, "
                f"Borrower={self._borrower}")


class Bmi:
    """Body Mass Index calculator for health assessments."""
    
    def __init__(self, name, age, weight, height):
        """
        Initialize a new BMI calculator.
        
        Args:
            name (str): Person's name
            age (int): Person's age
            weight (float): Weight in kilograms
            height (float): Height in centimeters
        """
        self._name = name
        self._age = age
        self._weight = weight
        self._height = height
    
    def getName(self):
        """Get person's name."""
        return self._name
    
    def getAge(self):
        """Get person's age."""
        return self._age
    
    def getWeight(self):
        """Get weight in kg."""
        return self._weight
    
    def getHeight(self):
        """Get height in cm."""
        return self._height
    
    def getBmi(self):
        """
        Calculate BMI.
        
        Returns:
            float: Body Mass Index value
        """
        height_in_meters = self._height / 100
        return self._weight / (height_in_meters ** 2)
    
    def getStatus(self):
        """
        Get BMI category status.
        
        Returns:
            str: BMI category (Underweight, Normal weight, Overweight, Obesity)
        """
        bmi = self.getBmi()
        if bmi < 18.5:
            return "Underweight"
        elif bmi < 25:
            return "Normal weight"
        elif bmi < 30:
            return "Overweight"
        else:
            return "Obesity"
    
    def __str__(self):
        """String representation of BMI calculation."""
        return (f"BMI for {self._name} (age {self._age}): "
                f"{round(self.getBmi(), 2)} - {self.getStatus()}")


# Example usage
def demo():
    """Demonstrate the usage of the finance models."""
    # Stock example
    apple = Stock("AAPL", "Apple Inc.")
    apple.setPreviousClosingPrice(150.0)
    apple.setCurrentPrice(155.25)
    print(apple)
    print(f"Change: {apple.getChangePercent()}")
    
    print("\n" + "-" * 40 + "\n")
    
    # Loan example
    loan = Loan(4.5, 5, 10000, "John Doe")
    print(loan)
    print(f"Monthly Payment: ${loan.getMonthlyPayment():.2f}")
    print(f"Total Payment: ${loan.getTotalPayment():.2f}")
    
    print("\n" + "-" * 40 + "\n")
    
    # BMI example
    person = Bmi("Jane Smith", 30, 70, 170)
    print(person)


if __name__ == "__main__":
    demo()
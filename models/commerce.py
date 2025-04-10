"""
Business operations module for client and invoice management.
Contains classes for Address, Prospect, Client, Invoice, and Product.
"""


class Address:
    """Physical address with street, city, zip code, and country."""
    
    def __init__(self, street, city, zip_code, country):
        """
        Initialize a new Address.
        
        Args:
            street (str): Street address
            city (str): City name
            zip_code (int or str): Postal or zip code
            country (str): Country name
        """
        self._street = street
        self._city = city
        self._zip_code = zip_code
        self._country = country
    
    def getStreet(self):
        """Get street address."""
        return self._street
    
    def getCity(self):
        """Get city name."""
        return self._city
    
    def getZipCode(self):
        """Get zip code."""
        return self._zip_code
    
    def getCountry(self):
        """Get country name."""
        return self._country
    
    def __str__(self):
        """String representation of an Address."""
        return (f"Address: {self._street}, {self._city}, "
                f"{self._zip_code}, {self._country}")


class Prospect:
    """Potential customer with contact information."""
    
    def __init__(self, first_name, last_name, email, address):
        """
        Initialize a new Prospect.
        
        Args:
            first_name (str): Person's first name
            last_name (str): Person's last name
            email (str): Email address
            address (Address): Physical address
        """
        self._first_name = first_name
        self._last_name = last_name
        self._email = email
        self._address = address
    
    def getFirstName(self):
        """Get first name."""
        return self._first_name
    
    def getLastName(self):
        """Get last name."""
        return self._last_name
    
    def getFullName(self):
        """Get full name."""
        return f"{self._first_name} {self._last_name}"
    
    def getEmail(self):
        """Get email address."""
        return self._email
    
    def setEmail(self, email):
        """Set email address."""
        self._email = email
    
    def getAddress(self):
        """Get address."""
        return self._address
    
    def setAddress(self, address):
        """Set address."""
        self._address = address
    
    def __str__(self):
        """String representation of a Prospect."""
        return (f"Prospect: {self.getFullName()}, "
                f"Email: {self._email}, Address: {self._address}")


class Client(Prospect):
    """Confirmed customer with a client code and invoices."""
    
    def __init__(self, first_name, last_name, email, address, code):
        """
        Initialize a new Client.
        
        Args:
            first_name (str): Client's first name
            last_name (str): Client's last name
            email (str): Email address
            address (Address): Physical address
            code (int or str): Client identification code
        """
        super().__init__(first_name, last_name, email, address)
        self._code = code
        self._invoices = []
        self._num_of_invoices = 0
    
    def getCode(self):
        """Get client code."""
        return self._code
    
    def getInvoices(self):
        """Get list of client invoices."""
        return self._invoices
    
    def getNumberOfInvoices(self):
        """Get number of client invoices."""
        return self._num_of_invoices
    
    def addInvoice(self, invoice):
        """Add an invoice to the client's invoice list."""
        self._invoices.append(invoice)
        self._num_of_invoices += 1
    
    def printInvoices(self):
        """Print all client invoices."""
        for invoice in self.getInvoices():
            invoice.printProducts()
    
    def __str__(self):
        """String representation of a Client."""
        return (f"Client: {self.getFullName()}, "
                f"Code: {self._code}, Email: {self._email}, "
                f"Invoices: {self._num_of_invoices}")


class Product:
    """Product with title and cost."""
    
    def __init__(self, title, cost):
        """
        Initialize a new Product.
        
        Args:
            title (str): Product name or title
            cost (float): Product cost
        """
        self._title = title
        self._cost = cost
    
    def getTitle(self):
        """Get product title."""
        return self._title
    
    def getCost(self):
        """Get product cost."""
        return self._cost
    
    def __str__(self):
        """String representation of a Product."""
        return f"Product: {self._title} - ${self._cost}"


class Invoice:
    """Invoice containing products and purchase information."""
    
    def __init__(self, date):
        """
        Initialize a new Invoice.
        
        Args:
            date (str or datetime): Invoice date
        """
        self._date = date
        self._products = []
        self._num_of_products = 0
    
    def getDate(self):
        """Get invoice date."""
        return self._date
    
    def getProducts(self):
        """Get list of products on the invoice."""
        return self._products
    
    def getNumberOfProducts(self):
        """Get number of products on the invoice."""
        return self._num_of_products
    
    def getTotalCost(self):
        """Calculate total cost of all products on the invoice."""
        return sum(product.getCost() for product in self._products)
    
    def addProduct(self, product):
        """Add a product to the invoice."""
        self._products.append(product)
        self._num_of_products += 1
    
    def printProducts(self):
        """Print the invoice details and all products."""
        print(self)
        for product in self.getProducts():
            print(f"  {product}")
    
    def __str__(self):
        """String representation of an Invoice."""
        return (f"Invoice Date: {self._date}, "
                f"Number of Products: {self._num_of_products}, "
                f"Total: ${self.getTotalCost()}")


# Example usage
def demo():
    """Demonstrate business operations."""
    # Create an address
    address = Address("123 Main St", "Anytown", 12345, "USA")
    
    # Create a client
    client = Client("John", "Doe", "john.doe@example.com", address, "C1001")
    
    # Create an invoice with products
    invoice = Invoice("2023-04-10")
    invoice.addProduct(Product("Laptop", 1200.99))
    invoice.addProduct(Product("Mouse", 25.50))
    invoice.addProduct(Product("Keyboard", 85.75))
    
    # Add the invoice to the client
    client.addInvoice(invoice)
    
    # Print client and invoice information
    print(client)
    print("\nClient Invoices:")
    client.printInvoices()


if __name__ == "__main__":
    demo()
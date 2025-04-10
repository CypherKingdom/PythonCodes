"""
Appliance models with similar properties like speed, on/off status, radius, and color.
Contains base classes for appliances such as Fan and Motorcycle.
"""

class Appliance:
    """Base class for appliances with common properties."""
    
    def __init__(self, speed=1, on=False, radius=5.0, color="white"):
        """
        Initialize a new Appliance.
        
        Args:
            speed (int): Speed setting of the appliance (usually 1-5)
            on (bool): Whether the appliance is on
            radius (float): Physical radius of appliance component
            color (str): Color of the appliance
        """
        self._speed = speed
        self._on = on
        self._radius = radius
        self._color = color
    
    def getSpeed(self):
        """Get appliance speed."""
        return self._speed
    
    def setSpeed(self, speed):
        """Set appliance speed."""
        self._speed = speed
    
    def isOn(self):
        """Check if appliance is on."""
        return self._on
    
    def setOn(self, status):
        """Set appliance on/off status."""
        self._on = status
    
    def getRadius(self):
        """Get appliance radius."""
        return self._radius
    
    def setRadius(self, radius):
        """Set appliance radius."""
        self._radius = radius
    
    def getColor(self):
        """Get appliance color."""
        return self._color
    
    def setColor(self, color):
        """Set appliance color."""
        self._color = color
    
    def __str__(self):
        """String representation of an Appliance."""
        return f"Speed: {self._speed} | On: {self._on} | Radius: {self._radius} | Color: {self._color}"


class Fan(Appliance):
    """Fan appliance with speed, on/off status, radius, and color."""
    
    def __init__(self, speed=1, on=False, radius=5.0, color="white"):
        """
        Initialize a new Fan.
        
        Args:
            speed (int): Speed setting (1-5)
            on (bool): Whether the fan is on
            radius (float): Radius of fan blades (5-25)
            color (str): Color of the fan (gray, white, or silver)
        """
        super().__init__(speed, on, radius, color)
    
    def setSpeed(self, speed):
        """
        Set fan speed with validation.
        
        Args:
            speed (int): Speed setting (1-5)
        """
        if 1 <= speed <= 5:
            self._speed = speed
        else:
            print("Speed must be between 1 and 5")
    
    def setRadius(self, radius):
        """
        Set fan radius with validation.
        
        Args:
            radius (float): Radius of fan blades (5-25)
        """
        if 5 <= radius <= 25:
            self._radius = radius
        else:
            print("Radius must be between 5 and 25")
    
    def setColor(self, color):
        """
        Set fan color with validation.
        
        Args:
            color (str): Color of the fan (gray, white, or silver)
        """
        if color in ["gray", "white", "silver"]:
            self._color = color
        else:
            print("Color must be gray, white or silver")
    
    def __str__(self):
        """String representation of a Fan."""
        return f"Fan: {super().__str__()}"


class Motorcycle(Appliance):
    """Motorcycle appliance with speed, on/off status, radius, and color."""
    
    def __init__(self, speed=1, on=False, radius=5.0, color="white"):
        """
        Initialize a new Motorcycle.
        
        Args:
            speed (int): Speed setting (1-5)
            on (bool): Whether the motorcycle is on
            radius (float): Wheel radius (0-25)
            color (str): Color of the motorcycle (gray, white, or silver)
        """
        super().__init__(speed, on, radius, color)
    
    def setSpeed(self, speed):
        """
        Set motorcycle speed with validation.
        
        Args:
            speed (int): Speed setting (1-5)
        """
        if 1 <= speed <= 5:
            self._speed = speed
        else:
            print("Error: Speed must be between 1 and 5.")
    
    def setRadius(self, radius):
        """
        Set motorcycle radius with validation.
        
        Args:
            radius (float): Wheel radius (0-25)
        """
        if 0 <= radius <= 25:
            self._radius = float(radius)
        else:
            print("Error: Radius must be between 0 and 25.")
    
    def setColor(self, color):
        """
        Set motorcycle color with validation.
        
        Args:
            color (str): Color of the motorcycle (gray, white, or silver)
        """
        if color in ["gray", "white", "silver"]:
            self._color = str(color)
        else:
            print("Error: Color must be gray, white, or silver.")
    
    def __str__(self):
        """String representation of a Motorcycle."""
        return f"Motorcycle: {super().__str__()}"


# Example usage
def demo():
    """Demonstrate the usage of the Fan and Motorcycle classes."""
    # Create a fan
    fan = Fan(speed=3, on=True, radius=10, color="gray")
    print(f"Fan: {fan}")
    
    # Create a motorcycle
    motorcycle = Motorcycle(speed=4, on=True, radius=15, color="silver")
    print(f"Motorcycle: {motorcycle}")


if __name__ == "__main__":
    demo()
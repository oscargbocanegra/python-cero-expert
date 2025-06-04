"""
Liskov Substitution Principle (LSP) Examples

"Objects of a superclass should be replaceable with objects of its subclasses 
without breaking the application."

LSP ensures that a subclass can stand in for its superclass without altering 
the correctness of the program.
"""

from abc import ABC, abstractmethod
import math


# ========================================
# ❌ VIOLATES Liskov Substitution Principle
# ========================================

class RectangleViolatesLSP:
    """❌ This class will be problematic when inherited by Square."""
    
    def __init__(self, width: float, height: float):
        self._width = width
        self._height = height
    
    @property
    def width(self) -> float:
        return self._width
    
    @width.setter
    def width(self, value: float):
        self._width = value
    
    @property
    def height(self) -> float:
        return self._height
    
    @height.setter
    def height(self, value: float):
        self._height = value
    
    def area(self) -> float:
        return self._width * self._height


class SquareViolatesLSP(RectangleViolatesLSP):
    """
    ❌ This Square class violates LSP because it changes the behavior
    expected from a Rectangle. Setting width also changes height,
    which breaks the Rectangle contract.
    """
    
    def __init__(self, side: float):
        super().__init__(side, side)
    
    @property
    def width(self) -> float:
        return self._width
    
    @width.setter
    def width(self, value: float):
        # ❌ Problem: Changing width also changes height
        self._width = value
        self._height = value  # This breaks Rectangle's expected behavior
    
    @property
    def height(self) -> float:
        return self._height
    
    @height.setter
    def height(self, value: float):
        # ❌ Problem: Changing height also changes width
        self._width = value  # This breaks Rectangle's expected behavior
        self._height = value


def test_lsp_violation():
    """
    ❌ This function demonstrates how LSP violation breaks code.
    """
    def resize_rectangle(rectangle: RectangleViolatesLSP):
        """This function expects Rectangle behavior but breaks with Square."""
        rectangle.width = 5
        rectangle.height = 4
        expected_area = 5 * 4  # 20
        actual_area = rectangle.area()
        
        print(f"Expected area: {expected_area}")
        print(f"Actual area: {actual_area}")
        
        # This assertion will fail when rectangle is actually a Square
        assert actual_area == expected_area, f"Expected {expected_area}, got {actual_area}"
    
    # Works fine with Rectangle
    rect = RectangleViolatesLSP(3, 2)
    print("Testing with Rectangle:")
    resize_rectangle(rect)
    print("✅ Rectangle test passed")
    
    # Breaks with Square (LSP violation)
    square = SquareViolatesLSP(3)
    print("\nTesting with Square:")
    try:
        resize_rectangle(square)
        print("✅ Square test passed")
    except AssertionError as e:
        print(f"❌ Square test failed: {e}")


# ========================================
# ✅ FOLLOWS Liskov Substitution Principle
# ========================================

class Shape(ABC):
    """✅ Abstract base class that defines the contract for all shapes."""
    
    @abstractmethod
    def area(self) -> float:
        """Calculate the area of the shape."""
        pass
    
    @abstractmethod
    def perimeter(self) -> float:
        """Calculate the perimeter of the shape."""
        pass


class Rectangle(Shape):
    """✅ Rectangle implementation that follows LSP."""
    
    def __init__(self, width: float, height: float):
        if width <= 0 or height <= 0:
            raise ValueError("Width and height must be positive")
        self._width = width
        self._height = height
    
    @property
    def width(self) -> float:
        return self._width
    
    @property
    def height(self) -> float:
        return self._height
    
    def area(self) -> float:
        return self._width * self._height
    
    def perimeter(self) -> float:
        return 2 * (self._width + self._height)
    
    def resize(self, width: float, height: float) -> 'Rectangle':
        """Return a new Rectangle with different dimensions."""
        return Rectangle(width, height)
    
    def __str__(self) -> str:
        return f"Rectangle(width={self._width}, height={self._height})"


class Square(Shape):
    """
    ✅ Square as a separate class that properly follows LSP.
    It doesn't inherit from Rectangle, avoiding the behavioral inconsistency.
    """
    
    def __init__(self, side: float):
        if side <= 0:
            raise ValueError("Side must be positive")
        self._side = side
    
    @property
    def side(self) -> float:
        return self._side
    
    def area(self) -> float:
        return self._side ** 2
    
    def perimeter(self) -> float:
        return 4 * self._side
    
    def resize(self, side: float) -> 'Square':
        """Return a new Square with different side length."""
        return Square(side)
    
    def __str__(self) -> str:
        return f"Square(side={self._side})"


class Circle(Shape):
    """✅ Circle implementation that follows LSP."""
    
    def __init__(self, radius: float):
        if radius <= 0:
            raise ValueError("Radius must be positive")
        self._radius = radius
    
    @property
    def radius(self) -> float:
        return self._radius
    
    def area(self) -> float:
        return math.pi * self._radius ** 2
    
    def perimeter(self) -> float:
        return 2 * math.pi * self._radius
    
    def resize(self, radius: float) -> 'Circle':
        """Return a new Circle with different radius."""
        return Circle(radius)
    
    def __str__(self) -> str:
        return f"Circle(radius={self._radius})"


# ========================================
# ADVANCED LSP EXAMPLE: File Handlers
# ========================================

class FileHandler(ABC):
    """✅ Abstract base class for file handlers."""
    
    @abstractmethod
    def read(self) -> str:
        """Read content from file."""
        pass
    
    @abstractmethod
    def write(self, content: str) -> bool:
        """Write content to file."""
        pass
    
    @abstractmethod
    def is_writable(self) -> bool:
        """Check if file is writable."""
        pass


class ReadWriteFileHandler(FileHandler):
    """✅ Handler for files that support both reading and writing."""
    
    def __init__(self, filename: str):
        self.filename = filename
        self.content = ""
    
    def read(self) -> str:
        # Simulate reading from file
        return self.content
    
    def write(self, content: str) -> bool:
        # Simulate writing to file
        self.content = content
        return True
    
    def is_writable(self) -> bool:
        return True


class ReadOnlyFileHandler(FileHandler):
    """✅ Handler for read-only files - follows LSP by being clear about limitations."""
    
    def __init__(self, filename: str, content: str = ""):
        self.filename = filename
        self.content = content
    
    def read(self) -> str:
        return self.content
    
    def write(self, content: str) -> bool:
        # ✅ Doesn't break LSP because is_writable() indicates this limitation
        return False
    
    def is_writable(self) -> bool:
        return False


# ❌ This would violate LSP
class BadReadOnlyFileHandler(FileHandler):
    """❌ Bad implementation that violates LSP."""
    
    def read(self) -> str:
        return "some content"
    
    def write(self, content: str) -> bool:
        # ❌ This violates LSP by throwing an exception unexpectedly
        raise NotImplementedError("This file is read-only")
    
    def is_writable(self) -> bool:
        return False


def process_shapes(shapes: list[Shape]):
    """
    ✅ This function works with any Shape subclass without knowing
    the specific type, demonstrating proper LSP compliance.
    """
    total_area = 0
    total_perimeter = 0
    
    for shape in shapes:
        # These calls work identically regardless of the specific shape type
        area = shape.area()
        perimeter = shape.perimeter()
        
        total_area += area
        total_perimeter += perimeter
        
        print(f"{shape}: area={area:.2f}, perimeter={perimeter:.2f}")
    
    print(f"\nTotal area: {total_area:.2f}")
    print(f"Total perimeter: {total_perimeter:.2f}")


def process_files(file_handlers: list[FileHandler]):
    """
    ✅ This function works with any FileHandler subclass,
    properly checking capabilities before using them.
    """
    for handler in file_handlers:
        # Read from all files
        content = handler.read()
        print(f"Read from {handler.filename}: {content[:50]}...")
        
        # Only write to writable files (respects LSP)
        if handler.is_writable():
            success = handler.write("New content")
            print(f"Write to {handler.filename}: {'success' if success else 'failed'}")
        else:
            print(f"Skipping write to {handler.filename} (read-only)")


def demonstrate_lsp():
    """Demonstrate the Liskov Substitution Principle."""
    
    print("=== LSP Violation Demonstration ===")
    test_lsp_violation()
    
    print("\n=== LSP Compliance Demonstration ===")
    
    # ✅ All shapes can be used interchangeably
    shapes = [
        Rectangle(5, 3),
        Square(4),
        Circle(2.5),
    ]
    
    process_shapes(shapes)
    
    print("\n=== File Handler LSP Demonstration ===")
    
    # ✅ All file handlers can be used interchangeably
    file_handlers = [
        ReadWriteFileHandler("document.txt"),
        ReadOnlyFileHandler("readonly.txt", "This is read-only content"),
    ]
    
    process_files(file_handlers)


if __name__ == "__main__":
    demonstrate_lsp()


"""
🔍 LSP COMPLIANCE CHECKLIST:

✅ CORRECT LSP IMPLEMENTATION:
1. Subclasses don't strengthen preconditions
2. Subclasses don't weaken postconditions  
3. Subclasses preserve the behavioral contract
4. Client code works with base class and all subclasses
5. No unexpected exceptions in subclasses
6. Method signatures remain compatible

❌ LSP VIOLATIONS TO AVOID:
1. Changing method behavior in unexpected ways
2. Throwing new exceptions not in base class contract
3. Strengthening input validation in subclasses
4. Weakening output guarantees in subclasses
5. Making subclass methods do nothing when base class expects action
6. Breaking the behavioral contract established by the base class

💡 LSP BENEFITS:
- Code that works with base class works with all subclasses
- Polymorphism works correctly
- No surprises when substituting objects
- Maintainable inheritance hierarchies
- Reliable abstraction boundaries
"""

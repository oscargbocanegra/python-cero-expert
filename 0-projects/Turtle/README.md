# Python Turtle Graphics Learning Project

A comprehensive collection of Python Turtle graphics examples and projects designed for learning computer graphics, programming concepts, and game development fundamentals.

## 🐢 About Turtle Graphics

Python's Turtle Graphics is a beginner-friendly module that provides an intuitive way to learn programming concepts through visual drawing. It's inspired by the Logo programming language and allows users to control a "turtle" that moves around a canvas, leaving a trail behind it.

## 📁 Project Structure

```
Turtle/
├── README.md
├── requirements.txt           # Project dependencies and Python version requirements
├── 10.1Turtle.py              # Basic turtle movements and commands
├── 10.2Movimiento.py          # Movement patterns and positioning
├── 10.3ComandosEspeciales.py  # Special commands (circles, dots, show/hide)
├── 10.4Personalizando.py      # Customization features (colors, shapes, sizes)
├── 10.5OtrosAtributos.py      # Advanced attributes (fill, pen control, stamps)
├── 10.6AutomatizandoDibujo.py # Automated drawing with loops and user input
├── project-01.py              # Turtle Racing Game
└── proyect-02-culebrita.py    # Snake Game (Advanced Project)
```

## 🎮 Featured Projects

### 1. Turtle Racing Game (`project-01.py`)
- **Description**: An interactive racing game with two turtle players
- **Features**:
  - Two colored turtles (Green and Blue)
  - Dice-based movement system
  - Circular racing track
  - Turn-based gameplay
  - Winner detection system
- **How to Play**: Press Enter to roll the dice for each turtle's turn

### 2. Snake Game (`proyect-02-culebrita.py`)
- **Description**: A complete implementation of the classic Snake game
- **Features**:
  - Arrow key controls (Up, Down, Left, Right)
  - Food collection system
  - Score tracking with high score memory
  - Progressive difficulty (speed increases)
  - Collision detection (walls and self-collision)
  - Game over and restart functionality
- **Controls**: Use arrow keys to control the snake

## 📚 Learning Modules

### Module 10.1: Basic Turtle Commands
- Forward, backward movement
- Left and right turns
- Short command aliases (fd, bk, rt, lt)

### Module 10.2: Movement and Positioning
- `goto()` for absolute positioning
- `home()` to return to origin
- Creating geometric shapes (squares)

### Module 10.3: Special Commands
- `speed()` control
- `circle()` for curved shapes
- `dot()` for creating filled circles
- `hideturtle()` and `showturtle()`
- Coordinate positioning with `setx()` and `sety()`

### Module 10.4: Customization
- Screen background colors
- Window titles
- Turtle shape and size modifications
- Pen size and colors
- Fill and pen color combinations

### Module 10.5: Advanced Attributes
- Fill operations (`begin_fill()`, `end_fill()`)
- Pen control (`penup()`, `pendown()`)
- Shape changing
- Drawing stamps
- Undo, clear, and reset operations

### Module 10.6: Automation
- Loop-based drawing patterns
- User input integration
- Conditional drawing
- Automated pattern generation

## 🚀 Getting Started

### Prerequisites

- Python 3.6+ (Turtle module is included in standard library)
- No external packages required - all dependencies are part of Python's standard library

### Installation

1. **Clone or download** the project files
2. **Navigate** to the Turtle project directory:
   ```bash
   cd Turtle
   ```

3. **Verify Python installation** includes turtle graphics:
   ```bash
   python -c "import turtle; print('Turtle graphics available!')"
   ```

4. **Check requirements** (optional):
   ```bash
   # View the requirements.txt file to understand dependencies
   cat requirements.txt
   ```

### Running the Examples

1. **Basic Examples**:
   ```bash
   python 10.1Turtle.py
   python 10.2Movimiento.py
   python 10.3ComandosEspeciales.py
   # ... and so on
   ```

2. **Turtle Racing Game**:
   ```bash
   python project-01.py
   ```

3. **Snake Game**:
   ```bash
   python proyect-02-culebrita.py
   ```

## 🎯 Key Programming Concepts Covered

### Fundamental Concepts
- **Object-Oriented Programming**: Working with Turtle objects
- **Coordinate Systems**: Understanding X,Y positioning
- **Event Handling**: Keyboard input processing
- **Loop Structures**: For loops and while loops
- **Conditional Logic**: If-else statements
- **Function Definition**: Creating reusable code blocks

### Game Development Concepts
- **Game Loop**: Continuous update cycles
- **Collision Detection**: Object intersection logic
- **Score Systems**: Point tracking and high scores
- **State Management**: Game states (playing, game over)
- **User Input**: Real-time keyboard controls
- **Animation**: Movement and visual effects

### Graphics Programming
- **Drawing Algorithms**: Line and shape creation
- **Color Management**: RGB and named colors
- **Screen Management**: Canvas setup and properties
- **Sprite Handling**: Multiple object management

## 🎨 Visual Features

### Colors Used
- **Background**: Gray, Red
- **Turtle Colors**: Green, Blue, Orange, White, Black
- **Custom Color Combinations**: Pen and fill color variations

### Shapes and Patterns
- Basic geometric shapes (squares, circles)
- Complex patterns through automation
- Custom turtle shapes
- Filled and outlined objects

## 🎮 Game Features

### Racing Game
- ✅ Two-player turn-based gameplay
- ✅ Random dice mechanics
- ✅ Visual racing track
- ✅ Win condition detection
- ✅ Interactive console prompts

### Snake Game
- ✅ Real-time movement controls
- ✅ Food spawning system
- ✅ Dynamic snake growth
- ✅ Collision detection system
- ✅ Score tracking
- ✅ Progressive difficulty
- ✅ Game restart capability

## 🔧 Technical Implementation

### Dependencies & Requirements

All dependencies are **Python Standard Library modules** - no external installations needed!

- **turtle**: Core graphics library (built-in with Python)
  - Provides drawing canvas and turtle object functionality
  - Used in all project files for graphics rendering
- **time**: Game timing and delays (built-in with Python)
  - Used in `proyect-02-culebrita.py` for game loop timing
  - Controls game speed and animation delays
- **random**: Random number generation (built-in with Python)
  - Used in both game projects for dice rolls and food positioning
  - Provides randomness for game mechanics

**Minimum Python Version**: 3.6+  
**Installation Requirements**: None (uses only standard library)

### Libraries Used
- **turtle**: Core graphics library
- **time**: Game timing and delays
- **random**: Random number generation for games

### Code Architecture
- **Modular Design**: Separate files for different concepts
- **Function-Based Structure**: Reusable code organization
- **Event-Driven Programming**: Responsive user interfaces
- **State Management**: Game condition tracking

## 📖 Educational Value

This project serves as an excellent introduction to:
- **Programming Fundamentals**: Variables, functions, loops, conditionals
- **Object-Oriented Concepts**: Method calls and object properties
- **Game Development**: Basic game mechanics and structure
- **Computer Graphics**: Coordinate systems and visual programming
- **User Interface Design**: Input handling and visual feedback


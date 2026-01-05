# AI Coding Guidelines for Python Exercises Project

## Project Overview
This codebase contains Python programming exercises organized by topic in separate files (question1.py through question4.py). Each file demonstrates basic Python concepts through practical examples and interactive code.

## Key Patterns and Conventions

### Code Structure
- **Exercise Organization**: Each major concept gets its own file (e.g., `question1.py` for lists/tuples/sets, `question2.py` for dictionaries/control flow)
- **Example-Driven**: Code includes both hardcoded examples and interactive input sections
- **Output Verification**: Use `print()` statements extensively to demonstrate results

### Input Handling
- **Interactive Sections**: Wrap user input in `input()` calls, but comment them out for non-interactive testing
- **Example Data**: Provide hardcoded values alongside input prompts for easy verification
- **Type Conversion**: Explicitly convert inputs (e.g., `int(input(...))`) when needed

### Naming Conventions
- **Descriptive Variables**: Use meaningful names like `stdName`, `player_id_list` instead of generic `list1`
- **Consistency**: Follow Python snake_case for variables and functions
- **Data Types in Names**: Include type hints in variable names when helpful (e.g., `num` for numbers, `frt` for fruits)

### Execution and Testing
- **Individual Runs**: Execute files independently with `python questionX.py`
- **No Dependencies**: Pure Python, no external libraries required
- **Output Inspection**: Verify results through console output

### Adding New Exercises
- **File Placement**: Add to existing topic files or create new `question5.py` for new concepts
- **Pattern Matching**: Follow existing structure with comments describing the exercise
- **Interactive Toggle**: Comment out `input()` lines for automated testing, uncomment for user interaction

### Example Patterns
```python
# Hardcoded example (from question1.py)
list2 = ["Apple", "Banana", "Cherry", "Date"]
list2[1] = "mango"
print(list2)

# Interactive with fallback (from question2.py)
# num = int(input("Enter a number: "))
num = 7  # Uncomment above for interactive
if num % 2 == 0:
    print("The number is even.")
else:
    print("The number is odd.")
```

### Key Reference Files
- `question1.py`: Data structures (lists, tuples, sets) operations
- `question2.py`: Dictionaries and control flow (if-else, match)
- `question3.py`: Function definitions and calls
- `question4.py`: Advanced pattern matching with tuples/zipping</content>
<parameter name="filePath">c:\Users\LENOVO\question.py\.github\copilot-instructions.md
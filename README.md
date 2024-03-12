# Assignment-0-Refactor
ICS 32/32A - Assignment refactor
## Overview
This repository contains a refactored Python script for generating a square pattern based on user input. The code was refactored to include the use of Higher-order functions

## Original Code
The original code utilized procedural programming with explicit loop control and lacked abstraction. It consisted of a single script with hardcoded logic to generate the square pattern.


### Introduction of Higher-Order Function
In the original code, the square pattern generation logic was tightly coupled with the main script. In the refactored version, we introduced a higher-order function `generate_pattern` that takes another function `square_printer` as an argument.

### 2. Improved Readability
The refactored code is more readable due to the use of descriptive function names and separation of concerns. Each function now has a clear responsibility, making it easier to understand and maintain.

### 3. Modularization
By separating the square pattern generation logic into a separate function (`square_printer`), we promote code reusability and modularity. This makes it easier to test and modify the square generation logic independently.

## Conclusion
The refactoring process has resulted in a more modular, readable, and maintainable codebase. By introducing a higher-order function and improving code organization, the refactored code offers greater flexibility and extensibility for future enhancements or modifications. 

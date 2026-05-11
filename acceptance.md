# Acceptance Criteria

## Task 1: Runner and package initialization

### Acceptance Criteria
- [x] Package `pyguide` is importable with `__name__` and `__path__` attributes
- [x] Runner discovers modules with `main()` functions using `pkgutil.walk_packages`
- [x] Runner executes each discovered `main()` function without errors
- [x] Runner skips modules that don't have a `main()` function
- [x] Runner handles import errors gracefully and reports which module failed
- [x] Runner reports success/failure status for each module
- [x] `main()` functions must have zero parameters (validated via `inspect.signature`)

## Task 2: Variable and expression modules

### Acceptance Criteria
- [x] Variable module demonstrates int, float, bool, str literal types
- [x] Variable module shows type() returns the class of each literal
- [x] Variable module demonstrates isinstance() checks
- [x] Variable module shows integer literal bases (decimal, hex, octal, binary)
- [x] Variable module demonstrates underscores in numeric literals
- [x] Variable module shows None literal and type(None)
- [x] Expression module shows basic arithmetic operations (+, -, *, /)
- [x] Expression module demonstrates integer division (//) vs float division (/)
- [x] Expression module shows exponentiation (**)
- [x] Expression module demonstrates chaining expressions

## Task 3: Bitwise operations module

### Acceptance Criteria
- [x] Module demonstrates bitwise AND (&), OR (|), XOR (^) operators
- [x] Module demonstrates bitwise NOT (~) operator
- [x] Module demonstrates left shift (<<) and right shift (>>) operators
- [x] Module shows binary representation with bin() function
- [x] Module demonstrates practical examples of bit manipulation

## Task 4: Conditional and loop modules

### Acceptance Criteria
- [ ] Conditional module demonstrates if statements
- [ ] Conditional module demonstrates if-else statements
- [ ] Conditional module demonstrates if-elif-else chains
- [ ] Conditional module shows comparison operators (==, !=, <, >, <=, >=)
- [ ] Conditional module demonstrates logical operators (and, or, not)
- [ ] Loop module demonstrates for loops with range()
- [ ] Loop module demonstrates for loops over sequences
- [ ] Loop module demonstrates while loops
- [ ] Loop module shows break and continue statements
- [ ] Loop module demonstrates enumerate() and zip()

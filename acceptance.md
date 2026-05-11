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
- [ ] Module demonstrates bitwise AND (&), OR (|), XOR (^) operators
- [ ] Module demonstrates bitwise NOT (~) operator
- [ ] Module demonstrates left shift (<<) and right shift (>>) operators
- [ ] Module shows binary representation with bin() function
- [ ] Module demonstrates practical examples of bit manipulation

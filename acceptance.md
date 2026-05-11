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
- [ ] Variable module demonstrates int, float, bool, str literal types
- [ ] Variable module shows type() returns the class of each literal
- [ ] Variable module demonstrates isinstance() checks
- [ ] Variable module shows integer literal bases (decimal, hex, octal, binary)
- [ ] Variable module demonstrates underscores in numeric literals
- [ ] Variable module shows None literal and type(None)
- [ ] Expression module shows basic arithmetic operations (+, -, *, /)
- [ ] Expression module demonstrates integer division (//) vs float division (/)
- [ ] Expression module shows exponentiation (**)
- [ ] Expression module demonstrates chaining expressions

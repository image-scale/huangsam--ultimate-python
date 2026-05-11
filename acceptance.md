# Acceptance Criteria

## Task 1: Runner and package initialization

### Acceptance Criteria
- [ ] Package `pyguide` is importable with `__name__` and `__path__` attributes
- [ ] Runner discovers modules with `main()` functions using `pkgutil.walk_packages`
- [ ] Runner executes each discovered `main()` function without errors
- [ ] Runner skips modules that don't have a `main()` function
- [ ] Runner handles import errors gracefully and reports which module failed
- [ ] Runner reports success/failure status for each module
- [ ] `main()` functions must have zero parameters (validated via `inspect.signature`)

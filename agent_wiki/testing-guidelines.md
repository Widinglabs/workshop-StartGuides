# Testing Guidelines

*Workshop goal: Define testing practices agents must follow. Focus on what to test, how to structure tests, and when tests are required.*

## Test Structure & Location
*Where tests live and how they're organized*
- **Test directory**: [location relative to source]
- **File naming**: [pattern, e.g., test_*.py or *_test.py]
- **Directory structure**: [mirror source / separate structure]

## Test Types & When to Use
*What kinds of tests to write and when*
- **Unit tests**: [when required] - Test [what specifically]
- **Integration tests**: [when required] - Test [what specifically]  
- **End-to-End tests**: [when required] - Test [what specifically]

## Required Test Coverage
*What must be tested before code can be merged*
- **New functions**: [always / when complex / when public]
- **Bug fixes**: [test for regression - yes/no]
- **API endpoints**: [all / critical paths only]
- **Minimum coverage**: [percentage if enforced]

## Test Naming & Organization
*How to name and structure individual tests*
```python
# Test function naming pattern:
def test_[what_is_being_tested]_[expected_outcome]():
    """[Documentation requirements]"""
    pass

# Example:
def test_user_creation_with_valid_data_creates_user():
    """Test that valid user data creates a new user successfully."""
    pass
```

## Test Data & Fixtures
*How to handle test data*
- **Test data location**: [directory/file pattern]
- **Fixtures**: [when to use / how to structure]
- **Database setup**: [per test / per class / per session]
- **External services**: [mock / stub / real]

## Assertions & Test Structure
*Standard pattern for writing tests*
```python
# Standard test structure:
def test_example():
    # Arrange: [Set up test data]
    
    # Act: [Execute the code being tested]
    
    # Assert: [Verify the results]
    assert result == expected
```

## Common Test Patterns
*Reusable patterns for different scenarios*
- **Testing exceptions**: 
```python
# Example pattern for testing exceptions
```
- **Testing async code**:
```python  
# Example pattern for async tests
```
- **Testing API endpoints**:
```python
# Example pattern for API tests
```

## Mock & Stub Guidelines
*When and how to use mocks*
- **External APIs**: [always mock / sometimes mock]
- **Database calls**: [mock in unit tests / real in integration]
- **File system**: [mock / use temp directories]
- **Time/dates**: [how to handle time-dependent tests]

## Test Commands
*How to run tests locally and in CI*
- **Run all tests**: `[command]`
- **Run specific test**: `[command pattern]`
- **Run with coverage**: `[command]`
- **Run in watch mode**: `[command]`

## CI/CD Requirements
*What must pass before merging*
- **All tests pass**: [yes/no]
- **Coverage threshold**: [percentage]
- **Linting passes**: [yes/no]
- **Performance tests**: [when required]

## What NOT to Test
*Avoid wasting time on these*
- L [Things that shouldn't be tested]
- L [Over-testing scenarios]
- L [Third-party library internals]

## Testing Tools & Setup
*Tools and configuration*
- **Test framework**: [pytest/unittest/etc.]
- **Mocking library**: [unittest.mock/pytest-mock/etc.]
- **Coverage tool**: [coverage.py/pytest-cov/etc.]
- **Config files**: [location of test configs]

---
*Workshop completed by: [Team members] on [Date]*
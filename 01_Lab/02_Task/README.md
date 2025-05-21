# API Data Validation Tests

This project contains automated tests to validate data from the Fake Store API (https://fakestoreapi.com/products).

## Test Objectives

1. Verify server response code (expected 200)
2. Validate product attributes:
   - `title` must not be empty
   - `price` must not be negative
   - `rating.rate` must not exceed 5
3. Generate a list of products containing defects

## Setup

1. Install the required dependencies:
```bash
pip install -r requirements.txt
```

## Running the Tests

To run the tests, execute:
```bash
pytest test_api_validation.py -v
```

The tests will:
- Check if the API responds with status code 200
- Validate all product attributes
- Print a list of any defective products found
- Fail if any defects are detected 
# Testing Strategy

## Overview

The Quick-Calc application uses a structured testing strategy to verify the correctness of the calculator logic and ensure that different components of the system work together properly. The testing approach combines unit testing and integration testing following standard software engineering practices.

---

## What Was Tested

The following components were tested:

* Individual arithmetic operations (addition, subtraction, multiplication, division)
* Handling of edge cases such as division by zero
* Support for negative numbers, decimal numbers, and large numbers
* Integration between the user input layer and the calculation logic
* Clear functionality resetting the calculator state

---

## What Was Not Tested

The project focuses primarily on functional correctness of the calculator logic. The following aspects were intentionally not tested:

* Performance testing
* Security testing
* User interface usability testing
* Stress or load testing

These aspects were not necessary for a simple command-line calculator application.

---

## Testing Pyramid

The testing strategy follows the **Testing Pyramid** model:

* **Unit Tests** form the base of the pyramid. They test individual calculation functions independently.
* **Integration Tests** verify that multiple components work together correctly.

Most of the tests in this project are unit tests because they are faster, simpler, and isolate functionality effectively.

---

## Black-box vs White-box Testing

**White-box testing** was used for the unit tests because the internal logic of each calculator function is known. The tests directly verify the behavior of specific functions.

**Black-box testing** is represented in the integration tests where the focus is on the interaction between components without considering internal implementation details.

---

## Functional vs Non-Functional Testing

The tests implemented in this project focus on **functional testing**, meaning they verify that the calculator performs the correct operations and produces accurate results.

Non-functional aspects such as performance, scalability, and usability were not tested because they are not critical for this small application.

---

## Regression Testing

The automated test suite acts as a regression testing mechanism. Whenever the code is modified or new features are added, the tests can be executed again to ensure that previously working functionality has not been broken.

---

## Test Results Summary

| Test Name             | Type        | Status |
| --------------------- | ----------- | ------ |
| test_addition         | Unit        | Pass   |
| test_subtraction      | Unit        | Pass   |
| test_multiplication   | Unit        | Pass   |
| test_division         | Unit        | Pass   |
| test_negative_numbers | Unit        | Pass   |
| test_decimal_numbers  | Unit        | Pass   |
| test_large_numbers    | Unit        | Pass   |
| test_division_by_zero | Unit        | Pass   |
| test_full_calculation | Integration | Pass   |
| test_clear_function   | Integration | Pass   |

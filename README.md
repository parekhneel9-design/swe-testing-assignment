# Quick-Calc

## Project Description

Quick-Calc is a simple calculator application developed as part of the Advanced Software Engineering course assignment. The application supports basic arithmetic operations including addition, subtraction, multiplication, and division. It also includes functionality to handle division by zero gracefully and to clear the calculator state.

The project demonstrates the implementation of software testing principles, version control practices using Git and GitHub, and structured documentation. The focus of this assignment is not the graphical interface but the reliability and correctness of the calculation logic supported by a comprehensive test suite.

---

## Features

* Addition of two numbers
* Subtraction of two numbers
* Multiplication of two numbers
* Division with division-by-zero handling
* Clear function to reset the calculator
* Unit tests for individual operations
* Integration tests for complete calculation flow

---

## Setup Instructions

### 1. Clone the repository

```
git clone https://github.com/parekhneel9-design/swe-testing-assignment.git
```

### 2. Navigate to the project folder

```
cd swe-testing-assignment
```

### 3. Install dependencies

```
pip install -r requirements.txt
```

---

## Running the Application

Run the calculator using:

```
python main.py
```

Follow the prompts to enter numbers and operations.

---

## Running the Tests

All tests can be executed using the following command:

```
python -m pytest
```

The test suite includes both unit tests and integration tests.

---

## Testing Framework Research

Two commonly used testing frameworks in Python are **Pytest** and **Unittest**.

**Unittest** is the built-in testing framework in Python and is inspired by the JUnit framework used in Java. It provides a structured approach to writing tests using test classes and methods. While it is powerful and widely used, it often requires more boilerplate code, making test files longer and sometimes harder to read.

**Pytest**, on the other hand, is a more modern and flexible testing framework. It allows developers to write concise tests using simple assert statements without needing complex class structures. Pytest also provides powerful features such as fixtures, parameterized tests, and automatic test discovery.

For this project, **Pytest was chosen** because it simplifies writing and running tests, reduces boilerplate code, and makes the testing process easier to maintain and understand.

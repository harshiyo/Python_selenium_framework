# Python Selenium Framework

[![Build](https://github.com/harshiyo/Python_Selenium_Framework/actions/workflows/build.yml/badge.svg)](https://github.com/harshiyo/Java_Selenium_Framework/actions/workflows/build.yml) 
[![Language: Java](https://img.shields.io/badge/Language-Python-orange.svg)](https://github.com/harshiyo/Python_Selenium_Framework)

A powerful and flexible framework for automating web application testing using Selenium WebDriver and Python.

## Features

- **Page Object Model (POM)**: The framework follows the POM design pattern for easy maintenance and scalability of tests.
- **Data-driven testing**: The framework supports data-driven testing using external data sources such as CSV, Excel, or JSON files.
- **Parallel execution**: The framework allows for parallel execution of tests using multi-threading or multiprocessing.
- **Built-in reporting and logging**: The framework includes built-in reporting and logging functionality for easy test results analysis and debugging.
- **Handling common web elements**: The framework includes a library of common web elements and their interactions such as buttons, links, forms, etc.
- **Cross-browser compatibility**: The framework supports testing on multiple browsers such as Chrome, Firefox, Edge, Safari, etc.

## Getting Started

To use the framework, you need to have Python and Selenium WebDriver installed on your system. You can install Selenium using pip:

```bash
pip install selenium
```
 

1. Clone the repository and navigate to the project directory:
2. git clone https://github.com/username/python-selenium-framework.git
3. cd python-selenium-framework
 

You can run the tests by executing the following command:
```bash
python -m pytest
```
 

You can also specify the browser on which you want to run the tests by passing the `--browser` argument:
```bash
python -m pytest --browser=chrome
```
 

## Integration

The framework can be integrated with other tools such as Jenkins, TestNG, or Allure for continuous integration, test management, and reporting.




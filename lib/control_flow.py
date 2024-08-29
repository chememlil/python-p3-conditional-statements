#!/usr/bin/env python3

def admin_login(username, password):
    # Check if the username is "admin" or "ADMIN" and the password is "12345"
    if (username == "admin" or username == "ADMIN") and password == "12345":
        return "Access granted"
    else:
        return "Access denied"

def hows_the_weather(temperature):
    # Determine the weather message based on the temperature
    if temperature < 40:
        response = "It's brisk out there!"
    elif 40 <= temperature <= 65:
        response = "It's a little chilly out there!"
    elif temperature > 85:
        response = "It's too dang hot out there!"
    else:
        response = "It's perfect out there!"
    return response

def fizzbuzz(num):
    # Return the appropriate FizzBuzz response
    if num % 3 == 0 and num % 5 == 0:
        return "FizzBuzz"
    elif num % 3 == 0:
        return "Fizz"
    elif num % 5 == 0:
        return "Buzz"
    else:
        return num

def calculator(operation, num1, num2):
    # Perform the calculation based on the operation provided
    if operation == "+":
        return num1 + num2
    elif operation == "-":
        return num1 - num2
    elif operation == "*":
        return num1 * num2
    elif operation == "/":
        return num1 / num2
    else:
        return "Invalid operation!"

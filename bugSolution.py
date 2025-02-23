def function_with_improved_error_handling(a, b):
    try:
        if not isinstance(a, (int, float)) or not isinstance(b, (int, float)):
            raise TypeError("Operands must be numbers")
        result = a / b
        return result
    except ZeroDivisionError:
        print("Error: Division by zero")
        return None
    except TypeError as e:
        print(f"Error: {e}")
        return None
    except Exception as e:
        print(f"An unexpected error occurred: {e}")
        return None

#Example
result1 = function_with_improved_error_handling(10, 2) # Output: 5.0
result2 = function_with_improved_error_handling(10, 0)  # Output: Error: Division by zero, None
result3 = function_with_improved_error_handling(10, "hello") # Output: Error: Operands must be numbers, None
result4 = function_with_improved_error_handling("hello",10) # Output: Error: Operands must be numbers, None
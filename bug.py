def function_with_uncommon_error(a, b):
    try:
        result = a / b
        return result
    except ZeroDivisionError:
        print("Error: Division by zero")
        return None
    except TypeError:
        if isinstance(a,(int,float)) and isinstance(b,(int,float)):
            raise
        else:
            print("Error: Invalid type for operands")
            return None
    except Exception as e:
        print(f"An unexpected error occurred: {e}")
        return None

# Example usage
result1 = function_with_uncommon_error(10, 2)  # Output: 5.0
result2 = function_with_uncommon_error(10, 0)  # Output: Error: Division by zero, None
result3 = function_with_uncommon_error(10, "hello")  # Output: Error: Invalid type for operands, None
result4 = function_with_uncommon_error("hello", 10) # Output: Error: Invalid type for operands, None
result5 = function_with_uncommon_error(10, 0.0) # Output: Error: Division by zero, None
result6 = function_with_uncommon_error(10.5, 2.0) # Output: 5.25
def log_call(func):
    """Decorator to print function name, args, kwargs, and return value."""
    def wrapper(*args, **kwargs):
        # Print arguments (using *args and **kwargs)
        arg_str = str(args) + ", " + str(kwargs) if args or kwargs else ""
        result = func(*args, **kwargs)
        print(f"Called {func.__name__} with args={arg_str}, returned {result}")
        return result
    return wrapper

@log_call
def calculate_total(*prices, discount=0):
    """Calculate total after applying a percentage discount."""
    total = sum(prices)
    final_total = total * (1 - (discount / 100))
    return round(final_total, 2)

# Demonstration calls
print("--- Call 1: Multiple prices ---")
calculate_total(10, 20, 30, discount=5) 

print("\n--- Call 2: Single price with no discount ---")
calculate_total(50) 

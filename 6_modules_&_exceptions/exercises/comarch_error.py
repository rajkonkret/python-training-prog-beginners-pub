
def very_complex_operation():
    pass

try:
    very_complex_operation()
except ValueError as e:
    print(f"I want to see you")
except Exception as e:
    print(f"I do not want to see you")
finally:
    print(f"I want to see you too")

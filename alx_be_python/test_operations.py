from fns_and_dsa.arithmetic_operations import perform_operation

def test():
    print("Test Add:", perform_operation(5, 6, "add"))         # Expected 11.0
    print("Test Subtract:", perform_operation(10, 3, "subtract")) # Expected 7.0
    print("Test Multiply:", perform_operation(4, 2, "multiply")) # Expected 8.0
    print("Test Divide:", perform_operation(9, 3, "divide"))    # Expected 3.0
    print("Test Divide by Zero:", perform_operation(5, 0, "divide")) # Expected error message

if __name__ == "__main__":
    test()


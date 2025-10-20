#From chatGPT
def test_fibonacci():
    # Test case 1: First 1 Fibonacci number
    assert fibonacci(1) == [0], "Test case 1 failed"

    # Test case 2: First 2 Fibonacci numbers
    assert fibonacci(2) == [0, 1], "Test case 2 failed"

    # Test case 3: First 5 Fibonacci numbers
    assert fibonacci(5) == [0, 1, 1, 2, 3], "Test case 3 failed"

    print("All test cases passed!")

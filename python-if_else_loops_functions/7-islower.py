def islower(c):
    """Check if a character is lowercase."""
    # ASCII value for 'a' is 97 and 'z' is 122
    return 97 <= ord(c) <= 122

# The following lines are part of your test script and not the function itself
if __name__ == "__main__":
    islower = __import__('7-islower').islower

    print("a is {}".format("lower" if islower("a") else "upper"))
    print("H is {}".format("lower" if islower("H") else "upper"))
    print("A is {}".format("lower" if islower("A") else "upper"))
    print("3 is {}".format("lower" if islower("3") else "upper"))
    print("g is {}".format("lower" if islower("g") else "upper"))

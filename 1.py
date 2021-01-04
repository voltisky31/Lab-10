text = f"""
There is no place for the weakwilled or hesitant.
Only by firm action and resolute faith will mankind survive.
No sacrifice is too great.
No treachery too small.
"""
print("Lower")
print(text.lower())
print("Swapcase")
print(text.swapcase())
print("Capitalize")
print(text.capitalize())
print("Replace")
print(text.replace(".", " !@^%*&^% "))
print("Lstrip")
print(text.lstrip())
print("Rstrip")
print(text.rstrip())
print("Reversed")
print(text[::-1])
print("Count : y pojawia się tyle razy: ")
print(text.count("y", 0, len(text)))
print("Find")
print(text.find("is", 0, len(text)))
print("Isallnum")
print(text.isalnum())
print("Startswith")
print(text.startswith("no", 0, len(text)))
print("Endswith")
print(text.endswith("great", 0, len(text)))
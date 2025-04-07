s = "A man, a plan, a canal: Panama"

string = "".join(char.lower() for char in s if char.isalnum())
print(  string ==  string[::-1])
import xmlrpc.client

print("=== RMI String Concatenation Client ===\n")

# Connect client to server
proxy = xmlrpc.client.ServerProxy("http://localhost:8000/")

# User input
str1 = input("Enter First String : ")
str2 = input("Enter Second String : ")

print("\n[Client] Sending strings to server for concatenation...")

# Remote method call
result = proxy.concatenate_strings(str1, str2)

# Display result
print(f"\n[Client] Result received from Server: '{result}'")
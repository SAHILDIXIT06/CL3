import xmlrpc.client

# Connect client to server
proxy = xmlrpc.client.ServerProxy("http://localhost:8000/RPC2")

# Take input from user
num = int(input("Enter a number: "))

# Send number to server
result = proxy.calculate_factorial(num)

# Print result
print("Factorial is:", result)
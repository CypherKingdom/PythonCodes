# Encrypted Message Router You are building a message routing system for a secure communication network. 
# Each message contains an encrypted routing path and a payload. The routing path is a string of characters 
# where each character represents a node in the network. The payload is the actual message content. 
# The system works as follows:
# Messages arrive in a queue and must be processed in order (first in, first out).
# For each message, you need to decode the routing path according to these rules:
# If a character is uppercase, the message should be routed to that node directly.
# If a character is lowercase, the message should skip that node.
# If a character is a digit (0-9), the message should be duplicated and sent to 
# the next N nodes in the path, where N is the value of the digit.
# After processing the routing path, output the final routing sequence and the payload.
# Write a function that processes a queue of messages and returns the final routing sequence and payload for each message.

# Example 1:
# Input:
# ['ABcD:Hello', 'X2Yz:World']
# Output:
# ['AC:Hello', 'XYY:World']
# Explanation:
# For 'ABcD:Hello', we keep 'A' (uppercase), skip 'b' (lowercase), keep 'C' (uppercase), and skip 'd' (lowercase), resulting in 'AC:Hello'.
# For 'X2Yz:World', we keep 'X' (uppercase), duplicate the next 2 characters ('Y' is kept, 'Z' is skipped), resulting in 'XYY:World'.

# Example 2:
# Input:
# ['1AB:Test', 'aB3c:Data']
# Output:
# ['AAB:Test', 'B:Data']
# Explanation:
# For '1AB:Test', the digit '1' means duplicate the next character once, which is 'A', so we get 'A' plus

def process_messages(messages):
    result = []

    for message in messages:
        path, payload = message.split(":")
        final_route = ""
        i = 0
        while i < len(path):
            char = path[i]
            if char.isupper():
                final_route += char
                i += 1
            elif char.islower():
                i += 1  # skip lowercase
            elif char.isdigit():
                count = int(char)
                for j in range(1, count + 1):
                    if i + j < len(path):
                        final_route += path[i + j]
                i += count + 1
        result.append(f"{final_route}:{payload}")
    
    return result

input1 = ['ACd:Hello', 'X2Yz:World']
output1 = process_messages(input1)
print(output1)

input2 = ['1AB:Test', 'aB3c:Data']
output2 = process_messages(input2)
print(output2)
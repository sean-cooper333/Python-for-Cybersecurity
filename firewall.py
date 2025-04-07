# import random to generate random numbers
import random

# generates a random final octet for the ip 192.168.1.__ between 0 and 20. I've seen people generate complete random IP's using random.randint(0,255)


def generate_random_ip():
    return f"192.168.1.{random.randint(0, 255)}"

# define firewall rules,receives ip and rules as arguments, use a for loop to unpack the dictionary by using the items function, will compare the randomly generated ip and compares it to the dictionary list.


def check_firewall_rules(ip, rules):
    for rule_ip, action in rules.items():
        if ip == rule_ip:
            return action
    return "block"


# define a function with a dictionary inside
def main():
    firewall_rule = {
        "192.168.1.1": "allow",
        "192.168.1.4": "allow",
        "192.168.1.9": "allow",
        "192.168.1.13": "allow",
        "192.168.1.16": "allow",
        "192.168.1.19": "allow"
    }

    # for loop used to simulate network traffic will run 12 times
    for _ in range(255):
        # declare ip address and assign it to the generate_random_ip function
        ip_address = generate_random_ip()
        # assigned the value returned by the function check_firewall_rule
        action = check_firewall_rules(ip_address, firewall_rule)
        # declare random_number between 0-9999, this will serve as a unique identifier for when we take multiple action against the same source IP to distinguish between the different instances of those actions.
        random_number = random.randint(0, 9999)
        # prints results of each function we declared above, lists the ip, the action taken against the IP and a random ID number.
        print(f"IP: {ip_address}, Action: {action}, Random: {random_number}")


# execute the main function
if __name__ == "__main__":
    main()

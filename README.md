# Firewall Simulator

A simple Python script that simulates network traffic through a firewall by generating random IP addresses within the 192.168.1.0/24 subnet and checking them against predefined firewall rules.

## Table of Contents

- [Overview](#overview)
- [Features](#features)
- [Installation](#installation)
- [Usage](#usage)

## Overview

This project demonstrates a basic simulation of firewall rules. The script:
- Generates random IP addresses in the form `192.168.1.X`
- Checks each generated IP against a dictionary of firewall rules (where specific IPs are allowed)
- Outputs the IP, the corresponding action (allow or block), and a random identifier

The code can be used as a learning tool to understand basic Python functions, dictionary lookups, and simulating network traffic for educational or testing purposes.

## Features

- **Random IP Generation:** Uses Python's `random.randint()` to simulate network traffic.
- **Firewall Rule Check:** Compares generated IPs to a set of allowed IPs defined in a dictionary.
- **Traffic Simulation:** Loops through multiple iterations to simulate continuous traffic.
- **Unique Identifier:** Generates a random ID for each request to simulate unique traffic entries.

## Installation

1. **Clone the repository:**

   ```bash
   git clone https://github.com/your-username/firewall-simulator.git
   cd firewall-simulator
## Usage 

- No real use, just a small project to help me better understand Python.

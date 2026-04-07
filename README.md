# Smart-Payment-Processing-System_Chetna_Singh_202501100700061-ECE-B


# Smart Payment Processing System (OOP in Python)

##  Overview
This project implements a **Smart Payment Processing System** using **Object-Oriented Programming (OOP)** concepts in Python. It simulates multiple payment methods with different business rules while maintaining a common interface.

---

## Features
- Supports multiple payment methods:
  - Credit Card
  - UPI
  - PayPal
  - Digital Wallet
- Demonstrates core OOP principles:
  - Abstraction
  - Inheritance
  - Polymorphism
- Generates payment receipts
- Handles wallet balance validation

---

## OOP Concepts Used

### 1. Abstraction
An abstract base class `Payment` defines a common interface for all payment types.

### 2. Inheritance
Each payment method inherits from the `Payment` class.

### 3. Polymorphism
The same function `process_payment()` behaves differently based on the object passed.

---

## Payment Logic

### Credit Card
- 2% gateway fee
- 18% GST on gateway fee

### UPI
- ₹50 cashback if amount > ₹1000

### PayPal
- 3% transaction fee
- ₹20 fixed conversion fee

### Wallet
- Deducts amount from balance
- Fails if insufficient balance

#     --- Payment Receipt ---
# User: Alice
# Original Amount: ₹1000
# Final Amount Paid: ₹1023.6
# ------------------------





#sample case 

# --- Payment Receipt ---
# User: Bob
# Original Amount: ₹1200
# Final Amount Paid: ₹1150
# ------------------------

# --- Payment Receipt ---
# User: Charlie
# Original Amount: ₹2000
# Final Amount Paid: ₹2080.0
# ------------------------

# --- Payment Receipt ---
# User: Daisy
# Original Amount: ₹300
# Final Amount Paid: ₹300
# ------------------------
# Remaining Wallet Balance: ₹200

# Transaction Failed: Insufficient Wallet Balance

---

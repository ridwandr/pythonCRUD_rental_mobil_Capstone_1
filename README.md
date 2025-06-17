# Python CRUD Application for Car Rental Management  
A comprehensive Python application for managing vehicle and customer data with Create, Read, Update, and Delete (CRUD) operations.

## Business Understanding  
This project caters to the car rental industry, specifically addressing the need to manage both vehicle and customer data efficiently.  
Vehicles and customer records play a crucial role in ensuring smooth rental operations, accurate billing, and seamless customer service.

### Benefits:
- Improved data accuracy and consistency
- Streamlined rental and return workflows
- Clear historical tracking of rental transactions
- Enhanced operational decision-making through accessible rental data

### Target Users:
This application is designed for rental agents, administrators, and operational staff within a rental service company to facilitate daily operations related to vehicle availability, customer tracking, and transaction management.

## Features

### Create:
- Add new vehicle entries with essential details like brand, model, year, and daily rental price.
- Add new customers including name, gender, and address.
- Validation rules ensure no duplicate vehicle entries based on attributes.

### Read:
- Search and retrieve specific vehicles or customers based on ID or name.
- Display detailed, tabulated information for each record.
- Includes keyword-based search for partial matches.

### Update:
- Modify vehicle or customer data to reflect changes in pricing, address, etc.
- Provides confirmation messages to ensure updates are intentional and successful.

### Delete:
- Remove vehicles or customers with confirmation checks.
- Prevents accidental deletion through user prompts.

### Security:
- Basic input validation to prevent bad data entry.
- Logical access flow to avoid unintended access to functions.
- Future-ready structure for integrating login or admin control features.

### Reporting:
- Maintains a history of rental transactions per vehicle.
- Calculates rental duration and total payment based on price per day.
- Easily extendable to support export (CSV, JSON) or analytics (optional).

## Installation

### Prerequisites:
- Python 3.8 or higher
- `tabulate` module

### Installation:
- Prerequisites:

  - Python version 3.13.3
  - tabulate modul

- Installation:
    ```bash
    pip install tabulate
    ```

---

## Usage
- Run the application:
```bash
python main.py
```

- Don't forget to install  `tabulate` modul first:
```bash
pip install tabulate
```

---

## 🧾 Table View Example:

```
+------------+--------+---------+-------+---------------------+
| ID Mobil   | Merk   | Tipe    | Tahun | Harga Sewa / Hari   |
+------------+--------+---------+-------+---------------------+
| TM001      | Toyota | Avanza  | 2020  | Rp 350.000          |
+------------+--------+---------+-------+---------------------+
```

---

## Project Structure

```text
main.py          # File utama program
README.md        # Deskripsi ini
```

---

## CRUD Operations:

- Create: Add a new vehicle or customer, providing details like brand, type, name, or contact information.
- Read: Search for vehicles or customers by ID or name to view detailed information.
- Update: Modify existing entries, such as changing a car's daily rate or updating a customer’s address.
- Delete: Remove records after confirmation, ensuring safety of operational data.

---

## Data Model
This project uses structured Python dictionaries to store and manage car and customer data.

### Vehicles:
id_mobil: (String) - Unique ID for the vehicle
merk: (String) - Car brand
tipe: (String) - Car model/type
tahun: (Integer) - Manufacturing year
harga_per_hari: (Integer) - Rental price per day
status: (String) - Indicates availability
penyewa: (String/None) - ID of the current renter if applicable
tanggal_sewa: (String/Date) - Start date of rental
tanggal_kembali: (String/Date) - Return date
total_harga: (Integer) - Total cost calculated

### Customers:
id_pelanggan: (String) - Unique ID for the customer
nama: (String) - Full name
kelamin: (String) - Gender
alamat: (String) - Address

## Contributing
We welcome contributions to this project!
Feel free to:
Fork the repository and open a pull request
Submit an issue for bugs or suggestions
Contact me directly at: ridwandr.idn@gmail.com
Created by Ridwan Darmawan – Purwadhika Capstone Project
2025

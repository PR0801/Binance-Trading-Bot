# Binance Futures Testnet Trading Bot

A Python-based trading bot for **Binance USDT-M Futures Testnet** that supports MARKET and LIMIT orders through a clean CLI interface and optional UI dashboard.

This project was built as part of a technical assignment to demonstrate structured code design, API handling, logging, validation, and user-friendly interaction.

---

## 🚀 Features

* Place **MARKET** and **LIMIT** orders
* Supports **BUY** and **SELL**
* Works on **Binance Futures Testnet (USDT-M)**
* CLI input validation
* Structured modular code
* Logging of requests & responses
* Exception handling
* Menu-driven CLI dashboard
* Optional Streamlit UI dashboard
* Order history view
* Positions viewer
* Account balance display
* Clean formatted outputs

---

## 🗂 Project Structure

```
Binance-Trading-Bot/
│
├── bot/
│   ├── __init__.py
│   ├── client.py          # Binance client wrapper
│   ├── orders.py          # Order placement logic
│   ├── cli.py             # CLI entry point (required)
│   ├── validators.py      # Validate input
│   ├── logging_config.py  # Logging setup
│
├── app.py                  # Basic Streamlit UI
├── logs/
│   └── bot.log
└── runtime.txt             # Version used for running the streamlit app
├── .env
├── requirements.txt
└── README.md
```

---

## ⚙️ Setup Instructions

### 1. Clone repository

```bash
git clone <your_repo_link>
cd trading_bot
```

### 2. Create virtual environment (optional but recommended)

```bash
python -m venv venv
venv\Scripts\activate   # Windows
```

### 3. Install dependencies

```bash
pip install -r requirements.txt
```

---

## 🔐 Binance Testnet Setup

1. Go to Binance Futures Testnet
   [https://testnet.binancefuture.com](https://testnet.binancefuture.com)

2. Create API key & secret

3. Create `.env` file in root folder:

```
BINANCE_API_KEY=your_key
BINANCE_API_SECRET=your_secret
```

---

## ▶️ Running the CLI (Required)

```bash
python bot/cli.py
```

Menu:

```
1. Place Order
2. View Balance
3. View Positions
4. Order History
5. Exit
```

### Place Order example

```
Symbol: BTCUSDT
Side: BUY
Order Type: M (Market) or L (Limit)
Quantity: 0.003
```

---

## 🖥 Running the UI (Bonus)

```bash
streamlit run ui.py
```

Features:

* Account balance
* Place orders
* Positions
* Order history

---

## 🧾 Logging

Logs are saved in:

```
logs/bot.log
```

Includes:

* API requests
* Responses
* Errors

---

## 🧠 Design Approach

The project follows a layered architecture:

```
CLI/UI → Validation → Order Service → Binance Client → API
```

This ensures:

* Reusability
* Clean separation of concerns
* Easy debugging
* Maintainability

---

## 📌 Assumptions

* Uses Binance Futures **Testnet only**
* Default leverage set automatically
* Only USDT-M futures supported
* Spot trading not included (not required)

---

## 📊 Example CLI Output

```
--- Order Summary ---
Symbol: BTCUSDT
Side: BUY
Type: MARKET
Quantity: 0.003

✔ Order placed successfully
Order ID: 123456
Status: FILLED
Executed Qty: 0.003
```

---



  
## 👨‍💻 Author
Pratyush Raunak

---

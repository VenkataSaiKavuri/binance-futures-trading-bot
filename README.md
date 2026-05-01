# Binance Futures Trading Bot

## 📌 Overview

A CLI-based Python trading bot for Binance Futures Testnet that supports Market and Limit orders with logging, validation, and error handling.

---

## 🚀 Features

* Place MARKET and LIMIT orders
* Supports BUY and SELL
* CLI-based input
* Input validation
* Logging of API requests and responses
* Error handling

---

## ⚙️ Setup

```bash
git clone https://github.com/<your-username>/binance-futures-trading-bot.git
cd binance-futures-trading-bot
python -m venv venv
venv\Scripts\activate
pip install -r requirements.txt
```

---

## 🔐 Environment

Create `.env` file:

```
API_KEY=your_testnet_api_key
API_SECRET=your_testnet_api_secret
```

---

## ▶️ Usage

### Market Order

```bash
python -m bot.cli --symbol BTCUSDT --side BUY --type MARKET --quantity 0.001
```

### Limit Order

```bash
python -m bot.cli --symbol BTCUSDT --side SELL --type LIMIT --quantity 0.001 --price 60000
```

---

## 📁 Project Structure

```
bot/
client.py
orders.py
validators.py
logging_config.py
cli.py
```

---

## 🧪 Logs

Logs are stored in:

```
logs/bot.log
```

---

## ⚠️ Notes

* Uses Binance Futures Testnet
* Requires valid API keys
* Run CLI using `python -m bot.cli`

### Order Execution Debugging (Time: 10 mins)

* Fixed limit order price validation issue
* Understood market price constraints for BUY/SELL orders
* Successfully executed both MARKET and LIMIT orders

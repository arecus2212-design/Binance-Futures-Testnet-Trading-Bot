# Binance Futures Testnet Trading Bot

## Overview

This project is a Python-based trading interface that allows users to place orders on the Binance Futures Testnet (USDT-M).

The application is built using Streamlit and integrates with the Binance Futures API.

## Features

* Place Market, Limit, and Stop orders
* Real-time price retrieval
* USDT balance display
* Session-based order history
* Logging for debugging
* Error handling for invalid inputs and API failures

## Technologies Used

* Python
* Streamlit
* Binance API (python-binance)

## Installation

Install dependencies:
```bash
pip install streamlit python-binance
```
## Run the Application
```
streamlit run bot.py
```
## Usage

1. Enter Binance Futures Testnet API Key and Secret in the sidebar.
2. Select trading symbol.
3. Choose order type.
4. Enter quantity and price.
5. Click "Place Order".

## Logs

All trading activity and errors are logged in:
trading_bot.log

## Disclaimer
This application interacts with Binance Futures Testnet and is intended for testing purposes only.

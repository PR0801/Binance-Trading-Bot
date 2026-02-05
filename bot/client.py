import os
from dotenv import load_dotenv
from binance.client import Client
import streamlit as st
class BinanceClient:
    def __init__(self):
        load_dotenv()
        api_key = os.getenv("BINANCE_API_KEY")
        api_secret = os.getenv("BINANCE_API_SECRET")
        if not api_key and "BINANCE_API_KEY" in st.secrets:
            api_key = st.secrets["BINANCE_API_KEY"]
            api_secret = st.secrets["BINANCE_API_SECRET"]
        self.client = Client(api_key, api_secret)
        self.client.FUTURES_URL = "https://testnet.binancefuture.com/fapi"
    def get_client(self):
        return self.client

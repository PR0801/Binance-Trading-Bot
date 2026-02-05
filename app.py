# streamlit run d:/PROGRAMMING/Binance-Trading-Bot/app.py
from turtle import update
import streamlit as st
import pandas as pd
from bot.client import BinanceClient
from bot.orders import OrderService
import bot.logging_config
@st.cache_data(ttl=300)
def get_symbols():
    from bot.client import BinanceClient
    client = BinanceClient().get_client()

    info = client.futures_exchange_info()
    return sorted(
        s["symbol"]
        for s in info["symbols"]
        if s["quoteAsset"] == "USDT" and s["status"] == "TRADING"
    )
symbols = get_symbols()
st.set_page_config(
    page_title="Binance Futures Trading Bot",
    page_icon="🤖",
    layout="wide"
)
st.sidebar.title("BFT Bot") 
page = st.sidebar.radio(
    "Navigation",
    [
        "Account Balance",
        "Place Order",
        "Positions",
        "Order History",
    ]
)
client = BinanceClient().get_client()
service = OrderService(client)
st.title("Dashboard")
if page == "Account Balance":
    st.subheader("Account Balance")
    try:
        balances = client.futures_account_balance()
        df = pd.DataFrame(balances)
        df["balance"] = df["balance"].astype(float)
        df["availableBalance"] = df["availableBalance"].astype(float)
        df = df[df["balance"] > 0]
        df = df.sort_values("balance", ascending=False)
        df = df.reset_index(drop=True)
        df.insert(0, "No.", range(1, len(df) + 1))
        df = df.rename(columns={
            "asset": "Asset",
            "balance": "Balance",
            "availableBalance": "Available Balance"
        })
        df = df[["No.", "Asset", "Balance", "Available Balance"]]
        st.dataframe(df, use_container_width=True, hide_index=True)
        total_balance = df["Balance"].sum()
        st.markdown("---")
        st.metric(
            "Total Value",
            f"{total_balance:,.2f} $"
        )
    except Exception as e:
        st.error(f"Balance fetch error: {str(e)}")
elif page == "Place Order":
    st.subheader("Place Order")
    col1, col2, col3 = st.columns(3)
    with col1:
       symbol = st.selectbox(
           "Symbol",
           symbols,
           index=symbols.index("BTCUSDT") if "BTCUSDT" in symbols else 0,
           )
    with col2:
        side = st.selectbox("Side",["BUY","SELL"])
    with col3:
        order_type = st.selectbox("Order Type",["MARKET","LIMIT"])
    col4, col5 = st.columns(2)
    with col4:
        quantity = st.number_input(
            "Quantity", min_value=0.001, value=0.003
        )
    with col5:
        price = None
        if order_type == "LIMIT":
            price = st.number_input(
                "Price", value=75000.0, step=100.0
            )
    if st.button("Place Order", use_container_width=True):
        try:
            with st.spinner("Placing order....."):
                result = service.place_order(
                    symbol=symbol,
                    side=side,
                    order_type=order_type,
                    quantity=quantity,
                    price=price
                )
            st.success("Order placed successfully")
            st.json(result)
        except Exception as e:
            st.error(str(e))
elif page == "Positions":
    st.subheader("Open Positions")
    positions = client.futures_position_information()
    df = pd.DataFrame(positions)
    df = df[df["positionAmt"].astype(float) != 0]
    if df.empty:
        st.info("No open positions")
    else:
        wanted_cols = [
            "symbol",
            "positionAmt",
            "entryPrice",
            "unRealizedProfit",
            "leverage",
        ]
        existing_cols = [c for c in wanted_cols if c in df.columns]
        df = df[existing_cols]
        st.dataframe(df, use_container_width=True, hide_index=True)
elif page == "Order History":
    st.subheader("Order History")
    symbol_options = ["ALL"] + symbols
    selected_symbol = st.selectbox(
        "Select Symbol",
        symbol_options
    )
    try:
        all_orders = []
        if selected_symbol == "ALL":
            common_symbols = [
                "BTCUSDT",
                "ETHUSDT",
                "BNBUSDT",
                "SOLUSDT",
            ]
            for sym in common_symbols:
                orders = client.futures_get_all_orders(
                    symbol=sym,
                    limit=50
                )
                all_orders.extend(orders)
        else:
            all_orders = client.futures_get_all_orders(
                symbol=selected_symbol,
                limit=50
            )
        df = pd.DataFrame(all_orders)
        if df.empty:
            st.warning("No orders found yet. Place an order first.")
        else:
            if "updateTime" in df.columns:
                df["Time"] = pd.to_datetime(df["updateTime"], unit="ms")
            wanted_cols = [
                "symbol",
                "side",
                "type",
                "status",
                "price",
                "executedQty",
                "avgPrice",
                "Time",
            ]
            cols = [c for c in wanted_cols if c in df.columns]
            df = df[cols]
            st.dataframe(df, use_container_width=True, hide_index=True)
    except Exception as e:
        st.error(str(e))
st.markdown("---")
st.caption("Built with Python • Binance Futures Testnet • Streamlit")
st.caption("© 2026 Binance Trading Bot by Pratyush Raunak")

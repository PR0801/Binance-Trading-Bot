import logging
import time
from binance.exceptions import BinanceAPIException
class OrderService:
    def __init__(self, client):
        self.client = client
    def set_leverage(self, symbol, leverage=10):
        try:
            self.client.futures_change_leverage(symbol=symbol, leverage=leverage)
        except:
            pass
    def place_order(self, symbol, side, order_type, quantity, price=None):
        try:
            self.set_leverage(symbol)
            params = {
                "symbol": symbol,
                "side": side,
                "type": order_type,
                "quantity": quantity,
            }
            if order_type == "LIMIT":
                params["price"] = price
                params["timeInForce"] = "GTC"
            logging.info(f"Placing order: {params}")
            order = self.client.futures_create_order(**params)
            order_id = order["orderId"]
            time.sleep(2)
            final = self.client.futures_get_order(
                symbol=symbol,
                orderId=order_id
            )
            logging.info(f"Final order: {final}")
            return {
                "orderId": final["orderId"],
                "status": final["status"],
                "executedQty": final["executedQty"],
                "avgPrice": final.get("avgPrice"),
            }
        except BinanceAPIException as e:
            logging.error(e)
            raise Exception(e.message)
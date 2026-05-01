import argparse
from datetime import datetime
from binance.exceptions import BinanceAPIException

from bot.client import get_client
from bot.orders import place_order
from bot.validators import validate_side, validate_order_type, validate_price
from bot.logging_config import setup_logger


def main():
    setup_logger()

    parser = argparse.ArgumentParser(description="Binance Futures Trading Bot")

    parser.add_argument("--symbol", required=True)
    parser.add_argument("--side", required=True)
    parser.add_argument("--type", required=True)
    parser.add_argument("--quantity", type=float, required=True)
    parser.add_argument("--price", type=float)

    args = parser.parse_args()

    # Normalize input
    args.side = args.side.upper()
    args.type = args.type.upper()
    args.symbol = args.symbol.upper()

    try:
        validate_side(args.side)
        validate_order_type(args.type)
        validate_price(args.type, args.price)

        client = get_client()

        print("=" * 40)
        print("📌 Order Request Summary")
        print(f"Symbol      : {args.symbol}")
        print(f"Side        : {args.side}")
        print(f"Type        : {args.type}")
        print(f"Quantity    : {args.quantity}")
        print(f"Price       : {args.price if args.price else 'N/A'}")
        print(f"Time        : {datetime.now()}")
        print("=" * 40)

        order = place_order(
            client,
            args.symbol,
            args.side,
            args.type,
            args.quantity,
            args.price
        )

        print("\n✅ Order Successful!")
        print(f"Order ID    : {order.get('orderId')}")
        print(f"Status      : {order.get('status')}")
        print(f"ExecutedQty : {order.get('executedQty')}")
        print(f"Avg Price   : {order.get('avgPrice', 'N/A')}")
        print("=" * 40)

    except ValueError as ve:
        print("\n❌ Validation Error:", str(ve))

    except BinanceAPIException as be:
        print("\n❌ Binance API Error:", be.message)

    except Exception as e:
        print("\n❌ Unexpected Error:", str(e))


if __name__ == "__main__":
    main()
import argparse
from bot.validators import validate_side, validate_order_type, validate_price

def main():
    parser = argparse.ArgumentParser(description="Binance Futures Trading Bot")

    parser.add_argument("--symbol", required=True, help="Trading pair (e.g., BTCUSDT)")
    parser.add_argument("--side", required=True, help="BUY or SELL")
    parser.add_argument("--type", required=True, help="MARKET or LIMIT")
    parser.add_argument("--quantity", type=float, required=True, help="Order quantity")
    parser.add_argument("--price", type=float, help="Required for LIMIT orders")

    args = parser.parse_args()

    try:
        # Validation
        validate_side(args.side)
        validate_order_type(args.type)
        validate_price(args.type, args.price)

        print("\n📌 Order Request Summary")
        print(f"Symbol   : {args.symbol}")
        print(f"Side     : {args.side}")
        print(f"Type     : {args.type}")
        print(f"Quantity : {args.quantity}")
        print(f"Price    : {args.price if args.price else 'N/A'}")

        print("\n✅ Input validated successfully")

    except Exception as e:
        print("\n❌ Validation Error:", str(e))


if __name__ == "__main__":
    main()
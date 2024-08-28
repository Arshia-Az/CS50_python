def main():
    out_put = payment_coke()
    out_put = out_put.replace("\n", "")
    return out_put


# get coin from input and calculate
def payment_coke():
    coin = 0
    amount_due = 50

    while True:
        if amount_due > 0:
            print(f"Amount Due: {amount_due}")
            coin = int(input("Insert Coin: "))
            if coin == 5 or coin == 10 or coin == 25:
                amount_due -= coin
        else:
            change_owed = str(amount_due).replace("-", "")
            return f"Change Owed: {change_owed}"

if __name__ == "__main__":
    print(main())

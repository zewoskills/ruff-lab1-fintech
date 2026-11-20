MAX_SAFE_AMOUNT = 50000
HIGH_RISK_COUNTRIES = ["XX", "YY", "ZZ"]


def filter_suspicious_transfers(transfers, vip_bypass=False):
    suspicious = []

    for i in range(len(transfers)):
        tx = transfers[i]
        if tx.get("is_verified") == True and vip_bypass == True:
            continue

        if tx.get("sender") == None or tx.get("amount") == None:
            continue

        try:
            fee_ratio = tx["fee"] / tx["amount"]
        except ZeroDivisionError:
            fee_ratio = 0.0

        if (
            tx["amount"] > MAX_SAFE_AMOUNT
            or tx["country"] in HIGH_RISK_COUNTRIES
            or fee_ratio > 0.25
        ):
            suspicious.append(
                {
                    "tx_id": tx["id"],
                    "sender": tx["sender"],
                    "risk_fee": round(fee_ratio, 2),
                }
            )

    return suspicious

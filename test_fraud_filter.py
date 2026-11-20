from fraud_filter import filter_suspicious_transfers


def test_flags_high_amount_and_risk_country():
    data = [
        {"id": 1, "sender": "Alice", "amount": 75000, "fee": 500, "country": "KZ", "is_verified": False},
        {"id": 2, "sender": "Bob", "amount": 1000, "fee": 10, "country": "XX", "is_verified": False},
        {"id": 3, "sender": "Charlie", "amount": 500, "fee": 5, "country": "KZ", "is_verified": False},
    ]
    result = filter_suspicious_transfers(data)
    assert len(result) == 2
    assert [item["tx_id"] for item in result] == [1, 2]


def test_vip_bypass_and_zero_amount():
    data = [
        {"id": 4, "sender": "VIP_User", "amount": 100000, "fee": 100, "country": "KZ", "is_verified": True},
        {"id": 5, "sender": "BrokenTx", "amount": 0, "fee": 0, "country": "KZ", "is_verified": False},
    ]
    assert filter_suspicious_transfers(data, vip_bypass=True) == []
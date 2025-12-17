def wallet_history():
    return [
        {"action": "swap", "value": 120, "time_delta": 300},
        {"action": "stake", "value": 200, "time_delta": 600},
        {"action": "swap", "value": 90, "time_delta": 200},
        {"action": "stake", "value": 250, "time_delta": 500},
    ]

def new_behavior():
    return [
        {"action": "nft_mint", "value": 5, "time_delta": 50},
        {"action": "nft_mint", "value": 6, "time_delta": 40},
    ]

from fastapi import FastAPI
app = FastAPI()

@app.get('/')
def home():
    return {"Alphabank API Version: 0.1"}

@app.get('/accounts')
def get_account():
    return {'''{
                "accounts": [
                    {
                    "account_id": "blgvvBlXw3cq5GMPwqB6s6q4dLKB9WcVqGDGo",
                    "balances": {
                        "available": 100,
                        "current": 110,
                        "iso_currency_code": "USD",
                        "limit": null,
                        "unofficial_currency_code": null
                    },
                    "mask": "0000",
                    "name": "Plaid Checking",
                    "official_name": "Plaid Gold Standard 0% Interest Checking",
                    "subtype": "checking",
                    "type": "depository"
                    },
                    {
                    "account_id": "6PdjjRP6LmugpBy5NgQvUqpRXMWxzktg3rwrk",
                    "balances": {
                        "available": null,
                        "current": 23631.9805,
                        "iso_currency_code": "USD",
                        "limit": null,
                        "unofficial_currency_code": null
                    },
                    "mask": "6666",
                    "name": "Plaid 401k",
                    "official_name": null,
                    "subtype": "401k",
                    "type": "investment"
                    },
                    {
                    "account_id": "XMBvvyMGQ1UoLbKByoMqH3nXMj84ALSdE5B58",
                    "balances": {
                        "available": null,
                        "current": 65262,
                        "iso_currency_code": "USD",
                        "limit": null,
                        "unofficial_currency_code": null
                    },
                    "mask": "7777",
                    "name": "Plaid Student Loan",
                    "official_name": null,
                    "subtype": "student",
                    "type": "loan"
                    }
                ],
                "item": {
                    "available_products": [
                    "balance",
                    "identity",
                    "payment_initiation",
                    "transactions"
                    ],
                    "billed_products": [
                    "assets",
                    "auth"
                    ],
                    "consent_expiration_time": null,
                    "error": null,
                    "institution_id": "ins_117650",
                    "item_id": "DWVAAPWq4RHGlEaNyGKRTAnPLaEmo8Cvq7na6",
                    "update_type": "background",
                    "webhook": "https://www.genericwebhookurl.com/webhook"
                },
                "request_id": "bkVE1BHWMAZ9Rnr"'''}

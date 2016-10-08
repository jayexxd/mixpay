from paypalrestsdk import BillingPlan
import logging, random, os
from pprint import pprint
os.environ['PAYPAL_MODE'] = "sandbox"
os.environ['PAYPAL_CLIENT_ID'] = "ASUu0Pp7oePCdm2iVehU3ekpnwVaXdvWyPp1wIJ-6jqbgqIrr6dpvpbQawJwVfUvGJd4dpzGaKWR3YWa"
os.environ['PAYPAL_CLIENT_SECRET'] = "EDKkKGae9m4RE6gD8f32Z2V7HgyUcDk__pi6QHq2dPiAbeFy7KZ_RtvW8mwduOENWmUXsiacwNwkqhNg"

logging.basicConfig(level=logging.INFO)

billing_plan = BillingPlan({
    "description": "Create Plan for Regular",
    "merchant_preferences": {
        "auto_bill_amount": "yes",
        "cancel_url": "http://www.cancel.com",
        "initial_fail_amount_action": "continue",
        "max_fail_attempts": "1",
        "return_url": "http://www.success.com",
        "setup_fee": {
            "currency": "USD",
            "value": "25"
        }
    },
    "name": "Testing1-Regular1",
    "payment_definitions": [
        {
            "amount": {
                "currency": "USD",
                "value": "519"
            },
            "charge_models": [
                {
                    "amount": {
                        "currency": "USD",
                        "value": "13.60"
                    },
                    "type": "SHIPPING"
                },
                {
                    "amount": {
                        "currency": "USD",
                        "value": "12.20"
                    },
                    "type": "TAX"
                }
            ],
            "cycles": "0",
            "frequency": "SECOND",
            "frequency_interval": "5",
            "name": "Regular 1",
            "type": "REGULAR"
        }
    ],
    "type": "INFINITE"
})

if billing_plan.create():
    print("Billing Plan [%s] created successfully" % (billing_plan.id))
else:
    print(billing_plan.error)

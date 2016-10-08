from paypalrestsdk import Payout, ResourceNotFound
import random
import string

def mixpay_payout():
    sender_batch_id = ''.join(
        random.choice(string.ascii_uppercase) for i in range(12))

    payout = Payout({
        "sender_batch_header": {
            "sender_batch_id": sender_batch_id,
            "email_subject": "You have a payment"
        },
        "items": [
            {
                "recipient_type": "EMAIL",
                "amount": {
                    "value": 1.50,
                    "currency": "USD"
                },
                "receiver": "mixpay-employee-1@gmail.com",
                "note": "Thank you.",
                "sender_item_id": "item_1"
            },
            {
                "recipient_type": "EMAIL",
                "amount": {
                    "value": 2.50,
                    "currency": "USD"
                },
                "receiver": "mixpay-employee-2@gmail.com",
                "note": "Thank you.",
                "sender_item_id": "item_2"
            },
            {
                "recipient_type": "EMAIL",
                "amount": {
                    "value": 3.50,
                    "currency": "USD"
                },
                "receiver": "mixpay-employee-3@gmail.com",
                "note": "Thank you.",
                "sender_item_id": "item_3"
            }
        ]
    })

    if payout.create():
        print("payout[%s] created successfully" % (payout.batch_header.payout_batch_id))
    else:
        print(payout.error)

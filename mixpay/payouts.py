from paypalrestsdk import Payout, ResourceNotFound
import random
import string

def mixpay_payout(payment_list):
    
    sender_batch_id = ''.join(
        random.choice(string.ascii_uppercase) for i in range(12))
    items = []
    for i, payment in enumerate(payment_list):
        items.append({
            "recipient_type": "EMAIL",
            "amount": {
                "value": payment["amount"],
                "currency": "SGD"
            },
            "receiver": payment["email"],
            "note": payment["note"],
            "sender_item_id": "item_%d" %i,
        })        
    payout = Payout({
        "sender_batch_header": {
            "sender_batch_id": sender_batch_id,
            "email_subject": "You have a payment"
        },
        "items" : items
    })

    if payout.create():
        print("payout[%s] created successfully" % (payout.batch_header.payout_batch_id))
    else:
        print(payout.error)

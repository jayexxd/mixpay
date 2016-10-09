from paypalrestsdk import Payout, ResourceNotFound
import random, os, string, time

os.environ['PAYPAL_MODE'] = "sandbox"
os.environ['PAYPAL_CLIENT_ID'] = "ASUu0Pp7oePCdm2iVehU3ekpnwVaXdvWyPp1wIJ-6jqbgqIrr6dpvpbQawJwVfUvGJd4dpzGaKWR3YWa"
os.environ['PAYPAL_CLIENT_SECRET'] = "EDKkKGae9m4RE6gD8f32Z2V7HgyUcDk__pi6QHq2dPiAbeFy7KZ_RtvW8mwduOENWmUXsiacwNwkqhNg"


block = 5000
chg = [0.35, 0.15, 0.40, 0.10]
for i, val in enumerate(chg):
    chg[i] *= block
note = "Your income, delivered by MixPay."
payment_list = [{"email" : "mixpay-employee-1@gmail.com", "amount" : "%d" % chg[0]  , "note" : note}, {"email" : "mixpay-employee-2@gmail.com", "amount" : "%d" % chg[1]  , "note" : note}, {"email" : "mixpay-employee-3@gmail.com", "amount" : "%d" % chg[2]  , "note" : note}, {"email" : "mixpay-employee-4@gmail.com", "amount" : "%d" % chg[3]  , "note" : note} ]
#print payment_list
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
            "email_subject": "You have a payment, powered by MixPay"
        },
        "items" : items
    })

    if payout.create():
        print("payout[%s] created successfully" % (payout.batch_header.payout_batch_id))
        for payment in payment_list:
            print "    Paid out %d to %s" % (int(payment["amount"]), payment["email"])
        print "    TOTAL: %d\n\n" % block
    else:
        print(payout.error)

while 1:
    mixpay_payout(payment_list)
    time.sleep(10)

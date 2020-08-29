import stripe

SECRET_KEY = "sk_test_4eC39HqLyjWDarjtT1zdp7dc"

stripe.api_key=SECRET_KEY

def generate_card_token(cardnumber,expmonth,expyear,cvv):
    data= stripe.Token.create(
            card={
                "number": str(cardnumber),
                "exp_month": int(expmonth),
                "exp_year": int(expyear),
                "cvc": str(cvv),
            })
    card_token = data['id']

    return card_token


def create_payment_charge(tokenid,amount):

    payment = stripe.Charge.create(
                amount= int(amount)*100,                  # convert amount to cents
                currency='usd',
                description='Example charge',
                source=tokenid,
                )

    payment_check = payment['paid']    # return True for payment

    return payment_check
     
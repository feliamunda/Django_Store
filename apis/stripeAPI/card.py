from . import stripe

def create_card(user, token):
    source = stripe.Customer.create_source(
        user.customer_id,
        source=token
    )
    return source

def delete_card(user, billing_profile):
    card = stripe.Customer.delete_source(
        user.customer_id,
        billing_profile.card_id
    )
    return card
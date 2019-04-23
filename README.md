# Affirm Python SDK

Affirm Python SDK is a client library to interact with [Affirm](https://www.affirm.com/). 


# Usage
## Client Creation

    from affirm import Client
    client = Client(auth=(<PUBLIC_API_KEY>, <PRIVATE_API_KEY>))

## Performing Authorize

    from affirm import Client
    client = Client(auth=(<PUBLIC_API_KEY>, <PRIVATE_API_KEY>))
    resp = client.charge.create(data={"checkout_token":<CHECKOUT_TOKEN_FROM_AFFIRM>, "order_id": <YOUR_GENERATED_ORDER_ID>)

## Performing Capture

    from affirm import Client
    client = Client(auth=(<PUBLIC_API_KEY>, <PRIVATE_API_KEY>))
    resp = client.charge.capture(charge_id = <CHARGE_ID>, order_id=<YOUR_GENERATED_ORDER_ID>)
    
## Performing Refund

    from affirm import Client
    client = Client(auth=(<PUBLIC_API_KEY>, <PRIVATE_API_KEY>))
    resp = client.charge.capture(charge_id = <CHARGE_ID>, order_id= <YOUR_GENERATED_ORDER_ID>)

## Perform Update

    from affirm import Client
    client = Client(auth=(<PUBLIC_API_KEY>, <PRIVATE_API_KEY>))
    resp = client.charge.update(charge_id = <CHARGE_ID>, order_id": <YOUR_GENERATED_ORDER_ID>)

## Perform Void

    from affirm import Client
    client = Client(auth=(<PUBLIC_API_KEY>, <PRIVATE_API_KEY>))
    resp = client.charge.void(charge_id=<CHARGE_ID>, order_id=<YOUR_GENERATED_ORDER_ID>)
    
If you have any questions please shoot a mail to anshul[dot]jmi[at]gmail[dot]com.

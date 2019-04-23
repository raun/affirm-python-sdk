# Affirm Python SDK

Affirm Python SDK is a client library to interact with [Affirm](https://www.affirm.com/). For API reference: https://docs.affirm.com/Integrate_Affirm/Direct_API/Affirm_API_Reference

Affirm helps customers to pay over time for things they want to buy. The customers are in control of how long you get to make monthly payments. They do the approval process in minutes. This client will help you integrate with Affirm.


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

## Using the client for Production(or live)
The only change you need to make pass a `prod` keyward while to client creation step.

    from affirm import Client
    client = Client(auth=(<PUBLIC_API_KEY>, <PRIVATE_API_KEY>), prod=True)

    
If you have any questions please shoot a mail to anshul[dot]jmi[at]gmail[dot]com.

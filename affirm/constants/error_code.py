class ERROR_CODE(object):
    AUTH_DECLINE = "auth-declined"  # Charge authorization hold declined.
    REQUESTING_HIGHER_CAPTURE = "capture-greater-instrument"  # Cannot capture charges on this instrument for more than the authorization hold amount.
    CAPTURE_UNEQUAL_AMOUNT = "capture-unequal-instrument"  # Cannot capture charges on this instrument for an amount unequal to the authorization hold amount.
    CAPTURE_VOIDED = "capture-voided"  # Cannot capture voided charge.
    PARTIAL_CAPTURE = "partial-capture-instrument"  # Cannot partially capture charges on this instrument.
    REQUESTING_HIGHER_REFUND = "refund-exceeded"  # Exceeded maximum refund.
    REQUESTING_UNCAPTURED_REFUND = "refund-uncaptured"  # Cannot refund a charge that hasn't been captured.
    REQUESTING_VOIDED_REFUND = "refund-voided"  # Cannot refund a voided charge.
    CAPTURE_DECLINE = "capture-declined"  # Charge capture declined.
    EXCEEDED_CAPTURE_AMOUNT = "capture-limit-exceeded"  # Exceed maximum capture amount on charge.
    EXPIRED_AUTHORIZATION = "expired-authorization"  # Cannot capture a charge with an expired authorization hold.
    EXPIRED_REFUND = "refund-expired"  # Charges on this instrument must be refunded within N days of capture.
    INVALID_FIELD = "invalid_field"  # An input field resulted in invalid request.
    UNSPECIFIED_PUBLIC_KEY = "public-api-key-not-specified"  # Please provide a public API key.
    INVALID_PUBLIC_KEY = "public-api-key-invalid"  # Please provide a valid public API key.
    PUBLIC_KEY_ENVIRONMENT_MISMATCH = "public-api-key-wrong-environment"  # Please provide a live public API key when not using the sandbox environment.
    INACTIVE_PUBLIC_KEY = "public-api-key-inactive"  # Please provide an active public API key.
    BOTH_KEY_NOT_PROVIDED = "api-key-pair-not-specified"  # Please provide an API key pair.
    INVALID_PRIVATE_KEY = "private-api-key-invalid"  # Please provide a valid private API key.
    KEY_PAIR_ENVIRONMENT_MISMATCH = "api-key-pair-wrong-environment"  # Please provide a live API key pair when not using the sandbox environment.
    INACTIVE_KEY_PAIR = "api-key-pair-inactive"  # Please provide an active API key pair.
    NOT_FOUND = "not_found"  # Could not find the resource(s) specified in the request.

    BAD_REQUEST_CODES = (CAPTURE_VOIDED, )
    AMOUNT_MISMATCH_CODES = (REQUESTING_HIGHER_CAPTURE, CAPTURE_UNEQUAL_AMOUNT, REQUESTING_HIGHER_REFUND,
                             EXCEEDED_CAPTURE_AMOUNT, PARTIAL_CAPTURE, )
    BAD_AUTH_CRED_CODE = ()

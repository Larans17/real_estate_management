# API RESPONSE MESSAGES
USER_ALREADY_EXISTS = 'Email already exists'
CODE = 'authorization'
VALIDATION_MSG = 'Must include "username" and "password"'
INVALID_ACCOUNT = "This account is invalid."
LOGIN_VERIFIED = "Logged-in successfully"
INVALID_EMAIL = "Email is incorrect"
INVALID_PASSWORD = "Password is incorrect"



class CommonApiMessages:

    @staticmethod

    def create(msg):
        message = f"{msg} created successfully"
        return message
    
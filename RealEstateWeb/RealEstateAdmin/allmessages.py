from django.utils import timezone
from datetime import datetime

LOGIN_VALIDATION = 'Email and password is incorrect..!'
LOGIN_FAILED = 'Failed to login'
LOGOUT = 'Logged out successfully'
ERROR_MSG = 'Something went wrong'

getCurrentDate = timezone.now()
getCurrentDateTime = datetime.now()


class RealEstateMessages:

    @staticmethod

    def create (msg):
        message = f"{msg} created successfully"
        return message
    
    def update (msg):
        message = f"{msg} updated successfully"
        return message
    
    def delete (msg):
        message = f"{msg} deleted successfully"
        return message
    
    def status (msg):
        message = f"{msg} status updated successfully"
        return message
    
    def sync (msg):
        message = f"{msg} sync successfully finished"
        return message
    
    def Signup(msg):
        message = f"{msg} registered successfully"
        return message
    
    def Otp(msg):
        message = f"{msg} registered successfully"
        return message
    
    def login():
        message = "Logged in successfully"
        return message
    
    def logout():
        message = "Logout successfully"
        return message
    
    def artist(msg):
        message = f" Not {msg} in this event"
        return message

    def submit(msg):
        message = f"{msg} submitted successfully"
        return message
    
    def save(msg):
        message = f"{msg} saved successfully"
        return message
    
    def event_status(msg):
        message = f"Event {msg} successfully"
        return message
    
    def duplicate(msg):
        message = f"{msg} duplicated successfully"
        return message
    
    def status_update_failed(msg):
        message = f"Failed to {msg}"
        return message
    
    def remove(msg):
        message = f"{msg} removed successfully"
        return message
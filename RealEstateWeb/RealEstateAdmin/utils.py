from django.utils.timezone import localtime
from datetime import datetime, timezone
from django.conf import settings
import traceback

url = settings.API_URL
dt = datetime.now(timezone.utc)
dt = localtime(dt)

class RealEstateResponse:
   
    @staticmethod
    def Response_errorhandler(Transactionname, error, request):
        import socket
        user_id = request.session['UserId']
        Ip = request.META['REMOTE_ADDR']
        
        HOSTNAME = socket.gethostname()
        dt = datetime.now(timezone.utc)
        dt = localtime(dt)
        msg={'error':str(error),'traceback':traceback.format_exc()}
        data = {"TransactionName": Transactionname, "Mode": "Web-site",
                "LogDate": dt, "LogMessage": str(msg), "Ip_address": Ip,
                'userId': user_id, 'SystemName': HOSTNAME}
       
        # requests.post('{url}/common/log/'.format(url=url), data=data).json()
        if error=="Unauthorized access":
            access_error = True
        else:
            access_error = False    
        # return render(request,'error.html',context={"error":error,"access_error":access_error})
    
    
    
    @staticmethod
    def Token_Authentication(request):
        
        try:
            Token = request.session['Token']
            headers = {'Authorization': 'Token {Token}'.format(Token=Token)}
            return headers
        except KeyError:
            headers = None
            
            

        

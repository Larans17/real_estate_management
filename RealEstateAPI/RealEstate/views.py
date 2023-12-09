from rest_framework import status
from rest_framework.views import APIView
from rest_framework.response import Response
from RealEstate.serializer import *
from RealEstate.bulk_creation import *

# KNOX TOKEN
from knox.auth import AuthToken
from knox.auth import TokenAuthentication
from rest_framework.permissions import IsAuthenticated


# CUSTOM METHODS
from RealEstate.utils import *
from datetime import datetime


# LOGIN FUNCTION ::
class LoginAPI(APIView):
    """
        Summary or Description of the Function:
            * Log-in SuperAdmin.
    """
    def post(self, request, *args, **kwargs):      
        try:
            serializer_class = LoginSerializer(data=request.data, context={'request': request})
            if serializer_class.is_valid():
                # call_bulk_creation()
                data = doAdminLogin(serializer_class, request)
                return Response(data,status.HTTP_200_OK)
            else:
                return RealEstateAPIResponse.serializer_error(self.__class__.__name__, request, serializer_class)
            
        except Exception as e:
            return RealEstateAPIResponse.exception_error(self.__class__.__name__, request, e)

def doAdminLogin(serializer_class, request):
    user = serializer_class.validated_data['user']
    token = AuthToken.objects.create(user)[1]
    user_data = getObject(User,{'user_name':user})
    if user_data.is_super_admin:
        data={  
            'user_id':user_data.id,
            'is_super_admin':user_data.is_super_admin,
            'emailId':user_data.email,
            'user_name':user_data.user_name,
            "message": LOGIN_VERIFIED,
            "Token": token,
        }
    
    return data

# def call_bulk_creation():
#     if Units.objects.all().exists == False:
#         units_creation()
#     return True



class PostPropertyAPI(APIView):
    # authentication_classes = [TokenAuthentication]
    # permission_classes = [IsAuthenticated]

    def get(self,request):
        """
        Summary or Description of the function:
        Get all property data from database.

        """
        try:
            query_set = Property.objects.all()
            serializer_class =PostPropertySerializer(query_set,many=True)
            return Response(serializer_class.data,status=status.HTTP_200_OK)
        except Exception as e:
            RealEstateAPIResponse.exception_error(self.__class__.__name__,request,e)


    def post(self,request):
        """
        Summary or Description of the function:
        Post property data to database.

        """ 
        try:
            print(request.data)
            serializer_class = PostPropertySerializer(data=request.data,context={'request':request})
            if serializer_class.is_valid():
                serializer_class.save()
                response = serializer_class.data
                response['status']=status.HTTP_201_CREATED
                response['message']=CommonApiMessages.create('Property')
                return Response(response,status=status.HTTP_201_CREATED)
            else:
                return Response(serializer_class.errors,status=status.HTTP_400_BAD_REQUEST)
            
        except Exception as e:
            RealEstateAPIResponse.exception_error(self.__class__.__name__,request,e)


# class GetAndPPropertyAPI(APIView):
#     # authentication_classes = [TokenAuthentication]
#     # permission_classes = [IsAuthenticated]

#     def get(self,request):
#         """
#         Summary or Description of the function:
#         Get all property data from database.

#         """
#         try:
#             query_set = Property.objects.all()
#             serializer_class =PostPropertySerializer(query_set,many=True)
#             return Response(serializer_class.data,status=status.HTTP_200_OK)
#         except Exception as e:
#             RealEstateAPIResponse.exception_error(self.__class__.__name__,request,e)



class PostUnitsAPI(APIView):
    authentication_classes = [TokenAuthentication]
    permission_classes = [IsAuthenticated]


    def post(self,request):
        """
        Summary or Description of the function:
            Post units data to database.

        """ 
        try:
            serializer_class = PostUnitsSerializer(data=request.data,context={'request':request})
            if serializer_class.is_valid():
                serializer_class.save()
                response = serializer_class.data
                response['status']=status.HTTP_201_CREATED
                response['message']=CommonApiMessages.create('Unit')
                return Response(response,status=status.HTTP_201_CREATED)
            else:
                return Response(serializer_class.errors,status=status.HTTP_400_BAD_REQUEST)
        except Exception as e:
            RealEstateAPIResponse.exception_error(self.__class__.__name__,request,e)

    def get(self,request):
        """
        Summary or Description of the function:
        Get all units data from database.

        """
        try:
            query_set = Units.objects.all()
            serializer_class =GetUnitsSerializer(query_set,many=True)
            return Response(serializer_class.data,status=status.HTTP_200_OK)
        except Exception as e:
            RealEstateAPIResponse.exception_error(self.__class__.__name__,request,e)


class PostTenantAPI(APIView):
    authentication_classes = [TokenAuthentication]
    permission_classes = [IsAuthenticated]


    def post(self,request):
        """
        Summary or Description of the function:
            Post tenant data to database.

        """ 
        try:
            data = request.data.copy()
            data['agreement_end_date']=date_format(data.get('agreement_end_date'))
            data['monthly_rent_date']=date_format(data.get('monthly_rent_date'))
            serializer_class = PostTenantSerializer(data=data,context={'request':request})
            if serializer_class.is_valid():
                serializer_class.save()
                response = serializer_class.data
                response['status']=status.HTTP_201_CREATED
                response['message']=CommonApiMessages.create('Tenant')
                return Response(response,status=status.HTTP_201_CREATED)
            else:
                return Response(serializer_class.errors,status=status.HTTP_400_BAD_REQUEST)
        except Exception as e:
            RealEstateAPIResponse.exception_error(self.__class__.__name__,request,e)


    def get(self,request):
        """
        Summary or Description of the function:
        Get all tenant data from database.

        """
        try:
            query_set = Tenant.objects.all()
            serializer_class = GetTenantSerializer(query_set,many=True,context={'request':request})
            return Response(serializer_class.data,status=status.HTTP_200_OK)
        except Exception as e:
            RealEstateAPIResponse.exception_error(self.__class__.__name__,request,e)


def date_format(input_date):
    # Convert to 'YYYY-MM-DD' format
    try:
        date_obj = datetime.strptime(input_date.strip(), "%d/%m/%Y")
        formatted_date = date_obj.strftime("%Y-%m-%d")
        return formatted_date
    except ValueError:
        print("Invalid date format")

#DJANGO DEFAULT PACKAGE IMPORT
from RealEstate.models import *
from django.contrib.auth.hashers import check_password
from rest_framework import serializers
from RealEstate.api_response_message import *
from RealEstate.utils import *



class LoginSerializer(serializers.ModelSerializer):
    email = serializers.EmailField()
    password = serializers.CharField(
        label=("password"),
        style={'input_type': 'password'},
        trim_whitespace=False,
        max_length=125,
        write_only=True
    )

    class Meta:
        model = User
        fields = ['id', 'email', 'password']


    def validate(self, data):
        Email = data.get('email')
        Password = data.get('password')
        if Email and Password:
            user = getAllObjectWithFilter(User,{'email':Email}).first()
            
            if user is None:
                raise serializers.ValidationError({'Email':INVALID_EMAIL}, CODE)
            
            if not check_password(Password, user.password):
                raise serializers.ValidationError({'Password':INVALID_PASSWORD}, CODE)
        else:
            raise serializers.ValidationError(VALIDATION_MSG, CODE)

        data['user'] = user
        return data
    


class PostPropertySerializer(serializers.ModelSerializer):
    class Meta:
        model = Property
        fields = '__all__'

class PostUnitsSerializer(serializers.ModelSerializer):
    class Meta:
        model = Units
        fields = '__all__'

class GetUnitsSerializer(serializers.ModelSerializer):
    property_name = serializers.StringRelatedField(source='property.name')
    class Meta:
        model = Units
        fields = ['unitid','property','rent_cost','unit_type','property_name']

class PostTenantSerializer(serializers.ModelSerializer):
    class Meta:
        model = Tenant
        fields = '__all__'

class GetTenantSerializer(serializers.ModelSerializer):
    agreement_end_date = serializers.DateField(format="%d/%m/%Y")
    monthly_rent_date = serializers.DateField(format="%d/%m/%Y")
    doc_url = serializers.SerializerMethodField()
    class Meta:
        model = Tenant
        fields = ['tenantid','name','address','documents','doc_url','unit','agreement_end_date','monthly_rent_date']

    def get_doc_url(self,obj):
        request = self.context.get('request')
        url=""
        if obj.documents:
            url = request.build_absolute_uri(obj.documents.url)
        return url
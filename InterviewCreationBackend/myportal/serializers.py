from .models import UserDetails, InterviewDetails
from rest_framework import serializers
from .validations import validators


class InterviewDetailsSerializer(serializers.ModelSerializer):
    class Meta:
        model = InterviewDetails
        fields = "__all__"

    def validate(self, attrs):
        validateObj = validators(
            attrs["startTime"], attrs["endTime"], attrs["participants"])
        validateObj.validateTime()
        validateObj.validateCountofParticipants()
        validateObj.validateOverlappings()

        if validateObj.isvalid() == False:
            raise serializers.ValidationError(validateObj.getErrorMessage())

        return attrs


class UserDetailsSerializer(serializers.ModelSerializer):
    class Meta:
        model = UserDetails
        fields = ['id', 'username', 'email', 'userType']

    def validate(self, attrs):
        return attrs

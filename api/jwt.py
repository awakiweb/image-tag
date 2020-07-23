from datetime import datetime
from calendar import timegm

from rest_framework_jwt.settings import api_settings
from employee.models import Employee


def jwt_payload_handler(user):
    try:
        employees = Employee.objects.get(user=user)

        return {
            'user_id': user.pk,
            'employee_id': employees.pk,
            'username': user.username,
            'email': user.email,
            'first_name': user.first_name,
            'last_name': user.last_name,
            'is_admin': user.is_superuser,
            'active': employees.active,
            'exp': datetime.utcnow() + api_settings.JWT_EXPIRATION_DELTA,
            'orig_iat': timegm(datetime.utcnow().utctimetuple())
        }
    except Employee.DoesNotExist:
        return {
            'employee_id': 0
        }


def jwt_response_payload_handler(token, user=None, request=None):
    return {
        'success': True,
        'token': token
    }

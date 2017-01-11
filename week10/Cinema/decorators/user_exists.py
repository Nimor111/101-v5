from functools import wraps
from queries.manage_db_queries import *
from database.modify_database import *
from user_interface.user import User, set_password, set_username
from decorators.password import encode_pass
import user_interface.validators


def user_exists(func):
    """
    Does user exist in the system? Check login, check registration
    """
    def accepter(user, password):
        user_interface.validators.check_user(user)
        if logged(user):
            return func(user, password)
        user_interface.validators.check_login(user, password)
        return func(user, password)
    return accepter

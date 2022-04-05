"""App errors."""
from typing import List
from typing import Optional


class WritePermissionError(Exception):
    """Could not write to db exception."""

    def __init__(self):
        """Init exception."""
        self.status_code = 403
        self.detail = "You do not have permissions to modify this model"
        self.message = self.detail
        super(WritePermissionError, self).__init__(self.detail)


class RecordNotFoundError(Exception):
    """Could not find record in db exception."""

    def __init__(self, uuid: str, model_name: str):
        """Init exception."""
        self.status_code = 404
        self.detail = f"Record with uuid: {uuid} not found in table: {model_name}"
        self.message = self.detail
        super(RecordNotFoundError, self).__init__(self.detail)


class ModelNotFoundError(Exception):
    """Could not find table for given model exception."""

    def __init__(self, table_name: str):
        """Init exception."""
        self.detail = f"Could not find a model for the table named {table_name}"
        self.message = self.detail
        self.status_code = 404
        super(ModelNotFoundError, self).__init__(self.detail)


class InvalidEnvironment(Exception):
    """Specified environment is not valid."""

    def __init__(self, environment: str):
        """Init exception."""
        self.detail = f"{environment} is not a valid environment."
        self.message = self.detail
        self.status_code = 404
        super(InvalidEnvironment, self).__init__(self.detail)


class InvalidUserId(Exception):
    """User_id is not a valid user."""

    def __init__(self, user_id):
        """Init exception."""
        self.status_code = 500
        self.detail = f"User id: {user_id}, is invalid."
        self.message = self.detail
        super(InvalidUserId, self).__init__(self.detail)


#  ==== Filtering Errors ====


class FilterSchemasMismatch(Exception):
    """Filter fields object fields differ from filter function fields."""

    def __init__(self, filter_fields: object, filter_functions: object):
        """Init exception."""
        self.status_code = 500
        self.detail = (
            f"filter field names in class '{type(filter_fields).__name__}'"
            f" do not match field names in class '{type(filter_functions).__name__}'"
        )
        self.message = self.detail
        super(FilterSchemasMismatch, self).__init__(self.detail)


class InvalidFilterClass(Exception):
    """Provided filter class is not valid."""

    def __init__(self, filter_field: str):
        """Init exception."""
        self.status_code = 500
        self.detail = f"filter class for {filter_field} is invalid."
        self.message = self.detail
        super(InvalidFilterClass, self).__init__(self.detail)


# ==== Ordering Errors ====


class InvalidOrderField(Exception):
    """Invalid field provided to order by."""

    def __init__(self, order_field: str, possible_fields: List[str]):
        """Init exception."""
        self.status_code = 400
        self.detail = f"field {order_field} is not a valid field to order by. Use one of: {possible_fields}"
        self.message = self.detail
        super(InvalidOrderField, self).__init__(self.detail)


class InvalidOrderType(Exception):
    """Invalid field provided to order by."""

    def __init__(self, order_type: str, possible_types: List[str]):
        """Init exception."""
        self.status_code = 400
        self.detail = f"order type {order_type} is not a valid order type. Please use: {possible_types}"
        self.message = self.detail
        super(InvalidOrderType, self).__init__(self.detail)


# ==== Testing ====


class InvalidTestingEnvironment(Exception):
    """Invalid testing environment."""

    def __init__(self, environment: Optional[str], valid_environments: List[str]):
        """Init exception."""
        self.status_code = 500
        self.detail = f"{environment} is not a valid testing environment. Valid Environments: {valid_environments}"
        self.message = self.detail
        super(InvalidTestingEnvironment, self).__init__(self.detail)

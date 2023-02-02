from src.enums.global_enums import GlobalErrorMessages
import json

class Response:

    """ Basics for response / validation / HTTP-code etc. """
    def __init__(self, response):
        self.response = response
        self.response_json = response.json()
        self.response_status = response.status_code

    # Pydantic validator method
    def pydantic_validate(self, schema):
        if isinstance(self.response_json, list):
            for item in self.response_json:
                schema.parse_obj(item)
        else:
            schema.parse_obj(self.response_json)
        return self

    # Status code validator method
    def assert_status_code(self, status_code):
        if isinstance(status_code, list):
            assert self.response_status in status_code, GlobalErrorMessages.WRONG_STATUS_CODE.value
        else:
            assert self.response_status == status_code, GlobalErrorMessages.WRONG_STATUS_CODE.value
        return self

    # Output reformat
    def __str__(self):
        return \
            f"\nStatus code: {self.response_status} \n" \
            f"\nRequested URL: {self.response.url} \n" \
            f"Response body: {self.response_json}"
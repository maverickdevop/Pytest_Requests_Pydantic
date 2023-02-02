from enum import Enum

""" Standart error enums """
class GlobalErrorMessages(Enum):
    WRONG_STATUS_CODE = "Received status code is not equal to expected!"
    WRONG_JSON_SCHEMA = "JSON schema is not equal to expected schema!"


class Team(Enum):
    FOUNDER = "Founder"
    DEV = "Blockchain Developer"
    NODE_DEV = "Node js Developer"

import requests
from configuration import Configuration
from src.schemas.coinpaprika import Paprika
from src.baseclasses.response import Response
from src.enums.global_enums import GlobalErrorMessages

class Test_Coinpaprika:

    def test_btc_bitcoin(self):

        # Send request with URL from configuration file
        request = requests.get(url=Configuration.URL + "/v1/coins/btc-bitcoin")

        # Set variable with Response method
        response = Response(request)

        # Check response and schema validation from Response method
        # If status code or JSON schema validation will fail - raise error text from Enum list
        response.assert_status_code(200), GlobalErrorMessages.WRONG_STATUS_CODE.value
        response.pydantic_validate(Paprika), GlobalErrorMessages.WRONG_JSON_SCHEMA.value
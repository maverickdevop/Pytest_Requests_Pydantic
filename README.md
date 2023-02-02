# PyTest API testing with Request HTTP lib and Pydantic validation

# Information about this test
## The purpose of this test is validating of the JSON schema, in accordance with the basic pydantic model  

## Installation
  
Install the dependencies before run test.  

```sh
pip3 install --upgrade pip
pip3 install -r requirements.txt
```

Run test.  

```sh
python3 -m pytest -sv --tb=short ./tests/coinpaprika_test.py
```

## Documentation  

Documentation

| Plugin | README |
| ------ | ------ |
| Requests | [Requests documentation](https://requests.readthedocs.io/en/latest/) |
| Pydantic | [Pydantic documentation](https://docs.pydantic.dev/) |

# 📣 Please note that!
## Testing GET request was taken from an open API source: [Open GET request](https://api.coinpaprika.com/v1/coins/btc-bitcoin)

# Short info 

⭕️ Tests with example contain in *./test* folder  
⭕️ Parameters for tests (filters query params, login and pass and etc) contains in *./configuration.py*  
⭕️ Error messages contain in GlobalError messages in *./src.enums*  
⭕️ Baseclasses to work with tests and responses contain in src.baseclasses in */response.py*   
⭕️ For JSON validation I use schemas in *./src.schema*  
⭕️ The ./environment allows you to run the test with the URL *prod/stage*.   To run the tests in docker, set the desired environment in the *./Dockerfile*  

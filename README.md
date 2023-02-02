# PyTest API testing with Request HTTP lib and Pydantic validation

# Information about this test
The purpose of this test is validating of the JSON schema in accordance with the basic pydantic model  

## Installation
  
Install the dependencies before run test.  

```sh
pip3 install --upgrade pip
pip3 install -r requirements.txt
```

Run test with command.  

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

⭕️ Tests with example contain in *test* folder  
⭕️ Parameters for tests contains in *configuration.py*  
⭕️ Error messages and test data list contain in GlobalError messages in *src.enums/global_enums.py*  
⭕️ Baseclasses to work with tests and responses contain in *src/baseclasses/response.py*   
⭕️ For JSON validation was used pydantic Basemodel validatiom in *src/schemas/coinpaprika.py*  
⭕️ Use *Dockerfile* to run test in Docker  

# PyTest API testing with Request HTTP lib and Pydantic validation

# Information about this test
The purpose of this test is validating of the JSON schema in accordance with the basic pydantic model
Basemodel example

```python
from enum import Enum
class Team(Enum):
    FOUNDER = "Founder"
    DEV = "Blockchain Developer"
    NODE_DEV = "Node js Developer"

from pydantic import BaseModel, validator, Field, ValidationError
from datetime import datetime, date
from src.enums.global_enums import Team

class PaprikaTags(BaseModel):
    id: str
    name: str
    coin_counter: int
    ico_counter: int

class PaprikaTeam(BaseModel):
    id: str = Field(min_length=1, description="id lenght should not be 0")
    name: str = Field(max_length=255, description="Name should be less than 255 symbols")
    position: Team = Field(description="Team members took from Enum list")
```

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

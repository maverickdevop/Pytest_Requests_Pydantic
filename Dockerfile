# Lib and workdir
FROM python
WORKDIR .

# Copy requirements from root folder
COPY . .
COPY requirements.txt .

# Update pip and install all requirements
RUN pip3 install --upgrade pip
RUN pip3 install -r requirements.txt

# Run tests
CMD python3 -m pytest -sv --tb=short /tests/base_test.py
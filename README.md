# Cryptocurrency Prices

Program that allows you to obtain exchange rates at the moment 
of different markets.

1) ArgenBTC
2) Bitex
3) Bitso
4) Buda
5) Buenbit
6) Copter
7) CriptoFacil
8) Ripio

# Change Quote Prices

Go to folder ".../functions/payloads.py" -> and change the values:

* **{coin}: str** 
* **{fiat}: str**
* **{vol}: float**

For more information visit: 'https://criptoya.com/api/'

Limit: 60 requests per minute.

# Pre Requirements 📋

* **Python 3**-**Pipenv** / **Docker**

# Setup Python Virtual Environment 🔧 #
```cmd
pip install pipenv
```

**Windows** CMD:
```cmd
python -m venv venv
.\venv\Scripts\activate
pip install -r requirements.txt
```
**Linux / MAC** command:
```cmd
python -m venv venv
source venv/bin/activate
python -m pip install -r requirements.txt
```
# Running Python Script 🐼
```cmd
python main.py
```
**Unittest:**
```cmd
python test.py -v
```
# Running Docker 🐳
```cmd
docker build -t crypto .
docker run -it crypto
```
# Author 🖋

* Rodrigo Quispe - Developer - [RRodriQZ]
 
[RRodriQZ]: https://github.com/RRodriQZ
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

* **Docker**

# Running Docker 🐳
```
docker build -t crypto .
```
```
docker run -it crypto
```
Unittest:
```
docker run crypto python test.py -v
```
# Author 🖋

* Rodrigo Quispe - Developer - [RRodriQZ]
 
[RRodriQZ]: https://github.com/RRodriQZ
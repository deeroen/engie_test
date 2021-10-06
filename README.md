# REST API engie

This is an application providing a REST
API for engie challenge.

The entire application is contained within the `main.py` file.

`solver.py` contains the development of the result where the sum of the power generated by each of the different 
powerplants is exactly equal to the load specified in the payload.


## Install

    pip install -r requirements.txt

## Run the app

    python main.py


# REST API

The REST API to the example app is described below.

## Create a new Thing

### Request

`POST /productionplan` on port 8888

    curl -X POST localhost:8888/productionplan -d '<YOUR Json INPUT>'

### Response


    Content-Type: application/json
    Content-Length: 369
    Server: Werkzeug/2.0.1 Python/3.9.2
    Date: Wed, 06 Oct 2021 08:59:36 GMT
    
    [{
        "name": "gasfiredbig1",
        "p": 460
    },
    {
        "name": "gasfiredbig2",
        "p": 226.0
    },
    {
        "name": "gasfiredsomewhatsmaller",
        "p": 0
    },
    {
        "name": "tj1",
        "p": 16
    },
    {
        "name": "windpark1",
        "p": 150
    },
    {
        "name": "windpark2",
        "p": 36
    }]




Body: 



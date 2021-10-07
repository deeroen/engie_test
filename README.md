# Challenge engie

This is an application providing a REST
API for engie challenge.

The entire application is contained within the `app.py` file.

`solver.py` contains the development of the result where the sum of the power generated by each of the different 
powerplants is exactly equal to the load specified in the payload.
This solver takes into account the price of the CO2 emitted. 

## Install with Docker

    docker build -t python-docker .
    


## Run the container

    docker run --publish 8080:5000 python-docker


# REST API

The REST API to the example app is described below.

## Request the loads

### Request

`POST /productionplan` on port 8888 and localhost (http://localhost:8080/productionplan) 
along with the proper json file (body)

    
### Response


    Content-Type: application/json
    Content-Length: 369
    Server: Werkzeug/2.0.1 Python/3.8.12
    Date: Wed, 06 Oct 2021 08:59:36 GMT
    
    [
    {
        "name": "gasfiredbig1",
        "p": 460
    },
    {
        "name": "gasfiredbig2",
        "p": 235.1
    },
    {
        "name": "gasfiredsomewhatsmaller",
        "p": 0
    },
    {
        "name": "tj1",
        "p": 0
    },
    {
        "name": "windpark1",
        "p": 150
    },
    {
        "name": "windpark2",
        "p": 36
    }]










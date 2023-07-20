# SimpleGeoNLPAnnotator
## Introduction
This is an example SimpleGeoNLPAnnotator NLP kind annotator it supports text data and annotates entities and relationships.

## Running the Annotator
To run this example make sure you've installed the full environment including the optional installs provided in poetry

    poetry install --all-extras

Then simply start the server with

    python -m deepsearch.model.examples.simple_geo_nlp_annotator.main

## Simple Interaction with the Annotator

You can direcly access the API via a browser to the provided url on the console upon running the application, usually:

    http://127.0.0.1:8000
This will take you to the landing page. Here you will likely find that you are not authenticated, however you can still check if the API is responsive by accessing the /health endpoint

    http://127.0.0.1:8000/health
It will be easier to interact with the application via the provided documentation endpoint

    http://127.0.0.1:8000/docs

## Security
By default, the API requires an API-key to be used with every request to most endpoints, this key is defined on:

    deepsearch/model/examples/simple_geo_nlp_annotator/main.py
this API key must be provided on the authorization header, sample request headers to /:

    {'host': '127.0.0.1:8000', 'connection': 'keep-alive', 'sec-ch-ua': '"Not.A/Brand";v="8", "Chromium";v="114", "Google Chrome";v="114"', 'accept': 'application/json', 'sec-ch-ua-mobile': '?0', 'authorization': 'example123', 'user-agent': 'Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/114.0.0.0 Safari/537.36', 'sec-ch-ua-platform': '"Linux"', 'sec-fetch-site': 'same-origin', 'sec-fetch-mode': 'cors', 'sec-fetch-dest': 'empty', 'referer': 'http://127.0.0.1:8000/docs', 'accept-encoding': 'gzip, deflate, br', 'accept-language': 'en-US,en;q=0.9'}

## Advanced Interaction with the Annotator
On the /docs endpoint after inserting the api key you may see the following information about the API server

on endpoint:

 - / - A list of all the annotators hosted on this server, in this example you will find only "SimpleGeoNLPAnnotator" on each annotator you will find its annotation capabilities as well as the kind of annotator it is (NLPAnnotator) which in turn tells you how to make requests to the annotator
 - /model/{model_name}  - You will find the annotation capabilities for the given annotator as well as it's kind.
 - /model/{model_name}/predict - You can make POST requests to have the model annotate your data, refer to [Sample Requests](#Sample-Requests)

## Sample Requests

### Sample Entity Annotation

```python
{
  "apiVersion": "string",
  "kind": "NLPModel",
  "metadata": {
    "annotations": {
      "deepsearch.res.ibm.com/x-deadline": "2038-01-18T00:00:00.000Z",
      "deepsearch.res.ibm.com/x-transaction-id": "string",
      "deepsearch.res.ibm.com/x-attempt-number": "string",
      "deepsearch.res.ibm.com/x-max-attempts": "string"
    }
  },
  "spec": {
    "findEntities": {
      "entityNames": ["cities", "countries", "provinces"],
      "objectType": "text",
      "texts": [
        "Lisbon, Madrid, Paris and Zurich are Capitals of european countries",
        "Berlin is the capital of Germany"
      ]
    }
  }
}
```

 - You may alter propertyNames to have any number of the property types the annotator declares it can annotate, or an empty list to annotate all.
 - This annotator has declared that it can only annotate text, as such the objectType must be text
 - texts may be as long or as short as you need it.
 - The x-deadline must lie some time in the future
 - This annotator has declared that it is of kind NLPModel as such the kind for the request must match
 - refer to the /docs for details on the NLPRequest type

Will result in the following output:

```python
{
  "entities": [
    {
      "cities": [
        {
          "type": "cities",
          "match": "Lisbon",
          "original": "Lisbon",
          "range": [
            0,
            6
          ]
        },
        {
          "type": "cities",
          "match": "Madrid",
          "original": "Madrid",
          "range": [
            8,
            14
          ]
        },
        {
          "type": "cities",
          "match": "Paris",
          "original": "Paris",
          "range": [
            16,
            21
          ]
        }
      ],
      "countries": []
    },
    {
      "cities": [
        {
          "type": "cities",
          "match": "Berlin",
          "original": "Berlin",
          "range": [
            0,
            6
          ]
        }
      ],
      "countries": [
        {
          "type": "countries",
          "match": "Germany",
          "original": "Germany",
          "range": [
            25,
            32
          ]
        }
      ]
    }
  ]
}
```

### Sample Relationship Annotation

```python
{
   "apiVersion":"string",
   "kind":"NLPModel",
   "metadata":{
      "annotations":{
         "deepsearch.res.ibm.com/x-deadline":"2038-01-18T00:00:00.000Z",
         "deepsearch.res.ibm.com/x-transaction-id":"string",
         "deepsearch.res.ibm.com/x-attempt-number":"string",
         "deepsearch.res.ibm.com/x-max-attempts":"string"
      }
   },
   "spec":{
      "findRelationships":{
         "relationshipNames": null,
         "objectType":"text",
         "texts":[
            "Lisbon, Madrid, Paris and Zurich are Capitals of european countries",
            "Berlin is the capital of Germany"
         ],
         "entities":[
            {
               "cities":[
                  {
                     "type":"cities",
                     "match":"Lisbon",
                     "original":"Lisbon",
                     "range":[
                        0,
                        6
                     ]
                  },
                  {
                     "type":"cities",
                     "match":"Madrid",
                     "original":"Madrid",
                     "range":[
                        8,
                        14
                     ]
                  },
                  {
                     "type":"cities",
                     "match":"Paris",
                     "original":"Paris",
                     "range":[
                        16,
                        21
                     ]
                  }
               ],
               "countries":[
                  
               ]
            },
            {
               "cities":[
                  {
                     "type":"cities",
                     "match":"Berlin",
                     "original":"Berlin",
                     "range":[
                        0,
                        6
                     ]
                  }
               ],
               "countries":[
                  {
                     "type":"countries",
                     "match":"Germany",
                     "original":"Germany",
                     "range":[
                        25,
                        32
                     ]
                  }
               ]
            }
         ]
      }
   }
}
```
 - Note that for relationship annotation it is required that you provide an annotation of the entities of those same pieces of text
 - You may alter propertyNames to have any number of the property types the annotator declares it can annotate, or an empty list to annotate all.
 - This annotator has declared that it can only annotate text, as such the objectType must be text
 - texts may be as long or as short as you need it.
 - The x-deadline must lie some time in the future
 - This annotator has declared that it is of kind NLPModel as such the kind for the request must match
 - refer to the /docs for details on the NLPRequest type

Will result in the following output:

```python
{
  "relationships": [
    {
      "cities-to-countries": {
        "header": [
          "cities",
          "countries",
          "weight",
          "source"
        ],
        "data": []
      },
      "cities-to-provincies": {
        "header": [
          "cities",
          "provincies",
          "weight",
          "source"
        ],
        "data": []
      },
      "provincies-to-countries": {
        "header": [
          "provincies",
          "countries",
          "weight",
          "source"
        ],
        "data": []
      }
    },
    {
      "cities-to-countries": {
        "header": [
          "cities",
          "countries",
          "weight",
          "source"
        ],
        "data": [
          [
            "cities.0",
            "countries.0",
            1,
            "entities"
          ]
        ]
      },
      "cities-to-provincies": {
        "header": [
          "cities",
          "provincies",
          "weight",
          "source"
        ],
        "data": []
      },
      "provincies-to-countries": {
        "header": [
          "provincies",
          "countries",
          "weight",
          "source"
        ],
        "data": []
      }
    }
  ]
}
```
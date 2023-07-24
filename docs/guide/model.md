## Launching a model

To run this example make sure you've installed the full environment including the optional installs provided in poetry

    poetry install --all-extras

Then run the model with:

    python -m deepsearch.model.examples.<folder_name>.<script.py>
    
Illustrated by running the dummy_nlp_annotator example below
    
    python -m deepsearch.model.examples.dummy_nlp_annotator.main

### Security

By default, the API requires an API-key to be used with every request to most endpoints, this key is defined on a per model basis, as an example:

```python
    # deepsearch/model/examples/dummy_nlp_annotator/main.py
    ...
    
    def run():
        -> settings = Settings(api_key="example123") <-
        app = ModelApp(settings)
        app.register_model(DummyNLPAnnotator())
    ...
```
this API key must be provided on the authorization header for most application endpoints

## A map of the annotator endpoints
 
 - / - A list of all the annotators hosted on this server with all their information.
 - /model/{model_name}  - You will find the annotation capabilities for the given annotator.
 - /model/{model_name}/predict - You can make POST requests to have the model annotate your data, refer to the [Sample Requests](#Sample NLP kind models requests and responses)
 - /health - An endpoint that will respond with a preset message letting you know that the webserver is healthy.

### Annotator API endpoints guide

You can direcly access the API via a browser to the provided url on the console upon running the application, usually:

    http://127.0.0.1:8000
This will take you to the landing page. Here you will likely find that you are not authenticated, however you can still check if the API is responsive by accessing the /health endpoint

    http://127.0.0.1:8000/health
It will be easier to interact with the application prediction capabilities via the provided documentation endpoint

    http://127.0.0.1:8000/docs

## Sample NLP kind models requests and responses

### Entity annotation
<a name="marker1"></a>
```json
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
				"entityNames": ["entity_foo", "entity_bar"],
				"objectType": "text",
				"texts": [
					"A piece of text",
					"Yet another piece of text"
				]
			}
		}
	}
```

response

```json
{
   "entities":[
      {
         "entity_foo":[
            {
               "type":"entity_foo",
               "match":"a 'entity_foo' match in 'A piece of text'",
               "original":"a 'entity_foo' original in 'A piece of text'",
               "range":[
                  1,
                  5
               ]
            },
            {
               "type":"entity_foo",
               "match":"another 'entity_foo' match in 'A piece of text'",
               "original":"another 'entity_foo' original in 'A piece of text'",
               "range":[
                  12,
                  42
               ]
            }
         ],
         "entity_bar":[
            {
               "type":"entity_bar",
               "match":"a 'entity_bar' match in 'A piece of text'",
               "original":"a 'entity_bar' original in 'A piece of text'",
               "range":[
                  1,
                  5
               ]
            },
            {
               "type":"entity_bar",
               "match":"another 'entity_bar' match in 'A piece of text'",
               "original":"another 'entity_bar' original in 'A piece of text'",
               "range":[
                  12,
                  42
               ]
            }
         ]
      },
      {
         "entity_foo":[
            {
               "type":"entity_foo",
               "match":"a 'entity_foo' match in 'Yet another piece of text'",
               "original":"a 'entity_foo' original in 'Yet another piece of text'",
               "range":[
                  1,
                  5
               ]
            },
            {
               "type":"entity_foo",
               "match":"another 'entity_foo' match in 'Yet another piece of text'",
               "original":"another 'entity_foo' original in 'Yet another piece of text'",
               "range":[
                  12,
                  42
               ]
            }
         ],
         "entity_bar":[
            {
               "type":"entity_bar",
               "match":"a 'entity_bar' match in 'Yet another piece of text'",
               "original":"a 'entity_bar' original in 'Yet another piece of text'",
               "range":[
                  1,
                  5
               ]
            },
            {
               "type":"entity_bar",
               "match":"another 'entity_bar' match in 'Yet another piece of text'",
               "original":"another 'entity_bar' original in 'Yet another piece of text'",
               "range":[
                  12,
                  42
               ]
            }
         ]
      }
   ]
}
```

### Relationship annotation
request
```json
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

response

```json
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
### Property annotation

## Sample QAGen kind models requests and responses

### Generate
Request
```json
{
  "apiVersion": "string",
  "kind": "QAGenModel",
  "metadata": {
    "annotations": {
      "deepsearch.res.ibm.com/x-deadline": "2038-01-18T00:00:00.000Z",
      "deepsearch.res.ibm.com/x-transaction-id": "string",
      "deepsearch.res.ibm.com/x-attempt-number": "string",
      "deepsearch.res.ibm.com/x-max-attempts": "string"
    }
  },
  "spec": {
    "generateAnswers": {
            "contexts": [
                ["What is the best model"]
            ],
            "questions": [
                "If you are a dummy repeat what I said!"
            ]
    }
  }
}
```

Response

```json
{
  "answers": [
    "If you are a dummy repeat what I said!"
  ]
}
```

## Important considerations

- Each annotator has a kind, for example NLPModel, as such the kind for the request must match.
- For NLP Kind annotators under the spec you must define the appropriate types to be annotated, for the dummyNLPAnnotator
[refer to this example](#marker1) you will find on the request that we would like to find *entity_foo* and *entity_bar* an empty list will lead to
no annotations being made, a null object will lead to *all* possible annotations being made.
- Each annotator declared what sort of input it supports, a list constituted of any number of (text, table and image).
- The x-deadline on each request is already implemented and must lie some time in the future.
- refer to the /docs page on any annotator instance for more specification on the request types
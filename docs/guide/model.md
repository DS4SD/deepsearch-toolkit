# Model API
> Currently in **beta**.

The Model API is a unified and extensible inference API across different model kinds.

Built-in model kind support includes NLP annotators and QA generators.

## Installation
To use the Model API, install including the `api` extra, i.e.:
- with poetry:
`poetry add "deepsearch-toolkit[api]"`
- with pip: `pip install "deepsearch-toolkit[api]"`

To launch a model:

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

### OpenAPI

The OpenAPI UI is served under `/docs`, e.g. http://127.0.0.1:8000/docs.

## Developing a new model
To develop a new model class for an existing [kind](kinds/), inherit from the base model
class of that kind and implement the abstract methods and attributes.

The framework will automatically use the correct controller for your model.

To use a custom controller instead, pass it to `ModelApp.register_model()` via the
optional parameter `controller`.

### Examples
- [Dummy NLP annotator](examples/dummy_nlp_annotator/)
- [Simple geo NLP annotator](examples/simple_geo_nlp_annotator/)
- [Dummy QA generator](examples/dummy_qa_generator/)

## Sample NLP kind models requests and responses

### Entity annotation
??? note "Entity annotation request payload"
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

??? note "Entity annotation request response"
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
??? note "Relationship annotation request payload"
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

??? note "Relationship annotation request response"
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
 TBD
## Sample QAGen kind models requests and responses

### Generate
??? note "Genarate request payload"
    ```json
    {
       "apiVersion":"v1",
       "kind":"QAGenModel",
       "metadata":{
          "annotations":{
             "deepsearch.res.ibm.com/x-deadline":"2028-04-20T12:26:01.479484+00:00",
             "deepsearch.res.ibm.com/x-transaction-id":"testing",
             "deepsearch.res.ibm.com/x-attempt-number":5,
             "deepsearch.res.ibm.com/x-max-attempts":5
          }
       },
       "spec":{
          "generateAnswers":{
             "contexts":[
                [
                   {
                      "text":"A textual transformation of a given table",
                      "type":"table",
                      "representation_type":"triplets"
                   },
                   {
                      "text":"A raw paragraph as it appears on the raw text",
                      "type":"text",
                      "representation_type":"raw"
                   }
                ]
             ],
             "questions":[
                "42"
             ]
          }
       }
    }
    ```

??? note "Generate request response"
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
no annotations being made, a null object will lead to **all** possible annotations being made.
- Each annotator declares what sort of input it supports, a list constituted of any number of (text, table and image).
- The x-deadline on each request is already implemented and must lie some time in the future.
- refer to the /docs page on any annotator instance for more specification on the request types
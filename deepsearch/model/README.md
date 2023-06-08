# Model API

> Currently in **beta**.

The Model API allows users to serve and integrate their own models.

## Installation
To use the Model API, install including the `api`
extra, i.e.:
- with poetry:
`poetry add "deepsearch-toolkit[api]"`
- with pip: `pip install "deepsearch-toolkit[api]"`

## Usage
To run, register a [model factory](factories/) with a
[`ModelApp`](server/deepsearch_annotator_app.py) and run the app:
```python
from deepsearch.model.server.deepsearch_annotator_app import ModelApp

model_factory = ...  # e.g. SimpleTextGeographyFactory()
app = ModelApp()
app.register_model_factory(model_factory)
app.run(host="127.0.0.1", port=8000)
```

### OpenAPI

The OpenAPI UI is served under `/docs`, e.g. http://127.0.0.1:8000/docs.

## Developing a new model
To develop a new model, inherit from a [model factory](factories/) and implement the
methods and attributes that are declared as abstract.

### Examples
- [Minimal annotator](examples/minimal_annotator)
- [Geography annotator](examples/simple_text_geography_annotator/)
- [Dummy QA generator](examples/dummy_qa_generator/)

### Inference
As as example, an input payload for the `/predict` endpoint for the geography annotator
could look as follows (note that `deepsearch.res.ibm.com/x-deadline` should be a
future timestamp):
```json
{
    "apiVersion": "v1",
    "kind": "NLPModel",
    "metadata": {
        "annotations": {
            "deepsearch.res.ibm.com/x-deadline": "2024-04-20T12:26:01.479484+00:00",
            "deepsearch.res.ibm.com/x-transaction-id": "abc",
            "deepsearch.res.ibm.com/x-attempt-number": 5,
            "deepsearch.res.ibm.com/x-max-attempts": 5
        }
    },
    "spec": {
        "findEntities": {
            "entityNames": ["cities", "countries"],
            "objectType": "text",
            "texts": [
                "Bern, the capital city of Switzerland, is built around a crook in the Aare River.",
                "Athens is a major coastal urban area in the Mediterranean and is both the capital and largest city of Greece."
            ]
        }
    }
}
```

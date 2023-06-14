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
To run a model, register it with a [`ModelApp`](server/model_app.py) and run the app:
```python
from deepsearch.model.server.deepsearch_annotator_app import ModelApp

model = ...  # e.g. SimpleGeoNLPAnnotator()
app = ModelApp()
app.register_model(model)
app.run(host="127.0.0.1", port=8000)
```

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

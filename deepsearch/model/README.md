# Model API
> Currently in **beta**.

The Model API is a unified and extensible inference API across different model kinds.

Built-in model kind support includes NLP annotators and QA generators.

## Installation
To use the Model API, install including the `api` extra, i.e.:
- with poetry:
`poetry add "deepsearch-toolkit[api]"`
- with pip: `pip install "deepsearch-toolkit[api]"`

## Basic usage
```python
from deepsearch.model.server.model_app import ModelApp

# (1) create an app
app = ModelApp()

# (2) register your model(s)
app.register_model(
    model=...  # e.g. SimpleGeoNLPAnnotator()
)

# (3) run the app
app.run()
```

### OpenAPI
The OpenAPI UI is served under `/docs`, i.e. by default at http://127.0.0.1:8000/docs.

## Configuration

The user can explicitly specify the settings when instantiating the app:
```python
app = ModelApp(
    settings=ModelAppSettings(...)
)
```

Settings can also be defined via environment variables, as described in [Toolkit
Configuration][toolkit_configuration].

For example, the required API key can be injected via env var
`DEEPSEARCH_MODELAPP_API_KEY`.

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

Note: these examples configure the app with API key "example123"; when running them, use
the same key to access the protected endpoints.

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

[toolkit_configuration]: https://ds4sd.github.io/deepsearch-toolkit/guide/configuration/

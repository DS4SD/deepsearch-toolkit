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
To run a model, register it with a `DeepSearchAnnotatorApp` and run the app:
```python
from deepsearch.model.server.deepsearch_annotator_app import DeepSearchAnnotatorApp

annotator = ...  # e.g. SimpleTextGeographyAnnotator()
app = DeepSearchAnnotatorApp()
app.register_annotator(annotator)
app.run()
```

## Developing a new model
To develop a new model class, inherit from a [base model class](base/) and implement the methods and attributes that are declared as abstract.

### Examples
- Minimal dummy example:
[examples/minimal_annotator/](examples/minimal_annotator/).
- Simple geography annotator:
[examples/simple_text_geography_annotator/](examples/simple_text_geography_annotator/).

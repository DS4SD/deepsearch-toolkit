# Model API

> Currently in **beta**.

The Model API allows users to serve and integrate their own models.

## Usage
```python
from deepsearch.model.server.deepsearch_annotator_app import DeepSearchAnnotatorApp

annotator = ...  # e.g. SimpleTextGeographyAnnotator()
app = DeepSearchAnnotatorApp()
app.register_annotator(annotator)
app.run()
```

For a complete example, check [examples/main.py](examples/main.py).

## Models
For an example, check
[examples/simple_text_geography_annotator/](examples/simple_text_geography_annotator/).

## Base models
Check [base/](base/).

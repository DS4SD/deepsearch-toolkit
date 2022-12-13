This page shows how to convert documents and download the converted `.json` files. Instead of downloading the converted `.json` files, if you'd like to add the converted document to your project see [Adding documents in a project](../guide/data_indices.md#adding-documents-in-a-project).

For the tasks on this page, you are required to identify your project within Deep Search via a `PROJ_KEY`. [Listing projects](projects.md#listing-projects-listprojects) shows the `PROJ_KEY` for all of your projects. 


## Converting local documents

The toolkit provides an easy method to convert documents from your local machine. The [`deepsearch documents`](../cli-reference.md#documents) component processes your input, uploads local files, submits for conversion and downloads the results to your machine. 


Following inputs are supported:

1. Single document in PDF format.
2. Multiple documents in ZIP format.
3. Directory containing multiple documents in PDF and ZIP formats.

??? warning
        ZIP files containing additional ZIP files are not supported.


Let `PATH_DOCS` be the path to a PDF document or a ZIP file or a directory in your local machine. 

=== "CLI"
    <div class="termy">

    ```console
    $ deepsearch documents convert -p PROJ_KEY -i PATH_DOCS
    ```

    </div>

=== "Python"       
    ```python
    import deepsearch as ds                                         
    documents = ds.convert_documents(api=api, proj_key=PROJ_KEY, source_path=PATH_DOCS)

    # Let's download all the converted documents locally in RESULT_DIR
    documents.download_all(result_dir = RESULT_DIR)
    ```

- For CLI: 
The converted documents are automatically downloaded in a `result_TIMESTAMP` directory of the user's current working directory. The `TIMESTAMP` has the format `YYYY-MM-DD_HHhMMmSSs`. 

- For python:
The user specifies the location where converted documents are downloaded. 

--- 

## Converting remote documents

### Single URL

Let `URL` be the web address for an online document.

=== "CLI"
    <div class="termy">

    ```console
    $ deepsearch documents convert -p PROJ_KEY -u URL
    ```

    </div>


=== "Python"       
    ```python
    import deepsearch as ds                                         
    documents = ds.convert_documents(api=api,proj_key=PROJ_KEY, urls=URL)

    # Let's download all the converted documents locally in RESULT_DIR
    documents.download_all(result_dir = RESULT_DIR)
    ```

--- 

### Multiple URLs

Multiple online documents can also be conveniently converted. 

- For CLI:
Create a text file containing the web addresses for online documents, separated by empty lines. For example, the contents of `ONLINE-DOCS.txt` could be:

```text
URL1
URL2
URL3
```
Let `PATH_ONLINE_DOCS` be the path to this text file.

- For python:
Simply pass a python list object containing multiple urls. Let `URL` be a list containing several URLs. 

=== "CLI"
    <div class="termy">

    ```console
    deepsearch documents convert -p PROJ_KEY -u PATH_ONLINE_DOCS
    ```

    </div>


=== "Python"       
    ```python
    import deepsearch as ds
    URL = ["https:///URL1", "https://URL2", "https://URL3"]
    documents = ds.convert_documents(api=api,proj_key=PROJ_KEY, urls=URL)

    # Let's download all the converted documents locally in RESULT_DIR
    documents.download_all(result_dir = RESULT_DIR)
    ```

As we saw [before](#converting-local-documents), converted documents are automatically downloaded when using the CLI. Using python, the user specifies the directory where converted documents are downloaded. 

---

## Generating reports

It is possible to create reports which inform the user about the document conversion tasks and their statuses. Such a report is useful in analysis and debugging large tasks.

- For CLI:
When a document conversion job is launched from the CLI, the task id for each submitted batch is saved to a result directory. Let `PATH_TASK_IDS` be the path to text file containing the `task ids`.

- For python:
The `DocumentConversionResult` object has a built-in method for generating reports.

=== "CLI"
    <div class="termy">

    ```console
    deepsearch documents get-report -p PROJ_KEY -t PATH_TASK_IDS
    ```

    </div>


=== "Python"
    ```python
    import deepsearch as ds                                         
    documents = ds.convert_documents(api=api, proj_key=PROJ_KEY, source_path=PATH_DOCS)

    # Let's generate the report for this document conversion job
    documents.generate_report(result_dir="./result/", progress_bar=True)
    ```
    
---

## Customize conversion settings

You can exercise control over the conversion settings used in document conversion through the python SDK as follows.

To do so, initialise a `ConversionSettings` object, either using the system defaults, or the settings of a particular project.

```python
from deepsearch.documents.core.models import ConversionSettings

conv_settings = ConversionSettings.from_defaults(api)
# or by using the project key:
conv_settings = ConversionSettings.from_project(api, proj_key=PROJ_KEY)

# Modify conv_settings, see sections below...

documents = ds.convert_documents(
  api=api,
  proj_key=PROJ_KEY,
  source_path=PATH_DOCS,
  conversion_settings=conv_settings # pass conv_settings as argument
)           

```

### Modify the conversion pipeline models

You can modify the behaviour of the conversion pipeline by setting custom models for a task, or disabling them altogether. Currently, you may modify which models to use for layout segmentation (`clusters`), and for table structure prediction (`tables`).

#### Example 1: Disable the table structure predictions

You can simply disable a model by setting it to `None`

```python
conv_settings.pipeline.tables = None

```

#### Example 2: Pick an alternative system model for table structure

Deep Search may offer multiple alternative models for the same task, e.g. for table structure prediction. You can list all available models, and set a different model.


```python
from deepsearch.documents.core.models import DefaultConversionModel

# Find out which system models are available
available_models = DefaultConversionModel.get_models(api) 

for m in available_models:
  print(f"Got model type={m.type}, name={m.name}")


# Modify the settings to use another model (assuming it is available)
conv_settings.pipeline.tables = \
    DefaultConversionModel(type="WalnutTableStructureModel")
```

#### Example 3: Pick a custom project model for table structure

If you previously set up a custom model in your project, you can choose it the same way as above.

```python
from deepsearch.documents.core.models import ProjectConversionModel

project_models = ProjectConversionModel.get_models(api, proj_key)

for pm in project_models:
  if pm.name == "my-ts-model-test-1": # basic example: match by name
    conv_settings.pipeline.tables = pm

```

### Modify OCR settings

If you want to use OCR, you can enable it and choose an OCR backend.

#### Example 1: Enable default OCR

```python
from deepsearch.documents.core.models import ConversionSettings, OCRSettings

conv_settings = ConversionSettings.from_defaults(api)
conv_settings.ocr.enabled = True
```

#### Example 2: Choose alternative OCR backend

```python
from deepsearch.documents.core.models import ConversionSettings, OCRSettings

conv_settings = ConversionSettings.from_defaults(api)
conv_settings.ocr.enabled = True

# Find out which OCR backends are available
ocr_backends = OCRSettings.get_backends(api) 

for b in ocr_backends:
  print(f"Got OCR backend id={b.id}, name={b.name}")

conv_settings.ocr.backend = "alpine-ocr" # set a different backend

```

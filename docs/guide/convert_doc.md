This page shows how to convert documents and download the converted `.json` files. Instead of downloading the converted `.json` files, if you'd like to add the converted document to your project see [Adding documents in a project](../guide/data_indices.md#adding-documents-in-a-project).

For the tasks on this page, you are required to identify your project within Deep Search via a `PROJ_KEY`. [Listing projects](projects.md#listing-projects-listprojects) shows the `PROJ_KEY` for all of your projects. 


## Converting local documents

The toolkit provides an easy method to convert documents from your local machine. The [`deepsearch documents`](../cli-reference.md#documents) component processes your input, uploads local files, submits for conversion and downloads the results to your machine. 


Let `PATH_DOCS` be the path to a PDF document in your local machine. 

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

To do so, initialise a `ConversionSettings` object.

```python
from deepsearch.documents.core.models import ConversionSettings

conv_settings = ConversionSettings()

# Modify conv_settings, see sections below...

documents = ds.convert_documents(
  api=api,
  proj_key=PROJ_KEY,
  source_path=PATH_DOCS,
  conversion_settings=conv_settings # pass conv_settings as argument
)           

```

### Modify the conversion pipeline models

You can modify the behaviour of the conversion pipeline by setting custom models for a task, or disabling them altogether. Currently, you may modify which models to use for table structure prediction (`tables`).

#### Example 1: Disable the table structure predictions

You can simply disable a model by setting it to `False`

```python
conv_settings.table_structure.do_table_structure = False

```

#### Example 2: Pick an alternative system model for table structure

Deep Search offer two alternative models for the same task, e.g. for table structure prediction. You can choose between `fast` and `accurate` where's default is `fast`.


You can simply change the table structure by setting it to `accurate`

```python
conv_settings.table_structure.table_structure_mode = "accurate"

```

### Modify OCR settings

By default OCR is enable, you can disable it or choose an OCR backend.

#### Example 1: Disable default OCR

```python
from deepsearch.documents.core.models import ConversionSettings

conv_settings = ConversionSettings()
conv_settings.ocr.do_ocr = False
```

#### Example 2: Choose alternative OCR engine

The default OCR engine is `easyocr`, you can change it to alternative `tesserocr`.

```python
from deepsearch.documents.core.models import ConversionSettings

conv_settings = ConversionSettings()
conv_settings.ocr.kind = "tesserocr"
```

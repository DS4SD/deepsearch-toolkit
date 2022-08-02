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


Let `PATH_DOCS` be the path to a PDF document or a ZIP file or a directory in your local machine:

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

---

## Downloading converted documents

- For CLI:
The converted documents are downloaded automatically.

- For python:

=== "Python"       
    ```python
    import deepsearch as ds
    URL = ["https:///URL1", "https://URL2", "https://URL3"]
    documents = ds.convert_documents(api=api,proj_key=PROJ_KEY, urls=URL)

    # Let's download all the converted documents locally in RESULT_DIR
    documents.download_all(result_dir = RESULT_DIR)

    # We can also iterate over them individually.
    for doc in documents:
        doc.download(result_dir=result_dir, progress_bar=True)
    ```

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

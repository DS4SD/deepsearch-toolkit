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
    documents = ds.convert_documents(api=api,proj_key=PROJ_KEY, url=URL)

    # Let's download all the converted documents locally in RESULT_DIR
    documents.download_all(result_dir = RESULT_DIR)
    ```

### Get your credentials

After registering with [Deep Search](https://ds4sd.github.io/), you can obtain your authentication data by clicking on "API" in the top-right corner. Your credentials consist of your `User name` and your `API key`.

![Deep Search Authentication Info](../images/deepsearch-auth-info.png)


---
### Set up a profile

=== "CLI"
    Set up a [profile][profiles] using `deepsearch profile config`.
    In its basic form it looks like this:
    <div class="termy">

    ```console
    $ deepsearch profile config
    Host: https://ds.example.com  # the Deep Search instance you are using
    Username: name@example.com    # your username
    Api key: (hidden)             # your API key
    ```

    </div>

    By providing a profile name (via option `--profile-name`) you can configure multiple
    different profiles, which you can then easily switch between and manage.

    For details, check [Profiles][profiles].

### Validate the setup

You can perform a simple validation of the profile configuration by [listing your projects](../guide/projects.md#listprojects):

=== "CLI"


    <div class="termy">

    ```console
    $ deepsearch cps projects list

    > key                         name
      --------------------------  ---------
      aaeb8bf7f6d9d12858a0b2b...  project-1
      317ffb14b1ec92fcd5985b3...  project-2
      ...                         ...
    ```

    </div>


=== "Python"
    ```python
    from deepsearch.cps.client.api import CpsApi

    api = CpsApi.from_env()

    print([p.name for p in api.projects.list()])
    # > ['project-1', 'project-2', ...]
    ```

---

### Convert documents

Here, we show a simple way to convert documents using [Deep Search](https://ds4sd.github.io/). See the guide on [document conversion](../guide/convert_doc.md) for more details. Let `PATH_DOCS` be the path to a PDF document or a ZIP file or a directory in your local machine:

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
    documents.download_all(result_dir=RESULT_DIR)
    ```

---


[profiles]: ../guide/configuration.md#profiles

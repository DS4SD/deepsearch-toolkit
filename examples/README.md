# Deep Search examples

## Install

The examples notebooks contained in this folder require additional dependencies for being executed.

To install the toolkit with all example dependencies

```console
$ pip install "deepsearch-toolkit[examples]"
```


### How to run

```console
$ jupyter notebook
```


## Authentication

The example notebooks load the authentication credentials from a file called `cps-auth.json` with a content similar to 
```json
{
    "email": "EMAIL",
    "api_key": "API_KEY"
}
```

More details on how to retrieve the API credentials are available in the [documentation](https://ds4sd.github.io/deepsearch-toolkit/getting_started/#authentication).


## Query notebooks

Note: Managing and querying knowledge graphs is only enabled on dedicated Deep Search instances, see [get access](https://ds4sd.github.io/).

|    | Name              | Description |
| -- | ----------------- | ----------- |
| 1. | [Convert_Documents.ipynb](notebooks/Convert_Documents.ipynb) | Full example on programmatic document conversion |
| 1. | [Query_NodeData.ipynb](notebooks/Query_NodeData.ipynb) | Simple query search for terms and output the text containing them |
| 2. | [Query_WF_Execute.ipynb](notebooks/Query_WF_Execute.ipynb) | Run query copied from the UI editor |
| 3. | Query_FTS.ipynb | Using the FullTextSearch functionality |
| 4. | [Query_Paginate.ipynb](notebooks/Query_Paginate.ipynb) | Examples of different output pagination |
| 5. | [Query_ForEach.ipynb](notebooks/Query_ForEach.ipynb) | Using the ForEach functionality |
| 6. | [Query_DataQuery.ipynb](notebooks/Query_DataQuery.ipynb) | Query the data collection |


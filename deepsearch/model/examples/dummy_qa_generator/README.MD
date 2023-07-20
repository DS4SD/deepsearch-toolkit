# DummyNlpAnnotator
## Introduction
This is an example dummy QA kind annotator.

## Running the Annotator
To run this example make sure you've installed the full environment including the optional installs provided in poetry

    poetry install --all-extras

Then simply start the server with

    python -m deepsearch.model.examples.dummy_qa_generator.main

## Simple Interaction with the Annotator

You can direcly access the API via a browser to the provided url on the console upon running the application, usually:

    http://127.0.0.1:8000
This will take you to the landing page. Here you will likely find that you are not authenticated, however you can still check if the API is responsive by accessing the /health endpoint

    http://127.0.0.1:8000/health
It will be easier to interact with the application via the provided documentation endpoint

    http://127.0.0.1:8000/docs

## Security
By default, the API requires an API-key to be used with every request to most endpoints, this key is defined on:

    deepsearch/model/examples/dummy_qa_generator/main.py
this API key must be provided on the authorization header, sample request headers to /:

    {'host': '127.0.0.1:8000', 'connection': 'keep-alive', 'sec-ch-ua': '"Not.A/Brand";v="8", "Chromium";v="114", "Google Chrome";v="114"', 'accept': 'application/json', 'sec-ch-ua-mobile': '?0', 'authorization': 'example123', 'user-agent': 'Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/114.0.0.0 Safari/537.36', 'sec-ch-ua-platform': '"Linux"', 'sec-fetch-site': 'same-origin', 'sec-fetch-mode': 'cors', 'sec-fetch-dest': 'empty', 'referer': 'http://127.0.0.1:8000/docs', 'accept-encoding': 'gzip, deflate, br', 'accept-language': 'en-US,en;q=0.9'}

## Advanced Interaction with the Annotator
On the /docs endpoint after inserting the api key you may see the following information about the API server

on endpoint:

 - / - A list of all the annotators hosted on this server, in this example you will find only "DummyQAGenerator" on each annotator you will find its annotation capabilities as well as the kind of annotator it is (QAGenModel) which in turn tells you how to make requests to the annotator
 - /model/{model_name}  - You will find the annotation capabilities for the given annotator as well as it's kind.
 - /model/{model_name}/predict - You can make POST requests to have the model generate your data, refer to [Sample Requests](#Sample-Requests)

## Sample Requests

```python
{
  "apiVersion": "string",
  "kind": "QAGenModel",
  "metadata": {
    "annotations": {
      "deepsearch.res.ibm.com/x-deadline": "2038-01-18T00:00:00.000Z",
      "deepsearch.res.ibm.com/x-transaction-id": "string",
      "deepsearch.res.ibm.com/x-attempt-number": "string",
      "deepsearch.res.ibm.com/x-max-attempts": "string"
    }
  },
  "spec": {
    "generateAnswers": {
            "contexts": [
                ["What is the best model"]
            ],
            "questions": [
                "If you are a dummy repeat what I said!"
            ]
    }
  }
}
```

Will result in the following output:

```python
{
  "answers": [
    "If you are a dummy repeat what I said!"
  ]
}
```
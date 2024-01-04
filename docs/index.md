# Deep Search Toolkit

[![PyPI version](https://img.shields.io/pypi/v/deepsearch-toolkit)](https://pypi.org/project/deepsearch-toolkit/)
[![PyPI - Python Version](https://img.shields.io/pypi/pyversions/deepsearch-toolkit)](https://pypi.org/project/deepsearch-toolkit/)
[![License MIT](https://img.shields.io/github/license/ds4sd/deepsearch-toolkit)](https://opensource.org/licenses/MIT)
[![Code style: black](https://img.shields.io/badge/code%20style-black-000000.svg)](https://github.com/psf/black)
[![Docs](https://img.shields.io/badge/website-live-brightgreen)](https://ds4sd.github.io/deepsearch-toolkit/)

*Interact with the Deep Search platform for new knowledge explorations and discoveries*

The Deep Search Toolkit is a Python SDK and CLI allowing users to interact with the Deep Search platform.
The Toolkit provides easy-to-use functionalities for several common processes such as document conversion, graph creation and querying.


[Learn about IBM Deep Search :octicons-link-external-16:](https://ds4sd.github.io/){ .md-button }


## Quick Links

[Deep Search](https://ds4sd.github.io/){ .md-button .md-button--primary }
[Github](https://github.com/ds4sd/){ .md-button .md-button--primary }
[Getting started](getting_started/index.md){ .md-button .md-button--primary }
[Examples](https://github.com/DS4SD/deepsearch-examples){ .md-button .md-button--primary }


## Install the Deep Search Toolkit

The Deep Search Toolkit is available as a [PyPI package](https://pypi.org/project/deepsearch-toolkit/).
It can be installed using the standard Python package managers like `pip`, `poetry`, etc.

### Requirements

Python 3.8+

### Install using pip

<div class="termy">

```console
$ pip install deepsearch-toolkit

---> 100%
```

</div>


### Start using the toolkit


<div class="termy">

```console
// Set up a profile, see <a href="./guide/configuration#profiles">profiles</a>.
$ deepsearch profile config
...

// Convert a document
// for more details, see <a href="https://ds4sd.github.io/deepsearch-toolkit/guide/convert_doc/">document conversion</a>.
$ deepsearch documents convert -p 1234567890abcdefghijklmnopqrstvwyz123456 -u https://arxiv.org/pdf/2206.00785.pdf
Submitting input:     : 100%|██████████████████████████████| 1/1 [00:01<00:00,  1.52s/it]
Converting input:     : 100%|██████████████████████████████| 1/1 [00:33<00:00, 33.80s/it]
Downloading result:   : 100%|██████████████████████████████| 1/1 [00:01<00:00,  1.11s/it]
Total online documents             1
Successfully converted documents   1
```

</div>

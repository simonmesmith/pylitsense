# pylitsense

![build](https://github.com/simonmesmith/pylitsense/actions/workflows/build.yml/badge.svg?branch=main)

The `pylitsense` package is an unofficial Python wrapper for the [NCBI LitSense](https://www.ncbi.nlm.nih.gov/research/litsense/) API. It allows you to query the LitSense API and get back a list of `LitSenseResult` objects, which contain the text of relevant sentences and a score of their similarity to your query.

NCBI describes LitSense as follows:

> LitSense is a unique search system for making sense of the biomedical literature at the sentence level, providing a unified access to over half a billion statements extracted from PubMed and PubMed Central.
> 
> Given a query, LitSense finds the best-matching sentences based on overlapping terms as well as semantic similarity via a cutting-edge neural embedding approach.

For example, given this query:

```
"Breast cancers with HER2 amplification"
```

You will receive an array of results, each with a score of how relevant it is to your query, like this:

```
[
    LitSenseResult(
        text='HER2 amplification/overexpression accounts for aggressive clinical features of HER2 positive breast cancer.', 
        score=0.9443494081497192, 
        annotations=[
            '79|4|gene|2064', 
            '93|13|disease|MESH:D001943', 
            '0|4|gene|2064'
        ],
        pmid=28800870,
        pmcid=None,
        section='abstract'
    ), 
    ...
]
```

## Installation

```bash
pip install pylitsense
```

## Usage

```python
from pylitsense.pylitsense import PyLitSense

# Initialize
pls = PyLitSense()

# Query
results = pls.query("your query here")

# Print results
for result in results:
    print(result.text, result.score)
```

## Parameters

- `query_str` (str): The query string for the API.
- `rerank` (bool, optional): Whether to rerank the results. Defaults to True.  [It seems](https://www.ncbi.nlm.nih.gov/pmc/articles/PMC6602490/) that this refers to reranking using "semantic vectors" (embeddings).
- `limit` (int, optional): Limit the number of results. Defaults to None (no limit).
- `min_score` (float, optional): Minimum score threshold for results. Defaults to None (no minimum score).

## Limitations

The LitSense API itself has the following limitations:

* Maximum of 100 results per query
* Rate limit of one request per user per second

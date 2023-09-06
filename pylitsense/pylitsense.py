"""Python wrapper for the LitSense API."""

from dataclasses import dataclass

import requests


@dataclass
class LitSenseResult:
    """Dataclass for a single result from the LitSense API."""

    text: str
    score: float
    annotations: list[str]
    pmid: int
    pmcid: str
    section: str


class PyLitSense:
    """Python wrapper for the LitSense API."""

    def __init__(
        self,
        base_url="https://www.ncbi.nlm.nih.gov/research/litsense-api/api/",
    ):
        self.base_url = base_url

    def query(
        self,
        query_str: str,
        rerank: bool = True,
        limit: int | None = None,
        min_score: float | None = None,
    ) -> list[LitSenseResult]:
        """Queries the LitSense API."""
        params = {"query": query_str, "rerank": rerank}
        response = requests.get(self.base_url, params=params)
        response.raise_for_status()

        results = response.json()
        parsed_results = [LitSenseResult(**result) for result in results]

        if limit:
            parsed_results = parsed_results[:limit]

        if min_score:
            parsed_results = [
                result
                for result in parsed_results
                if result.score >= min_score
            ]

        return parsed_results

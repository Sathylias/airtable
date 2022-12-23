"""
Name: api.py
Description: Implementation of the Airtable API

Author: Maxime Daraiche <max@techstew.dev>

"""

from typing import Optional
import requests
from requests import Response


class AirtableAPI:
    """
    Handles connection to the API and methods to access data
    :params str token: The Personal Access Token to be used for the requests
    :params Optional[int] timeout: The request timeout specified in seconds
    """

    def __init__(self, token: str, timeout: Optional[int] = 30):
        self.token = token
        self.timeout = timeout

    def gen_headers(self) -> dict[str, str]:
        """
        Generates headers for authentication to the API using a Personal Access Token
        :return: Dictionary containing our Personal Token to be sent to the API
        """

        headers = {
            "Content-Type": "application/json",
            "Accept": "application/json",
            "Authorization": "Bearer " + self.token,
        }

        return headers

    def construct_url(
        self, url: str, fields: list[str], prefix: str = "fields%5B%5D="
    ) -> str:
        """
        Construct the url to be used for specified fields
        Example field: 'fields%5B%5D=Name'
        :param str url: URL of the API endpoint
        :param list[str] fields: The fields that we want to retrieve from the response
        :param str prefix: The prefix used to generate the url, shouldn't need to be changed
        :return: Returns a url containing the encoded fields
        """

        return url + prefix + f"&{prefix}".join(fields)

    def _base_request(
        self, method: str, url: str, fields: Optional[list[str]] = None
    ) -> Response:
        """
        Simple method to avoid duplicate code on all of different API requests
        :params str method:
        :params str url:
        :params Optional[list[str]] fields: The fields that we want to retrieve from the request
        :return: Returns the JSON response from the API request that was executed
        """

        if fields is None:
            return requests.request(
                method, url, headers=self.gen_headers(), timeout=self.timeout
            )

        return requests.request(
            method,
            self.construct_url(url, fields),
            headers=self.gen_headers(),
            timeout=self.timeout,
        )

    def list_records(
        self, base_id: str, table_name: str, fields: Optional[list[str]] = None
    ) -> Response:
        """
        List records in a table
        :params str base_id: The ID of the database used for the request
        :params str table_name: Name or ID of the table
        :params Optional[list[str]] fields: The fields that we want to retrieve from the request
        :return: Return the _base_request function, which carries out the API request
        """

        return self._base_request(
            "GET", f"https://api.airtable.com/v0/{base_id}/{table_name}?", fields=fields
        )

    def list_tables(self, base_id: str) -> Response:
        """
        List all tables in a database
        :params str base_id: The ID of the Airtable Database used for the request
        :return: Return the _base_request function, which carries out the API request
        """

        return self._base_request(
            "GET", f"https://api.airtable.com/v0/meta/bases/{base_id}/tables?"
        )

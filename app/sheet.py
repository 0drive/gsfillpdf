"""
sheet.py - Contains the GSheets class which handles all interactions with Google Sheets.
"""

from __future__ import print_function

from config import _SCOPES, _SPREADSHEET_ID, _SHEET_NAME

import os.path
from google.auth.transport.requests import Request
from google.oauth2.credentials import Credentials
from google_auth_oauthlib.flow import InstalledAppFlow
from googleapiclient.discovery import build

from typing import List
import logging

logger = logging.getLogger(__name__)


class GSheets:
    """A class to organize Google Sheets functionality"""

    def __init__(self) -> None:
        """Constructor method authenticates Sheets API:
        https://developers.google.com/sheets/api/quickstart/python"""

        creds = None

        # The file token.json stores the user's access and refresh tokens, and is
        # created automatically when auth flow completes for the first time
        if os.path.exists("../auth/token.json"):
            creds = Credentials.from_authorized_user_file("../auth/token.json", _SCOPES)

        # If there are no (valid) credentials available, let the user log in.
        if not creds or not creds.valid:
            if creds and creds.expired and creds.refresh_token:
                creds.refresh(Request())
            else:
                flow = InstalledAppFlow.from_client_secrets_file(
                    "../auth/credentials.json", _SCOPES
                )
                creds = flow.run_local_server(port=0)

            # Save the credentials for the next run
            with open("../auth/token.json", "w") as token:
                token.write(creds.to_json())

        service = build("sheets", "v4", credentials=creds)

        logger.info("Successful authentication.")
        self.service = service

    def get_pdf_data(self) -> List:
        """Obtains row/column data from Google Sheet

        :return: list of lists containing [[data on each row], ...]]
        """
        res = (
            self.service.spreadsheets()
            .values()
            .get(
                spreadsheetId=_SPREADSHEET_ID,
                range=_SHEET_NAME,
                valueRenderOption="UNFORMATTED_VALUE",
            )
            .execute()
        )
        return res["values"]

"""
main.py - starting point of gsfillpdf execution
"""

from config import _TEMPLATE_NAME

from sheet import GSheets
from fillpdf import fillpdfs

import pandas as pd
import traceback
import logging

# Log settings
logger = logging.getLogger()
logger.setLevel(logging.INFO)
formatter = logging.Formatter("%(asctime)s:%(name)s:%(message)s")

stream_handler = logging.StreamHandler()
stream_handler.setFormatter(formatter)
file_handler = logging.FileHandler("testing.log")
file_handler.setLevel(logging.INFO)
file_handler.setFormatter(formatter)

logger.addHandler(stream_handler)
logger.addHandler(file_handler)
logger.info("Logging setup complete!")


def main() -> None:
    """Starting point for script"""

    # read in pdf data from GSheet
    sheets = GSheets()
    pdf_data = sheets.get_pdf_data()
    headers = pdf_data.pop(0)
    df = pd.DataFrame(pdf_data, columns=headers)
    df = df.set_index("Label")

    # get form fields from PDF doc
    template_dict = fillpdfs.get_form_fields(f"input/{_TEMPLATE_NAME}")
    logger.info(f"Template dict: {template_dict}")

    # loop through pdf data and populate form fields
    for col in df.columns:
        fill_dict = df[col].to_dict()
        fill_dict = {k: v for (k, v) in fill_dict.items() if k in template_dict and v}

        fillpdfs.write_fillable_pdf(
            f"input/{_TEMPLATE_NAME}", f"output/{col}.pdf", fill_dict
        )

    sheets.service.close()


if __name__ == "__main__":
    logger.info("========= STARTING SCRIPT =========")

    try:
        main()
    except Exception as e:
        print(f"An error occurred: {e}")
        logger.error(traceback.format_exc())

    logger.info("Script complete.")

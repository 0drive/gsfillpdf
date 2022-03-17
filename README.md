# gsfillpdf
Automatically fill template PDFs with data from Google Sheets.

Example sheet and pdf here: https://drive.google.com/drive/folders/15D3r6sVeow_rz40H6ZIK0x_bdpz52yT_?usp=sharing

Credit to [t-houssian](https://github.com/t-houssian/fillpdf) for the excellent fillpdf package!

## Usage
### Google Sheets Access Auth
A couple extra steps are necessary here to ensure that the script can access your private GSheets in a secure manner:

1. Clone this repo: `git clone https://github.com/0drive/gsfillpdf.git`
2. Create a Google Cloud Project on [GCP](https://console.cloud.google.com/).
3. Enable the [Google Sheets API](https://console.cloud.google.com/apis/api/sheets.googleapis.com) on your project.
4. Create Credentials > OAuth Client Id > Desktop App. You will be asked to configure an OAuth consent screen first.
5. Download credentials JSON file and rename to `credentials.json`. Drag into the `auth` folder.

### Template Setup
6. Create a GSheet with the template labels under a "Label" column and the pdf names as headers of the other columns (Example [here](https://docs.google.com/spreadsheets/d/1X0wsfpb5-sm2PE4_dJDliBOrXIOzvVrYrA1JYeyS06c/edit#gid=0)).
7. Place template pdf in `app/input/`.
7. Configure `app/config.py` with the GSheet spreadsheet id (found in url), sheet name, and template file name.
8. Use the run script to get results:
    - Linux: `run.sh`. You will have to grant permission first (`chmod +x run.sh`)
    - Windows: `run.bat` (may have to run as admin)
8. Check `app/output/` for filled in PDFs.
# Streamlit gsheet_connect

Connect to public or private Google Sheets from your Streamlit app. Powered by st.experimental_connection() and gspread.

GSheets Connection works in two modes:

in Read Only mode, using publicly shared Spreadsheet URLs (Read Only mode)
CRUD operations support mode, with Authentication using Service Account. In order to use Service Account mode you need to enable Google Drive and Google Sheets API in Google Developers Console. Follow Initial setup for CRUD mode section in order to authenticate your Streamlit app first.

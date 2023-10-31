# Python script with GitHub Actions

This example shows how to run a Python script with GitHub Actions. It calls an API and logs the response in `status.log`

- Implemented script in `scraping_ndtv.py`
- Github actions has Ci/CD pipeline and it can install and use third party packages from `requirements.txt`
- Inspect and configured job in GitHub Action `.github/workflows/actions.yml`.
    - This job runs when there is an update on the main branch or if there is a pull request from main branch.
- Upon complete running, it updates 'news.csv' file with scraped data from NDTV website.
- It contains two fields, first is 'News Title' and second is 'News Link'. File format is .csv.
- This script also contains 'status.log' file, which gets updated with loggers regarding file execution.

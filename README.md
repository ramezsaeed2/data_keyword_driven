# data_keyword_driven

## How to run tests

1.  **Install dependencies:**
    ```bash
    python3 -m venv myenv
    source myenv/bin/activate
    pip3 install -r requirements.txt
    ```
    (Assuming a `requirements.txt` file exists or will be created with `pytest` and `selenium`.)

2.  **Ensure ChromeDriver is installed:**
    Make sure you have Google Chrome installed and the ChromeDriver executable is available in your system's PATH or specified in `conftest.py`. The current `conftest.py` expects it at `/usr/bin/chromedriver`.

3.  **Run tests:**
    ```bash
    pytest -v tests
    ```
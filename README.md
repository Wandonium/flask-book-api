
# GiveDirectly Take Home Interview Task

![Landing Page Screenshot](./give-directly.png?raw=true "Landing Page")

## Overview

This is a Python3-Flask server for a book library where we are adding a new ​/request endpoint which allows a user to request a book by title. All CRUD endpoints accept and return valid JSON. Sqlite was used as a datastore.

## Prerequisites

- Use of venv for python virtual environment
- Use of pip for installing dependencies

## Library Used

- [Flask](https://flask.palletsprojects.com/en/2.1.x/)
- Python v3.8.10.

Command to install libraries:

```bash
pip install -r requirements.txt
```

## Run Code locally

To run the project locally, please follow the steps given below.

- Clone this Repository

  ```bash
      git clone https://github.com/Wandonium/give-directly.git
  ```

- Go to Project directory

  ```bash
  cd give-directly
  ```

- Create python virtual environment for project

  ```bash
  python3 -m venv .venv
  ```

- Activate virtual environment

  ```bash
  source .venv/bin/activate
  ```
- Install all dependencies from requirements.txt

  ```bash
  pip install -r requirements.txt
  ```

- Run the server
  ```bash
  python app.py
  ```

### Now, I'm expecting this Output

![Landing Page Screenshot](./give-directly.png?raw=true "Landing Page")


## About Author

Was not done after the 3 hour mark. Would have done the following with some extra time:

- Add test cases for each endpoint using either [Selenium](https://www.selenium.dev/) or [PyTest](https://docs.pytest.org/en/7.1.x/)
- Optimized time and space complexity for each endpoint

<!-- It is mandatory to add this.-->

Any comments, suggestions or corrections are welcome. Contribution are welcome as This repository is licensed under [MIT](https://opensource.org/licenses/MIT) License.


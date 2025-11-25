# TodoMVC Playwright Tests (Python)

Automated tests for `https://demo.playwright.dev/todomvc/#/` written using **Python + Playwright + pytest**.  
The project uses **pipenv** for environment and dependency management. But you can use whatever you prefer (e.g., venv and pip).

---

## 🎥 Demo

![til](https://raw.githubusercontent.com/hashrocket/hr-til/master/app/assets/images/banner.png)

![Test workflow demo](./docs/demo.gif)

## 🚀 Installation

Make sure pipenv is installed:

```bash
pip install --user pipenv
```

**OR (macOS)**

```bash
brew install pipenv
```

### 1. Create the virtual environment

```bash
pipenv --python 3.14
```

### 2. Install dependencies

```bash
pipenv install pytest-playwright pytest-xdist
```

### 3. Install Playwright browsers

```bash
pipenv run playwright install
```

### 4. (Optional) Create your own pytest.ini

```bash
cp pytest.ini.example pytest.ini
```

---

## Running the tests

From inside the pipenv shell:

```bash
pipenv shell
pytest -v
```

Or directly:

```bash
pipenv run pytest -v
```

```bash
# if you want to run tests in parallel
pytest -v --numprocesses 4
```

```bash
# if you want to run tests with browser shown and/or different browsers
pytest -v --browser webkit --browser chromium
```

Or if you want to run tests in headless mode, remove the "--headed" option from pytest.ini

---

## Using PyCharm

1. Open the project in PyCharm
2. Go to **Settings → Project → Python Interpreter**
3. Click **Add Interpreter**
4. Select **Pipenv Environment**
5. PyCharm will auto-detect the pipenv environment
6. Click **OK**

PyCharm will automatically enable:

- Playwright autocompletion
- Page Object classes
- pytest integration

---

## Test Coverage

- Adding todo items: English, non-English, numeric, symbols
- Marking items as completed
- Verifying the "Completed" view
- Deleting items
- Active/Completed filter behavior
- Correct list state after operations

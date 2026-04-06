# How to Set Up a Python Project For Automation and Collaboration

**Source:** https://eugeneyan.com//writing/setting-up-python-project-for-automation-and-collaboration/
**Ingested:** 2026-04-02
**Re-scraped:** 2026-04-05
**Tags:** recsys, ml-systems

---

As your Python project gets larger in scope, it can become difficult to manage.

* How can we automate checks (e.g., unit testing, type-checking, linting)?
* How can we minimise collaboration overhead (e.g., code reviews, consistency)?
* How can we maximise developer experience by adding the least extra steps?

In this article, I’ll share an approach that works well for me. When we’re done, we’ll have an automated workflow of units tests, coverage reports, lint checks, and type checks that’ll catch the the majority of errors and facilitate collaboration. This workflow will run in local with a single command (`make check`) and in your remote repository with each `git push`.

* [Install a Python Version Manager](#install-a-python-version-manager)
* [Set Up A Virtualenv and Install Packages](#set-up-a-virtualenv-and-install-packages)
* [Alternatively, use Docker as a Dev Environment instead](#alternatively-use-docker-as-a-dev-environment-instead)
* [Set Up a Consistent Project Structure](#set-up-a-consistent-project-structure)
* [Add Some Basic Methods](#add-some-basic-methods)
* [Write Some Unit Tests; They’re Our Safety Harness](#write-some-unit-tests-theyre-our-safety-harness)
* [Check for Coverage; How Extensive Are Our Tests?](#check-for-coverage-how-extensive-are-our-tests)
* [Lint to Ensure Consistency (Across Projects)](#lint-to-ensure-consistency-across-projects)
* [Check For Type Errors to Prevent Them](#check-for-type-errors-to-prevent-them)
* [Build a Wrapper For Developer Experience](#build-a-wrapper-for-developer-experience)
* [Automate Checks with each `git push`](#automate-checks-with-each-git-push-and-pull-request)
* [Apply these Practices and Profit](#apply-these-practices-and-profit)

To keep this article short and simple, we’ll use a single–most commonly used–tool for each step. I’ll also suggest popular alternatives.

> Follow along with the accompanying repository [here](https://github.com/eugeneyan/python-collab-template/) 🌟.

(Note: These steps should work on a recent Mac or Linux OS. For Windows, you’ll want to enable the [Linux Subsystem](https://docs.microsoft.com/en-us/windows/wsl/install-win10).)

## Install a Python Version Manager

To start, we’ll need a version manager for Python. This allows us to install and manage multiple versions of Python on our local machine. The de facto standard is [`pyenv`](https://github.com/pyenv/pyenv). Here’s how would we install it via [`pyenv-installer`](https://github.com/pyenv/pyenv-installer).

```
# Install pyenv
curl https://pyenv.run | bash

# Restart shell (so the pyenv path changes take effect)
exec $SHELL
```

Now, we’re ready to install and switch between python versions. (Note: `pyenv` inserts a directory of shims in your `PATH`. Read more about it [here](https://github.com/pyenv/pyenv#understanding-path).)

```
# This is the system python
$ python --version
Python 2.7.16

# Install Python 3.8.2
$ pyenv install 3.8.2
python-build: use [email protected] from homebrew
python-build: use readline from homebrew
Downloading Python-3.8.2.tar.xz...
-> https://www.python.org/ftp/python/3.8.2/Python-3.8.2.tar.xz
Installing Python-3.8.2...
python-build: use readline from homebrew
python-build: use zlib from xcode sdk
Installed Python-3.8.2 to /Users/eugene/.pyenv/versions/3.8.2

# Set our local python
$ pyenv local 3.8.2
$ python --version
Python 3.8.2

# Check your different python versions
$ pyenv versions
  system
  3.7.7
  3.8.0
* 3.8.2 (set by /Users/eugene/projects/python-collab-template/.python-version)
```

Python 3.8.2 will be the default version for this project. I.e., when you’re in this directory, invoking `python` will use Python 3.8.2.

Aside: Testing if Python is working fine

As you update python versions, how do you know if you’ve installed it properly on your system? Here’s a tip: Run Python’s built-in test suite.

```
$ python -m test
0:00:00 load avg: 1.89 Run tests sequentially
0:00:00 load avg: 1.89 [  1/423] test_grammar
0:00:00 load avg: 1.89 [  2/423] test_opcodes
0:00:00 load avg: 1.89 [  3/423] test_dict
0:00:00 load avg: 1.89 [  4/423] test_builtin
0:00:00 load avg: 1.98 [  5/423] test_exceptions
0:00:01 load avg: 1.98 [  6/423] test_types
0:00:01 load avg: 1.98 [  7/423] test_unittest
0:00:03 load avg: 1.98 [  8/423] test_doctest
...
Total duration: 18 min 9 sec
Tests result: SUCCESS
```

In this version, Python has 423 internal tests. Just chill and enjoy the satisfaction of seeing test after test passing. 😎

## Set Up A Virtualenv and Install Packages

To manage our Python environments and install packages, we’ll use the most basic `venv` and `pip`. Both come with standard python and are easy to use, and it’s likely most beginner Pythonistas will be familiar with them.

```
# Create a virtual environment
python -m venv .venv

# Activate the virtual environment
source .venv/bin/activate

# Upgrade pip
pip install --upgrade pip
```

Alternatively, here's using poetry

```
# Create a poetry project
poetry init --no-interaction

# Add numpy as dependency
poetry add numpy

# Recreate the project based on the pyproject.toml
poetry install

# To get the path to poetry venv (for PyCharm)
poetry env info
```

With our (virtual) environment set up and activated, we can proceed to install python packages. To keep our production environment as light as possible, we’ll want to separate the packages needed for `dev` and `prod`:

* `dev`: These are only used for development (e.g., testing, linting, etc.) and are not required for production.
* `prod`: These are needed in production (e.g., data processing, machine learning, etc.).

```
# Install dev packages which we'll use for testing, linting, type-checking etc.
pip install pytest pytest-cov pylint mypy codecov

# Freeze dev requirements
pip freeze > requirements.dev

# Install prod packages
pip install pandas

# Freeze dev requirements
pip freeze > requirements.prod
```

In this *simple* project, I cleaned up the `requirements` files by hand (i.e., removed the lower level dependencies that the packages we installed above require). In bigger projects that involve multiple packages and dependencies, you’ll want to use a dependency management tool (discussed below). Here’s how the current requirements looks:

```
$ cat requirements.dev
codecov==2.1.7
mypy==0.780
pylint==2.5.3
pytest==5.4.3
pytest-cov==2.10.0
Sphinx==3.1.1

$ cat requirements.prod
numpy==1.18.5
pandas==1.0.4
```

Aside: Managing dependencies

When you have a big project with multiple packages, updating any of them could break the others. You can mitigate this with a dependency management tool. These tools should also allow you to separate `dev` and `prod` requirements easily.

I didn’t cover this is the main section as there’s still no consensus on them, but here’s a couple of options:

* [`pipenv`](https://pipenv.pypa.io/en/latest/): This looked promising in 2018. But I found it buggy and slow, which reduced build velocity. Nonetheless, things seem to have improved with the updates in 2020.
* [`pip-tools`](https://github.com/jazzband/pip-tools): This works with a standard `requirements.txt` and allows for simple upgrades via `pip-compile --upgrade`. Seems promising.
* [`poetry`](https://python-poetry.org): This has gotten popular recently and allows for direct building and publishing to PyPI. Version 1.0.0 was [released](https://python-poetry.org/blog/announcing-poetry-1-0-0.html) in December 2019. It could become the de facto someday.

Some other alternatives: [`pyflow`](https://github.com/David-OConnor/pyflow), [`dephell`](https://github.com/dephell/dephell), and [`flit`](https://github.com/takluyver/flit). My friend Yu Xuan wrote about Python Environments and its various tools. Read more about it [here](https://yxtay.github.io/blog/python-environment-package-dependency-management/).

## Alternatively, use Docker as a Dev Environment instead

An alternative to versioning Python (via `pyenv`) and Python dependencies (via `venv`) is using Docker as our dev environment. This way, the team can ensure the OS environment (and not just the Python environment) is consistent. Also, some ML platforms, such as SageMaker, run training workflows and deploy via Docker containers—thus it’s good practice to develop in the same containers. This is my recommended approach now.

We start by creating a simple Dockerfile that builds on Python3.8, copies our requirements, and installs the dependencies.

```
ARG BASE_IMAGE=python:3.8

FROM ${BASE_IMAGE} as base

LABEL maintainer='eugeneyan <[email protected]>'

# Use the opt directory as our dev directory
WORKDIR /opt

ENV PYTHONUNBUFFERED TRUE

COPY requirements.dev .
COPY requirements.prod .

# Install python dependencies
RUN pip install --upgrade pip \
    && pip install --no-cache-dir wheel \
    && pip install --no-cache-dir -r requirements.dev \
    && pip install --no-cache-dir -r requirements.prod \
    && pip list
```

To build our environment, we simply run:

```
DOCKER_BUILDKIT=1 docker build -t dev -f Dockerfile .
```

Then, we develop on via an IDE on our local machine as usual. And when we want to run tests on our Docker container, we can spin it up as follows. This command mounts our current directory to the `/opt` dir on our docker container and runs the `bash` command.

```
docker run --rm -it --name run-checks -v $(pwd):/opt -t dev bash
```

## Set Up a Consistent Project Structure

Not much to say here, except we’ll have the standard `src` and `tests` directory. The `tests` directory should mirror the `src` directory.

```
├── requirements.dev
├── requirements.prod
├── src
│   ├── __init__.py
│   └── data_prep
└── tests
    ├── __init__.py
    └── data_prep
```

## Add Some Basic Methods

Before we proceed with the next steps, we’ll first need some code to test.

For this article, I’ve written some *basic* methods to process sample data from the Titanic data set. (They say you should never write about the Titanic or MNIST datasets, but you understand the focus of this article is not about the data, right?)

We have a `categorical` module to process names and extract titles (e.g., Mr, Mrs, Miss), and a `continuous` module to fill missing values (specifically, age). Here’s how the `extract_title` method looks like. The rest of `src` is [here](https://github.com/eugeneyan/python-collab-template/tree/master/src/data_prep).

```
def extract_title(df: pd.DataFrame, col: str, replace_dict: dict = None, 
                  title_col: str = 'title') -> pd.DataFrame:
    """Extracts titles into a new title column

    Args:
        df: DataFrame to extract titles from
        col: Column in DataFrame to extract titles from
        replace_dict (Optional): Optional dictionary to map titles
        title_col: Name of new column containing extracted titles

    Returns:
        A DataFrame with an additional column of extracted titles
    """
    df[title_col] = df[col].str.extract(r' ([A-Za-z]+)\.', expand=False)

    if replace_dict:
        df[title_col] = np.where(df[title_col].isin(replace_dict.keys()),
                                 df[title_col].map(replace_dict),
                                 df[title_col])

    return df
```

## Write Some Unit Tests; They’re Our Safety Harness

Unit tests verify the functionality of our methods. This is important to ensure that updates don’t break anything, especially in data science where data transformation and feature engineering errors usually fail silently. Thus, we’ll include some mock data in our tests.

> “Tests are stories we tell the next generation of programmers on a project.” – Roy Osherove

The de facto for unit tests is [`pytest`](https://docs.pytest.org/en/latest/). There’s also [`unittest`](https://docs.python.org/3/library/unittest.html) which comes with python (though most people just use `pytest`).

To test our `extract_title` method, we’ll want to create a sample `DataFrame` for testing. Here’s how it would look like:

```
def test_extract_title():
    string_col = ['futrelle, mme. jacques heath (lily may peel)',
                  'johnston, ms. catherine helen "carrie"',
                  'sloper, mr. william thompson',
                  'ostby, lady. engelhart cornelius',
                  'backstrom, major. karl alfred (maria mathilda gustafsson)']
    df_dict = {'string': string_col}
    lowercased_df = pd.DataFrame(df_dict)

    result = extract_title(lowercased_df, col='string')
    assert result['title'].tolist() == ['mme', 'ms', 'mr', 'lady', 'major']
```

Running the test is then as simple as:

```
$ pytest
============================= test session starts ==============================
platform darwin -- Python 3.8.2, pytest-5.4.3, py-1.8.2, pluggy-0.13.1
rootdir: /Users/eugene/projects/python-collab-template/tests/data_prep
collected 1 item

test_categorical.py::test_lowercase_column PASSED                        [100%]

============================== 1 passed in 0.24s ===============================
```

You’ll notice that the `extract_title` method lets you pass in an optional dictionary to map titles. For example, we might want to map `'ms'` to `'miss'`, and `'lady'` and `'major'` to `'rare'`. We’ll want to test this too.

### Take Advantage of Fixtures for Reuse

Instead of copy-pasting the code for creating that `DataFrame`, we can make it a [fixture](https://docs.pytest.org/en/latest/fixture.html) for reuse. This is easily done with the `pytest.fixture` decorator. Now, we can use that `lowercase_df` across our tests and stay [DRY](https://en.wikipedia.org/wiki/Don%27t_repeat_yourself).

```
@pytest.fixture
def lowercased_df():
    string_col = ['futrelle, mme. jacques heath (lily may peel)',
                  'johnston, ms. catherine helen "carrie"',
                  'sloper, mr. william thompson',
                  'ostby, lady. engelhart cornelius',
                  'backstrom, major. karl alfred (maria mathilda gustafsson)']
    df_dict = {'string': string_col}
    df = pd.DataFrame(df_dict)
    return df

def test_extract_title(lowercased_df):
    result = extract_title(lowercased_df, col='string')
    assert result['title'].tolist() == ['mme', 'ms', 'mr', 'lady', 'major']

def test_extract_title_with_replacement(lowercased_df):
    title_replacement = {'mme': 'mrs', 'ms': 'miss', 'lady': 'rare', 'major': 'rare'}
    result = extract_title(lowercased_df, col='string', replace_dict=title_replacement)
    assert result['title'].tolist() == ['mrs', 'miss', 'mr', 'rare', 'rare']
```

Let’s run the tests again. Perfect. 👍

```
$ pytest
============================= test session starts ==============================
platform darwin -- Python 3.8.2, pytest-5.4.3, py-1.8.2, pluggy-0.13.1
rootdir: /Users/eugene/projects/python-collab-template/tests/data_prep
collected 2 items

test_categorical.py::test_extract_title PASSED                           [ 50%]
test_categorical.py::test_extract_title_with_replacement PASSED          [100%]

============================== 2 passed in 0.30s ===============================
```

### Test for Exceptions Too

In the `fill_numeric` method, we allow users to select the method to fill missing values, such as `mean`, `median`, etc. If the user selects an incorrect method, it should return a [`NotImplementedError`](https://github.com/eugeneyan/python-collab-template/blob/master/src/data_prep/continuous.py#L25). We can test for this in `pytest` too.

```
def test_fill_numeric_not_implemented(dummy_df):
    with pytest.raises(NotImplementedError):
        fill_numeric(dummy_df, col='int', fill_type='random')
```

Aside: Deliberately Breaking a Test

To better appreciate the value of unit tests, we’ll deliberately introduce a bug where we check if `replace_dict` is `True`, instead of whether a dictionary was passed in.

```
def extract_title(df: pd.DataFrame, col: str, replace_dict: dict = None, 
                  title_col: str = 'title') -> pd.DataFrame:

    df[title_col] = df[col].str.extract(r' ([A-Za-z]+)\.', expand=False)

    if replace_dict == True:  # BUG INTRODUCED HERE
        df[title_col] = np.where(df[title_col].isin(replace_dict.keys()),
                                 df[title_col].map(replace_dict),
                                 df[title_col])

    return df
```

Running our tests again will immediately flag this bug, raise an error, and prevent the build from progressing.

```
$ pytest --pyargs tests/data_prep/test_categorical.py
============================= test session starts ==============================
platform darwin -- Python 3.8.2, pytest-5.4.3, py-1.8.2, pluggy-0.13.1
rootdir: /Users/eugene/projects/python-collab-template
plugins: cov-2.10.0
collected 4 items

tests/data_prep/test_categorical.py ...F                                 [100%]

=================================== FAILURES ===================================
_____________________ test_extract_title_with_replacement ______________________

    def test_extract_title_with_replacement(lowercased_df):
        title_replacement = {'mme': 'mrs', 'ms': 'miss', 'lady': 'rare', 'major': 'rare'}
        result = extract_title(lowercased_df, col='string', replace_dict=title_replacement)
>       assert result['title'].tolist() == ['mrs', 'miss', 'mr', 'rare', 'rare']
E       AssertionError: assert ['mme', 'ms',...ady', 'major'] == ['mrs', 'miss...rare', 'rare']
E         At index 0 diff: 'mme' != 'mrs'
E         Use -v to get the full diff

tests/data_prep/test_categorical.py:50: AssertionError
=========================== short test summary info ============================
FAILED tests/data_prep/test_categorical.py::test_extract_title_with_replacement
```

This way, we know when any changes break something or cause a regression.

## Check for Coverage; How Extensive Are Our Tests?

Now that we have tests, we can check how comprehensive they are (i.e., code coverage). Which parts of our code were executed (via unit testing) and which were skipped? We’ll use [`Coverage.py`](https://coverage.readthedocs.io/) for this and install it with [`pytest-cov`](https://pytest-cov.readthedocs.io/en/latest/) which integrates `Coverage.py` with `pytest`.

Measuring coverage is as simple as adding the `--cov` option.

```
$ pytest --cov=src
============================= test session starts ==============================
platform darwin -- Python 3.8.2, pytest-5.4.3, py-1.8.2, pluggy-0.13.1
rootdir: /Users/eugene/projects/python-collab-template
plugins: cov-2.10.0
collected 9 items

tests/data_prep/test_categorical.py ....                                 [ 44%]
tests/data_prep/test_continuous.py .....                                 [100%]

---------- coverage: platform darwin, python 3.8.2-final-0 -----------
Name                           Stmts   Miss  Cover
--------------------------------------------------
src/__init__.py                    0      0   100%
src/data_prep/__init__.py          0      0   100%
src/data_prep/categorical.py      12      0   100%
src/data_prep/continuous.py       11      0   100%
--------------------------------------------------
TOTAL                             23      0   100%

============================== 9 passed in 0.49s ===============================
```

Aside: Deliberately dropping coverage

In the example above, we have 100% code coverage. What happens when it’s not 100%? To do this, we’ll remove `test_extract_title_with_replacement` and run `pytest` again. We can identify the lines of code without coverage with `--cov-report=term-missing`.

```
pytest --cov=src --cov-report=term-missing
============================= test session starts ==============================
platform darwin -- Python 3.8.2, pytest-5.4.3, py-1.8.2, pluggy-0.13.1
rootdir: /Users/eugene/projects/python-collab-template
plugins: cov-2.10.0
collected 8 items

tests/data_prep/test_categorical.py ...                                  [ 37%]
tests/data_prep/test_continuous.py .....                                 [100%]

---------- coverage: platform darwin, python 3.8.2-final-0 -----------
Name                           Stmts   Miss  Cover   Missing
------------------------------------------------------------
src/__init__.py                    0      0   100%
src/data_prep/__init__.py          0      0   100%
src/data_prep/categorical.py      12      1    92%   50
src/data_prep/continuous.py       11      0   100%
------------------------------------------------------------
TOTAL                             23      1    96%

============================== 8 passed in 0.44s ===============================
```

Here, we have 92% coverage on `data_prep.categorical` where line 50 is not executed by our unit tests. Restoring `test_extract_title_with_replacement` fixes this.

## Lint to Ensure Consistency (Across Projects)

It can be difficult to ensure that code consistency within a project, not to mention across projects. Sloppy, inconsistent code makes it difficult to work on different projects; sometimes, they lead to bugs. Here’s where a linter can help. Linters analyze code to flag proramming errors, bugs, and deviations from standards.

In this article, we use [`pylint`](https://www.pylint.org). A common alternative is [`flake8`](https://flake8.pycqa.org/en/latest/). What’s the difference? In a nutshell, `pylint` is seen as a superset of `flake8`, and can have false alarms.

> Also check out the recently released [GitHub Super Linter](https://github.blog/2020-06-18-introducing-github-super-linter-one-linter-to-rule-them-all/).

Here’s running `pylint` on our (initially inconsistent) code. It calls out which lines have issues and includes suggestions on how to fix them. We also get a summary of the linting errors and a score (4.17/10 😢).

```
$ pylint src.data_prep.categorical --reports=y
************* Module src.data_prep.categorical
src/data_prep/categorical.py:20:0: C0330: Wrong continued indentation (add 9 spaces).
                        df[title_col].map(replace_dict),
                        ^        | (bad-continuation)
src/data_prep/categorical.py:21:0: C0330: Wrong continued indentation (add 9 spaces).
                        df[title_col])
                        ^        | (bad-continuation)
src/data_prep/categorical.py:16:12: W1401: Anomalous backslash in string: '\.'. String constant might be missing an r prefix. (anomalous-backslash-in-string)
src/data_prep/categorical.py:1:0: C0114: Missing module docstring (missing-module-docstring)
src/data_prep/categorical.py:5:0: C0116: Missing function or method docstring (missing-function-docstring)
src/data_prep/categorical.py:9:0: C0116: Missing function or method docstring (missing-function-docstring)
src/data_prep/categorical.py:14:0: C0116: Missing function or method docstring (missing-function-docstring)

Report
======
12 statements analysed.

...

Messages
--------
+------------------------------+------------+
|message id                    |occurrences |
+==============================+============+
|missing-function-docstring    |3           |
+------------------------------+------------+
|bad-continuation              |2           |
+------------------------------+------------+
|missing-module-docstring      |1           |
+------------------------------+------------+
|anomalous-backslash-in-string |1           |
+------------------------------+------------+

-----------------------------------
Your code has been rated at 4.17/10
```

Let’s tidy our code and run `pylint` again.

```
pylint src.data_prep.categorical --reports=y

Report
======
...

-------------------------------------------------------------------
Your code has been rated at 10.00/10 (previous run: 4.17/10, +5.83)
```

Looks much better now (10/10).

## Check For Type Errors to Prevent Them

Who here loves type annotations? 🙋🏻‍♂️

Since I started working with Scala (and Spark), I’ve grown to love specifying types. I was elated when [`typing`](https://docs.python.org/3/library/typing.html) was introduced in Python 3.5. There’re several benefits to specifying types, including:

* Informative: Users know what to provide as input and what to expect as output
* Error-handling: If the wrong type is passed in, the code will complain
* Ease of maintenance and debugging

The Python runtime does not enforce type annotations; it’s dynamically typed and only verifies types (at runtime) via [duck typing](https://en.wikipedia.org/wiki/Duck_typing). Nonetheless, we can use type annotations and a static type checker to verify the type correctness of our code. We’ll use [`mypy`](http://mypy-lang.org) for this.

```
$ mypy src
Success: no issues found in 4 source files
```

Note: Some of the FAANG companies have also released their own type checkers. You might want to check out [`pytype`](https://github.com/google/pytype) (Google), [`pyre`](https://github.com/facebook/pyre-check) (Facebook), and [`pyright`](https://github.com/microsoft/pyright) (Microsoft).

Aside: Deliberately Breaking Types

What if the types are incorrect? To demonstrate, we’ll update `fill_numeric` to fill missing values with `'-1'` (`str` type) instead of `-1` (`int` type). `mypy` immediately flags the incompatible types.

```
$ mypy src
src/data_prep/continuous.py:23: error: Incompatible types in assignment (expression has type "str", variable has type "float")
Found 1 error in 1 file (checked 4 source files)
```

## Build a Wrapper For Developer Experience

Now we have the big pieces set up: unit tests, coverage reports, linting, type checking. As your project grows, the workflow will include more checks; it’ll be tedious to type out all these commands. The *harder* it is to use, the *fewer* users we’ll have.

We’ll rely on `make` and wrap these commands in a `Makefile`. The `Makefile` defines a set of tasks and the commands needed to execute them. The intent is to provide a simple interface and encourage usage of our checks. Here’s what in the `Makefile` for `test`; it runs the `pytest` command with the params.

```
test:
    . .venv/bin/activate && py.test tests --cov=src --cov-report=term-missing --cov-fail-under 95
```

And how to run it.

```
$ make test
. .venv/bin/activate && py.test tests --cov=src --cov-report=term-missing --cov-fail-under 95
============================= test session starts ==============================
platform darwin -- Python 3.8.2, pytest-5.4.3, py-1.8.2, pluggy-0.13.1
rootdir: /Users/eugene/projects/python-collab-template
plugins: cov-2.10.0
collected 8 items

tests/data_prep/test_categorical.py ...                                  [ 37%]
tests/data_prep/test_continuous.py .....                                 [100%]

---------- coverage: platform darwin, python 3.8.2-final-0 -----------
Name                           Stmts   Miss  Cover   Missing
------------------------------------------------------------
src/__init__.py                    0      0   100%
src/data_prep/__init__.py          0      0   100%
src/data_prep/categorical.py      12      0   100%
src/data_prep/continuous.py       11      0   100%
------------------------------------------------------------
TOTAL                             23      0   100%

Required test coverage of 95% reached. Total coverage: 100.00%

============================== 8 passed in 1.05s ===============================
```

So instead of activating the environment, remembering the params, and typing out that long command, *or copy-pasting*, we can just do `make test`.

Before running our tests, it’s also a good idea to clean up the existing `pyc` files and coverage report. We can add them to the `Makefile` too and chain it with `test`, like so.

```
clean-pyc:
    find . -name '*.pyc' -exec rm -f {} +
    find . -name '*.pyo' -exec rm -f {} +
    find . -name '*~' -exec rm -f {} +
    find . -name '__pycache__' -exec rm -fr {} +

clean-test:
    rm -f .coverage
    rm -f .coverage.*

clean: clean-pyc clean-test

test: clean
    . .venv/bin/activate && py.test tests --cov=src --cov-report=term-missing --cov-fail-under 95
```

Then, we can have a `make check` task to run the full suite of checks. Here’s how it looks like in the `Makefile`. (For the full `Makefile`, check out the [repo](https://github.com/eugeneyan/python-collab-template/blob/master/Makefile)).

```
checks: test lint mypy
```

## Automate Checks with each `git push` (and pull request)

Code reviews take a lot of time. We can reduce the burden on reviewers by ensuring that our code is working by running the checks before each pull request. Reviewing an erroneous pull request is a waste of time; these errors can be—and should be—minimised with automated checks.

Furthermore, while the `Makefile` makes (no pun intended) it easy to run the checks on local, sometimes, things slip through. We might be in a rush to squash a critical bug and forget to run the checks before creating and *merging* a hotfix, thus creating more bugs.

> “The earlier you catch defects, the cheaper they are to fix.” ― David Farley

Thus, we’ll run our checks automatically before each pull request (with each push event). We can do this with [GitHub Actions](https://github.com/features/actions) by adding `tests.yml` in our `.github/workflows` directory.

```
# .github/workflows/tests.yml
name: Tests
on: push
jobs:
  tests:
    runs-on: ubuntu-latest
    steps:
    - uses: actions/checkout@v2
    - uses: actions/setup-python@v1
      with:
        python-version: 3.8
        architecture: x64
    - run: make setup-venv
    - run: make checks
```

With each push, the tests workflow will run on the latest `ubuntu` image with Python version 3.8. It first sets up the environment (`make setup`) by installing the necessary packages, before running the checks (`make check`).

Here’s what happens when a pull request introduces a bug. The workflow runs and reports that a check has failed. This should prompt us to fix the issues, and saves effort from unnecessary code reviews.

We can save time by not reviewing erroneous pull requests.

After the pull request is updated to fix the bug, GitHub reports all checks passing; now we can review it. As a rough estimate, this has saved my previous teams about 50-60% of code review effort. Yea, we introduced *(and thankfully prevented)* errors with each PR.

**Now** we can begin the code review.

> You can view this pull request [here](https://github.com/eugeneyan/python-collab-template/pull/3).

Keeping the master branch error-free earns us this shiny badge.

Aside: Adding the `codecov` badge.

We can add a coverage reporting service to make code coverage more visible. For this, we'll use [`codecov`](https://codecov.io).

Set up an account at Codecov and add your repository to it. Then, follow the steps and upload your `CODECOV_TOKEN` as a secret in your repo. We'll also add to the last line of our `tests.yml` file, so it looks like this:

```
# .github/workflows/tests.yml
name: Tests
on: push
jobs:
  tests:
    runs-on: ubuntu-latest
    steps:
    - uses: actions/checkout@v2
    - uses: actions/setup-python@v1
      with:
        python-version: 3.8
        architecture: x64
    - run: make setup
    - run: make check
    - run: bash <(curl -s https://codecov.io/bash)
```

This allows us to add the `codecov` badge.

## Apply these Practices and Profit

Thanks for sticking with me so far. We covered the basics of setting up python and package management, unit testing, code coverage, linting, type checking, makefiles, and running automated checks with each push (and pull request).

> Check out the Github repo of the code for this write-up [here](https://github.com/eugeneyan/python-collab-template/) 🌟.

These practices ensure code quality, reduce bugs, and save effort. Get started by forking the repository, updating the code (deliberately with bugs), and making a [pull request](https://github.com/eugeneyan/python-collab-template/compare). Or clone the repository and try breaking things. Let me know how it goes in the comments below.

P.S., Was this article useful for you? If so, please share this tweet. 👇

## Further reading

* [Managing multiple python versions with `pyenv`](https://realpython.com/intro-to-pyenv/)
* [How to Use Static Type Checking in Python 3.6](https://medium.com/@ageitgey/learn-how-to-use-static-type-checking-in-python-3-6-in-10-minutes-12c86d72677b)
* [Hypermodern Python](https://cjolowicz.github.io/posts/hypermodern-python-01-setup/)

**Thanks** to Yang Xinyi, [Stew Fortier](https://stewfortier.com/) and [Joel Christiansen](https://joelchristiansen.com) for reading drafts of this.

P.S., I learnt much of this from [Zhao Chuxin](https://www.linkedin.com/in/chuxin-kiza-zhao/). The good stuff is due to him; the mistakes are mine alone.

  

If you found this useful, please cite this write-up as:

> Yan, Ziyou. (Jun 2020). How to Set Up a Python Project For Automation and Collaboration. eugeneyan.com.
> https://eugeneyan.com/writing/setting-up-python-project-for-automation-and-collaboration/.

or

```
@article{yan2020python,
  title   = {How to Set Up a Python Project For Automation and Collaboration},
  author  = {Yan, Ziyou},
  journal = {eugeneyan.com},
  year    = {2020},
  month   = {Jun},
  url     = {https://eugeneyan.com/writing/setting-up-python-project-for-automation-and-collaboration/}
}
```

  
Share on:

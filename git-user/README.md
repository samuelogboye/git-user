# git-user

### Purpose of the Package

A Python library for GitHub API integration. Retrieve user info, repositories, and more. Simplify GitHub-related tasks effortlessly.

### Features

- ------List of functions------
  - format_username(username)
  - confirm_username(username)
  - get_response(username)
  - full_name(username)
  - twitter(username)
  - repos(username)
  - bio(username)
  - location(username)
  - repo_count(username)
  - followers_count(username)
  - following_count(username)
  - joined_date(username)
  - confirm_token(username, token)
  - create_repo(username, token, repo_name)

### Dependencies

Python >3
Request `pip install requests`

### Getting Started

The package can be found on pypi hence you can install it using pip

### Installation

```bash
pip install git_user23
```

# How to use

## List of functions

format_username(username)
This function removes leading and trailing spaces from the given username.

```python
>>> from git_user23 import *
>>> format_username("           samuelogboye")
'samuelogboye'
>>> format_username("     samuelogboye        ")
'samuelogboye'
```

confirm_username(username)
Checks if a given username is valid on GitHub.

```python
>>> from git_user23 import *
>>> confirm_username("samuelogboye")
True
>>> confirm_username("samuelogboy")
False
```

get_response(username)
Retrieves all user information from GitHub API and returns it as a dictionary.

```python
>>> from git_user23 import *
>>> get_response("samuelogboye")
info
```

full_name(username)
Retrieves the full name of the user

```python
>>> from git_user23 import *
>>> full_name("samuelogboye")
'Samuel Ogboye'

```

twitter(username)
Retrieves the twitter username of a user

```python
>>> from git_user23 import *
>>> twitter("samuelogboye")
'samuel_ogboye'

```

repos(username)
Retrieves a list of all repositories owned by the user.

```python
>>> from git_user23 import *
>>> repos("samuelogboye")
list of repo

```

bio(username)
Retrieves the bio of the user

```python
>>> from git_user23 import *
>>> bio("samuelogboye")
'Software Engineer || Open Source || Technical Writer || C || Python'

```

location(username)
Retrieves the location of the user.

```python
>>> from git_user23 import *
>>> location("samuelogboye")
'Nigeria'

```

repo_count(username)
Retrives the count of public repositories owned by the user.

```python
>>> from git_user23 import *
>>> repo_count("samuelogboye")
30

```

followers_count(username)
Retrieves the count of followers of the user.

```python
>>> from git_user23 import *
>>> followers_count("samuelogboye")
75

```

following_count(username)
Retrieves the count of users that the user is following.

```python
>>> from git_user23 import *
>>> following_count("samuelogboye")
64

```

joined_date(username)
Retrieves the date when the user joined GitHub.

```python
>>> from git_user23 import *
>>> joined_date("samuelogboye")
'2023-02-16'

```

confirm_token(username, token)
Confirms if both username and token are valid. Returns True or False

```python
>>> from git_user23 import *
>>> confirm_token("samuelogboye", *********)
False

```

create_repo(username, token, repo_name)
Creates a public GitHub repository instantly with a README file and returns True if successful.

```python
>>> from git_user23 import *
>>> create_repo("samuelogboye", "******", "testing")
True

```

### Contribution

Contributions are welcome
Notice a bug, let us know. Thanks

### Author

- Main Maintainer: Samuel Ogboye
- Jesus Saves

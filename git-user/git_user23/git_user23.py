#!/usr/bin/env python3

import requests

# ------List of functions------
# format_username(username)
# confirm_username(username)
# get_response(username)
# full_name(username)
# twitter(username)
# repos(username)
# bio(username)
# location(username)
# repo_count(username)
# followers_count(username)
# following_count(username)
# joined_date(username)
# confirm_token(username, token)
# create_repo(username, token, repo_name)


def format_username(username):
    """format_username(username) -> str
    Parameters:
    ----------
    username (str): The username to format

    Returns:
    --------
    str: The formatted username

    Usage:
    -------
    >>> from git_user import format_username
    >>> format_username("  github ")
    "github"

    """
    # Ensure username is a string
    username = str(username)
    # Extract the first word without leading/trailing whitespace
    username_formated = username.strip().split()[0]
    return username_formated


def confirm_username(username):
    """confirm_username(username) -> bool
    Parameters:
    ----------
    username (str): The username to confirm

    Returns:
    --------
    bool: True if the username exists, False otherwise

    Usage:
    -------
    >>> from git_user import confirm_username
    >>> confirm_username("github")
    True

    """
    username = format_username(username)
    url = f"https://api.github.com/users/{username}"
    response = requests.get(url)
    if response.status_code == 200:
        return True
    else:
        return False


def get_response(username):
    """get_response(username) -> dict
    Parameters:
    ----------
    username (str): The username to get the response for

    Returns:
    --------
    dict or str: if successful, returns a dictionary containing user data
                 if an error occurs, returns an error message

    Usage:
    -------
    >>> from git_user import get_response
    >>> get_response("github")
    {'login': 'github', 'id': 9919, 'node_id': 'MDEyOk9yZ2FuaXphdGlvbjk5MTk=', 'avatar_url': 'https://avatars.githubusercontent.com/u/9919?v=4', 'gravatar_id': '', 'url': 'https://api.github.com/users/github', 'html_url': '

    """
    try:
        username = format_username(username)
        url = f"https://api.github.com/users/{username}"
        response = requests.get(url)

        response.raise_for_status()  # Raise an exception if the request was not successful (e.g., 404 or 500 error)

        user_data = response.json()
        return user_data
    except requests.exceptions.RequestException as e:
        return f"Failed to fetch user data. Error: {str(e)}"


def full_name(username):
    """full_name(username) -> str
    Parameters:
    ----------
    username (str): The username to get its full name

    Returns:
    --------
    str: The full name of the user

    Usage:
    -------
    >>> from git_user import full_name
    >>> full_name("github")
    "GitHub"

    """
    username = format_username(username)
    user_data = get_response(username)
    if isinstance(user_data, dict):
        full_name = user_data.get("name")
        if full_name is not None:
            return full_name
        else:
            return "null"
    else:
        return user_data


def twitter(username):
    """twitter(username) -> str
    Parameters:
    ----------
    username (str): The username to get its twitter username

    Returns:
    --------
    str: The twitter username of the user

    Usage:
    -------
    >>> from git_user import twitter
    >>> twitter("github")
    "github"

    """
    username = format_username(username)
    user_data = get_response(username)
    if isinstance(user_data, dict):
        twitter = user_data.get("twitter_username")
        if twitter is not None:
            return twitter
        else:
            return "null"
    else:
        return user_data


def repos(username):
    """repos(username) -> list
    Parameters:
    ----------
    username (str): The username to get its repositories

    Returns:
    --------
    list: The list of repositories of the user

    Usage:
    -------
    >>> from git_user import repos
    >>> repos("github")
    [repo1, repo2, repo3]

    """
    username = format_username(username)
    url = f"https://api.github.com/users/{username}/repos"
    response = requests.get(url)
    if response.status_code == 200:
        repositories = response.json()
        repo_names = [repo["name"] for repo in repositories]
        return repo_names
    else:
        return f"Failed to fetch repositories. Status code: {response.status_code}"


def bio(username):
    """bio(username) -> str
    Parameters:
    ----------
    username (str): The username to get its bio

    Returns:
    --------
    str: The bio of the user

    Usage:
    -------
    >>> from git_user import bio
    >>> bio("github")
    "A Software Developer"

    """
    username = format_username(username)
    user_data = get_response(username)
    if isinstance(user_data, dict):
        bio = user_data.get("bio")
        if bio is not None:
            return bio
        else:
            return "null"
    else:
        return user_data


def location(username):
    """location(username) -> str
    Parameters:
    ----------
    username (str): The username to get its location

    Returns:
    --------
    str: The location of the user

    Usage:
    -------
    >>> from git_user import location
    >>> location("github")
    "San Francisco, CA"

    """
    username = format_username(username)
    user_data = get_response(username)
    if isinstance(user_data, dict):
        location = user_data.get("location")
        if location is not None:
            return location
        else:
            return "null"
    else:
        return user_data


def repo_count(username):
    """repo_count(username) -> int
    Parameters:
    ----------
    username (str): The username to get its repository count

    Returns:
    --------
    int: The number of repositories of the user

    Usage:
    -------
    >>> from git_user import repo_count
    >>> repo_count("github")
    100

    """
    username = format_username(username)
    user_data = get_response(username)
    if isinstance(user_data, dict):
        repo_count = user_data.get("public_repos")
        if repo_count is not None:
            return repo_count
        else:
            return "null"
    else:
        return user_data


def followers_count(username):
    """followers_count(username) -> int
    Parameters:
    ----------
    username (str): The username to get its followers count

    Returns:
    --------
    int: The number of followers of the user

    Usage:
    -------
    >>> from git_user import followers_count
    >>> followers_count("github")
    100

    """
    username = format_username(username)
    user_data = get_response(username)
    if isinstance(user_data, dict):
        followers_count = user_data.get("followers")
        if followers_count is not None:
            return followers_count
        else:
            return "null"
    else:
        return user_data


def following_count(username):
    """following_count(username) -> int
    Parameters:
    ----------
    username (str): The username to get its following count

    Returns:
    --------
    int: The number of following of the user

    Usage:
    -------
    >>> from git_user import following_count
    >>> following_count("github")
    100

    """
    username = format_username(username)
    user_data = get_response(username)
    if isinstance(user_data, dict):
        following_count = user_data.get("following")
        if following_count is not None:
            return following_count
        else:
            return "null"
    else:
        return user_data


def joined_date(username):
    """joined_date(username) -> str
    Parameters:
    ----------
    username (str): The username to get its joined date

    Returns:
    --------
    str: The joined date of the user

    Usage:
    -------
    >>> from git_user import joined_date
    >>> joined_date("github")
    "2008-04-10"

    """
    username = format_username(username)
    user_data = get_response(username)
    if isinstance(user_data, dict):
        joined_date = user_data.get("created_at")
        if joined_date is not None:
            return joined_date[:10]
        else:
            return "null"
    else:
        return user_data


def confirm_token(username, token):
    """confirm_token(username, token) -> bool
    Parameters:
    ----------
    username (str): The username to confirm
    token (str): The token to confirm

    Returns:
    --------
    bool: True if the token is valid, False otherwise

    Usage:
    -------
    >>> from git_user import confirm_token
    >>> confirm_token("github", "1234567890")
    True

    """
    username = format_username(username)
    url = f"https://api.github.com/users/{username}"
    headers = {}
    headers["Authorization"] = f"token {token}"
    response = requests.get(url, headers=headers)
    if response.status_code == 200:
        return True
    else:
        return False


def create_repo(username, token, repo_name):
    """create_repo(username, token, repo_name) -> bool
    Parameters:
    ----------
    username (str): The username to create the repository for
    token (str): The token to create the repository with
    repo_name (str): The name of the repository to create

    Returns:
    --------
    bool: True if the repository was created, False otherwise

    Usage:
    -------
    >>> from git_user import create_repo
    >>> create_repo("github", "1234567890", "test")
    True

    """
    username = format_username(username)
    url = "https://api.github.com/user/repos"
    headers = {}
    headers["Authorization"] = f"token {token}"
    payload = {"name": repo_name, "auto_init": True, "private": False}
    response = requests.post(url, headers=headers, json=payload)
    if response.status_code == 201:
        return True
    else:
        return False

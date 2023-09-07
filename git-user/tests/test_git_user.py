from git_user import __version__
from git_user import *

FAILED = "Failed to fetch user data. Error: \
        404 Client Error: Not Found for url: \
            https://api.github.com/users/nonexistentuser"
def test_version():
    assert __version__ == '0.0.1'

def test_format_username():
    assert format_username("  github ") == "github"
    assert format_username("GITHUB") == "GITHUB"
    assert format_username("GitHuB") == "GitHuB"
    assert format_username("user123!!") == "user123!!"

def test_confirm_username():
    assert confirm_username("github") == True
    assert confirm_username("nonexistentuser") == False

def test_get_response():
    # Test with an existing username (e.g., "github")
    response = get_response("github")
    assert isinstance(response, dict)
    assert response.get("login") == "github"

    # Test with a non-existing username (e.g., "nonexistentuser")
    response = get_response("nonexistentuser")
    assert isinstance(response, str)
    assert FAILED in response

def test_full_name():
    # Test with an existing username (e.g., "github")
    name = full_name("samuelogboye")
    assert isinstance(name, str)
    assert name == "Samuel Ogboye"

    # Test with a non-existing username (e.g., "nonexistentuser")
    name = full_name("nonexistentuser")
    assert isinstance(name, str)
    assert name == FAILED

def test_twitter():
    # Test with an existing username (e.g., "github")
    twitter_username = twitter("samuelogboye")
    assert isinstance(twitter_username, str)
    assert twitter_username == "samuel_ogboye"

    # Test with a non-existing username (e.g., "nonexistentuser")
    twitter_username = twitter("nonexistentuser")
    assert isinstance(twitter_username, str)
    assert twitter_username == FAILED

def test_repos():
    # Test with an existing username (e.g., "github")
    repo_list = repos("github")
    assert isinstance(repo_list, list)
    assert ".github" in repo_list
    assert "accessibilityjs" in repo_list

    # Test with a non-existing username (e.g., "nonexistentuser")
    repo_list = repos("nonexistentuser")
    assert isinstance(repo_list, str)
    assert FAILED in repo_list
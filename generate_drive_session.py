from pydrive.auth import GoogleAuth


def main():
    gauth = GoogleAuth()
    # Try to upload registered client credentials
    gauth.LoadCredentialsFile("secret.json")
    if gauth.credentials is None:
        # Authenticate if they're not there
        gauth.LocalWebserverAuth()
    elif gauth.access_token_expired:
        # Renew if expired
        gauth.Refresh()
    else:
        # Initiate saved credentials
        gauth.Authorize()
    # Save valid credentials to a file
    gauth.SaveCredentialsFile("secret.json")


if __name__ == '__main__':
    main()

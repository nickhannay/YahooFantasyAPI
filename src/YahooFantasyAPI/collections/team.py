

def get_teams(token, client, team_keys=None):
    if team_keys is None:
        # retrieve teams for current user
        url = '/users;use_login=1/teams'
    else:
        #retrieve teams for each given team key
        url = f'/teams;team_keys={team_keys}'

    teams = client.get(url, headers={'Authorization': f'Bearer {token.access_token}'})
    return teams

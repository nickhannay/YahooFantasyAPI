from ..utils import xml2dict

'''
    A function that returns a list of teams = team_keys or
    all of the teams for the current user
'''
def get_teams(token, client, team_keys=None):
    if team_keys is None:
        # retrieve teams for current user
        url = '/users;use_login=1/teams'
    else:
        #retrieve teams for each given team key
        url = f'/teams;team_keys={team_keys}'

    res = client.get(url, headers={'Authorization': f'Bearer {token.access_token}'})
    res_parsed = xml2dict(res.text)
    print(res_parsed)
    teams = res_parsed['fantasy_content']['users']['user']['teams']['team']
    return teams

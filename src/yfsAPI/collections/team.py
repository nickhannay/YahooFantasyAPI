from ..utils import xml2dict


def get_teams(token, client, team_keys=None):
    """
        A function that returns a list of teams = team_keys or
        all of the teams for the current user
    """
    if team_keys is None:
        # retrieve teams for current user
        url = '/users;use_login=1/teams'
    else:
        #retrieve teams for each given team key
        url = f'/teams;team_keys={",".join(team_keys)}'

    res = client.get(url, headers={'Authorization': f'Bearer {token.access_token}'})
    res_parsed = xml2dict(res.text)
    if team_keys is None:
        teams = res_parsed['fantasy_content']['users']['user']['teams']['team']
    else:
        teams = res_parsed['fantasy_content']['teams']['team']
    return teams


def get_roster(token, client, team_key, week=None):
    """
        A function that retrieves the roster provided team
    """
    if week is not None:
        url = f'/team/{team_key}/roster;week={week}'
    else:
        url = f'/team/{team_key}/roster'

    res = client.get(url, headers={'Authorization': f'Bearer {token.access_token}'})
    res_dict = xml2dict(res.text)
    roster = res_dict['fantasy_content']['team']['roster']
    return roster


def get_stats(token, client, team_key, week=None):
    """
        A function that retrieves the stats for a provided team roster
    """
    if week is not None:
        url = f'/team/{team_key}/roster;week={week}/players/stats'
    else:
        url = f'/team/{team_key}/roster/players/stats'

    res = client.get(url, headers={'Authorization': f'Bearer {token.access_token}'})
    res_dict = xml2dict(res.text)
    stats = res_dict['fantasy_content']['team']['roster']
    return stats



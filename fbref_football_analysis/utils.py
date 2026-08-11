import requests
from bs4 import BeautifulSoup
import pandas as pd


def get_season_tables(season_url):
    """
    Function to get the stats tables for the season from the given season URL.
    Args:
        season_url (str): The URL of the season page on FBref.
    Returns:
        BeautifulSoup object: The season table as a BeautifulSoup object.
    """
    season_data = requests.get(season_url)
    season_soup = BeautifulSoup(season_data.text, features="lxml")
    season_table = season_soup.select("table.stats_table")[0]

    return season_table

def get_team_urls(season_links):
    """
    Function to create the team URLs from the season links.
    Args:
        season_links (list): A list of BeautifulSoup link objects for the season.
    Returns:
        list: A list of team URLs.
    """
    squad_links = [l for l in [l.get("href") for l in season_links] if '/squads/' in l]
    team_urls = [f"https://fbref.com{l}" for l in squad_links]

    return team_urls
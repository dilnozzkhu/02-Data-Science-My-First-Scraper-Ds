import requests
from bs4 import BeautifulSoup

def request_github_trending(url):
    """
    Sends a GET request to the provided URL and returns the response.
    """
    response = requests.get(url)
    return response.text

def extract(page):
    """
    Extracts the HTML code of repository rows from the provided HTML page.
    """
    soup = BeautifulSoup(page, 'html.parser')
    repo_rows = soup.find_all('article', class_='Box-row')
    return repo_rows

def transform(html_repos):
    repositories_data = []
    for repo_row in html_repos:
        developer = repo_row.find('h1', class_='h3 color-fg-muted').a.text.strip()
        repo_name = repo_row.find('h1', class_='h3 color-fg-muted').a.span.text.strip()
        nbr_stars = int(repo_row.find('span', class_='Counter').text.strip())
        repositories_data.append({'developer': developer, 'repository_name': repo_name, 'nbr_stars': nbr_stars})
    return repositories_data

def format(repositories_data):
   
    csv_rows = ['Developer,Repository Name,Number of Stars']
    for repo in repositories_data:
        csv_row = f"{repo['developer']},{repo['repository_name']},{repo['nbr_stars']}"
        csv_rows.append(csv_row)
    return '\n'.join(csv_rows)

def main():
    url = 'https://github.com/trending'
    page = request_github_trending(url)
    repo_rows = extract(page)
    repositories_data = transform(repo_rows)
    csv_content = format(repositories_data)
    print(csv_content)

if __name__ == '__main__':
    main()

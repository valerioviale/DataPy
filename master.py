import requests

def get_top_trending_repositories():
    url = "https://api.github.com/search/repositories"
    params = {
        "q": "language:python",
        "sort": "stars",
        "order": "desc",
        "per_page": 5  # Change this to get more repositories
    }
    response = requests.get(url, params=params)
    data = response.json()
    return data["items"]

top_repositories = get_top_trending_repositories()


repository_names = [repo["name"] for repo in top_repositories]
stars_count = [repo["stargazers_count"] for repo in top_repositories]

import matplotlib.pyplot as plt

def plot_bar_chart(repository_names, stars_count):
    plt.figure(figsize=(10, 6))
    plt.bar(repository_names, stars_count, color='skyblue')
    plt.xlabel("Repository")
    plt.ylabel("Number of Stars")
    plt.title("Top Trending Python Repositories on GitHub")
    plt.xticks(rotation=45, ha='right')
    plt.tight_layout()
    plt.show()

plot_bar_chart(repository_names, stars_count)

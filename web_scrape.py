from bs4 import BeautifulSoup


def get_content(url):
    res = requests.get(url)
    page_content = res.content.decode("utf-8")
    return page_content

def save_download_file(content, file_name):
    with open(file_name, "wb") as f:
        f.write(content)
    print("Done!")
    
def get_data_source_from_lws(file_index, save=False, save_file_name="file.csv"):
    """Get file source from learnwithshin."""
    url = "https://learnwithshin.github.io/docs/files/"
    content = get_content(url)
    soup = BeautifulSoup(content, "html.parser")
    article = soup.find('article')
    anchors = article.find_all("a")
    
    base_url = "https://learnwithshin.github.io/docs/"
    target_anchor = anchors[file_index]
    file_url = target_anchor["href"]
    file_url = file_url.replace("../", base_url)
    
    res = requests.get(file_url)
    if save:
        save_download_file(res.content, save_file_name)
    return res.content
    


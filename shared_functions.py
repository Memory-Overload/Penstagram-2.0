import re

def replace_tags(string: str, current_user: str):
    tags: list = re.findall(r"@[\w._-]+(?<!.[._-]$)", string)
    for tag in tags:
      string = string.replace(tag, f"""<a href="#{tag[1:]}_profile_{current_user}" class="tag" rel="nofollow">{tag}</a>""")
    return string
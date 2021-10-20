# KEYYWORD ARGUMENT LIST

def create_html(tag, text, **attributes):
    html = f"<{tag}"

    for key, value in attributes.items():
        html = html + f" {key}='{value}'"

    html = html + f">{text}</{tag}>"
    return html


html = create_html(
    "p", "Ini tag paragraph dengan keyword argument list python")
print(html)

html = create_html(
    "a", "Tag anchor dengan keyword argument list python", href="google.com")
print(html)

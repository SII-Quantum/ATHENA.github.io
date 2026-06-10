with open('index.html', 'r', encoding='utf-8') as f:
    html = f.read()

html = html.replace('src="./static/images/figure1.png"', 'src="./static/images/figure1_athena.png"')

with open('index.html', 'w', encoding='utf-8') as f:
    f.write(html)

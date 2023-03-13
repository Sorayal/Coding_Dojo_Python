from os import walk

html = """
<html>
    <head>
        <title>My Gallery</title>
        <style>
            img {
                width: 400px;
                height: 150px;
                object-fit: cover;
            }
        </style>
    </head>
    """
_, _, filenames = next(walk('img'))

html += """
    <body>
        <main>
            <div>
                <h1>Test Gallery</h1>"""
for f in filenames:
    html += '<img src="img/' + f + '">' + '\n'

html += """
            </div>
        </main>
    </body>
</html>
"""

print(html)
# Write HTML to index.html
with open("index.html", "w") as file:
    file.write(html)

import wikipedia
result = wikipedia.page('Linus_Sebastian')
print(result.summary)
for link in result.links:
    print(link)

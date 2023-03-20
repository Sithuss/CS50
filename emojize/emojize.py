import emoji

inp = input("Input: ").strip()
ans = emoji.emojize(inp, language='alias')
print(ans)
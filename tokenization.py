import tiktoken
encode = tiktoken.encoding_for_model("gpt-4")
text= input("Enter your text: ")
result= encode.encode(text)
print(result)
decoded =encode.decode(result)
print(decoded)
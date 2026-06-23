str=input("Enter your text: ")
from langchain_text_splitters import RecursiveCharacterTextSplitter
text_splitter = RecursiveCharacterTextSplitter(chunk_size=5, chunk_overlap=0)
#smartly checks for generic text because it uses a list of separators in priority order (default: ["\n\n", "\n", " ", ""]).
strs= text_splitter.split_text(str)
print(f"by using recursive character text splitter {strs}")
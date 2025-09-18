import os
from bs4 import BeautifulSoup
from crewai_tools import RagTool


def html_docs(html_folder):
    # Carpeta con tus archivos HTML
    documents = []

    # Procesar todos los archivos HTML en la carpeta
    for filename in os.listdir(html_folder):
        # if filename.endswith(".html"):
        if filename.endswith(".txt"):
            documents.append(f"{html_folder}/{filename}")
    return documents


def create_rag_tool(config_rag, folder):


    print(os.path.exists("./media/2024.txt"))
    
    rag_tool = RagTool(
        config = config_rag,
        chunk_size = 1200,
        chunk_overlap=200
    )

    # rag_tool.add(source="./media/2024.txt", data_type="file")
    rag_tool.add("./media/2024.txt")

    # urls =[
    #     "https://www.sec.gov/Archives/edgar/data/1018724/000101872425000004/amzn-20241231.htm",
    #     "https://www.sec.gov/Archives/edgar/data/1018724/000101872424000008/amzn-20231231.htm",
    #     "https://www.sec.gov/Archives/edgar/data/1018724/000101872423000004/amzn-20221231.htm"
    # ]

    # for url in urls:
    #     rag_tool.add(source=url, data_type="web_page")

    # docs = html_docs(HTML_FOLDER)
    # for doc in docs:
    #     rag_tool.add(doc)

    


    return rag_tool
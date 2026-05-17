from ingestion.pdf_loader import load_pdf
from ingestion.txt_loader import load_txt

def load_documents():
    pdf_docs = load_pdf("data/Attension Arvix.pdf")
    txt_docs = load_txt("data/speech.txt")

    return pdf_docs + txt_docs
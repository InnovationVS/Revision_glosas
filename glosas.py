import streamlit as st
import pandas as pd
import re
import io
import zipfile

def extract_EPS(uploaded_excel):
    glosa = pd.read_excel(uploaded_excel, sheet_name="GLOSA")
    glosa = glosa[["Factura_EPS"]].dropna()
    glosa["Factura_EPS"] = glosa["Factura_EPS"].astype(str)
    return glosa["Factura_EPS"].tolist()

def extract_number(file_name: str) -> str:
    match_name = re.search(r"-(\w+)\.pdf$", file_name)
    if match_name:
        return match_name.group(1)
    return None

st.image("LOGO_RED_SLOGM-02.png", width=300, use_container_width=True)

st.title("Gestion Documentos Glosas")

# upload excel file
uploaded_excel = st.file_uploader("Sube el archivo Excel con los datos", type=["xlsx", "xls"])
excel_bill = None
if uploaded_excel:
    excel_bill = extract_EPS(uploaded_excel)
    st.write("Facturas cargadas:", excel_bill)

# found documents
found_documents = []

# upload PDF files
uploaded_files = st.file_uploader("Sube los documentos (PDF)", type=["pdf"], accept_multiple_files=True)
if uploaded_files:
    if excel_bill is None:
        st.error("Por favor, sube primero el archivo Excel para comparar las facturas.")
    else:
        for file in uploaded_files:
            num_bill = extract_number(file.name)
            if num_bill is None:
                st.warning(f"{file.name}: Formato no valido")
            elif num_bill in excel_bill:
                st.success(f"{file.name}: Archivo disponible y agregado")
                file.seek(0) # File read from the beginning
                found_documents.append((file.name, file.read()))
            else:
                st.error(f"{file.name}: Ese archvio no se encuentra disponible")
if st.button("Generar ZIP"):
    if found_documents:
        zip_buffer = io.BytesIO()
        with zipfile.ZipFile(zip_buffer, "w") as zip_final:
            for name, content in found_documents:
                zip_final.writestr(name, content)
        zip_buffer.seek(0)
        st.download_button(label="Descargar ZIP", data=zip_buffer, file_name="glosas.zip", mime="application/zip")
    else:
        st.info("No hay documentos disponibles para comprimir.")
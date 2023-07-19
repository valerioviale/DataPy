import pandas as pd
import matplotlib.pyplot as plt
from matplotlib.backends.backend_pdf import PdfPages

# Step 1: Read data from the Excel file
file_path = "hdi.xls"
df = pd.read_excel(file_path)

# Step 2: Sort the DataFrame by HDI (optional, for better visualization)
df.sort_values(by="HDI", ascending=False, inplace=True)

# Step 3: Split the data into three DataFrames (approximately 67 values each)
chunk_size = len(df) // 3
df_page1 = df.iloc[:chunk_size]
df_page2 = df.iloc[chunk_size: 2 * chunk_size]
df_page3 = df.iloc[2 * chunk_size:]

# Step 4: Create a PDF file for the chart
with PdfPages("hdi_chart.pdf") as pdf:
    # Page 1
    plt.figure(figsize=(12, 6))
    plt.bar(df_page1.index, df_page1["HDI"], width=0.6, align='center')
    plt.xlabel("Country")
    plt.ylabel("Human Development Index (HDI)")
    plt.title("Zoomed Human Development Index by Country (Page 1)")
    plt.xticks(df_page1.index, df_page1["Nation"], rotation=60, ha='right')
    plt.tight_layout()
    pdf.savefig()
    plt.close()

    # Page 2
    plt.figure(figsize=(12, 6))
    plt.bar(df_page2.index, df_page2["HDI"], width=0.6, align='center')
    plt.xlabel("Country")
    plt.ylabel("Human Development Index (HDI)")
    plt.title("Zoomed Human Development Index by Country (Page 2)")
    plt.xticks(df_page2.index, df_page2["Nation"], rotation=60, ha='right')
    plt.tight_layout()
    pdf.savefig()
    plt.close()

    # Page 3
    plt.figure(figsize=(12, 6))
    plt.bar(df_page3.index, df_page3["HDI"], width=0.6, align='center')
    plt.xlabel("Country")
    plt.ylabel("Human Development Index (HDI)")
    plt.title("Zoomed Human Development Index by Country (Page 3)")
    plt.xticks(df_page3.index, df_page3["Nation"], rotation=60, ha='right')
    plt.tight_layout()
    pdf.savefig()
    plt.close()

# The PDF file "hdi_chart.pdf" now contains three pages with approximately 67 values on each page

import tabula

pdf_path = "./AAPL/"
file = "AAPL_FY23_Q1.pdf"

dfs = tabula.read_pdf(pdf_path+file, pages="all", multiple_tables=True, guess=False)

print(len(dfs))
dfs[0]

print()
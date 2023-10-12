import pandas as pd
import os
from flask import Flask, render_template, request, send_file


app = Flask(__name__)

@app.route("/")
def home():
    return render_template("upload.html")


@app.route("/upload", methods=["POST"])
def upload_file():
    uploaded_file = request.files["file"]

    if uploaded_file.filename != "":
        # Save the uploaded file temporarily
        temp_csv_path = "temp.csv"
        uploaded_file.save(temp_csv_path)

        # Read and format the CSV data
        df = pd.read_csv(temp_csv_path, delimiter=';')
        df['Transaction Amount'] = df['Transaction Amount'].str.replace(',', '.').astype(float)
        df['Transaction Amount'] = df['Transaction Amount'].apply(
            lambda x: '{:,.2f}'.format(x).replace(',', 'X').replace('.', ',').replace('X', '.'))

        # Save as an Excel file
        output_excel_path = "formatted_output.xlsx"
        df.to_excel(output_excel_path, index=False)

        # Clean up temp file
        os.remove(temp_csv_path)

        # Send the Excel file to the user
        return send_file(output_excel_path, as_attachment=True)

    return "No file uploaded"


if __name__ == "__main__":
    app.run(debug=True)

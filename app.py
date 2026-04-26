from flask import Flask, render_template, request
import requests

# Initialize the Flask app
app = Flask(__name__)

# Handle requests to the home page
@app.route("/", methods=["GET", "POST"])
def index():
    result = None
    error = None

    # If the user submitted the form (clicked the button)
    if request.method == "POST":
        country_name = request.form.get("country")  # Get country name from the input field
        
        url = f"https://restcountries.com/v3.1/name/{country_name}"
        response = requests.get(url)

        if response.status_code == 200:
            data = response.json()[0]
            
            # Extract the data we need
            result = {
                "name": data["name"]["common"],
                "capital": data.get("capital", ["N/A"])[0],
                "population": f"{data['population']:,}",
                "region": data["region"],
                "flag": data.get("flag", ""),
                "currency": list(data.get("currencies", {}).values())[0]["name"] if data.get("currencies") else "N/A",
                "language": ", ".join(data.get("languages", {}).values()) if data.get("languages") else "N/A"
            }
        else:
            error = f"Country '{country_name}' not found."

    # Render the HTML page and pass result/error to it
    return render_template("index.html", result=result, error=error)

if __name__ == "__main__":
    app.run(debug=True)
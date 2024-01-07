import requests
import base64

from chatgpt_description_view import ChatGPTDescription

api_key = "AIzaSyAvDKqix1IUhC_OcIlW08TKrmNlJwiun7A"
image_url = "https://www.google.com/search?sca_esv=591924779&sxsrf=AM9HkKkXvgUO1zUiCVdvtc6BRN6_dmtuMg:1702925231432&q=bella+hadid&tbm=isch&source=lnms&sa=X&ved=2ahUKEwjHjf7r0pmDAxXXh_0HHRkaBwEQ0pQJegQIChAB&biw=1536&bih=738&dpr=1.25#imgrc=hT_d7S9mYD8WiM"

class PhotoAnalyzer:
    def __init__(self, api_key):
        self.api_key = api_key
        self.api_endpoint = "https://vision.googleapis.com/v1/images:annotate"

    def analyze_image(self, image_url):
        # Read the image file
        with requests.get(image_url, stream=True) as image_response:
            image_content = base64.b64encode(image_response.content).decode("utf-8")

        # Prepare the request payload
        request_data = {
            "requests": [
                {
                    "image": {"content": image_content},
                    "features": [{"type": "LABEL_DETECTION"}],
                }
            ]
        }

        # Add API key to the request URL
        request_url = f"{self.api_endpoint}?key={self.api_key}"

        # Make the API request
        response = requests.post(request_url, json=request_data)

        if response.status_code == 200:
            # Successful request, parse and return relevant information
            result = response.json()
            main_subject = self.extract_main_subject(result)
            return main_subject
        else:
            # Handle error cases
            print(f"Error: {response.status_code} - {response.text}")
            return None

    def extract_main_subject(self, api_response):
        # Extract the main subject from the API response
        if "responses" in api_response and api_response["responses"]:
            labels = api_response["responses"][0].get("labelAnnotations", [])
            if labels:
                # Assuming the first label is the main subject
                main_subject = labels[0]["description"]
                return main_subject

        return "Main subject not identified"


# Example usage:


analyzer = PhotoAnalyzer(api_key)
main_subject = analyzer.analyze_image(image_url)

print(f"Main Subject: {main_subject}")

chat = ChatGPTDescription()

# Use the get_gpt_description method
description = chat.get_gpt_description(main_subject)

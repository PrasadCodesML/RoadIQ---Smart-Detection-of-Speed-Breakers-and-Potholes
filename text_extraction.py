import os
import re
from google.cloud import vision

# Set the environment variable for the Google Cloud Vision API credentials
os.environ['GOOGLE_APPLICATION_CREDENTIALS'] = 'digital-vim-424619-t9-4b65976464bb.json'

def detect_text(path):
    """Detects text in the file."""
    client = vision.ImageAnnotatorClient()

    with open(path, "rb") as image_file:
        content = image_file.read()

    image = vision.Image(content=content)

    # Use document_text_detection for dense text
    response = client.document_text_detection(image=image)
    texts = response.text_annotations
    ocr_text = []

    for text in texts:
        ocr_text.append(text.description)

    if response.error.message:
        raise Exception(
            "{}\nFor more info on error messages, check: "
            "https://cloud.google.com/apis/design/errors".format(response.error.message)
        )
    return ocr_text

image_path = "gps.jpg"
text = detect_text(image_path)
print("Extracted Text:", text)
print("Type of Text:", type(text))

# Convert the list of extracted text into a single string
text_string = ' '.join(text)

# Regex patterns to extract latitude and longitude
lat_pattern = r'Lat\s*([\d.]+)°'
long_pattern = r'Long\s*([\d.]+)°'

# Search for latitude and longitude in the text
lat_match = re.search(lat_pattern, text_string)
long_match = re.search(long_pattern, text_string)

if lat_match and long_match:
    latitude = lat_match.group(1)
    longitude = long_match.group(1)
    print(f"Latitude: {latitude}, Longitude: {longitude}")
else:
    print("No latitude and longitude found")

# https://learn.microsoft.com/en-us/azure/ai-services/computer-vision/concept-detecting-adult-content
from azure.cognitiveservices.vision.computervision import ComputerVisionClient
from azure.cognitiveservices.vision.computervision.models import VisualFeatureTypes
from msrest.authentication import CognitiveServicesCredentials
import os
from PIL import Image

# Set your Azure subscription key and endpoint
subscription_key = "YOUR_AZURE_COMPUTER_VISION_KEY"
endpoint = "YOUR_AZURE_COMPUTER_VISION_ENDPOINT"

# Create a Computer Vision client
computervision_client = ComputerVisionClient(endpoint, CognitiveServicesCredentials(subscription_key))

# Remote image URL (Replace with your image)
remote_image_url = "https://raw.githubusercontent.com/Azure-Samples/cognitive-services-sample-data-files/master/ComputerVision/Images/sample_image.jpg"

# Local image file path (Uncomment if using a local image)
# local_image_path = "test_image.jpg"

# Function to analyze an image for adult content
def analyze_image(image_url=None, image_path=None):
    if image_url:
        print("\nAnalyzing remote image for adult content...")
        analysis = computervision_client.analyze_image(image_url, visual_features=[VisualFeatureTypes.adult])
    elif image_path:
        print("\nAnalyzing local image for adult content...")
        with open(image_path, "rb") as image_file:
            analysis = computervision_client.analyze_image_in_stream(image_file, visual_features=[VisualFeatureTypes.adult])
    else:
        print("No image provided!")
        return

    # Extract adult content results
    adult_info = analysis.adult
    print("\nAnalysis Results:")
    print(f"Adult Score: {adult_info.adult_score:.4f}")
    print(f"Racy Score: {adult_info.racy_score:.4f}")
    print(f"Gore Score: {adult_info.gore_score:.4f}")
    print(f"Is Adult Content? {'Yes' if adult_info.is_adult_content else 'No'}")
    print(f"Is Racy Content? {'Yes' if adult_info.is_racy_content else 'No'}")
    print(f"Is Gory Content? {'Yes' if adult_info.is_gory_content else 'No'}")

# Analyze a remote image
analyze_image(image_url=remote_image_url)

# Analyze a local image (Uncomment to use)
# analyze_image(image_path=local_image_path)

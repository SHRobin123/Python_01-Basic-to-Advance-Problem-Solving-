#Image Downloader Example

import requests

image_url = input("Enter image URL: ")

response = requests.get(image_url)

if response.status_code == 200:

    with open("downloaded_image.jpg", "wb") as file:
        file.write(response.content)

    print("Image downloaded successfully")

else:
    print("Failed to download image")

'''
output:-

Enter image URL: https://example.com/image.jpg

Image downloaded successfully
'''
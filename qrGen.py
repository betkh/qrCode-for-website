import qrcode
from PIL import Image
import os


def generate_qr_code(website_url, filename="website_qr.png"):
    # Create QR code instance
    qr = qrcode.QRCode(
        version=1,  # controls the size of the QR Code (1-40)
        error_correction=qrcode.constants.ERROR_CORRECT_L,  # error correction level
        box_size=10,  # size of each box in pixels
        border=4,  # thickness of the border (minimum is 4)
    )

    # Add the website URL to the QR code
    qr.add_data(website_url)
    qr.make(fit=True)

    # Create an image from the QR Code instance
    qr_image = qr.make_image(fill_color="black", back_color="white")

    # Save the image
    qr_image.save(filename)
    print(f"QR code saved as {filename}")

    # Display the image (optional, works if you have a display environment)
    try:
        qr_image.show()
    except:
        print("Image display not available in this environment")


if __name__ == "__main__":
    # Replace this with your website URL
    website = input(
        "Please enter your website URL (e.g., https://www.example.com): ")

    # Validate the URL has a proper format (basic check)
    if not website.startswith("http://") and not website.startswith("https://"):
        website = "https://" + website

    # Generate the QR code
    generate_qr_code(website)

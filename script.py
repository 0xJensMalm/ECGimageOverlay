from PIL import Image, ImageDraw, ImageFont
import os

# Define the area for the patient info overlay
patient_info_area = (0, 0, 900, 300)

# Load the Roboto font
font = ImageFont.truetype("Roboto.ttf", 40)  # Adjust the font size as needed

def add_overlay(image_path, study_id):
    # Open the image
    with Image.open(image_path) as img:
        # Create a drawing context
        draw = ImageDraw.Draw(img)
        
        # Draw the rectangle for the patient info area with a solid fill to hide the image below
        draw.rectangle(patient_info_area, outline="black", fill="white")  # Change "white" to any color as needed
        
        # Text to be added
        text = f"study_id: {study_id}"
        
        # Calculate the width and height of the text to be added
        try:
            text_width, text_height = draw.textsize(text, font=font)
        except AttributeError:
            # If the above fails, manually calculate text size (less accurate)
            text_width, text_height = font.getmask(text).size
        
        # Calculate the position for the centered text
        text_x = patient_info_area[0] + (patient_info_area[2] - patient_info_area[0] - text_width) / 2
        text_y = patient_info_area[1] + (patient_info_area[3] - patient_info_area[1] - text_height) / 2
        
        # Add the centered text with the specified color
        draw.text((text_x, text_y), text, font=font, fill="black")  # Change "black" to any text color as needed
        
        # Save the image in the output folder
        output_path = os.path.join("output", os.path.basename(image_path))
        img.save(output_path)

        print(f"Overlay added and image saved to: {output_path}")  # Completion of overlay addition and saving

# Make sure the output directory exists
os.makedirs("output", exist_ok=True)

# Iterate through your image files
for i in range(1, 3):  # Adjust the range based on your images
    image_path = f"{i}.png"
    add_overlay(image_path, i)

print("All images have been processed.")  # Overall completion
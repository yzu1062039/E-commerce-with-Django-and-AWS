from PIL import Image, ImageDraw, ImageFont
import os

# Create a new image with a white background
width = 800
height = 600
background_color = (240, 240, 240)
img = Image.new('RGB', (width, height), background_color)

# Get a drawing context
draw = ImageDraw.Draw(img)

# Draw a rectangle
rect_color = (200, 200, 200)
draw.rectangle([(50, 50), (width-50, height-50)], outline=rect_color, width=2)

# Add text
text = "Product Image"
text_color = (100, 100, 100)
text_position = (width//2, height//2)

# Draw text in the center
draw.text(text_position, text, fill=text_color, anchor="mm")

# Save the image
output_path = os.path.join('static', 'img', 'placeholder.jpg')
img.save(output_path, 'JPEG', quality=95)

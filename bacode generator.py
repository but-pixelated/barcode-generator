import barcode
from barcode.writer import ImageWriter
from PIL import Image

number = input("Enter the code: ")

if number.isdigit() and len(number) == 12:

    barcode_format = barcode.get_barcode_class('upc')
    my_barcode = barcode_format(number, writer=ImageWriter())
    
    my_barcode.save("generated_barcode")

    img = Image.open("generated_barcode.png")
    img.show()
else:
    print("Error: UPC code must be exactly 12 digits long and contain only numeric characters.")

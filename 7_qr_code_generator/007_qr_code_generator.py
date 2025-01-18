# Step 1: Import Required Modules
# Import the qrcode module, which is used for generating QR codes.
# Include a comment reminding you to install the Pillow library, as it is necessary for customizing QR code colors.
import qrcode
import PIL


# Step 2: Define the MyQR Class
# Purpose: To encapsulate the functionality of QR code generation into an easy-to-use class.
# Initialize the Class (__init__ method):

class MyQR:

    # Define a constructor that accepts size (box size) and padding (border size) as parameters.
    # Create an instance of qrcode.QRCode using the parameters and assign it to self.qr.

    def __init__(self, size: int, padding: int):
        self.qr = qrcode.QRCode(box_size=size, border=padding)


    # Create the create_qr Method:

    # Define a method to generate a QR code with customization options.
    # Add parameters for the file name (file_name), foreground color (fg), and background color (bg).

    def create_qr(self, file_name: str, fg: str, bg: str):

        # Use a placeholder string for the QR code data (user_input), simulating what would typically be input by the user.
        
        # Wrap the QR code generation process in a try-except block to handle and display any errors.

        try:

            # Add Data to the QR Code:
            # Use the .add_data() method of QRCode to add the text data to the QR code.
            # Generate and Save the QR Code:

            user_input = "https://chatgpt.com/c/678bf26b-6720-800a-91f1-606c29f9aca4"
            self.qr.add_data(user_input)
            
            # Use the .make_image() method with fill_color and back_color to customize colors.
            # Save the generated QR code image using the .save() method, providing the file name.
            # Handle Errors:

            qr_image = self.qr.make_image(fill_color=fg, back_color=bg)
            qr_image.save(file_name)

            print(f"Successfully created! ({file_name})")
        except Exception as e:
            print(f"Error: {e}")

# Step 3: Define the main Function
# Purpose: To act as the entry point for the script.
# Create an Instance of MyQR:

def main():

    # Instantiate the MyQR class with a box size and border size.
    # Call the create_qr Method:
    # Provide the file name, foreground color, and background color as arguments.

    entry = MyQR(size=30, padding=2)
    entry.create_qr(file_name="sample_qr.png", fg="#48c9b0", bg="white")


if __name__ == '__main__':
    main()








# These parameters control the output file and QR code appearance.

# Step 4: Set the Script Entry Point
# Use the if __name__ == '__main__': construct to ensure the script runs only when executed directly (not imported).
# Call the main() function to execute the QR code generation process.




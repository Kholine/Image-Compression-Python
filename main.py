import cv2


def compress_image(image_path, output_path, quality=90):
    # Read the image
    img = cv2.imread(image_path)

    # Check if the image was loaded successfully
    if img is None:
        print("Error: Could not read the image.")
        return

    # Encode the image with JPEG compression
    encode_param = [int(cv2.IMWRITE_JPEG_QUALITY), quality]
    _, encoded_img = cv2.imencode('.jpg', img, encode_param)

    # Decode the compressed image back to an array
    compressed_img = cv2.imdecode(encoded_img, cv2.IMREAD_COLOR)

    # Save the compressed image
    cv2.imwrite(output_path, compressed_img)

    print(f"Compressed image saved as {output_path}")


# Example usage
if __name__ == "__main__":
    input_image_path = 'eldenring.jpg'  # Replace with your JPEG file path
    output_image_path = 'compressed_image.jpg'  # Output file path
    compress_quality = 20  # Set compression quality (0-100)

    compress_image(input_image_path, output_image_path, compress_quality)

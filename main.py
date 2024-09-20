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


def resize_image(image_path, output_path, scale_percent):
    img = cv2.imread(image_path)
    width = int(img.shape[1] * scale_percent / 80)
    height = int(img.shape[0] * scale_percent / 80)
    dim = (width, height)

    resized_img = cv2.resize(img, dim, interpolation=cv2.INTER_AREA)
    cv2.imwrite(output_path, resized_img)
    print(f"Resized image saved as {output_path}")


def add_text_and_shapes(image_path, output_path):
    img = cv2.imread(image_path)

    # Add text to the image
    font = cv2.FONT_HERSHEY_SIMPLEX
    cv2.putText(img, 'Elden Ring Shadow of the Erdtree', (10, 30), font, 5, (255, 255, 255), 2)

    # Draw a rectangle on the image
    start_point = (50, 50)
    end_point = (200, 200)
    color = (0, 255, 0)
    thickness = -1

    img_with_shapes = cv2.rectangle(img.copy(), start_point, end_point, color, thickness)

    cv2.imwrite(output_path, img_with_shapes)
    print(f"Annotated image saved as {output_path}")


# Example usage
if __name__ == "__main__":
    input_image_path = 'eldenring.jpg'  # Replace with your JPEG file path
    output_image_path = 'compressed_image.jpg'  # Output file path
    compress_quality = 20  # Set compression quality (0-100)

    compress_image(input_image_path, output_image_path, compress_quality)

    resize_image('eldenring.jpg', 'resized_image.jpg', 50)

    add_text_and_shapes('eldenring.jpg', 'annotated_image.jpg')
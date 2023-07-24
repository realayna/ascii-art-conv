#include <iostream>
#include <opencv4/opencv2/opencv.hpp>

// Replace these ASCII characters based on intensity or color.
const std::string ASCII_CHARS = "@%#*+=-:. ";

int main() {
    // Load the JPG image using OpenCV
    cv::Mat image = cv::imread("input.jpg");

    if (image.empty()) {
        std::cerr << "Failed to open the image." << std::endl;
        return 1;
    }

    // Convert image to grayscale
    cv::cvtColor(image, image, cv::COLOR_BGR2GRAY);

    // Resize the image (optional)
    cv::resize(image, image, cv::Size(), 0.5, 0.5);

    // Calculate grayscale values and create ASCII art
    std::string asciiArt;
    for (int y = 0; y < image.rows; ++y) {
        for (int x = 0; x < image.cols; ++x) {
            uchar pixel = image.at<uchar>(y, x);
            int index = pixel * ASCII_CHARS.size() / 256;
            asciiArt += ASCII_CHARS[index];
        }
        asciiArt += '\n'; // Add newline after each row
    }

    // Print the ASCII art or save it to a file
    std::cout << asciiArt;

    return 0;
}

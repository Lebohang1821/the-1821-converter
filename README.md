# Document Converter

This project is a Streamlit-based web application that provides various document conversion tools, including image-to-text conversion using OCR.

## Features

- **Image to Text**: Upload an image (PNG, JPG, JPEG) and extract text using OCR.
- **PDF to Text**: (Coming soon)
- **Word to Text**: (Coming soon)

## Setup

### Prerequisites

- Python 3.7 or higher
- pip (Python package installer)

### Installation

1. Clone the repository:

    ```sh
    git clone https://github.com/yourusername/the-1821-converter.git
    cd the-1821-converter
    ```

2. Create and activate a virtual environment (optional but recommended):

    ```sh
    python -m venv venv
    source venv/bin/activate  # On Windows use `venv\Scripts\activate`
    ```

3. Install the required packages:

    ```sh
    pip install -r requirements.txt
    ```

4. Create a `.env` file in the project root directory and add your API keys:

    ```plaintext
    OCR_SPACE_API_KEY=your_ocr_space_api_key
    CLOUDCONVERT_API_KEY=your_cloudconvert_api_key
    ```

### Running the Application

1. Run the Streamlit app:

    ```sh
    streamlit run app.py
    ```

2. Open your web browser and go to `http://localhost:8501` to access the application.

## Usage

- Navigate to the "Image to Text" tab to upload an image and extract text.
- The "PDF to Text" and "Word to Text" tabs are placeholders for future features.

## License

This project is licensed under the MIT License. See the [LICENSE](LICENSE) file for details.
```
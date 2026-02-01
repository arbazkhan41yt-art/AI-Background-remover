# Background Remover Tool

A professional AI-based background removal tool powered by Python, standard libraries, and Streamlit.

## Features
- **One-Click Background Removal**: Uses `rembg` for high-quality AI segmentation.
- **Drag & Drop Interface**: Simple and intuitive upload process.
- **Live Comparison**: Side-by-side view of Original vs. Removed Background.
- **Transparency Grid**: Visual confirmation of transparency.
- **HD Download**: Download your result in PNG format.
- **Clean UI**: Modern, clean aesthetics similar to industry leaders.

## Installation & Running

Since this is a Python application, you need Python installed on your system.

1.  **Install Requirements**
    Open your terminal in this folder and run:
    ```bash
    pip install -r requirements.txt
    ```

2.  **Run the App**
    Start the web interface with:
    ```bash
    streamlit run app.py
    ```

## Deployment (Phase 4)
This app is ready to be hosted on **Hugging Face Spaces**.
1. Create a new Space on Hugging Face.
2. Select "Streamlit" as the SDK.
3. Upload `app.py` and `requirements.txt`.
4. The app will build and go live automatically.

## Note on First Run
When you run the app for the first time, `rembg` will download a pattern recognition model (u2net). This might take a few moments depending on your internet connection.

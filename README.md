# Real-Time-Image-Stitching
 Overview

This project demonstrates how to capture video from multiple RTSP streams (or webcams) and stitch them together using OpenCV. The `RTSPStream` class handles video capture and threading, while the `process_frame` function stitches the frames together. The application uses Python and OpenCV for real-time video processing and stitching.

## Features

- Capture video from multiple RTSP streams or webcams.
- Real-time frame resizing and stitching.
- Multi-threaded video capture for smooth performance.
- Display individual and stitched video feeds.

## Usage

1. **Clone the repository:**

   ```bash
   git clone https://github.com/siri2704/rtsp-stream-stitching.git
   cd rtsp-stream-stitching
Create a virtual environment (optional but recommended):

bash
Copy code
python -m venv venv
source venv/bin/activate  # On Windows use `venv\Scripts\activate`
Install dependencies:

bash
Copy code
pip install opencv-python
Edit the main function in main.py to specify your RTSP sources or webcam device IDs.

python
Copy code
source1 = 2  # Webcam 1 or RTSP URL
source2 = 4  # Webcam 2 or RTSP URL
Run the application:

bash
Copy code
python main.py
Press 'q' to exit the application.
Contributing
Contributions are welcome! Please follow these steps to contribute:

Fork the repository.

Create a new branch for your feature or bug fix:

bash
Copy code
git checkout -b my-feature-branch
Make your changes and commit:

bash
Copy code
git add .
git commit -m "Add feature or fix bug"
Push to your forked repository:

bash
Copy code
git push origin my-feature-branch
Create a pull request from your forked repository.


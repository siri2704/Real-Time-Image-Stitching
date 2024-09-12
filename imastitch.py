import cv2
import threading
import queue

class RTSPStream:
    def __init__(self, source, width=320, height=240, fps=30):
        self.source = source
        self.width = width
        self.height = height
        self.fps = fps
        self.cap = cv2.VideoCapture(self.source)
        if not self.cap.isOpened():
            raise ValueError(f"Error: Cannot open video source {self.source}")
        self.cap.set(cv2.CAP_PROP_FPS, self.fps)
        self.queue = queue.Queue(maxsize=1)
        self.stopped = False
        self.thread = threading.Thread(target=self.update, daemon=True)
        self.thread.start()

    def update(self):
        while not self.stopped:
            ret, frame = self.cap.read()
            if ret:
                frame_resized = cv2.resize(frame, (self.width, self.height))
                if not self.queue.full():
                    self.queue.put(frame_resized, timeout=1)
            else:
                print(f"Warning: Failed to grab frame from {self.source}.")
                self.stopped = True  # Stop thread if capture fails

    def read(self):
        try:
            return self.queue.get_nowait()
        except queue.Empty:
            return None

    def stop(self):
        self.stopped = True
        self.cap.release()
        self.thread.join()

def process_frame(frame1, frame2):
    if frame1 is None or frame2 is None:
        return None

    stitcher = cv2.Stitcher_create()
    status, stitched_img = stitcher.stitch([frame1, frame2])

    if status == cv2.Stitcher_OK and stitched_img is not None:
        return stitched_img
    else:
        print(f"Stitching failed with status code: {status}")
        return None

def main():
    source1 = 2  # Webcam 1
    source2 = 4  # Webcam 2

    try:
        stream1 = RTSPStream(source1, width=320, height=240, fps=30)
        stream2 = RTSPStream(source2, width=320, height=240, fps=30)
    except ValueError as e:
        print(e)
        return

    print("Starting video capture and stitching. Press 'q' to exit.")

    while True:
        frame1 = stream1.read()
        frame2 = stream2.read()

        if frame1 is not None:
            cv2.imshow("Webcam 1", frame1)
        if frame2 is not None:
            cv2.imshow("Webcam 2", frame2)

        stitched_img = process_frame(frame1, frame2)

        if stitched_img is not None:
            cv2.imshow("Stitched Image", stitched_img)

        if cv2.waitKey(1) & 0xFF == ord('q'):
            break

    stream1.stop()
    stream2.stop()
    cv2.destroyAllWindows()
    print("All resources released. Program terminated gracefully.")

if __name__ == "__main__":
    main()

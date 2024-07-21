import cv2
import os
import time

def capture_and_save_snapshot(output_folder, snapshot_interval=5, num_snapshots=None, quality=95):
    os.makedirs(output_folder, exist_ok=True)

    capture = cv2.VideoCapture(0)  # Adjust the parameter (0) if you have multiple cameras

    # Set the desired resolution (1080p)
    capture.set(cv2.CAP_PROP_FRAME_WIDTH, 1920)
    capture.set(cv2.CAP_PROP_FRAME_HEIGHT, 1080)

    snapshot_count = 0
    try:
        while num_snapshots is None or snapshot_count < num_snapshots:
            ret, frame = capture.read()

            if not ret:
                print("Error capturing frame.")
                break

            snapshot_path = os.path.join(output_folder, f"snapshot.jpg")

            # Resize the frame to 1920x1080 (1080p)
            frame = cv2.resize(frame, (1920, 1080))

            cv2.imwrite(snapshot_path, frame, [int(cv2.IMWRITE_JPEG_QUALITY), quality])

            print(f"Snapshot saved: {snapshot_path}")

            snapshot_count += 1
            time.sleep(snapshot_interval)

    except KeyboardInterrupt:
        print("Snapshot capture interrupted.")
    finally:
        capture.release()

if __name__ == "__main__":
    output_folder = "snapshots"
    snapshot_interval = .04  # Adjust the interval between snapshots (in seconds)
    num_snapshots = None  # Set the number of snapshots to capture (None for continuous capture)
    image_quality = 100  # Adjust the quality (0-100, higher is better) for JPEG format

    capture_and_save_snapshot(output_folder, snapshot_interval, num_snapshots, image_quality)

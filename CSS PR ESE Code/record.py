import cv2

def record_video(output_file="output.mp4", duration=10):
    # Open the system camera (usually the default camera)
    cap = cv2.VideoCapture(0)

    # Define the codec and create VideoWriter object
    fourcc = cv2.VideoWriter_fourcc(*'mp4v')
    out = cv2.VideoWriter(output_file, fourcc, 20.0, (640, 480))

    print(f"Recording video for {duration} seconds...")

    start_time = cv2.getTickCount()

    while True:
        ret, frame = cap.read()

        # Write the frame to the output video file
        out.write(frame)

        # Display the resulting frame
        cv2.imshow('Recording', frame)

        # Break the loop if 'duration' seconds have passed
        if cv2.getTickCount() - start_time > duration * cv2.getTickFrequency():
            break

        # Break the loop if 'Esc' key is pressed
        if cv2.waitKey(1) & 0xFF == 27:
            break

    # Release everything when done
    cap.release()
    out.release()
    cv2.destroyAllWindows()

    print(f"Video recorded and saved to {output_file}")

if __name__ == "__main__":
    record_video()

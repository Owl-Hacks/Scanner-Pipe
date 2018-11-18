import cv2


def video_capture():
    cap = cv2.VideoCapture(1)

    while 1:
        ret, frame = cap.read()
        if ret:
            # cv2.circle(frame, (335, 240), 7, (0, 255, 0), -1)
            # cv2.circle(frame, (305, 240), 7, (0, 255, 0), -1)

            # cv2.circle(frame, (320, 240), 7, (0, 255, 0), -1)
            cv2.imshow(str(frame.shape), frame)

        if cv2.waitKey(1) & 0xFF == ord('q'):
            break

        if cv2.waitKey(1) == ord('a'):
            cv2.imwrite('./images/image0.jpg', frame)
            print("picture saved!")
            print("processing...")
            break

    cap.release()
    cv2.destroyAllWindows()

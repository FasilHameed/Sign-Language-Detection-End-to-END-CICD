import os
import cv2
import time
import uuid

Image_path = "CollectedImages"

labels = ['Hello', 'Yes', 'No', 'Thanks', 'IloveYou', 'Please']
number_of_images = 25

for label in labels:
    img_path = os.path.join(Image_path, label)
    os.makedirs(img_path, exist_ok=True)

    cap = cv2.VideoCapture(0)
    print(f"Collecting images for {label}")
    time.sleep(5)

    for imgnum in range(number_of_images):
        ret, frame = cap.read()
        if not ret:
            break
        imagename = os.path.join(img_path, f'{label}.{uuid.uuid1()}.jpg')
        cv2.imwrite(imagename, frame)
        cv2.imshow('frame', frame)
        time.sleep(2)

        if cv2.waitKey(1) & 0xFF == ord('q'):
            break

    cap.release()
    cv2.destroyAllWindows()

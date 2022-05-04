import cv2
import os

save_per_frame = 20
keyword = 'wettissue'

path = f'youtube/{keyword}'
save_path = f'images/youtube/{keyword}'
os.makedirs(f'{save_path}', exist_ok=True)
file_list = os.listdir(path)

index = 1
for video in (file_list):

    cap = cv2.VideoCapture(f'{path}/{video}')

    count = 0
    while cap.isOpened():

        ret, frame = cap.read()

        if ret and count % (save_per_frame * 30) == 0:
            cv2.imwrite(f'{save_path}/{index}.jpg', frame)
            index += 1

        count += 1

        if not ret:
            break

cap.release()
cv2.destroyAllWindows()
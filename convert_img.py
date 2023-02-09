import cv2
import os

image_folder = 'emotion/thirsty/'
video_name = f'{image_folder}video.avi'

images = [img for img in os.listdir(image_folder) if img.endswith(".png")]
frame = cv2.imread(os.path.join(image_folder, images[0]))
height, width, layers = frame.shape

video = cv2.VideoWriter(video_name, 0, 45, (width,height))

for i in range(180):
    video.write(cv2.imread(os.path.join(image_folder, f'frame{i}.png')))

cv2.destroyAllWindows()
video.release()
"""
Extract clip and save it to a file in example_clips directory
"""

import cv2
import os
import argparse


ap = argparse.ArgumentParser()
ap.add_argument('-f', '--file', required=True, help="mp4 video file")
args = vars(ap.parse_args())

input_file = args['file']

cap = cv2.VideoCapture(input_file)

# get fps, width and height
fps = cap.get(cv2.CAP_PROP_FPS)

width = int(cap.get(cv2.CAP_PROP_FRAME_WIDTH))
height = int(cap.get(cv2.CAP_PROP_FRAME_HEIGHT))

start_time, end_time = 38, 46

output_file = os.path.join(os.path.dirname(input_file), 'example_clips/output3.mp4')

fourcc = cv2.VideoWriter_fourcc(*'mp4v')
out = cv2.VideoWriter(output_file, fourcc, fps, (width, height))

frame_count = 0
while cap.isOpened() and frame_count/fps < end_time:
    success, frame = cap.read()
    if frame_count/fps < start_time:
        frame_count += 1
        continue
    if success:
        out.write(frame)
        frame_count += 1
    else:
        break

cap.release()
out.release()
cv2.destroyAllWindows()



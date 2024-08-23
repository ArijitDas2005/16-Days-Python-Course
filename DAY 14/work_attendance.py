import cv2
import face_recognition as fr
import os
import numpy
from datetime import datetime


# Create database
path = 'Employees'
my_images = []
employees_names = []
employees_list = os.listdir(path)

for name in employees_list:
    this_image = cv2.imread(f'{path}\\{name}')
    my_images.append(this_image)
    employees_names.append(os.path.splitext(name)[0])

print(employees_list)


# Encode images
def encode(images):

    # Create new list
    encoded_list = []

    # Convert all images to rgb
    for image in images:
        image = cv2.cvtColor(image, cv2.COLOR_BGRA2BGR)

        # Encode
        encoded = fr.face_encodings(image)[0]

        # Add to the list
        encoded_list.append(encoded)

    # Return encoded list
    return encoded_list


# Record attendance
def record_attendance(person):
    f = open('register.csv', 'r+')
    data_list = f.readlines()
    register_names = []

    for line in data_list:
        newcomer =  line.split(',')
        register_names.append(newcomer[0])

    if person not in register_names:
        right_now = datetime.now()
        string_right_now = right_now.strftime('%H:%M:%S')
        f.writelines(f'\n{person},{string_right_now}')


encoded_employees_list = encode(my_images)

# Take a webcam picture
capture = cv2.VideoCapture(0, cv2.CAP_DSHOW)

# Read the captured image
success, image = capture.read()

if not success:
    print('Capture could not be taken')
else:
    # Recognise a face in that capture
    captured_face = fr.face_locations(image)

    # Encode the captured face
    encoded_captured_face = fr.face_encodings(image, captured_face)

    # Search for a match
    for face, location_face in zip(encoded_captured_face, captured_face):
        matches = fr.compare_faces(encoded_employees_list, face)
        distances = fr.face_distance(encoded_employees_list, face)

        print(distances)

        match_index = numpy.argmin(distances)

        # Show coincidences if any
        if distances[match_index] > 0.6:
            print('Does not match any of our employees')
        else:
            # Search for the name of the employee found
            employees_name = employees_names[match_index]

            y1, x2, y2, x1 = location_face
            cv2.rectangle(image,
                          (x1, y1),
                          (x2, y2),
                          (0, 255, 0),
                          2)
            cv2.rectangle(image,
                          (x1, y2 - 35),
                          (x2, y2),
                          (0, 255, 0),
                          cv2.FILLED)
            cv2.putText(image,
                        employees_name,
                        (x1 + 6, y2 - 6),
                        cv2.FONT_HERSHEY_COMPLEX,
                        1,
                        (255, 255, 255),
                        2)

            record_attendance(employees_name)

            # Show the image obtained
            cv2.imshow('Web Image', image)

            # Keep window open
            cv2.waitKey(0)

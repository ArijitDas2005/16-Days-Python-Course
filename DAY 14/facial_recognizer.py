import cv2
import face_recognition as fr


# Load Images
control_picture = fr.load_image_file('PictureA.jpg')
test_picture = fr.load_image_file('PictureB.jpg')

# Transform images into rgb
control_picture = cv2.cvtColor(control_picture, cv2.COLOR_BGRA2BGR)
test_picture = cv2.cvtColor(test_picture, cv2.COLOR_BGRA2BGR)

# Locate control face
face_A_location = fr.face_locations(control_picture)[0]
coded_face_A = fr.face_encodings(control_picture)[0]

# Locate test face
face_B_location = fr.face_locations(control_picture)[0]
coded_face_B = fr.face_encodings(control_picture)[0]

# Show rectangles
cv2.rectangle(control_picture,
              (face_A_location[3], face_A_location[0]),
              (face_A_location[1], face_A_location[2]),
              (0, 255, 0),
              2)

# Show rectangles
cv2.rectangle(control_picture,
              (face_A_location[3], face_A_location[0]),
              (face_A_location[1], face_A_location[2]),
              (0, 255, 0),
              2)

cv2.rectangle(test_picture,
              (face_B_location[3], face_B_location[0]),
              (face_B_location[1], face_B_location[2]),
              (0, 255, 0),
              2)

# Perform comparison
result = fr.compare_faces([coded_face_A], coded_face_B)

# Measurement of distances
distance = fr.face_distance([coded_face_A], coded_face_B)

# Show results
cv2.putText(test_picture,
            f'{result} {distance.round(2)}',
            (50, 50),
            cv2.FONT_HERSHEY_COMPLEX,
            1,
            (0, 255, 0),
            2)

# Show images
cv2.imshow('My Control Picture', control_picture)
cv2.imshow('My Test Picture', test_picture)

# Keep the program working
cv2.waitKey(0)

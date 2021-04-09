
import boto3
import json
import numpy as np


# # Load the default font

# Create a Rekognition client
def detect_faces(photo):
    print('Detecting faces.')
    # client=boto3.client('rekognition')

# # vickiesbucket = "vickiesbucket"
# # vickie = "vickie"
#     response = client.detect_faces(
#         Image={
#          'S3Object':{
# #              'Bucket':vickiesbucket,
# #              'Name':vickie
#             'Bytes': photo },
       
#     Attributes=['ALL']
#     )
#     return response
# #Initialize camera 
# pygame.init()
# pygame.camera.init()

# cam = Device()
# cam.getImage(timestamp=0).resize((320, 240)).save('demo.jpg', quality=80)

# # screen = pygame.display.set_mode((400,300))

# # print(pygame.camera.list_cameras())
# # cam = pygame.camera.Camera(pygame.camera.list_cameras()[0])

# # cam.start()
# # print("start")

# # print(cam.get_image())

# # while True:
# # 	for e in pygame.event.get():


# # cam = cv2.VideoCapture(0)
# # if not (cam.isOpened()):

# #     print('Could not open video device')
# # cv2.namedWindow("test")

# # while True:
# #     ret, frame = cam.read()
# #     cv2.imshow("test", frame)
# #     if not ret:
# #         break
# #     k = cv2.waitKey(1)

# #     if k%256 == 27:
# #         # ESC pressed
# #         print("Escape hit, closing...")
# #         break
# #     elif k%256 == 32:
# #         # SPACE pressed
# #         # print(detect_faces(cv2.imencode('.jpg', frame)[1].tostring()))
     
# #         response = detect_faces(cv2.imencode('.jpg', frame)[1].tobytes())
# #         print(response)
          
#     for faceDetail in response['FaceDetails']:
#         print('Emotions: \t Confidence\n')
#     for emotion in faceDetail['Emotions']:

#         print(str(emotion['Type']) + '\t\t' + str(emotion['Confidence']))
#         print('\n')
# #Release control of the webcam and close window     
# cam.release()
# cv2.destroyAllWindows()

# # for faceDetail in response['FaceDetails']:
# #     print(faceDetail['Eyeglasses'])

# # for faceDetail in response['FaceDetails']:
# #     print('Emotions: \t Confidence\n')
# #     for emotion in faceDetail['Emotions']:

# #         print(str(emotion['Type']) + '\t\t' + str(emotion['Confidence']))
# #         print('\n')

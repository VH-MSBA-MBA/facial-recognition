import boto3


# Create a Rekognition client
def detect_faces(photo):
    client = boto3.client('rekognition')

    response = client.detect_faces(
        Image={'Bytes': photo},
        Attributes=['ALL']
    )
    return response

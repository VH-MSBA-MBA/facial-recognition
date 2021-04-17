import boto3
import base64


# Create a Rekognition client
def detect_faces(photo):
    client = boto3.client('rekognition')
    with open('imageToSave.png', 'wb') as fh:
        fh.write(base64.decodebytes(photo))
    with open('imageToSave.png', 'rb') as image:
        response = client.detect_faces(
            Image={'Bytes': image.read()},
            Attributes=['ALL']
        )

    emotion = response['FaceDetails'][0]['Emotions'][0]['Type']
    
    if (emotion == 'HAPPY'):
        comment = 'You look cheery, have a Qoo!'
        url = 'https://www.coolstuffjapan.com/image/cache/products/drinks/soft/dr0041-800x800.jpg'
    elif (emotion == 'CALM'):
        comment = 'You look calm, enjoy this warm tea.'
        url = 'https://www.itoen-global.com/image/travelers/oiocha/pic_sec01_product_02_sp.png'
    elif (emotion == 'ANGRY'):
        comment = 'You look angry, settle down with a vitamin packed CC Lemon.'
        url = 'https://www.suntory.com/brands/brands/img/CCLemon_190528.jpg'
    elif (emotion == 'DISGUSTED'):
        comment = 'You look disgusted, try this interesting pancake drink!'
        url = 'https://i.pinimg.com/originals/0a/c7/ec/0ac7ec419a4bc216e51a4a3ad862aa30.jpg'
    elif (emotion == 'SAD'):
        comment = 'You look sad, enjoy this Natchan drink to make you smile!'
        url = 'https://www.suntory.com/brands/img/Natchan.jpg'
    elif (emotion == 'FEAR'):
        comment = 'You look fearful, try this cucumber Pepsi to take you mind off things...'
        url = 'https://japantoday-asset.scdn3.secure.raxcdn.com/img/store/eb/d6/83c32df81bf0b1bb7b92ea6767de5a5d15ff/pepsi1.jpg'
    elif (emotion == 'SURPRISED'):
        comment = 'You look surprised, how about a nice, cold, Bikkle.'
        url = 'http://cdn.shopify.com/s/files/1/1423/1710/products/pocket-cvs_4901777285347_large.jpg?v=1548040111'
    elif (emotion == 'CONFUSED'):
        comment = 'You look confused. Have a Boss Coffee.'
        url = 'https://m.media-amazon.com/images/I/41o2bpqL7PL._SS250_.jpg'
    else:
        comment = 'Unable to read emotion.'
        url = ''
        
    return {
        'comment': comment,
        'rekognition_response': response,
        'url': url,
    }

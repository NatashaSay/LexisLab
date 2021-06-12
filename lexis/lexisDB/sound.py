import boto3
from tempfile import TemporaryFile
import os

def make_speech(text):


    print('make_speech')
    print(text)
    polly_client = boto3.Session(
        aws_access_key_id=os.environ.get('AWS_KEY'),                     
        aws_secret_access_key=os.environ.get('AWS_SECRET_KEY'),
        region_name='us-east-2').client('polly')


    response = polly_client.synthesize_speech(
        VoiceId='Marlene',
        OutputFormat='mp3', 
        #Text = 'Hallo, mein Name ist Marlene. Ich werde jeden Text vorlesen, den Sie eingeben.'
        Text = text
    )

    file = open('speech.mp3', 'wb')
    file.write(response['AudioStream'].read())
    file.close()

    print(type(response['AudioStream']))

    return file



import os
import httplib2
from apiclient.discovery import build
from oauth2client import client
from oauth2client.service_account import ServiceAccountCredentials


def publish(email, keyfile, package_name, track, track_status, apkfile):
    credentials = ServiceAccountCredentials.from_p12_keyfile(
        email,
        keyfile,
        scopes=['https://www.googleapis.com/auth/androidpublisher'])
    http = credentials.authorize(httplib2.Http())
    service = build('androidpublisher', 'v3', http=http)

    insert_request = service.edits().insert(body={}, packageName=package_name)
    insert_response = insert_request.execute()
    edit_id = insert_response['id']

    print(f'Edits.insert response. {insert_response}')

    upload_response = service.edits().apks().upload(
        editId=edit_id, packageName=package_name, media_body=apkfile).execute()
    version_code = upload_response['versionCode']

    print(f'Edits.apks.upload response. {upload_response}')

    update_response = service.edits().tracks().update(
        editId=edit_id,
        track=track,
        packageName=package_name,
        body={u'track': track, u'releases': [{u'versionCodes': [version_code], u'status': track_status}]}).execute()

    print(f'Edits.tracks.update response. {update_response}')

    commit_response = service.edits().commit(
        editId=edit_id, packageName=package_name).execute()

    print(f'Edits.commit response. {commit_response}')
    print(f'[GooglePlayConsole] versionCode={version_code} has been uploaded to {track} as {track_status}.')


if __name__ == '__main__':
    email        = 'sample@sample.iam.gserviceaccount.com'
    keyfile      = os.path.dirname(__file__) + '/key.p12'
    package_name = 'com.example'
    track        = 'alpha'
    track_status = 'draft'
    apkfile      = os.path.dirname(__file__) + '/sample.apk'
    publish(email, keyfile, package_name, track, track_status, apkfile)

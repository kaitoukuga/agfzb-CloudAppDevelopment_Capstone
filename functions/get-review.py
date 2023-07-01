from ibm_cloud_sdk_core.authenticators import IAMAuthenticator
from ibm_cloud_sdk_core import ApiException
from ibmcloudant.cloudant_v1 import CloudantV1
import json

def main(params):
    authenticator = IAMAuthenticator('TSgWbTjzq6jssiS84dyhno1-8Ndsegw233QlFv51JGLw')
    cloudant = CloudantV1(authenticator=authenticator)
    cloudant.set_service_url('https://28059ad8-d624-49da-9bc2-b47b4fe4f5cf-bluemix.cloudantnosqldb.appdomain.cloud')

    if 'dealerId' in params:
        dealership = int(params['dealerId'])
        try:
            response = cloudant.post_find(
                db='reviews',
                selector={'dealership': dealership}
            )
            result = response.result
            code = 200 if len(result['docs']) > 0 else 404
            return {
                'statusCode': code,
                'headers': {'Content-Type': 'application/json'},
                'body': result['docs']
            }
        except ApiException as e:
            print(f"Error: {e.code} - {e.message}")
            return {
                'statusCode': 500,
                'headers': {'Content-Type': 'application/json'},
                'body': {'error': 'Internal Server Error'}
            }
    else:
        try:
            response = cloudant.post_all_docs(
                db='reviews',
                include_docs=True
            )
            result = response.result
            code = 200 if len(result['rows']) > 0 else 404
            reviews = [row['doc'] for row in result['rows']]
            return {
                'statusCode': code,
                'headers': {'Content-Type': 'application/json'},
                'body': reviews
            }
        except ApiException as e:
            print(f"Error: {e.code} - {e.message}")
            return {
                'statusCode': 500,
                'headers': {'Content-Type': 'application/json'},
                'body': {'error': 'Internal Server Error'}
            }

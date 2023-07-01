from ibm_cloud_sdk_core.authenticators import IAMAuthenticator
from ibm_cloud_sdk_core import ApiException
from ibmcloudant.cloudant_v1 import CloudantV1

def main(dict):
    authenticator = IAMAuthenticator('TSgWbTjzq6jssiS84dyhno1-8Ndsegw233QlFv51JGLw')
    cloudant = CloudantV1(authenticator=authenticator)
    cloudant.set_service_url('https://28059ad8-d624-49da-9bc2-b47b4fe4f5cf-bluemix.cloudantnosqldb.appdomain.cloud')
    response = cloudant.post_document(db='reviews', document=dict["review"]).get_result()
    
    try:
        result= {
        'headers': {'Content-Type':'application/json'},
        'body': {'data':response}
        }
        return result
    except ApiException as e:
        print(f"Error: {e.code} - {e.message}")
        return {
            'statusCode': 500,
            'headers': {'Content-Type': 'application/json'},
            'body': {'error': 'Internal Server Error'}
        }

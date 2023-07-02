import sys 
from ibmcloudant.cloudant_v1 import CloudantV1
from ibm_cloud_sdk_core.authenticators import IAMAuthenticator

def main(dict): 
    authenticator = IAMAuthenticator("TSgWbTjzq6jssiS84dyhno1-8Ndsegw233QlFv51JGLw")
    service = CloudantV1(authenticator=authenticator)
    service.set_service_url("https://28059ad8-d624-49da-9bc2-b47b4fe4f5cf-bluemix.cloudantnosqldb.appdomain.cloud")
    response = service.post_find(
                db='reviews',
                selector={'dealership': {'$eq': int(dict['dealerId'])}},
            ).get_result()
    try: 
        # result_by_filter=my_database.get_query_result(selector,raw_result=True) 
        result= {
            'headers': {'Content-Type':'application/json'}, 
            'body': {'data':response} 
            }        
        return result
    except:  
        return { 
            'statusCode': 404, 
            'message': 'Something went wrong'
            }
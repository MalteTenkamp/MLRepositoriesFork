""" Example: Shows how to create and manage API keys. """

import urllib3

import feersum_nlu
from feersum_nlu.rest import ApiException
from examples import feersumnlu_host, feersum_nlu_auth_token

# Configure API key authorization: APIKeyHeader
configuration = feersum_nlu.Configuration()

# configuration.api_key['AUTH_TOKEN'] = feersum_nlu_auth_token
configuration.api_key['X-Auth-Token'] = feersum_nlu_auth_token  # Alternative auth key header!

configuration.host = feersumnlu_host

api_instance = feersum_nlu.ApiKeysApi(feersum_nlu.ApiClient(configuration))

create_details = feersum_nlu.ApiKeyCreateDetails(desc="Test API key.")

print()

try:
    api_key_to_delete = "Some existing API key."

    print("Delete specific named API key:")
    api_response = api_instance.api_key_del(api_key_to_delete)
    print(" type(api_response)", type(api_response))
    print(" api_response", api_response)
    print()

except ApiException as e:
    print("Exception when calling an api key operation: %s\n" % e)
except urllib3.exceptions.HTTPError as e:
    print("Connection HTTPError! %s\n" % e)

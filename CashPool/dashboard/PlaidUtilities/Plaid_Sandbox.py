import plaid_access_file
import plaid
from plaid.model.products import Products
from plaid.model.country_code import CountryCode
from plaid.api import plaid_api
from plaid.model.link_token_create_request import LinkTokenCreateRequest
from plaid.model.link_token_create_request_user import LinkTokenCreateRequestUser

import time
import jsonify
import json

# Available environments are
# 'Production'
# 'Development'
# 'Sandbox'
configuration = plaid.Configuration(
    host=plaid_access_file.PLAID_HOST,
    api_key={
        'clientId': plaid_access_file.PLAID_CLIENT_ID,
        'secret': plaid_access_file.PLAID_SANDBOX_KEY,
    }
)

api_client = plaid.ApiClient(configuration)
client = plaid_api.PlaidApi(api_client)


def generate_link_token():

    try:
        request = LinkTokenCreateRequest(
            products=[Products("income_verification")],
            client_name="Plaid Quickstart",
            country_codes=[CountryCode("US")],
            language='en',
            user=LinkTokenCreateRequestUser(
                client_user_id=str(time.time())
            )
        )

        request['redirect_uri'] = plaid_access_file.PLAID_REDIRECT_URL

        # create link token
        response = client.link_token_create(request)
        if "link_token" in response:
            return response["link_token"]
    except plaid.ApiException as e:
        print(json.loads(e.body))
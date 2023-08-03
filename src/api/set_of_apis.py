import json

import requests

class SetOfApis:

    def __init__(self, application_parameters, key, phone_or_qr, account_type):
        self.domain = application_parameters["domain"]
        self.attraction = application_parameters["attraction"]
        self.environment = application_parameters["environment"]
        self.site_code = application_parameters["site_code"]
        # self.country_code = GuestParameters.get_country_code_without_plus_prefix(key)
        self.phone_or_qr = phone_or_qr
        self.account_type = account_type

    def api_create_qr_user_request(self):
        end_point = f'https://api-{self.environment}.pomvom.com/api/v3/accounts'
        print("print end point: " + str(end_point))
        data = {"domain": self.domain,
                "uniqueId": self.phone_or_qr}

        create_qr_user = requests.post(end_point,
                                       headers={"x-api-key": "system", "x-client-id": "system",
                                                "Content-Type": "application/json"},
                                       data=json.dumps(data),
                                       verify=False)
    
        response = create_qr_user.status_code
        return response
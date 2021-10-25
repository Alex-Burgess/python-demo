import pytest


@pytest.fixture
def api_event():
    """ Generates API GW Event"""

    return {
        "resource": "/lists",
        "path": "/lists",
        "httpMethod": "GET",
        "queryStringParameters": None,
        "multiValueQueryStringParameters": None,
        "pathParameters": None,
        "stageVariables": None,
        "requestContext": {
            "resourceId": "sgzmgr",
            "resourcePath": "/lists",
            "httpMethod": "GET",
            "extendedRequestId": "BQGojGkBjoEFsTw=",
            "requestTime": "08/Oct/2019:16:22:40 +0000",
            "path": "/test/lists",
            "accountId": "123456789012",
            "protocol": "HTTP/1.1",
            "stage": "test",
            "domainPrefix": "4sdcvv0n2e",
            "requestTimeEpoch": 1570551760227,
            "requestId": "a3d965cd-a79b-4249-867a-a03eb858a839",
            "identity": {
                "cognitoIdentityPoolId": None,
                "accountId": None,
                "cognitoIdentityId": None,
                "caller": "AROAZUFPDMJL6KJM4LLZI:CognitoIdentityCredentials",
                "sourceIp": "31.49.230.217",
                "principalOrgId": "o-d8jj6dyqv2",
                "accessKey": None,
                "cognitoAuthenticationType": None,
                "cognitoAuthenticationProvider": None,
                "userArn": None,
                "userAgent": "Mozilla/5.0 (Linux; Android 6.0; Nexus 5 Build/MRA58N) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/77.0.3865.90 Mobile Safari/537.36",
                "user": None
            },
            "domainName": "4sdcvv0n2e.execute-api.eu-west-1.amazonaws.com",
            "apiId": "4sdcvv0n2e"
        },
        "body": None,
        "isBase64Encoded": "false"
    }


@pytest.fixture
def food_api_response():
    return {
        "establishments": [
          {
              "AddressLine1": "Cambridge",
              "AddressLine2": "Cambridgeshire",
              "AddressLine3": "",
              "AddressLine4": "",
              "BusinessName": "196",
              "BusinessType": "Restaurant/Cafe/Canteen",
              "BusinessTypeID": 1,
              "ChangesByServerID": 0,
              "Distance": None,
              "FHRSID": 507136,
              "LocalAuthorityBusinessID": "PI/000081182",
              "LocalAuthorityCode": "027",
              "LocalAuthorityEmailAddress": "env.health@cambridge.gov.uk",
              "LocalAuthorityName": "Cambridge City",
              "LocalAuthorityWebSite": "http://www.cambridge.gov.uk",
              "NewRatingPending": False,
              "Phone": "",
              "PostCode": "CB1 3NF",
              "RatingDate": "2015-01-22T00:00:00",
              "RatingKey": "fhrs_5_en-gb",
              "RatingValue": "5",
              "RightToReply": "",
              "SchemeType": "FHRS",
              "geocode": {
                  "latitude": "52.197345",
                  "longitude": "0.145033"
              },
              "links": [
                  {
                      "href": "http://api.ratings.food.gov.uk/establishments/507136",
                      "rel": "self"
                  }
              ],
              "meta": {
                  "dataSource": None,
                  "extractDate": "0001-01-01T00:00:00",
                  "itemCount": 0,
                  "pageNumber": 0,
                  "pageSize": 0,
                  "returncode": None,
                  "totalCount": 0,
                  "totalPages": 0
              },
              "scores": {
                  "ConfidenceInManagement": 5,
                  "Hygiene": 5,
                  "Structural": 0
              }
          }
        ]
    }

import requests
def ocr_space_file(filename, api_key ="f69d94d84f88957",overlay=False, language="eng"):
    payload = {"isOverlayRequired": overlay,
                "apikey":api_key,
                "language": language,
                }

    with open(filename, 'rb') as f:
        r  =requests.post('https://api.ocr.space/parse/image',
                            files = {filename: f},
                            data = payload,
                            )

    return r.content.decode()

test_file = ocr_space_file(filename="McKesson.jpg")
print("hey")

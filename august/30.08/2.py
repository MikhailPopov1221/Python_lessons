import requests


url = "https://www.google.com/search"

params = {
    "q":"что покушать на ужин"
}

headers = {
    "user-agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/139.0.0.0 Safari/537.36",
    "cookie": "__Secure-ENID=27.SE=jETy_ZVpk7St2dEqhENfeToJ2L46G1tERaVEEdq6ViLiX1dD1Gh6EGhkuZ_A3KTVtVfZpCwX5ti3Xa7gLm5KOKeVkE5HWJDiv-iADVOLryTqjwtGC5EfyV6T1Vird74AoI-n-6eUboHJpbxa6FZcHnEfBVV3BEYV18cbr72eeTS1lI-ChY-IKlEMsu8QjFTmxjopAb2kLxJ7SAmifg49TnM_2BZPROO8tnCVjNuTxFFF8_UY; AEC=AVh_V2hMZ1jQOP3ljGQs7ZEZ4PRYhuinDsJaxiDLiYeMzfaPKGRXv7CuLg; NID=525=pOpephKfxbSvRpGatVlhDfIGbl-Ne1SS2WhrzMITZl4aCzMfr1MI4-mEhFHiSxo8ztZlyQ-7M9mZRYo2SagWztSe7kOfRmMPSNwGzCAjQLBPRIU0Ip3VXlaOBvC2aqwl6UxXWPh-TUW_m-2XvwZqyXzqBCla05msgURbIe450588WGLeLuUdgYJ_7ldKUoGF0Xvm2gfQQTnyYaSvP1aY6L60v9f80jtemivfskgn0_J3LluyG5IirjdmxJd6aXHtjP6lnjA-hy68-6DG_NXXae6jpNjczdUVAl9L0EI5NVaGl-O96oWLcZemo8L_PUgEMpBuLUxb5623dt5JbiJ_1QE71fqy3bx-41Y-gX2t3i7Jye-P-Zu2afCxioTVC7YRiZHHDZsEEhEzzI6s4KF4RBGj98sy6TQSyk9QUxu0FoZE3-LuUWxAHtvMnPsmbnDiV0Xy-x3BjiWEgdzoljrT"
}


response = requests.get(
    url=url,
    params=params,
    headers=headers
    )

print(f"Код ответа: {response.status_code}")

print(f"Тело страницы: {response.text}")

with open("2.html", "w", encoding="utf-8") as fl:
    fl.write(response.text)
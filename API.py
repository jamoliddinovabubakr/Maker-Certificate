import requests


# from pprint import pprint as print

def PnflCheck(PNFL, ID):
    status = 0
    print(PNFL)
    print(ID)

    # Making our request
    token = {"Authorization": "Token 7b51e1a81f13b6baed76d846ea0b30e66f97cf42"}
    # jshshr = 30510906050036
    # course_id = 1
    endpoint = f"https://ejournal.uzbmb.uz/malaka/api/?jshshr={PNFL}&course={ID}"


    response = requests.get(endpoint, headers=token)
    print(response.status_code)
    if response.status_code == 200:
        print(response.json()['pdf_url'])
    
    elif response.status_code == 401 and response.status_code == 400:
        return "К сожалению, нам не удалось обработать ваш запрос. Проверьте введенные данные и повторите попытку"
    
    elif response.status_code == 404:
        return "Siz bu kursda qatnashmagansiz!\nВы не участвовали на этих курсах!"
        
PnflCheck(30510906050036, 1)
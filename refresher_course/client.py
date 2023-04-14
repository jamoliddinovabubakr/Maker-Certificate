import requests

jshshr = 32406995940027
course_id = 2

token = {"Authorization": "Token 5a66e5ff13410a657942043654e4d8e762c25781"}
endpoint = f"https://ejournal.uzbmb.uz/malaka/api/?jshshr={jshshr}&course={course_id}"
response = requests.post(endpoint, headers=token)
if requests.status_codes == 401:
    print("Ro'yxatdan o'tmadingiz!!!")
if response.status_code == 200:
    print("token invalid")
else:
    get_response = requests.get(endpoint, headers=token)
    data = get_response.json()
    try:
        print(data[0]['pdf_certificate'])
    except IndexError:
        print("Bu kursda o'qimagansiz")

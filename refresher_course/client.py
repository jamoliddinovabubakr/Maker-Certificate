import requests

jshshr = 30510906050036
course_id = 1

token = {"Authorization": "Token 7b51e1a81f13b6baed76d846ea0b30e66f97cf42"}
endpoint = f"https://ejournal.uzbmb.uz/malaka/api/?jshshr={jshshr}&course={course_id}"

if requests.status_codes == 401:
    print("Ro'yxatdan o'tmadingiz!!!")
else:
    get_response = requests.get(endpoint, headers=token)
    data = get_response.json()
    print(data)
import requests

jshshr = 41605975930036
course_id = 1
# endpoint = f"http://192.168.0.87:443/api/certificate/?jshshr={jshshr}&course={course_id}/"

token = {"Authorization": "Token 68fe70d7efd6a552208165fef4f4121f4982da9f"}
endpoint = f"http://127.0.0.1:8000/api/certificate/?jshshr={jshshr}&course={course_id}"
get_response = requests.get(endpoint, headers=token)

data = get_response.json()
print(data[0]['pdf_certificate'])

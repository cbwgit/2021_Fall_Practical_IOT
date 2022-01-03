import requests



def lineMessage(msg):


    headers = {

        "Authorization": "Bearer " +"YawT60FP43BLQHIkmMPuj0Xq7fWpPxyVsPuLbZukJej",

        "Content-Type" : "application/x-www-form-urlencoded"

    }



    payload = {'message': msg }

    r = requests.post("https://notify-api.line.me/api/notify", headers = headers, params = payload)

    return r.status_code

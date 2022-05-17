import requests



payload =  {'strategy': 'local', 'login': 'user_admin', 'password': 'admin123'}

r_auth =  requests.post('http://10.10.29.110/api/v1/authentication', data=payload)

Token_r = r_auth.json()
#print(Token_r['accessToken'])
#print(type(Token_r['accessToken']))

head = {'Authorization': Token_r['accessToken']}

url_2 = 'http://10.10.29.110/api/v1/discretejournal'



response = requests.get(url_2, headers=head, timeout=10)
#dict_ntp = response.json()[len(response.json())-1]
#print(type(response.json()[len(response.json())-1]))
print(response.json()[0])
print(len(response.content))

#print(response.json())
#Sprint(response.url)


{'Server': 'nginx/1.10.3', 'Date': 'Thu, 31 Mar 2022 11:50:54 GMT',
'Content-Type': 'application/json; charset=utf-8', 'Transfer-Encoding': 'chunked',
'Connection': 'keep-alive', 'X-DNS-Prefetch-Control': 'off', 'Expect-CT': 'max-age=0',
'X-Frame-Options': 'SAMEORIGIN', 'Strict-Transport-Security': 'max-age=15552000; includeSubDomains',
'X-Download-Options': 'noopen', 'X-Content-Type-Options': 'nosniff',
'X-Permitted-Cross-Domain-Policies': 'none', 'Referrer-Policy': 'no-referrer',
'X-XSS-Protection': '0', 'Access-Control-Allow-Origin': '*', 'Allow': 'GET',
'Vary': 'Accept, Accept-Encoding', 'ETag': 'W/"3662-LhA4YgooN+7Ts7Cy5s3LEr+cy70"',
'Content-Encoding': 'gzip'}
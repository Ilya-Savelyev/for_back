# data = {
#     "table_id": "EDW_GP_CORE_1_ADS_DIM_TST_1",
#     "component_name": "CDWH_GP",
#     "is_test": "True"
# }

payload = 'author=1&comment_status=open&content=test%20for%20test&date=2025-02-18T13%3A11%3A25&date_gmt=2025-02-18T13%3A11%3A25&format=standard&ping_status=open&slug=test123321&status=publish&sticky=false&title=test%20for%20test'
headers = {
  # 'authorization': 'Basic dGVzdF9iYWNrZW5kOnRlc3RfYmFja2VuZA==',
  # 'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/132.0.0.0 Safari/537.36',
  'accept': 'application/json',
  'Content-Type': 'application/x-www-form-urlencoded'
  # 'host': 'testbackend.local',
  # 'Authorization': 'Basic dGVzdF9iYWNrZW5kOnRlc3RfYmFja2VuZA==',
  # 'Cookie': 'wordpress_test_cookie=WP%20Cookie%20check'
}
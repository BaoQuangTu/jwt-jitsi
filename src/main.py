import jwt_utils
import os
from payload import *

# token = jwt_utils.generate_token('')
# jwt_utils.validate_token_sso("eyJ0eXAiOiJKV1QiLCJhbGciOiJSUzI1NiJ9.eyJpc3MiOiJhdXRoMCIsImNvbnRleHQiOiJ7XCJpZFwiOlwiMVwiLFwiZmlyc3ROYW1lXCI6XCJRdWFuZyBU4butXCIsXCJsYXN0TmFtZVwiOlwiQuG6o29cIixcIndlYnNpdGVcIjpcImd1aXRhcmthZi52blwifSJ9.rqbj4W1YU_hQ8DLTGaRku8sTVjWqedtOMSILO5jZjfqbdJTD9SC_Cf4iMmZvF_Rz2sjwl_br7KIvVPm9dpkwwpBU9AL14Lz-lbPaHI-HYXDApAzL1NlrtkG5uYmLDX7cHsUl2hIqzlshKFGxvUTVF8nX9ZkTVd5hcZEN1XRD-tRvzX3xoiHuW1o-fndmpvTao6XkjJrsFSOYWk5G7GI7gWSKHfBQ0HeOuW5tgww1jwC_iQQaCJ8iwFsiu9DuTZINPJDDamIN-634dqpeuRhcZDjjXityg1JMB421-GwiKPCwQmkIWgLB9CzF3E08kjAC8RjV4PenNzCmvB7SpHKdkg")

print(os.environ['HOME'])

user = User("abcd:a1b2c3-d4e5f6-0abc1-23de-abcdef01fedcba", "Bao Quang Tu", "https:/gravatar.com/avatar/abc123", "baoquangtu150707@gmail.com")
context = Context(user)
pay = Payload(context, "jitsi-hyperlogy", "chat app", "*", 4752455808684)

payloadJSON = json.dumps(pay, indent=4, cls=PayloadEncoder)
print(payloadJSON['context'])
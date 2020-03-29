#SOURCE: https://leetcode.com/problems/defanging-an-ip-address/
address = input()
print('"' + address.replace(".","[.]") + '"')

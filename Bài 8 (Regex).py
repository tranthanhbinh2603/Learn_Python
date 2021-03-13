str1 = "<title>Đây là nội dung bài học số 1 chương 2</title>"

## Example 1
# import re
# print(re.sub('gr(.*)','like',str1))

##Example 2
# import re
# print(re.split(' ',str1))

## Example 3:
import re
print(re.findall('<title>(.*?)</title>',str1))
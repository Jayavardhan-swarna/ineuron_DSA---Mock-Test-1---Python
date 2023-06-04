def firstUniqChar(s):
  count = {}
  for i in s:
    if i in count:
      count[i] += 1
    else:
      count[i] = 1
      
  for j, i in enumerate(s):
    if count[i] == 1:
      return j

  return -1


inp1 = "leetcode"
inp2 = "loveleetcode"
inp3 = "aabb"
print(firstUniqChar(inp1))
print(firstUniqChar(inp2))
print(firstUniqChar(inp3))
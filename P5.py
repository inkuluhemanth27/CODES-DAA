def findContentChildren(g, s):
    g.sort()
    s.sort()
    i = j = 0
    content_children = 0

    while i < len(g) and j < len(s):
        if s[j] >= g[i]:
            content_children += 1
            i += 1
        j += 1

    return content_children
g = [1, 2, 3]
s = [1, 1]
print(findContentChildren(g, s))

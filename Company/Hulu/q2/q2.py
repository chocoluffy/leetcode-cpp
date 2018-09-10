N = int(raw_input().strip())
pts = []
for _ in range(N):
    pts.append(int(raw_input().strip())/100)
# print pts
pts = sorted(pts)
cnt = 0
for i in range(len(pts)):
    remain = pts[i:]
    if len(remain) < 2:
        break
    else:
        line = 180 + i
        for j in range(i+1, len(pts)):
            if pts[j] > line:
                num = len(pts) - j
                cnt += (num * (num - 1)) / 2
                break
            for k in range(j+1, len(pts)):
                if i < pts[j] < line and line < pts[k] < 360:
                    break
                if (i < pts[j] < line and i < pts[k] < line) or (line < pts[j] < 360 and line < pts[k] < 360):
                    cnt += 1
print cnt
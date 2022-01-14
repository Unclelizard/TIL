
def dust_quality(dust):


if 150<dust:
    print('매우나쁨')

elif 80<dust<150:
    print('나쁨')

elif 30<dust<80:
    print("보통")

else:
    print("좋음")

dust_quality(100)

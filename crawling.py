from collecting import CollectingSource

keyword = input('수집하고자 하는 종류를 입력하세요 : ')

while True:
    
    try:
        crawling_num = int(input('수집하고자 하는 이미지 개수를 입력하세요 : '))
        break
    except:
        print('정수를 입력해주세요')

while True:
    
    try:
        collect_option = int(input('수집하려는 곳의 번호 선택해주세요(ex. 1)\n1.pixabay\n2.unsplash\n3.quit\n----> '))
    except:
        print('정수를 입력해주세요')
        continue

    if collect_option == 1:
        collect = CollectingSource(keyword, crawling_num)
        collect.pixabay()

    elif collect_option == 2:
        collect = CollectingSource(keyword, crawling_num)
        collect.unsplash()

    elif collect_option == 3:
        break

    else:
        print('주어진 번호 중에 선택해주세요')

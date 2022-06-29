L=[1, 9, 4, 2]

print("L =", L)
print("리스트 L의 원소를 내림차순으로 정렬한 리스트 M =", sorted(L, reverse=True))
print("리스트 L에 enumerate() 함수 실행한 결과:", list(enumerate(L)))
l=L.pop()
print("리스트 L에서 마지막 원소를 제거 & 제거한 데이터 출력 :",L, l)
L.append(l)
print("제거한 데이터 다시 리스트 L에 추가 :", L)

a=int(input("Enter int data : "))
L.insert(0, a)
print("입력받은 정수 데이터를 리스트의 첫번째 데이터로 추가 :", L)

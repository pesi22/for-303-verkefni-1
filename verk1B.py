for_list = []
gso_list = []
same_class_list = []

for_list_members_num = int(input("how many students are in the class FOR 303 ? :  "))

for i in range(for_list_members_num):
  name = input("name of student " )
  for_list.insert(for_list_members_num,name)

for_list.sort()

for index in range(len(for_list)):
   print ( for_list[index])

gso_list_members_num = int(input("how many students are in the class gso 303 ? :  "))

for i in range(gso_list_members_num):
  name = input("name of student " )
  gso_list.insert(gso_list_members_num,name)

gso_list.sort()

for index in range(len(gso_list)):
   print ( gso_list[index])

print("studants in the class FOR303")
for index in range(len(for_list)):
   print ( for_list[index])
print("----------------------")

print("studants in the class GSO303")
for index in range(len(gso_list)):
   print(gso_list[index])
print("----------------------")

gso_len = len(gso_list)
for_len = len(for_list)

if gso_len < for_len:
    print("more students are taking the FOR303 class")
elif gso_len == for_len:
    print("same amount of students are taking GSO303 and FOR303")
else:
    print("more students are atking the GSO303 class")

for element in for_list:
    if element in gso_list:
        same_class_list.append(element)

print("students who are taking both classes FOR303 & GSO303:")

for index in range(len(same_class_list)):
   print(same_class_list[index])

print("----------------------")

#this is the part where i move the last 2 students from FOR303 to GSF303
#kannski ekki besta leiðinn en hún virkar
for_to_gso_first = for_len - 1
for_to_gso_last = for_to_gso_first -1

print("moving the last 2 students of FOR303 to GSO303")
gso_list.insert(for_len, for_list[for_to_gso_first])
gso_list.insert(for_len, for_list[for_to_gso_last])
for index in range(len(gso_list)):
   print ( gso_list[index])



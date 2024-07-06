immutable_var = (1, False, 'pen')
mutable_list = [1, 2 , 'a', 'b']
#пример
#immutable_var[0]= 2 !!!!!!!!!- кортеж - не поддерживает обращение по элементам и является неизменяемой коллекцией!!!!!!!!!!
#print(immutable_var)
mutable_list.append('Mobified')
print(immutable_var)
print(mutable_list)
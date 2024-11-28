def calculate_total(num):
	return sum(num)
	
def retornate_antecesor_e_sucessor(number):
	antecessor = number - 1
	sucessor = number + 1
	
	return antecessor, sucessor
	
print(calculate_total([10,20,30]))
print(retornate_antecesor_e_sucessor(10))


def func_3():
	print("oi rapa")
	return None

func_3()
print(func_3)
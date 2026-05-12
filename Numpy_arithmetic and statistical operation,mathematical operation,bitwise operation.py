import numpy as np

def array_operations(A, B):

	# Convert A and B to NumPy arrays
	arr_A=np.array(A)
	arr_B=np.array(B)
	# Arithmetic Operations
	sum_result = arr_A + arr_B
	diff_result = arr_A - arr_B
	prod_result = arr_A * arr_B

	# Statistical Operations
	mean_A = np.mean(arr_A)
	median_A = np.median(arr_A)
	std_dev_A = np.std(arr_A)

	# Bitwise Operations
	and_result = np.bitwise_and(arr_A,arr_B)
	or_result = np.bitwise_or(arr_A,arr_B)
	xor_result = np.bitwise_xor(arr_A,arr_B)

    # Output results with one space between each element
	print("Element-wise Sum:", ' '.join(map(str, sum_result)))
	print("Element-wise Difference:", ' '.join(map(str, diff_result)))
	print("Element-wise Product:", ' '.join(map(str, prod_result)))
    
	print(f"Mean of A: {mean_A}")
	print(f"Median of A: {median_A}")
	print(f"Standard Deviation of A: {std_dev_A}")
    
	print("Bitwise AND:", ' '.join(map(str, and_result)))
	print("Bitwise OR:", ' '.join(map(str, or_result)))
	print("Bitwise XOR:", ' '.join(map(str, xor_result)))

A = list(map(int, input().split()))  # Elements of array A
B = list(map(int, input().split()))  # Elements of array B
array_operations(A, B)

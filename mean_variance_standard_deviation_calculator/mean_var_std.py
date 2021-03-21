import numpy as np

def calculate(list):
	if len(list) != 9:
		raise ValueError("List must contain nine numbers.")

	else:
		matrix = np.matrix(list).reshape(3,3)

		calculations = {
			'mean': [[np.mean(matrix.T[0]), np.mean(matrix.T[1]), np.mean(matrix.T[2])],\
			[np.mean(matrix[0]), np.mean(matrix[1]), np.mean(matrix[2])], np.mean(matrix)],
			'variance': [[np.var(matrix.T[0]), np.var(matrix.T[1]), np.var(matrix.T[2])],\
			[np.var(matrix[0]), np.var(matrix[1]), np.var(matrix[2])], np.var(matrix)],
			'standard deviation': [[np.std(matrix.T[0]), np.std(matrix.T[1]), np.std(matrix.T[2])],\
			[np.std(matrix[0]), np.std(matrix[1]), np.std(matrix[2])], np.std(matrix)],
			'max': [[np.max(matrix.T[0]), np.max(matrix.T[1]), np.max(matrix.T[2])],\
			[np.max(matrix[0]), np.max(matrix[1]), np.max(matrix[2])], np.max(matrix)],
			'min': [[np.min(matrix.T[0]), np.min(matrix.T[1]), np.min(matrix.T[2])],\
			[np.min(matrix[0]), np.min(matrix[1]), np.min(matrix[2])], np.min(matrix)],
			'sum': [[np.sum(matrix.T[0]), np.sum(matrix.T[1]), np.sum(matrix.T[2])],\
			[np.sum(matrix[0]), np.sum(matrix[1]), np.sum(matrix[2])], np.sum(matrix)]
		}
		return calculations
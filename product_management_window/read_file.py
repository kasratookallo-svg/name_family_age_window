import pickle

file = open("supermarket.dat", "rb")
product_list = pickle.load(file)
file.close()
print(product_list)
from data_list import *

data = data_list()
for i in range(150):
	data.add(i)

print(data.return_data(), data.start_index)
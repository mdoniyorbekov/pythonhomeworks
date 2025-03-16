import matplotlib.pyplot as plt

products = ['Product A', 'Product B', 'Product C', 'Product D', 'Product E']
sales = [200, 150, 250, 175, 225]

plt.figure(figsize=(8, 6))
plt.bar(products, sales, color=['blue', 'green', 'red', 'purple', 'orange'])
plt.xlabel('Products')
plt.ylabel('Sales')
plt.title('Sales Data for Different Products')
plt.show()
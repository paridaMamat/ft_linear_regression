import pandas as pd  
import matplotlib.pyplot as plt  


data = pd.read_csv('data.csv')  

'''plt.scatter(data.km, data.price) 
plt.show()'''  

def loss_function(m, b, points):     
total_error = 0     
for i in range(len(points)):         
    x = points.iloc[i].km         
    y = points.iloc[i].price         
    total_error += (y - (m * x + b)) ** 2     
total_error / float(len(points))   
    
    
def gradient_descent(m_now, b_now, points, L):     
    m_now = 0     b_now = 0      n = len(points)      
    m_gredient = 0     b_gredient = 0          
    for i in range(n):         
        x = points.iloc[i].km         
        y = points.iloc[i].price        
        m_gredient += -(2/n) * x * (y - (m_now * x + b_now))  
        b_gredient +=  -(2/n) * (y - (m_now * x + b_now))      
        m = m_now - m_gredient * L     
        b = b_now - b_gredient * L     
    return m, b  


m = 0 
b = 0 
L = 0.001 
epochs = 1000

for i in range(epochs):     
    m, b = gradient_descent(m, b, data, L) 
print(m, b)

# Scatter plot of the data
plt.scatter(data.km, data.price, color='black')

# Generate x values for the regression line
x_values = data.km
y_values = m * x_values + b  # Corresponding y values based on the regression line

# Plot the regression line
plt.plot(x_values, y_values, color='red')

# Show the plot
plt.show()
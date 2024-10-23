import numpy as np 
import matplotlib.pyplot as plt 

### create a random points from 0 to 100 
# x_data = np.random.random(50) * 100 
# y_data = np.random.random(50) * 100 
### create a scatter plot => A scatter plot is a diagram where each value in the data set is represented by a dot.

# plt.scatter(x_data , y_data)
# plt.show() 


### create line plot 
# years =[ 2006  + count for count in range(10) ]
# weights = [80 , 81 , 82 , 85 , 86 , 80 , 79 , 75 , 71 , 70 ] 

# plt.plot(years , weights  , "r--"  , lw = 3 )
# plt.show()  

### creat a bar plot 
# programmingLanguages = ['c++' , 'c#' , 'python' , 'java' , 'javaScript'] 
# votes = [50 , 70 , 100 , 45 , 140] 
# plt.bar(programmingLanguages , votes , color = "purple"  , width= 0.2 ) 
# plt.show() 

### create a histogram 
# test_score  = np.random.normal(20 , 2.1 , 20 ) 
# plt.hist(test_score) 
# print(test_score)
# plt.show()


### Note that the different between histogram and bar plot is  
### شكل الرسمة في الهيستوجرام متصلة انما ال البار فيه جابس في النص 


### create Pie chart 
# plt.pie(votes , labels=programmingLanguages , autopct= "%.2f%%")  
# plt.show() 

### The boxplot 

# heights = [100 , 80 , 60 , 20 ] 
# plt.boxplot(heights) 
# plt.show()  


### plot customization 
# income_ticks = list(range(80 ,200  , 4 ))
# years = list(range(2014 , 2024  , 1 ))
# income = [80 , 85 , 87 , 88 , 89 , 90 , 85 , 90 , 100 , 130] 
# plt.title("yearly income wiht us ") 
# plt.xlabel("income ") 
# plt.ylabel("years ")
# plt.yticks(income_ticks , [f"{x}k USD" for x in income_ticks])
# plt.plot(years , income) 
# plt.show()

### use multiple_plots 
# google = list(range(45 , 200 , 4)) 
# microsoft = list(range(46 , 90 , 2 )) 
# plt.plot(google , label = "google")  
# plt.plot(microsoft , label = "Microsoft") 
# plt.legend(loc = "upper right") 
# plt.show()  

#### create multiple graphs in the same figure and export the figure 
# x = np.arange(100) 
# fig , axs = plt.subplots(2 , 1 ) 
# axs[0].plot(x , np.sin(x))
# axs[0 ].set_title("sine wave \n") 
# axs[1].plot(x , np.cos(x))
# axs[1].set_title("\n cosine wave ") 
# fig.suptitle("figure 1 " )
# fig.tight_layout()
# fig.savefig("figure01.png" )

### create 3D 
x = np.arange(-5 , 5 , 0.1) 
y= np.arange(-5, 5 , 0.1 ) 
z = np.arange(-5 , 5 , 0.1)  
X , Y = np.meshgrid(x,y)
Z = np.sin(X) + np.cos(Y)

axs =plt.axes(projection = '3d') 

axs.plot_surface(X , Y , Z ,  cmap = "Spectral_r" ) 
plt.show()
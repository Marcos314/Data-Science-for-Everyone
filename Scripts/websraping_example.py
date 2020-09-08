# # Import package
# from urllib.request import urlretrieve

# # Import pandas
# import pandas as pd

# # Assign url of file: url
# url = "https://s3.amazonaws.com/assets.datacamp.com/production/course_1606/datasets/winequality-red.csv"

# # Save file locally
# urlretrieve(url,'winequality-red.csv')

# # Read file into a DataFrame and print its head
# df = pd.read_csv('winequality-red.csv', sep=';')
# print(df.head())
# print(df.shape)
# print(df.columns)

# Apenas lendo o arquivo sem gravar o mesmo localmente
# Import packages
# import matplotlib.pyplot as plt
# import pandas as pd

# # Assign url of file: url
# url = "https://s3.amazonaws.com/assets.datacamp.com/production/course_1606/datasets/winequality-red.csv"

# # Read file into a DataFrame: df
# df = pd.read_csv(url, sep=';')

# # Print the head of the DataFrame
# print(df.head())

# # Plot first column of df
# pd.DataFrame.hist(df.ix[:, 0:1])
# plt.xlabel('fixed acidity (g(tartaric acid)/dm$^3$)')
# plt.ylabel('count')
# plt.show()


# Pegando o html de uma página

# Import packages
# from urllib.request import urlopen, Request

# # Specify the url
# url = "https://campus.datacamp.com/courses/1606/4135?ex=2"

# # This packages the request
# request = Request(url)

# # Sends the request and catches the response: response
# response = urlopen(request)

# # Extract the response: html
# html = response.read()

# # Print the html
# print(html)

# # Be polite and close the response!
# response.close()

# Pegando o html com o pacote requests

# Import package
import requests

# Specify the url: url
url = "http://www.datacamp.com/teach/documentation"

# Packages the request, send the request and catch the response: r
r = requests.get(url)

# Extract the response: text
text = r.text

# Print the html
print(text)
<h1>Web-Scraping--Challenge</h1>
<hr>
<br>
<h3>Goal</h3>
<p>The purpose of this challenge was to create BeautifulSoup, Splinter, and Pandas to scrape five different web pages related to Mars and display the results on a webpage using MongoDB and Flask to demonstrate an effective web app to house data regarding Mars' weather, hemispheres, latest news, and facts. It is also meant to update as time goes on, meaning when new articles hit the Mars NASA page, the web app will update on its own, bringing further information to the app users.</p>
<br>
<h3>Process<h3/>
<hr>
<br>
<strong>Scraping Mars Data</strong>
Scraping was first done in a Jupyter notebook to test the code as it was written. After importing the necessary dependencies, I connected to the chromedriver and set up my browser to open each webpage I needed to scrape. I first scraped the <a href = "https://redplanetscience.com">NASA Mars News</a> website for the title and text of the most recent article, storing the results in variables to be referenced later. To do this, I used BeautifulSoup  to parse through the HTML and search for the appropriate elements and classes that contained the information I needed with `soup.find_all()`. Because the results come back as a list, I indexed the first item and took the text of that. 

![Screen Shot 2021-07-19 at 11 50 34 AM](https://user-images.githubusercontent.com/77529968/126197205-72a3c71d-e41b-47c9-a110-15312c50d3f3.png)

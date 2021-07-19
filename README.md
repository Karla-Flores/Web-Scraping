<h1>Web-Scraping--Challenge</h1>
<hr>
<br>
<h3>Goal</h3>
<p>The purpose of this challenge was to create BeautifulSoup, Splinter, and Pandas to scrape five different web pages related to Mars and display the results on a webpage using MongoDB and Flask to demonstrate an effective web app to house data regarding Mars' weather, hemispheres, latest news, and facts. It is also meant to update as time goes on, meaning when new articles hit the Mars NASA page, the web app will update on its own, bringing further information to the app users.</p>
<br>
<h3>Process</h3>
<hr>
<br>
<strong>Scraping Mars Data</strong>
<br>
<table border = 0 padding: 3>
<tr>
			<td><p align="justify">
First did a scrape code in a Jupyter notebook to test the code as it was written. Then, after importing the necessary dependencies, a connection to the chrome driver was established, and the browser was set up to open each webpage as it was needed to scrape.</p>
<p align = "justify">
The NASA Mars News was the first web being scraped getting the title and text of the most recent article, storing the results in variables to be referenced later. For this stage,  BeautifulSoup parsed through the HTML and searched for the appropriate elements and classes containing the information and needed with `soup.find_all()`. Because the results came back as a list, it was indexed to get the first title and text.</p></td>
			<td><img align="right" src='https://github.com/Karla-Flores/Web-Scraping--Challenge/blob/main/Missions_to_Mars./screenshots/Screen%20Shot%20Junbotron_scrapebutton_tititle_paragraph.png'></td>
 </tr>
 </table>






Next, was scraping Mars facts from the [Space Facts]
 website. Because the data was stored in a table, I used Pandas to scrape instead of BeautifulSoup. I used `pd.read_html()` to scrape for tables and took the second returned table which stored the facts I needed. I then renamed the columns and set the index before converting that data frame into an HTML table with `df.to_html()`. 

Lastly, I wanted to grab the images and names of all four of Mars’ hemispheres from the [USGS Astrogeology]
) page. I first searched for the hemisphere titles with BeautifulSoup and stored those names in a list, `hemi_names`. Then for the hemispheres, I searched for all thumbnail links and iterated through the results with a conditional, checking if the thumbnail element contained an image. If true, the relative image path was taken and combined with the main URL, and the full image URL was appended to an empty list (`thumbnail_links`) outside of the loop. To obtain the full-sized images of the hemispheres, I then iterated through each link in `thumbnail_links`, searching for all `img` elements with a `wide-image` class. The results were used to retrieve the full image path of the hemispheres, with the URLs being stored in a list, `full_imgs`. To match the hemisphere name to the correct image link, I zipped together `hemi_names` and `full_imgs` and iterated through that zipped object, first appending the hemisphere title to an empty dictionary as a key, and the image URL as the value, and then appending that dictionary to an empty list. 

After all the code was checked, it was then transferred from the notebook to a Python file and used to create a scraping function. The results of all the scraping was then stored as a dictionary to be returned at the end of the function. 

**Flask**

In a separate file, Flask was used to trigger the scrape function, update the Mongo database with the results, and then return that record of data from the database on a webpage. 

An instance of Flask was created, and then I used PyMongo to establish a connection to the MongoDB server. With this connection, I used the `/scrape` route to run the scrape function located in the imported `scrape_mars.py` file. I then updated the Mongo database with the new collection from the scrape, using `update` and `upsert=True`. The end of this route redirects to the home route. The home route searches for one record of data in the Mongo database and then renders the `index.html` template with that record. 

In `index.html`, the `/scrape` route was linked to a button, which a user could click to initiate the scrape. The remainder of that HTML file was formatted with Bootstrap to display the results from the scrape.

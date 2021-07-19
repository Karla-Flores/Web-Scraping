<h1>Web-Scraping--Challenge</h1>
<hr>
<br>
<h3>Goal</h3>
<p>The purpose of this challenge was to create BeautifulSoup, Splinter, and Pandas to scrape five different web pages related to Mars and display the results on a webpage using MongoDB and Flask to demonstrate an effective web app to house data regarding Mars' weather, hemispheres, latest news, and facts. It is also meant to update as time goes on, meaning when new articles hit the Mars NASA page, the web app will update on its own, bringing further information to the app users.</p>
<br>
<h3>Process</h3>
<hr>
<br>

<br>
<table border = 0px padding: 3px>
<tr>
			<td>
			<strong>Scraping Mars Data</strong>
				<br>
				<p align="justify">A web application was built that scrapes data from five different websites to gather data related to the Mission to Mars and displays the information in a single HTML page.</p>
			</td>
			<td>
				<p align="right"><img src= 'https://github.com/Karla-Flores/Web-Scraping--Challenge/blob/main/Missions_to_Mars./screenshots/Screen%20Shot%20Junbotron_scrapebutton_tititle_paragraph.png'>
				</p>
			</td>	
</tr>
<tr>
			<td>
			<strong>Flask</strong>
				<br>
				<p align="justify">A python script to run all of the scraping code was designed, and all of the scraped data was put into one Python dictionary. The function /scrape' set up a route that will import the Python script and call the scrape function was created and displayed on the index.html.</p>
			</td>
			<td>
				<p align="right"><img src= 'https://github.com/Karla-Flores/Web-Scraping--Challenge/blob/main/Missions_to_Mars./screenshots/Screen%20Shot_image_MarsFact.png'>
				</p>
			</td>
</tr>
<tr>
			<td>
			<strong>Mongo DB</strong>
				<p>A new database and a new collection were created, and all of the scraped data was stored in the above-created database. The root route / will query the database and pass the mars data into the HTML template was made.</p>
			</td>
			<td>
				<p align="right"><img src= 'https://github.com/Karla-Flores/Web-Scraping--Challenge/blob/main/Missions_to_Mars./screenshots/Screen%20Shot_loopforimages_links.png'>
				</p>
			</td>			
</tr>
</table>


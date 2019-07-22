# Crawler that scrapes newly built homes in Amsterdam area listed on funda.nl

### funda_link_extractor() 
Scrapes every link to home's landing page that come as a result of two search filters: nieuwbouw and amsterdam.
It stores those links as a csv file.

### homes_url()
Method that returns the above links as an array, making it easy to loop through for further scraping.

### funda_each()

Scrapes each link returned by homes_url() for the following items: 
* home_id - home title
* home_link - link to homes landing page
* wonen - living space in square meters
* kamers - number of rooms
* prijs - asking price

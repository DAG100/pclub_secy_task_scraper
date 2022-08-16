Deven Gangwani, 210327

Overview of making the scraper:
-language used: python
-modules/programs/etc. used: selenium + geckodriver (webdriver for firefox), time, json

Issues:
-slower connections may have problems because times were manually set - just change all 5s to 10s in that case (should do the job)
-tags added in incredibly slow fashion
-doesn't sequentially add info to json file, does it all in one go -> bad
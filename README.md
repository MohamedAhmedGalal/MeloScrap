# MeloScrap
Web Scraping for arabic songs /melodies download.

Having a folder of your popular composer/singer has became an old fashion, you should now listen using an online site or a cloud.
So,be it.... Lets create our favourite songs folder using web scraping super power.
A famous arabic site is called 'arab-zik.com' almost contains most of arabic melodies/songs.
Selenium library has been used to web scrap this site,and download all songs/melodies of one selected singer/composer.
The following variables should be changed according to your desire:
1-The code ehas been dedicated to Omar Khairat melodies,but it can be edited to any other singer/composer (arabic for sure, just to be present in above mentioned site) by changing the variable <web_url>
2-The variable called <down_directory> should also be changed to your desired download folder.
3-The prerequisite webdriver (chromedriver) may be changed to brave/mozilla ..... ,and the variable <webdriver_path> should contain the webdriver location.
4- The total number of songs/melodies to download can be set through variable <total_song_numb>

The code clicks the "Show more tracks" button whenever it is present in page just to load all songs/melodies in page.
The code loops through all songs/melodies present in web site (from 1 to total_song_numb). It first gets "href" attribute present in first download button element using download_prmpt function.The href attribute is the download link.The download link is opened in a new window tab.Second the "Download" button present in new opened download tab  is clicked. The download_wait function is called,and after finishing downloading or reaching the timeout the window tab is closed.The loop is repeated,and so on ...
Functions included in code:
1-def download_wait(directory, timeout, nfiles=None):
  -prompets window tab of file being downloaded until download completes,or reaching a certain predefined timeout,set as default into 120 sec.
  -If the folder contains a .crdownload file,this means that the download is not finished yet.
  -The functoin prints and returns the number of seconds taken to download the file.


2-download_prmpt(site_name,mel_no) takes the "href" attribute present in each download button element as input, together with the number of melody/song being downloaded. The <site_name> is then stripped out from unnecessary strings,just to get the clear actual song/melody name. the function then prints the song/melody name and nubmer being downloaded.

                                                                       ... ENJOY MUSIC ....

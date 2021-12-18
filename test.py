from selenium import webdriver
from bs4 import BeautifulSoup
import time
import mysql.connector
from selenium.webdriver.support.select import Select

con = mysql.connector.connect(host='localhost',
					   user='root',
					   passwd='fuck1234',
					   database='newdb'
					   )
curs = con.cursor()
curs = con.cursor(buffered=True)

chromedriver = 'chromedriver'
driver = webdriver.Chrome(chromedriver)
driver.get('https://www.whoscored.com/Regions/206/Tournaments/4/Seasons/5435/Spain-La-Liga')

def scraper(source,season):
    soup = BeautifulSoup(source, 'lxml')
    soupy = soup.find('tbody', {'id': 'player-table-statistics-body'}).find_all('tr')
    sql='SELECT player_id FROM player_table WHERE player_name = %s'
    for x in soupy:
        player_name = (x.find('a', {'class': 'player-link'}).text.strip()) 
        goals 		= (x.find('td', {'class': 'goal'}).text.strip())
        result 		= [player_name, goals, season]

        # print (player_name,goals,season)
        # sql='SELECT player_id FROM player_table WHERE player_name = %s'
# args=['liverpool']
        t = player_name
        tu = (t, )
        curs.execute(sql,tu)
        my = curs.fetchall()
        # yy = curs.fetchone()
            # print (y[0])
            # for z in y:
            #     print(z)
        # ct = [season, goals, yy[0]]
        # for e in my:
        #     print(e)
        # result 	= [season, goals, ex]
# print(curs.execute(sql,args))
        # my = curs.fetchall()
        # print(len(my))
        if len(my) == 0:
            curs.execute("INSERT IGNORE INTO player_table(player_name) VALUES (%s)", tu)
            con.commit()
            curs.execute(sql,tu)
            y = curs.fetchone()
            print (y[0])
            # for z in y:
            #     print(z)
            ult 	= [season, goals, y[0]]
            curs.execute("INSERT IGNORE INTO child_table(season,goals,fk_id) VALUES (%s,%s,%s)", ult)
            con.commit()
            # print(ult)
        else:
            curs.execute(sql,tu)
            yy = curs.fetchone()
            ct = [season, goals, yy[0]]
            curs.execute("INSERT IGNORE INTO child_table(season,goals,fk_id) VALUES (%s,%s,%s)", ct)
            con.commit()

         #    for re in my:
	        # print(re)
		# curs.execute("INSERT IGNORE INTO leaderboard(player_name,goals,seasons) VALUES (%s,%s,%s)", result)
		# con.commit()

season_constant = "20{}/20{}"

start_season = 14
end_season = 19

for i in range(start_season, end_season):
    sea = season_constant.format(start_season, start_season+1)
    start_season += 1
    # print (sea)

# for y in yo:
    select = Select(driver.find_element_by_id('seasons'))
	# driver.implicitly_wait(4)
    # time.sleep(5)
    select.select_by_visible_text(sea)
    time.sleep(5)
    driver.find_element_by_xpath('//*[@id="sub-navigation"]/ul/li[4]/a').click()
    for x in range(1,31):
        time.sleep(5)
        scraper(driver.page_source,sea)
        driver.find_element_by_xpath('//*[@id="next"]').click()
        time.sleep(3)
        print ('2ndloop',sea)
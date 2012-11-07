#_*_ encoding:utf-8 _*_
import sqlite3

def getStrokes(character):
	conn_g = sqlite3.connect('gb18030.db')
	cur = conn_g.cursor()
	cur.execute("select BH from china where CNword=\"%s\"" %(character,))
	result = cur.fetchone()[0]
	conn_g.close()
	return result
	
	
def getPinYin(character):
	conn_p = sqlite3.connect('py.sqlite')
	cur = conn_p.cursor()
	cur.execute("select code from words where string=\"%s\"" %(character,))
	result = cur.fetchone()[0]
	conn_p.close()
	return result
if __name__ == '__main__':
	print getStrokes('好')
	print getPinYin('好')

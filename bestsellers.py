# coding=UTF-8
import requests
import json
import os, sys
from collections import Counter

def getdata():
	currentPageNum=1
	a=0
	filename = 'shangpin.txt'
	headers={
	    'Cookie':'t=a3e18317c00b8675b5693d9c9122013a; thw=cn; UM_distinctid=1700a58382982f-0aed5a6eb807c1-6701b35-e1000-1700a58382a6db; cookie2=10a1ca102cee1c2c26b2b618cfce1d4c; _tb_token_=f33383d30b15e; hng=CN%7Czh-CN%7CCNY%7C156; _samesite_flag_=true; enc=O2BaoGzhkfbYHnqfTA4wjxv7e68yh4HB855wlD8BMtbvj4jaONkGdZchldiiqT0snN9jIppyebW2ZfFw%2Bf%2BoWA%3D%3D; cna=vruHFlaBhRECAW+mPx4SwELN; v=0; lgc=%5Cu5C0A%5Cu656C%5Cu7684%5Cu80E1%5Cu5148%5Cu751F; dnk=%5Cu5C0A%5Cu656C%5Cu7684%5Cu80E1%5Cu5148%5Cu751F; tracknick=%5Cu5C0A%5Cu656C%5Cu7684%5Cu80E1%5Cu5148%5Cu751F; tg=0; mt=ci=70_1; JSESSIONID=6919C68BE1A7589C464E4FF60AD705C9; sgcookie=DDaWcnRqUNK8Uou%2Fmi%2Bhf; uc3=lg2=WqG3DMC9VAQiUQ%3D%3D&vt3=F8dBxd32xY93RZl5SSs%3D&nk2=tO%2BWtpDhBQq7qWtz&id2=UUtMHBKKhZy49g%3D%3D; csg=b26ed479; skt=87df94d7924d114e; existShop=MTU4MzE2MTc3MA%3D%3D; uc4=id4=0%40U2l2xjAhng%2BQ1j70byYiDk7tYhUw&nk4=0%40tgnztQMLB7spzEYXksmDso%2FMW7Vaf6M%3D; _cc_=V32FPkk%2Fhw%3D%3D; tfstk=cYGRBJsg-nxuTW_C7FvmRHfW1ucdZIf8vaZN9eBG-KhPbPCdilhi6AwMFPI8MEC..; uc1=cookie16=URm48syIJ1yk0MX2J7mAAEhTuw%3D%3D&cookie21=Vq8l%2BKCLjhS4UhJVbhgU&cookie15=VFC%2FuZ9ayeYq2g%3D%3D&existShop=false&pas=0&cookie14=UoTUOa9szmLPLQ%3D%3D&tag=8&lng=zh_CN; x5sec=7b22726174656d616e616765723b32223a226337386632613730356366343135633532353930356438636132373939353438434d44612b6649464549486a79386667394f54726c41453d227d; _m_h5_tk=af01d865493c7eb7d6258f8421d50590_1583256672967; _m_h5_tk_enc=0dec67248d87da37067aeac4a13bb829; l=dBS7JNz7Qr4t5G0fBOfZIZCyjE7TnIRb8PVPHftFPICPOiCy_N6PWZ2EknL2CnGVHs_9R3J6m7-0BbTH-yd2lF7KkYyA6qM-ndC..; isg=BHV1K-LgR2oNO6Oikt0YYiEnhPEv8ikEV5w4iPeau-x-zpTAv0ND1JpIGJJ4i0G8',
	    'Connection':"keep-alive",
	    "referer":"https://item.taobao.com/item.htm",
	    'User-Agent':'Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/55.0.2883.87 Safari/537.36'
	}
	while True:
		url = 'https://rate.taobao.com/feedRateList.htm?auctionNumId='+sid+'&currentPageNum='+str(currentPageNum)
		req=requests.get(url,headers=headers).content.decode('utf-8')
		req=req[req.find('{'):req.rfind('}')+1]
		req=json.loads(req)
		if req["comments"] is None:
			print ("检索完成")
			break
		else:
			if len(req["comments"]):
				# print (type(req["comments"]))		
				req=req["comments"]		
				for i in range(len(req)):
					a=a+1
					print (a)
					# print (type(req))
					req1=req[i]
					print (req1["auction"]["sku"])
					reqc=req1["auction"]["sku"]
					with open(filename, 'a') as f:
						reqc=reqc.replace("&nbsp;&nbsp"," ")
						f.write(reqc+"\n")
					# if len(reqc):
					# 	# print ("不为空")
					# 	pass
					# else:
					# 	# print ("为空")
						pass
				currentPageNum=currentPageNum+1
			else:
				print ("检索完成")
				break
def dataprocessing():
	li1=[]
	f = open("shangpin.txt", "r")
	for line in f:
	    line=line.replace("\n","")
	    li1.append(line)
	f.close()
	os.remove("shangpin.txt")
	# cout = Counter(li1)
	# print(type(cout))
	result = Counter(li1).most_common(n)
	# print (type(result))
	print ("销量最好的前"+str(n)+"个商品：")
	print (result)

if __name__ == '__main__':
	sid='613900372087' #输入商品id
	n=2                  #销量最好的前n个产品
	getdata()
	dataprocessing()

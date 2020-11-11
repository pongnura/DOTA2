# Core Pkgs
import streamlit as st 

# EDA Pkgs
import pandas as pd 
import numpy as np

# Utils
import os
import joblib 
import hashlib
# passlib,bcrypt

# Data Viz Pkgs
import matplotlib.pyplot as plt 
import matplotlib
matplotlib.use('Agg')


##background
page_bg_img = '''
<style>
body {
background-image: url("https://wallpapercave.com/wp/wp4549603.jpg");
background-size: cover;
}
</style>
'''
st.markdown(page_bg_img, unsafe_allow_html=True)

##Head
st.markdown("<h1 style='text-align: center; color: red;'>Dota 2</h1>", unsafe_allow_html=True)

# Video
vid_file= open("./VF/Dota 2 - Join the Battle.mp4","rb")
st.video(vid_file)


st.header('BEST HERO AND ITEM PICKS')
st.markdown("""### กราฟที่ 1  คือ การวางitem ถูกตำแหน่งslot จะทำให้ให้งานitem ได้มีประสิทธฺภาพมาก  """)
st.markdown("""### กราฟที่ 2  คือ Win Rate   """)

job_selected = st.selectbox("HERO", ["Home","Visage", "Windranger", "Slardar"])


if job_selected =="Visage": ##Visago
	##GIF01
	st.markdown("![Alt Text](https://cdnb.artstation.com/p/assets/images/images/010/776/919/original/yunfeng-zhang-ingame-001.gif?1526171880)")
	#HEAD
	st.header('SKILL VISAGE ')
	# Video
	vid_file= open("./VF/Dota 2 Hero Spotlight - Visage the Necro'lic.mp4","rb")
	st.video(vid_file)
	##Table data Visaga win
	st.markdown(f'<div style="color: purple;">Table data Visaga win.</div>',
        unsafe_allow_html=True)

	if st.checkbox("Show/Hide"):
		@st.cache(persist=True)
		def load_data():
			Visage_data = {"radiant_win" : ['false','true','true','true','false','true','true','true','true','false','false','true','false','false','true','true','true','false','true','true'],
			"item_0" : [206,96,63,100,29,36,229,0,0,36,214,229,218,214,229,187,178,79,0,63],
			"item_1":[229,46,36,42,23,22,0,231,79,180,9,36,187,38,79,90,214,36,36,46],
			"item_2":[41,77,41,141, 50,69,48,36,0,0,166,0,118,50,220,1,166,46,168,78],
			"item_3":[9,214,187,40,46,108,112,0,29,46,36,214,127,37,100,23,218,125,214,79],
			"item_4":[108,36,108,214,21,48,214,0,0,166,168,0,108,0,24,242,46,180,229,185],
			"item_5":[214,53,46,229,22,110,48,0,229,0,108,0,168,46,0,21,0,43,0,112],
			"item_name" : ["phase_boots","ultimate_scepter","blink","bottle","black_king_bar","demon_edge","ogre_axe","desolator","null","maelstroll","force_staff","point_booster","lesser_crit","sphere","null_talisman","ring_of_basilius","travel_boots","tpscroll","magic_wand","greater_crit"]}
			Visage_data = pd.DataFrame(Visage_data, columns = ["radiant_win","item_0","item_1","item_2","item_3","item_4","item_5","item_name"])

			return Visage_data
		Visage_data = load_data()

		
		num_shown = st.slider("shown Visage data ..", 0, 20, 5)
		st.table(Visage_data[:num_shown])
		st.write("""only showing top 20 rows""")

	st.markdown("""### Graph: item ยอดนิยม มี 3 ชิ้น โดยกราฟจะแสดง itemที่อยู่ใน slot0-5 """)
	from PIL import Image
	img = Image.open("/Users/natty/Desktop/VF/Screen Shot 2020-11-09 at 21.53.23.png")
	st.image(img, width=800, caption="Simple Image")

	st.markdown("""
	- tranquil_boots เป็นitem เป็นแรกที่ควรออกในช่วงเริ่มเกม
	- solar crest item ควรซื้ออยู่ slot1 
	- magic wand เป็นitem รีHPรีมานาตาม จำนวนการใช้สกิลของศัตรู ควรซื้ออยู่ slot1
	""")

	st.markdown(f'<div style="color: purple;">item of Slot</div>',
        unsafe_allow_html=True)
	job_selected = st.selectbox("item", ["Table item All","item0", "item1", "item2", "item3","item4","item5"])
	
	if job_selected =="item0":	##item_0
		from PIL import Image
		img = Image.open("./VF/Screen Shot 2020-11-11 at 22.51.04.png")
		st.image(img, width=400, caption="tranquil_boots")
	
	if job_selected =="item1":    ##item_1
		from PIL import Image
		img = Image.open("./VF/Screen Shot 2020-11-11 at 22.52.26.png")
		st.image(img, width=400)

	if job_selected =="item1":    ##item_1
		from PIL import Image
		img = Image.open("./VF/Screen Shot 2020-11-10 at 09.47.57.png")
		st.image(img, width=400)

	st.markdown(""" ### Graph : Win Rate""")
	img = Image.open("./VF/Screen Shot 2020-11-09 at 22.33.51.png")
	st.image(img, width=800, caption="win rate")
	st.markdown(
	"""
	- น้ำเงิน คือชนะ
	- แดง คือ แพ้ 
	- จะเห็นว่า อัตราการชนะ เท่าๆกัน สรุปว่า การเลือกตัวละครไม่มีผลต่อการชนะ ต้องเเข็งแกร่งเองนะ TT
	
	"""
	)
if job_selected =="Windranger":
	##GIF01
	st.markdown("![Alt Text](https://i.imgur.com/xZmEC4E.gif)")
	#HEAD
	st.header('SKILL Windranger ')
	# Video
	vid_file= open("./VF/Dota 2 Hero Spotlight - Windranger [Remastered].mp4","rb")
	st.video(vid_file)

	st.markdown("""### Graph: item ยอดนิยม มี 3 ชิ้น โดยกราฟจะแสดง itemที่อยู่ใน slot0-5 """)

	from PIL import Image
	img = Image.open("./VF/Screen Shot 2020-11-11 at 22.32.00.png")
	st.image(img, width=800, caption="Windranger")
	st.markdown("""
	- phase_boots เป็นitem เป็นแรกที่ควรออกในช่วงเริ่มเกม
	- ultimate scepter item ควรซื้ออยู่ slot4 
	- dust เป็นitem ไม่นิยมโดยทั่วไปไม่ได้เป็นitem ติดslotไหนเลย ช่วยใหญ่ผู้เล่นมักให้อยู่ slot2,5
	""")

	job_selected = st.selectbox("item", ["Table item All","item0", "item1", "item2", "item3","item4","item5"])
	if job_selected =="item2":	##item_2 dust
		from PIL import Image
		img = Image.open("./VF/Screen Shot 2020-11-11 at 22.44.37.png")
		st.image(img, width=400, caption="tranquil_boots")
	
	if job_selected =="item5":    ##item_5 dust
		from PIL import Image
		img = Image.open("./VF/Screen Shot 2020-11-11 at 22.44.37.png")
		st.image(img, width=400)

	if job_selected =="item0":    ##item_1 phase boots
		from PIL import Image
		img = Image.open("./VF/Screen Shot 2020-11-11 at 22.48.32.png")
		st.image(img, width=400)

	if job_selected =="item4":    ##item_1 phase boots
		from PIL import Image
		img = Image.open("./VF/Screen Shot 2020-11-11 at 22.49.46.png")
		st.image(img, width=400)

	st.markdown(""" ### Graph : Win Rate""")
	img = Image.open("./VF/Screen Shot 2020-11-10 at 10.12.22.png")
	st.image(img, width=800, caption="win rate")
	st.markdown(
	"""
	- น้ำเงิน คือชนะ
	- แดง คือ แพ้ 
	- จะเห็นว่า อัตราการชนะ เท่าๆกัน สรุปว่า การเลือกตัวละครไม่มีผลต่อการชนะ ต้องเเข็งแกร่งเองนะ TT
	
	"""
	)
if job_selected =="Slardar":
	##GIF01
	st.markdown("![Alt Text](https://cdna.artstation.com/p/assets/images/images/011/919/660/original/staz-vladz-slard.gif?1532088920)")
	#HEAD
	st.header('SKILL SLARDAR ')
	# Video
	vid_file= open("./VF/Dota 2 Hero Spotlight - Slardar [Remastered].mp4","rb")
	st.video(vid_file)

	##อธิบาย Graph
	st.markdown("""### Graph: item ยอดนิยม มี 3 ชิ้น โดยกราฟจะแสดง itemที่อยู่ใน slot0-5  """)
	from PIL import Image
	img = Image.open("./VF/slardar.png")
	st.image(img, width=800, caption="SLARDAR")

	st.markdown("""
	- blink เป็นitem เป็นแรกที่ควรออกในช่วงเริ่มเกม
	- power treads  item ควรซื้ออยู่ slot3 รองเท้าช่วยเคลื่อนที่
	- black king bar เป็นitem slot1
	""")

	##Table item 
	st.markdown(f'<div style="color: purple;">item of Slot</div>',
        unsafe_allow_html=True)
	job_selected = st.selectbox("item", ["Table item All","item0", "item1", "item2", "item3","item4","item5"])
	
	if job_selected =="item0":	##item_0
		from PIL import Image
		img = Image.open("./VF/Screen Shot 2020-11-11 at 18.37.44.png")
		st.image(img, width=400, caption="tranquil_boots")
	
	if job_selected =="item3":    ##item_3 power treads
		from PIL import Image
		img = Image.open("./VF/Screen Shot 2020-11-11 at 18.42.26.png")
		st.image(img, width=400)

	if job_selected =="item1":    ##item_1 black king bar
		from PIL import Image
		img = Image.open("./VF/Screen Shot 2020-11-11 at 18.44.26.png")
		st.image(img, width=400)
	
	
	##Pie plot 
	st.markdown(""" ### Graph : Win Rate""")
	img = Image.open("./VF/Screen Shot 2020-11-11 at 18.47.57.png")
	st.image(img, width=800, caption="win rate")
	st.markdown(
	"""
	- น้ำเงิน คือชนะ
	- แดง คือ แพ้ 
	- จะเห็นว่า อัตราการชนะ เท่าๆกัน สรุปว่า การเลือกตัวละครไม่มีผลต่อการชนะ ต้องเเข็งแกร่งเองนะ TT
	
	""")

##WORST HERO AND ITEM
st.header('WORST HERO AND ITEM ')
job_selected = st.selectbox("HERO", ["Home","Elder Titan"])
if job_selected =="Elder Titan": ##Visago
	##GIF01
	st.markdown("![Alt Text](https://media.giphy.com/media/lkimmOoBiBlYOfcAM/giphy.gif)")
	#HEAD
	st.header('SKILL Elder Titan ')
	# Video
	vid_file= open("./VF/Dota 2 Hero Spotlight - Elder Titan.mp4","rb")
	st.video(vid_file)
	##Table data Visaga win
	st.markdown(f'<div style="color: purple;">Table data Elder Titan win.</div>',
        unsafe_allow_html=True)

	if st.checkbox("Show./Hide."):
		@st.cache(persist=True)
		def load_data():
			Elder_data = {"radiant_win" : ['true','true','true','false','false','true','true','true','true','false','false','true','true','false','false','false','false','true','false','true'],
			"item_0" : [0,170,63,36,29,36,229,0,77,36,214,129,218,214,69,180,178,54,0,63],
			"item_1":[36,242,36,108,23,22,0,231,79,180,21,90,187,38,79,64,9,36,36,46],
			"item_2":[29,100,108,0, 50,69,48,36,0,0,166,0,118,50,20,1,120,46,168,0],
			"item_3":[0,46,0,40,36,108,53,0,29,46,36,214,127,37,100,56,218,125,214,0],
			"item_4":[46,108,36,189,21,48,24,0,0,245,168,0,108,0,24,242,46,180,229,44],
			"item_5":[229,63,9,11,22,110,48,0,29,0,108,0,143,46,0,21,0,43,0,201],
			"item_name" : ["phase_boots","ultimate_scepter","blink","bottle","black_king_bar","demon_edge","ogre_axe","desolator","null","maelstroll","force_staff","point_booster","lesser_crit","sphere","null_talisman","ring_of_basilius","travel_boots","tpscroll","magic_wand","greater_crit"]}
			Elder_data = pd.DataFrame(Elder_data, columns = ["radiant_win","item_0","item_1","item_2","item_3","item_4","item_5","item_name"])

			return Elder_data
		Elder_data = load_data()

		
		num_shown = st.slider("shown Elder Titan data ..", 0, 20, 5)
		st.table(Elder_data[:num_shown])
		st.write("""only showing top 20 rows""")

	st.markdown("""### Graph: item ยอดนิยม มี 3 ชิ้น โดยกราฟจะแสดง itemที่อยู่ใน slot0-5 """)
	from PIL import Image
	img = Image.open("/Users/natty/Desktop/VF/Screen Shot 2020-11-11 at 23.37.28.png")
	st.image(img, width=800, caption="Elder Titan")

	st.markdown("""
	- arcane boots เป็นitem เป็นแรกที่ควรออกในช่วงเริ่มเกม 
	- blade mail item พื้นฐาน ช่วยพลังโจมตี  เจาะเกราะสะท้อน 
	- vladmir เป็นitem ไม่นิยม จากกราฟผู้เล่นจะเอาitem ไว้ใน slotไหนก็ได้
	""")

	st.markdown(f'<div style="color: purple;">item of Slot</div>',
        unsafe_allow_html=True)
	job_selected = st.selectbox("item", ["Table item All.","item_0", "item_1", "item_2", "item_3","item_4","item_5"])
	
	if job_selected =="item_0":	##item_0 arcane boots
		from PIL import Image
		img = Image.open("./VF/Screen Shot 2020-11-11 at 23.43.40.png")
		st.image(img, width=400, caption="tranquil_boots")
	
	if job_selected =="item_0":    ##item_0 blade mail
		from PIL import Image
		img = Image.open("./VF/Screen Shot 2020-11-11 at 23.41.30.png")
		st.image(img, width=400)

	if job_selected =="item_1":    ##item_1
		from PIL import Image
		img = Image.open("./VF/Screen Shot 2020-11-11 at 23.44.44.png")
		st.image(img, width=400)

	st.markdown(""" ### Graph : Win Rate""")
	img = Image.open("./VF/Screen Shot 2020-11-11 at 23.54.41.png")
	st.image(img, width=800, caption="win rate")
	st.markdown(
	"""
	- น้ำเงิน คือชนะ
	- แดง คือ แพ้ 
	- จะเห็นว่า อัตราการชนะ เท่าๆกัน สรุปว่า การเลือกตัวละครไม่มีผลต่อการชนะ สู้ต่อไปนะElder Titan 
	""")






















	

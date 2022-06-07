#for i in range(100):
#	i = i + 9760
#	print("PROV{i}:0 \"#D PROV{i}#!\"".format(i = i))


heritages = ["qin_heritage","qi_heritage","zhao_heritage","chu_heritage","yue_heritage","wei_heritage","wei4_heritage","song_heritage","lu_heritage","han_heritage","yan_heritage","zhou_heritage","goguryeo_heritage","baekje_heritage","saro_heritage","guya_heritage","yamato_heritage","chinese_heritage"]

for i in heritages:
	y = i 
	z = str(i.capitalize())
	for i in range(len(z)):
		if z[i] == "_":
			z = z[:i + 1] + z[i + 1].capitalize() + z[i + 2:]
	z = z.replace("_", " ")
	print("{y}:0 \"{z}\"\n{y}_desc:0 \"\"\n".format(y=y,z=z))
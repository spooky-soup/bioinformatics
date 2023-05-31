import os, subprocess, re

if __name__ == "__main__":
	out = subprocess.check_output(['samtools', 'flagstat', 'samviewout.bam'])
	out = out.decode('utf-8')
	#Пишем в файл
	with open('flagstat_res.txt', 'w') as f:
		f.write(out)
	out = out.split("\n")
	r_percent = r"(\d mapped \()\d\d\.\d\d"
	percent_match = float(re.search(r_percent, out[6]).group(0)[-5:])
	
	print("Percent match: " + str(percent_match))
	if percent_match >= 75.0:
		print("OK")
	else:
		print("Bad mapping")

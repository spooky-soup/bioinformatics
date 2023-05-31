import os
import subprocess
import re

def run_fastqc(f="") -> str:
	directory = os.path.dirname(f)
	command = "fastqc -o {} {}".format(directory, f)
	subprocess.check_call(command, shell=True)
	zip_file = os.path.join(f[:-7] + "_fastqc.zip")
	os.remove(zip_file)
	return("none")

def run_bwa_index(ref_path: str):
	command = "bwa index {}".format(os.path.abspath(ref_path))
	subprocess.check_call(command, shell=True)
	return("none")

def run_bwa_mem(ref_path: str, fastq1_path: str, fastq2_path) -> str:
	ref_path = os.path.abspath(ref_path.replace('\n', ""))
	fastq1_path = os.path.abspath(fastq1_path.replace('\n', ""))
	fastq2_path = os.path.abspath(fastq2_path.replace('\n', ""))
	out_path = os.path.join(os.path.dirname(fastq1_path), "bwa_mem_out.sam")
	command = "bwa mem {} {} {} -o {}".format(ref_path, fastq1_path, fastq2_path, out_path)
	subprocess.check_call(command, shell=True)
	return(out_path)

def run_samtools_view(path_to_sam: str):
	out_path = os.path.join(os.path.dirname(path_to_sam), "samtools_view_out.bam")
	command = "samtools view {} -o {}".format(path_to_sam, out_path)
	subprocess.check_call(command, shell=True)
	return out_path

def analyze_flagstat(path_to_bam: str):
	out = subprocess.check_output(['samtools', 'flagstat', path_to_bam])
	out = out.decode('utf-8').split("\n")
	r_percent = r"(\d mapped \()\d\d\.\d\d"
	percent_match = float(re.search(r_percent, out[6]).group(0)[-5:])
	print("Percent match: " + str(percent_match))
	if percent_match >= 75.0:
		print("OK")
		return True
	else:
		print("Bad mapping")
		return False
	
def run_samtools_sort(is_running: bool, path_to_bam: str):
	if not is_running:
		return False, "None"
	directory = os.path.dirname(path_to_bam)
	sorted_path = os.path.join(directory, "sample.sorted.bam")
	command = "samtools sort {} -o {}".format(path_to_bam, sorted_path)
	subprocess.check_call(command, shell=True)
	return True, sorted_path

def run_freebayes(path_to_ref: str, path_to_sorted_bam: str, is_running: bool):
	if not is_running:
		return False
	out_path = os.path.join(os.path.dirname(path_to_sorted_bam), "var.vcf")
	command = "freebayes -f {} {} >{}".format(path_to_ref, path_to_sorted_bam, out_path)
	command = command.replace("\n", "")
	subprocess.check_call(command, shell=True)
	print("Pipeline finished. .vcf file saved to {}".format(out_path))
	return("None")
	

from kedro.pipeline import Pipeline, node

from .nodes import *

fastqc_file_path = "/home/spooky/3year/bioinformatics/HW3/SRR24651073_1.fastq"

def create_pipeline(**kwargs):
    return Pipeline(
        [
            node(
                run_fastqc,
                inputs="fastqc1path",
                outputs="fastqc1out",
            ),
            node(
                run_fastqc,
                inputs="fastqc2path",
                outputs="fastqc2out",
            ),
            node(
                run_bwa_index,
                inputs="refseq_fasta_path",
                outputs="index_out"
            ),
            node(
                run_bwa_mem,
                inputs=["refseq_fasta_path", "fastqc1path", "fastqc2path"],
                outputs="bwa_mem_out_path"
            ),
            node(
                run_samtools_view,
                inputs="bwa_mem_out_path",
                outputs="bam_path"
            ),
            node(
                analyze_flagstat,
                inputs="bam_path",
                outputs="is_launching_sort"
            ),
            node(
                run_samtools_sort,
                inputs=["is_launching_sort", "bam_path"],
                outputs=["is_launching_freebayes", "sorted_bam_path"]
            ),
            node(
                run_freebayes,
                inputs=["refseq_fasta_path", "sorted_bam_path", "is_launching_freebayes"],
                outputs="none"
            )
        ]
    )

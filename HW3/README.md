Пайплайн для оценки картирования генома

Для запуска пайплайна, нужно указать расположение входных файлов в системе.
В директории …/kedro-environment/helloworld/data/01_raw содержатся конфигурационные файлы, указывающие на расположение входных данных.
В файле ./bwa_in/refseq_fasta_path.txt нужно указать путь до референсной последовательности, а в ./fastqc_in/ пути до двух входных .fastq файлов соответственно.

Запуск:
В папке kedro-environment активировать виртуальную среду: 
source .venv/bin/activate
cd helloworld
kedro run –pipeline genomic_pipeline

Для визуализации:
pip install kedro-viz

В папке kedro-environment/helloworld:
kedro viz 

Визуализация полученного пайплайна:
![kedro-pipeline](https://github.com/spooky-soup/bioinformatics/assets/63796624/adbc31fd-4680-481d-9d72-12c8832b1815)


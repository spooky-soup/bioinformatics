Биоинформатика. Домашнее задание 5.
=====================
Предсказание и парное выравнивание
структур белков.
-----------------------------------

**Последовательность белка:** MKGMLTGPVTILNWSWPREDITHEEQTKQLALAIRDEVLDLEAAGIKIIQIDEAALREKLPLRKSDWHAKYLDWAIPAFRLVHSAVKPTTQIHTHMCYSE
5-methyltetrahydropteroyltriglutamate-- homocysteine methyltransferase

**Иструменты предсказания структуры:** [AlphaFold2](https://colab.research.google.com/github/sokrypton/ColabFold/blob/main/AlphaFold2.ipynb), [OmegaFold](https://colab.research.google.com/github/sokrypton/ColabFold/blob/main/beta/omegafold.ipynb).
*В качестве результата работы AlphaFold2 был взят один наилучший результат (по rank).*

**Инструмент выравнивания:** [iPBA](https://www.dsimb.inserm.fr/dsimb_tools/ipba/)

**Результат выравнивания:**
![Result](https://github.com/spooky-soup/bioinformatics/blob/main/HW5/alignment_pyMOL_transp.png)

Раскраска выполнена по вторичной структуре белков. 
На выравнивании мы видим, что структуры очень схожи, однако имеются различия в местах предсказания бета-листов. Несколько разнится их длина в двух предсказанных структурах. 


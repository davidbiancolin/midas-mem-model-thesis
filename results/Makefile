all: heatmap.png java-alloc-detailed.png java-alloc-1khz.png java-alloc-macro.png

heatmap.png:
	python plot-java-timeseries.py --xmin 0 --xmax 600 --mode addrtrace --file data/java-timeseries-midas/pmd2.series --out %@

java-alloc-detailed.png:
	python plot-java-timeseries.py --xmin 150 --xmax 170 --mode latency --file data/java-timeseries-midas/pmd2.series --out $@ --ymax 200000

java-alloc-1khz.png:
	python plot-java-timeseries.py --xmin 150 --xmax 170 --mode latency --file data/java-timeseries-midas/pmd2.series --out $@ --average 1000000

java-alloc-macro.png:
	python plot-java-timeseries.py --xmin 0 --xmax 600 --mode latency --file data/java-timeseries-midas/pmd2.series --out $@ --average 1000000

rowmisses_pmd.png:
	python plot-memory.py --files data/output-MAS-open/pmd_memory_stats.csv --gcpauses data/output-MAS-open/pmd.out --delta --out rowmisses_pmd.png

rowmisses_sunflow.png:
	python plot-memory.py --files data/output-MAS-open/sunflow_memory_stats.csv --gcpauses data/output-MAS-open/sunflow.out --delta --out rowmisses_sunflow.png

rowmisses_luindex.png:
	python plot-memory.py --files data/output-MAS-open/luindex_memory_stats.csv --gcpauses data/output-MAS-open/luindex.out --delta --out rowmisses_luindex.png

rowmisses_xalan.png:
	python plot-memory.py --files data/output-MAS-open/xalan_memory_stats.csv --gcpauses data/output-MAS-open/xalan.out --delta --out rowmisses_xalan.png

rowmisses_lusearch.png:
	python plot-memory.py --files data/output-MAS-open/lusearch_memory_stats.csv --gcpauses data/output-MAS-open/lusearch.out --delta --out rowmisses_lusearch.png

rowmisses_avrora.png:
	python plot-memory.py --files data/output-MAS-open/avrora_memory_stats.csv --gcpauses data/output-MAS-open/avrora.out --delta --out rowmisses_avrora.png

rowmisses: rowmisses_avrora.png rowmisses_lusearch.png rowmisses_xalan.png rowmisses_luindex.png rowmisses_sunflow.png rowmisses_pmd.png

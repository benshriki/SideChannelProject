Flush+Flush key logger attack:

Code used:
	cache_template_attacks-master: https://github.com/IAIK/cache_template_attacks
	flush_flush-master: https://github.com/IAIK/flush_flush

Code instructions:
	Appear either in the report or the above git repositories

Output:
	We have supplied an example of output as "Example_logfile", this file reflects 	information gathered from the cache template attack that can be utilized using 				the spy tool in the "204613624_203309562 - Flush + Flush\flush_flush-master\sc\ff" directory 
	
Changes:
./cache_template_attacks-master/profiling/linux_low_frequency_example/spy.c at line 103: 
"printf("%8s","addr");" -> "  printf("file,addr");"  we have change this line so the parser will work properly.

How to use the parser:
Open the csv file with any suitable program (Excel, LiberaOffice, ext...).
save the file as is and exit the program.

Using a terminal in the cwd:
	1. python BenShriki_AnalysisScript.py
	2. Enter file name with suffix (.csv, .xl etc..)
	3. Analyse results


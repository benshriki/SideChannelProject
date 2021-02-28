Flush+Flush key logger attack:
git used:
	https://github.com/IAIK/flush_flush
	https://github.com/IAIK/cache_template_attacks
changes:
./cache_template_attacks-master/profiling/linux_low_frequency_example/spy.c at line 103: 
"printf("%8s","addr");" -> "  printf("file,addr");"  we have change this line so the parser will work properly.

How to use the parser:
first open the csv file with any sutibale program (Excel, LiberaOffice, ext...).
save the file as is and exit the program.
run the parser and enter the correct file name.


list = LOAD 'piginfile' using PigStorage(' ') AS (word:chararray, count:int);
sorted_list = ORDER list BY count DESC;
limit_list = LIMIT sorted_list 10 ;
dump limit_list ;
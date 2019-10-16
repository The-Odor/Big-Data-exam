list = LOAD 'hdfs://localhost/user/root/output1e/part-00000' using PigStorage(' ') AS (word:chararray, count:int) ;
sorted_list = ORDER list BY count DESC ;
limit_list = LIMIT sorted_list 10 ;
dump limit_list ;

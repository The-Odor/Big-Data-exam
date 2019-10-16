list = LOAD 'hdfs://localhost/user/root/output1e/part-00000' using PigStorage(' ') AS (word:chararray, count:int) ;
sorted_list = ORDER list BY count DESC ;
limit_list = LIMIT sorted_list 10 ;
DUMP limit_list;
STORE limit_list INTO '1ePig_Output' using PigStorage(' ');

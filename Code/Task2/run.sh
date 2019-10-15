
hadoop fs -rm -r output_2b

hadoop jar $HADOOP_HOME/share/hadoop/tools/lib/hadoop-streaming-2.7.3.jar \
-input Users.xml \
-output output_2b \
-mapper 2bUnique.py \
-reducer 2bReducer.py

hadoop fs -copyToLocal

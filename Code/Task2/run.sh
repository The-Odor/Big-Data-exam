
hadoop fs -rm -r output_2c
rm output_2c/*

hadoop jar $HADOOP_HOME/share/hadoop/tools/lib/hadoop-streaming-2.7.3.jar \
-input Users.xml \
-output output_2c \
-mapper 2cTopMiners.py \
-reducer 2cReducer.py

hadoop fs -copyToLocal output_2c

hadoop fs -cat output_2c/*

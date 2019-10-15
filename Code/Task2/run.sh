
hadoop fs -rm -r output_2h
rm output_2h/*

hadoop jar $HADOOP_HOME/share/hadoop/tools/lib/hadoop-streaming-2.7.3.jar \
-input Users.xml \
-output output_2h \
-mapper 2hName.py \
-reducer 2hReducer.py

hadoop fs -copyToLocal output_2h

hadoop fs -cat output_2h/*

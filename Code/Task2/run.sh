
hadoop fs -rm -r output_2d
rm output_2d/*

hadoop jar $HADOOP_HOME/share/hadoop/tools/lib/hadoop-streaming-2.7.3.jar \
-input Posts.xml \
-output output_2d \
-mapper 2dTOpQuestions.py \
-reducer 2dReducer.py

hadoop fs -copyToLocal output_2d

hadoop fs -cat output_2d/*

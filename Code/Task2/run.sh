
hadoop fs -rm -r output_2e
rm output_2e/*

hadoop jar $HADOOP_HOME/share/hadoop/tools/lib/hadoop-streaming-2.7.3.jar \
-input Posts.xml \
-output output_2e \
-mapper 2eFavoriteQuestion.py \
-reducer 2eReducer.py

hadoop fs -copyToLocal output_2e

hadoop fs -cat output_2e/*

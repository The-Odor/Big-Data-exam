hadoop fs -rm -r output_1e

hadoop jar $HADOOP_HOME/share/hadoop/tools/lib/hadoop-streaming-2.7.3.jar \
-input Posts.xml \
-output output_1e \
-mapper 1eStopWords.py \
-reducer 1eReducer.py

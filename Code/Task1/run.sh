hadoop fs -rm -r output1e

hadoop jar $HADOOP_HOME/share/hadoop/tools/lib/hadoop-streaming-2.7.3.jar \
-input Posts.xml \
-output output1e \
-mapper 1ePigtop10.py \
-reducer 1eReducer.py

# Assumptions:
# 1. the dataset in the cluster is located at "news"
# 2. the current directory contains files mapper.py and reducer.py for mapper and reducer code respectively

task=1d
taskname=stopwords

mapperfile=$task$taskname.py
reducerfile="$task"reducer.py
outfile=output$task

apt-get install dos2unix

# hadoop fs -rm -r $outfile
dos2unix $mapperfile
dos2unix $reducerfile

hadoop jar $HADOOP_HOME/share/hadoop/tools/lib/hadoop-streaming-2.7.3.jar \
-files $mapperfile,$reducerfile \
-mapper $mapperfile \
-reducer $reducerfile \
-input posts.xml \
-output $outfile

hadoop fs -cat $outfile/*
hadoop fs -copyToLocal $outfile
hadoop fs -rm -r $outfile
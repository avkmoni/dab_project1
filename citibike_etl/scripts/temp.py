from databricks.connect import DatabricksSession
 
#spark = DatabricksSession.builder.getOrCreate()
 
spark = DatabricksSession.builder.remote(cluster_id = "0727-145044-oix23kaz").getOrCreate()
spark.sql("select 1 ").show()

package com.latif.spark

import org.apache.spark._
import org.apache.spark.SparkContext._
import org.apache.log4j._
import org.apache.spark.mllib.recommendation.ALS
import org.apache.spark.mllib.recommendation.Rating
import java.lang.System

object FinalProject {
 
  def main(args: Array[String]) {
   
    // Set the log level to only print errors
    Logger.getLogger("org").setLevel(Level.ERROR)
        
    // Create a SparkContext using every core of the local machine, named FinalProject
    val sc = new SparkContext("local[*]", "FinalProject")
    
    //Print out the first five elements to verify data shape:
    var now = System.nanoTime
    val data = sc.textFile("../clean_1m.dat")
    data.take(5).foreach(println)
    
    //Map through the dataset, and create a ratings variable, holding all the ratings as Ratings 
    //objects.
    val ratings = data.map(_.split(',') match { case Array(user, item, rate, timestamp) =>
      Rating(user.toInt, item.toInt, rate.toDouble)
    })
          
    //Set the rank (features) to one since all we care about is the 
    //User rating. Iterations is set to 10 to give enough samples for accurate 
    //results. 
    val rank = 1
    val numIterations = 10
    val model = ALS.train(ratings, rank, numIterations, 0.01)
   
    //Create the user products table to be able to predict with. Simply makes a 
    //object array of the user and product. 
    val usersProducts = ratings.map { case Rating(user, product, rate) =>
      (user, product)
    }
    
    //Takes the model from the ALS and userProduct - (user, product) and calcualtes
    //predictions for each user, product combo. 
    val predictions =
      model.predict(usersProducts).map { case Rating(user, product, rate) =>
        ((user, product), rate)
      }

    //Print out the first five predictions to validate. 
    predictions.take(5).foreach(println)

    val predictions_list = predictions.collect().toList
    
    //Stop spark
    sc.stop()
    
    //Verify that the size of the dataset. 
    println (predictions_list.length)
    
    //Printout the amount of time it took for Spark to process the job. 
    println("Time taken: ", System.nanoTime - now)
  }
}

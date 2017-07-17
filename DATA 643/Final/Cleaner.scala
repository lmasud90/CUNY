package com.latif.spark

import java.io._
import scala.io._

object Cleaner {
  def main(args: Array[String]) {
      val fw = new FileWriter("../clean_1m.dat", true)

      val filename="../ml-1m/ratings.dat"
      for (line <- Source.fromFile(filename).getLines) {
        fw.write(line.replace("::", ",")+"\n");

      }
      
       fw.close()
  }
}
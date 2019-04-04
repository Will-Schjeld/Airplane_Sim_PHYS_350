using System;
using System.IO;
using System.Diagnostics;
using System.Collections;
using System.Collections.Generic;
using UnityEngine;


namespace Flight
{
    class PythonCalls : MonoBehaviour
    {
        public List<double> xVelocity;
        public List<double> yVelocity;
        public List<double> zVelocity;

        public List<double> yaw;
        public List<double> pitch;
        public List<double> roll;

        public void callPython()
        {
    
            // full path of python interpreter 
            string python_path = "python";
            int index = 0;
            string path = Environment.GetEnvironmentVariable("PATH");
            string[] pathArr = path.Split(';');
            foreach(string item in pathArr)
            {
                List<string> itemList = item.Split('\\').ToList();
                if(itemList.Contains("Python37")) {
                    index = itemList.IndexOf("Python37");
                }
                else if(itemList.Contains("Python37-32")) {
                    index = itemList.IndexOf("Python37-32");
                }
                if(index == itemList.Count - 1) {
                    python_path = item + "\\python.exe";
                }
            }
            string python = @python_path;
         
            // python app to call 
            string myPythonApp = @"C:\Users\danie\Desktop\PaperPlane2\PHYS\Assets\motion.py";

            Flight.MainMenu main = new Flight.MainMenu();
            float speed =  main.speed;
            // Create new process start info 
            ProcessStartInfo myProcessStartInfo = new ProcessStartInfo(python);

            // make sure we can read the output from stdout 
            myProcessStartInfo.UseShellExecute = false;
            myProcessStartInfo.RedirectStandardOutput = true;
            myProcessStartInfo.RedirectStandardError = true;

            Process myProcess = new Process();
            // assign start information to the process 
            myProcess.StartInfo = myProcessStartInfo;
            // start python app with 1 argument 
            speed = 10;
            myProcessStartInfo.Arguments = myPythonApp + " " + speed;

            Console.WriteLine("Calling Python script with arguments {0} and {1}");
            // start the process 
            myProcess.Start();
            // Read the standard output of the app we called.  
            // in order to avoid deadlock we will read output first 
            // and then wait for process terminate: 
            StreamReader myStreamReader = myProcess.StandardOutput;
            string myString = myStreamReader.ReadToEnd();
  
            // wait exit signal from the app we called and then close it. 
            myProcess.WaitForExit();
            myProcess.Close();

            // Fix this latter so that you can pass input to create the class as in Java
            var velocities = new VelocityVectors();
            velocities.parseString(myString);

            xVelocity  = velocities.xVelocities;
            yVelocity = velocities.yVelocities;
            zVelocity = velocities.zVelocities;
            yaw = velocities.yawY;
            pitch = velocities.pitchX;
            roll = velocities.rollZ;

        }

    }

    public class VelocityVectors
    {
        public List<double> xVelocities = new List<double>();
        public List<double> yVelocities = new List<double>();
        public List<double> zVelocities = new List<double>();

        public List<double> yawY = new List<double>();
        public List<double> pitchX = new List<double>();
        public List<double> rollZ = new List<double>();

        public void parseString(string input)
        {
            string[] numbers = input.Split('\n');
            for (int i = 0; i < numbers.Length - 6; i+=6)
            {
                xVelocities.Add(Double.Parse(numbers[i]));
                yVelocities.Add(Double.Parse(numbers[i + 1]));
                zVelocities.Add(Double.Parse(numbers[i + 2]));
                rollZ.Add(Double.Parse(numbers[i + 3]));
                pitchX.Add(Double.Parse(numbers[i + 4]));
                yawY.Add(Double.Parse(numbers[i + 5]));

            }
        }
    }
}

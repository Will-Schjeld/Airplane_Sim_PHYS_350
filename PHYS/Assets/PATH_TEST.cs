using System;
using System.IO;
using System.Linq;
using System.Collections.Generic;

class PATH_TEST { 

static public void Main(String[] args) {
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
    Console.WriteLine(python_path);
}

}
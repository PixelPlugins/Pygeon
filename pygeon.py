import sys

print("Pygeon 1.0.0 ALPHA")

if(sys.argv[1] == "build"):
	pyfile = open("main.py", "r")
	pycode = pyfile.read()
	outfile = open("pygeonapp.cs", "w")
	outfile.write("using System;using System.Collections.Generic;using System.Diagnostics;using System.IO;using System.Linq;using System.Text;using System.Threading.Tasks;namespace ConsoleApplication1{class Program{static void Main(string[] args){using (FileStream fs = new FileStream(\"pygeonapp.py\", FileMode.Create)){using (StreamWriter w = new StreamWriter(fs, Encoding.UTF8)){w.WriteLine(\"" + pycode.replace("\n", "\\n") + "\");}ProcessStartInfo p = new ProcessStartInfo();p.FileName=\"C:\\\\Python27\\\\python.exe\";p.Arguments=\"pygeonapp.py\";Process.Start(p);}}}}");
	pyfile.close()
	outfile.close()
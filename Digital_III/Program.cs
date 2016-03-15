using System;
using Gtk;
using System.IO.Ports;

namespace Digital_III
{	
	class MainClass
	{
		public static SerialPort _serialPort;
		public static void Main (string[] args)
		{
			Application.Init ();
			MainWindow win = new MainWindow ();
			win.Show ();
			Application.Run ();

			_serialPort = new SerialPort ();
		}
	}
}

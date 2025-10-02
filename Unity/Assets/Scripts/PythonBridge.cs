using System.Diagnostics;
using System.IO;
using UnityEngine;

public static class PythonBridge
{
    public static string RunPython(string choicesJson)
    {
        ProcessStartInfo start = new ProcessStartInfo();
        start.FileName = "python";  // or "python3" depending on your system
        start.Arguments = $"export.py \"{choicesJson.Replace("\"", "\\\"")}\"";
        start.UseShellExecute = false;
        start.RedirectStandardOutput = true;
        start.RedirectStandardError = true;
        start.CreateNoWindow = true;

        using (Process process = Process.Start(start))
        {
            string output = process.StandardOutput.ReadToEnd();
            string error = process.StandardError.ReadToEnd();
            process.WaitForExit();

            if (!string.IsNullOrEmpty(error))
            {
                UnityEngine.Debug.LogError("Python error: " + error);
            }
            return output;
        }
    }
}

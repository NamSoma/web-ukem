using System;
using System.IO;
using System.Text;

public class Recover {
    public static void Test() {
        string path = @"e:\งาน\ลองทำ\สิ่งแวดล้อม\การบริหารจัดการพลังงานและการเปลี่ยนแปลงสภาพภูมิอากาศ.html";
        byte[] currentBytes = File.ReadAllBytes(path);
        
        // Let's decode current bytes as UTF-8
        string currentString = Encoding.UTF8.GetString(currentBytes);
        
        // Let's print the character codes of the first 200 characters to see what they are
        for(int i = 0; i < Math.Min(200, currentString.Length); i++) {
            Console.Write($"{(int)currentString[i]:X4} ");
        }
        Console.WriteLine();
    }
}

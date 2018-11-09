// Copyright (c) Microsoft Corporation. All rights reserved.
// Licensed under the MIT License.

using System;
using System.Collections.Generic;
using System.Linq;
using System.Text;
using System.Threading.Tasks;

namespace Bot
{
    public class NumberHelper
    {
        // !!! 需要提供实现的函数。
        // 请注意，该函数会在后台线程执行。
        public static Tuple<double, double> GetNumber(string input)
        {
            string[] strArray = input.Split(' ');
            double[] doubleArray = new double[strArray.Length];
            for (int i = 0; i < strArray.Length; i++)
            {
                doubleArray[i] = Convert.ToDouble(strArray[i]);
            }

            double GoldPoint = doubleArray[0];
            //double[] first_num = new double[strArray.Length / 2];
            //double[] second_num = new double[strArray.Length / 2];

            List<KeyValuePair<int, double>> firstlist = new List<KeyValuePair<int, double>>();
            List<KeyValuePair<int, double>> secondlist = new List<KeyValuePair<int, double>>();
            int j = 1;
            for (int i = 1; i%2 != 0 && i < doubleArray.Length; i++)
            {
                firstlist.Add(new KeyValuePair<int, double>(j, Math.Abs(doubleArray[i]-GoldPoint)));
                j++;
            }
            j = 1;
            for (int i = 1; i % 2 == 0 && i < doubleArray.Length; i++)
            {
                firstlist.Add(new KeyValuePair<int, double>(j, Math.Abs(doubleArray[i] - GoldPoint)));
                j++;
            }


















            return Tuple.Create(15.0, 16.0);
        }
    }
}

# ForexAssistant
Forex Trading Assistant, Prediction Algorithm

This program analyzes a currency pair then using trends and analytical tools is able to provide trading advice (i.e a good time to buy in or go short into a market). 

For information regarding trading philosophy, techniques used, direction of the program and/or upcoming features, contact Ashton Sidhu at ashton.sidhu1994@gmail.com

--------------------------------------------------------------------------------------------------------------------------------------

The files uploaded here are one version older than the most current version which was used to test the decision making and trading philosophy to make sure it was implemented correctly.

1) This program was coded using python 3.

2) The core trading logic and philosophy has been removed from the code (forecastalgoG.py) as it is not code intensive but more intuition. For any questions or inquiries about the trading logic and philosophym contact Ashton Sidhu at ashton.sidhu1994@gmail.com

3)The run_algoG.py pings the yahoo site for USD/CAD page for the current price, while the current version uses an api that gets live up to the minute values for more accuracy.

4) The latest version,which is undergoing testing, introduces a more sophistacted data "memory" so the program has a much larger data set to use for more accurate predictions.

How to run with no set of data:

PLAN 1:

  1) Download all files into 1 folder.
  
  2) Navigate to the folder using CMD line.
  
  3) Run the lines in setup.txt.
  
  4) Run run_algoG.pyfor a couple minutes to collect some data.
  
  5) Run forecastalgoG.py.
  
Plan 2 (if setup.py fails):

  1) Download all files into 1 folder.
  
  2) Download get-pip.py from the internet.
  
  3) Run get-pip.py
  
  4) Navigate to the folder using CMD line.
  
  5) Run the lines in backup.txt
  
  6) Run run_algoG.pyfor a couple minutes to collect some data.
  
  7) Run forecastalgoG.py
  
TO RUN THE PROGRAM WITH A FULL SET OF DATA:

  1) run forecastalgoGtest.py

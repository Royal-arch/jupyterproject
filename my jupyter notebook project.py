{
 "cells": [
  {
   "cell_type": "markdown",
   "metadata": {},
   "source": [
    "<center>\n",
    "    <img src=\"https://cf-courses-data.s3.us.cloud-object-storage.appdomain.cloud/IBMDeveloperSkillsNetwork-DS0105EN-SkillsNetwork/labs/Module2/images/SN_web_lightmode.png\" width=\"300\" alt=\"cognitiveclass.ai logo\">\n",
    "</center>\n"
   ]
  },
  {
   "cell_type": "markdown",
   "metadata": {},
   "source": [
    "#### Add your code below following the instructions given in the course\n"
   ]
  },
  {
   "cell_type": "markdown",
   "metadata": {},
   "source": [
    "# My Jupyter Notebook on IBM Watson Studio"
   ]
  },
  {
   "cell_type": "markdown",
   "metadata": {},
   "source": [
    "<strong> Raphael Williams.\n",
    "<p> data scientist "
   ]
  },
  {
   "cell_type": "markdown",
   "metadata": {},
   "source": [
    "<em>  I am interested in data science because i believe data and computing are the future of many industries. being able to understand data and how to utilize many of the skills learned will help you earn a good job. "
   ]
  },
  {
   "cell_type": "markdown",
   "metadata": {},
   "source": [
    "### This code will generate a random list of 5 numbers between 0 and 1, and then calculate their square roots. I'll use the random() function to generate a list of random numbers, and then use the square() function from the math module to calculate their square roots. Finally, it'll print both lists using the print() function."
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 3,
   "metadata": {},
   "outputs": [
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "Random numbers: [0.4498027378176852, 0.9747562066858312, 0.15754672646014978, 0.04941857179958653, 0.05770352241478427]\n",
      "Square roots: [0.6706733465836295, 0.9872974256452972, 0.39692156210030943, 0.22230288302131065, 0.240215574879699]\n"
     ]
    }
   ],
   "source": [
    "import random\n",
    "import math\n",
    "\n",
    "# Generate a list of 10 random numbers between 0 and 1\n",
    "random_numbers = [random.random() for i in range(5)]\n",
    "\n",
    "# Calculate the square root of each number using the math library\n",
    "sqrt_numbers = [math.sqrt(n) for n in random_numbers]\n",
    "\n",
    "# Print the original list and the square root list\n",
    "print(\"Random numbers:\", random_numbers)\n",
    "print(\"Square roots:\", sqrt_numbers)"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": null,
   "metadata": {},
   "outputs": [],
   "source": []
  }
 ],
 "metadata": {
  "kernelspec": {
   "display_name": "Python",
   "language": "python",
   "name": "conda-env-python-py"
  },
  "language_info": {
   "codemirror_mode": {
    "name": "ipython",
    "version": 3
   },
   "file_extension": ".py",
   "mimetype": "text/x-python",
   "name": "python",
   "nbconvert_exporter": "python",
   "pygments_lexer": "ipython3",
   "version": "3.7.12"
  }
 },
 "nbformat": 4,
 "nbformat_minor": 4
}

{
 "cells": [
  {
   "cell_type": "code",
   "execution_count": 4,
   "metadata": {},
   "outputs": [
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "Too many arguments!\n"
     ]
    }
   ],
   "source": [
    "#!/usr/bin/env python3\n",
    "# -*- coding: utf-8 -*-\n",
    "\n",
    "' a test moudle '\n",
    "\n",
    "__author__ = 'Micheal Liao'\n",
    "\n",
    "import sys\n",
    "\n",
    "def test():\n",
    "    args = sys.argv\n",
    "    if len(args)==1:\n",
    "        print('hello,world!')\n",
    "    elif len(args)==2:\n",
    "        print('hello,%s!'%arg[1])\n",
    "    else:\n",
    "        print('Too many arguments!')\n",
    "        \n",
    "if __name__=='__main__':\n",
    "    test()\n",
    "    \n"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": None,
   "metadata": {},
   "outputs": [],
   "source": []
  }
 ],
 "metadata": {
  "kernelspec": {
   "display_name": "Python 3",
   "language": "python",
   "name": "python3"
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
   "version": "3.8.3"
  }
 },
 "nbformat": 4,
 "nbformat_minor": 4
}

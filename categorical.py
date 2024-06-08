{
 "cells": [
  {
   "cell_type": "code",
   "execution_count": 1,
   "id": "87e5586c",
   "metadata": {},
   "outputs": [
    {
     "ename": "NameError",
     "evalue": "name 'null' is not defined",
     "output_type": "error",
     "traceback": [
      "\u001b[0;31m---------------------------------------------------------------------------\u001b[0m",
      "\u001b[0;31mNameError\u001b[0m                                 Traceback (most recent call last)",
      "\u001b[0;32m/tmp/ipykernel_118944/2689126451.py\u001b[0m in \u001b[0;36m<module>\u001b[0;34m\u001b[0m\n\u001b[1;32m      1\u001b[0m \u001b[0;32mimport\u001b[0m \u001b[0mpandas\u001b[0m \u001b[0;32mas\u001b[0m \u001b[0mpd\u001b[0m\u001b[0;34m\u001b[0m\u001b[0;34m\u001b[0m\u001b[0m\n\u001b[1;32m      2\u001b[0m \u001b[0;32mfrom\u001b[0m \u001b[0msklearn\u001b[0m\u001b[0;34m.\u001b[0m\u001b[0mpreprocessing\u001b[0m \u001b[0;32mimport\u001b[0m \u001b[0mLabelEncoder\u001b[0m\u001b[0;34m,\u001b[0m \u001b[0mOneHotEncoder\u001b[0m\u001b[0;34m\u001b[0m\u001b[0;34m\u001b[0m\u001b[0m\n\u001b[0;32m----> 3\u001b[0;31m \u001b[0;32mfrom\u001b[0m \u001b[0mdata_description\u001b[0m \u001b[0;32mimport\u001b[0m \u001b[0mDataDescription\u001b[0m\u001b[0;34m\u001b[0m\u001b[0;34m\u001b[0m\u001b[0m\n\u001b[0m\u001b[1;32m      4\u001b[0m \u001b[0;34m\u001b[0m\u001b[0m\n\u001b[1;32m      5\u001b[0m \u001b[0;32mclass\u001b[0m \u001b[0mCategorical\u001b[0m\u001b[0;34m:\u001b[0m\u001b[0;34m\u001b[0m\u001b[0;34m\u001b[0m\u001b[0m\n",
      "\u001b[0;32m~/data_description.py\u001b[0m in \u001b[0;36m<module>\u001b[0;34m\u001b[0m\n\u001b[1;32m     88\u001b[0m   {\n\u001b[1;32m     89\u001b[0m    \u001b[0;34m\"cell_type\"\u001b[0m\u001b[0;34m:\u001b[0m \u001b[0;34m\"code\"\u001b[0m\u001b[0;34m,\u001b[0m\u001b[0;34m\u001b[0m\u001b[0;34m\u001b[0m\u001b[0m\n\u001b[0;32m---> 90\u001b[0;31m    \u001b[0;34m\"execution_count\"\u001b[0m\u001b[0;34m:\u001b[0m \u001b[0mnull\u001b[0m\u001b[0;34m,\u001b[0m\u001b[0;34m\u001b[0m\u001b[0;34m\u001b[0m\u001b[0m\n\u001b[0m\u001b[1;32m     91\u001b[0m    \u001b[0;34m\"id\"\u001b[0m\u001b[0;34m:\u001b[0m \u001b[0;34m\"6125f707\"\u001b[0m\u001b[0;34m,\u001b[0m\u001b[0;34m\u001b[0m\u001b[0;34m\u001b[0m\u001b[0m\n\u001b[1;32m     92\u001b[0m    \u001b[0;34m\"metadata\"\u001b[0m\u001b[0;34m:\u001b[0m \u001b[0;34m{\u001b[0m\u001b[0;34m}\u001b[0m\u001b[0;34m,\u001b[0m\u001b[0;34m\u001b[0m\u001b[0;34m\u001b[0m\u001b[0m\n",
      "\u001b[0;31mNameError\u001b[0m: name 'null' is not defined"
     ]
    }
   ],
   "source": [
    "import pandas as pd\n",
    "from sklearn.preprocessing import LabelEncoder, OneHotEncoder\n",
    "from data_description import DataDescription\n",
    "\n",
    "class Categorical:\n",
    "    # The Task associated with this class.\n",
    "    tasks = [\n",
    "        '\\n1. Show Categorical Columns',\n",
    "        '2. Performing One Hot encoding',\n",
    "        '3. Show the Dataset'\n",
    "    ]\n",
    "    def __init__(self, data):\n",
    "        self.data = data\n",
    "\n",
    "    # function to show all the categorical columns and number of unique values in them.\n",
    "    def categoricalColumn(self):\n",
    "        print('\\n{0: <20}'.format(\"Categorical Column\") + '{0: <5}'.format(\"Unique Values\"))\n",
    "        # select_dtypes selects the columns with object datatype(which could be further categorize)\n",
    "        for column in self.data.select_dtypes(include=\"object\"):\n",
    "            print('{0: <20}'.format(column) + '{0: <5}'.format(self.data[column].nunique()))\n",
    "\n",
    "    # function to encode any particular column\n",
    "    def encoding(self):\n",
    "        categorical_columns = self.data.select_dtypes(include=\"object\")\n",
    "        while(1):\n",
    "            column = input(\"\\nWhich column would you like to one hot encode?(Press -1 to go back)  \").lower()\n",
    "            if column == \"-1\":\n",
    "                break\n",
    "            # The encoding function is only for categorical columns.\n",
    "            if column in categorical_columns:\n",
    "                self.data = pd.get_dummies(data=self.data, columns = [column])\n",
    "                print(\"Encoding is done.......\\U0001F601\")\n",
    "                \n",
    "                choice = input(\"Are there more columns to be encoded?(y/n)  \")\n",
    "                if choice == \"y\" or choice == \"Y\":\n",
    "                    continue\n",
    "                else:\n",
    "                    self.categoricalColumn()\n",
    "                    break\n",
    "            else:\n",
    "                print(\"Wrong Column Name. Try Again...\\U0001F974\")\n",
    "\n",
    "    # The main function of the Categorical class.\n",
    "    def categoricalMain(self):\n",
    "        while(1):\n",
    "            print(\"\\nTasks\\U0001F447\")\n",
    "            for task in self.tasks:\n",
    "                print(task)\n",
    "\n",
    "            while(1):\n",
    "                try:\n",
    "                    choice = int(input((\"\\n\\nWhat you want to do? (Press -1 to go back)  \")))\n",
    "                except ValueError:\n",
    "                    print(\"Integer Value required. Try again...\\U0001F974\")\n",
    "                    continue\n",
    "                break\n",
    "\n",
    "            if choice == -1:\n",
    "                break\n",
    "            \n",
    "            elif choice == 1:\n",
    "                self.categoricalColumn()\n",
    "\n",
    "            elif choice == 2:\n",
    "                self.categoricalColumn()\n",
    "                self.encoding()\n",
    "\n",
    "            elif choice == 3:\n",
    "                DataDescription.showDataset(self)\n",
    "\n",
    "            else:\n",
    "                print(\"\\nWrong Integer value!! Try again..\\U0001F974\")\n",
    "        # return the data after modifying\n",
    "        return self.data"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": null,
   "id": "262b32bf",
   "metadata": {},
   "outputs": [],
   "source": []
  }
 ],
 "metadata": {
  "kernelspec": {
   "display_name": "Python 3 (ipykernel)",
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
   "version": "3.9.13"
  }
 },
 "nbformat": 4,
 "nbformat_minor": 5
}
